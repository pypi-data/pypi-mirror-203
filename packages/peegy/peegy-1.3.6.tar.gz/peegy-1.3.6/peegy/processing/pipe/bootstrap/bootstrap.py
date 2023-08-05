import copy
import pandas
import tqdm
# from joblib import Parallel, delayed
from peegy.processing.pipe.definitions import InputOutputProcess
from peegy.processing.pipe.general import RemoveEvokedResponse
from peegy.processing.pipe.pipeline import PipePool
from peegy.definitions.tables import Tables
from peegy.processing.statistics.definitions import TestType
import numpy as np
import pandas as pd
import astropy.units as u


class BootstrapTarget(object):
    """
    This class is used to define the target tables that will be taking for bootstrapping.
    """
    def __init__(self,
                 table_name: str = None,
                 group_by: [str] = None,
                 target_values: [str] = None
                 ):
        """

        :param table_name: What table should be targeted for bootstrapping
        :param group_by: column names (present in the target statistical table) that should be used to group
        the data that should be bootstrapped.
        :param target_values: column names with the statistics that should be bootstrapped (e.g. f)
        """
        self.table_name = table_name
        self.group_by = group_by
        self.table_name = table_name
        self.target_values = target_values


class Bootstrap(InputOutputProcess):
    def __init__(self,
                 origin_input_process: InputOutputProcess = None,
                 before_bootstrapping_input_process: InputOutputProcess = None,
                 at_each_bootstrap_do: PipePool = None,
                 n_events: int = None,
                 event_code: float = 1,
                 dur: u.Quantity = 100 * u.us,
                 min_time: u.Quantity = None,
                 max_time: u.Quantity = None,
                 epoch_length: u.Quantity = None,
                 n_bootstraps: int = 1000,
                 bootstrap_targets: [BootstrapTarget] = None,
                 alpha_level: float = 0.05,
                 one_sided: bool = True,
                 **kwargs) -> InputOutputProcess:
        """
        Bootstrap input pipeline. It assumed that the origin_input_process contains the continuous, un-epoched data.
        The events will be randomized and the pipeline passed in at_each_bootstrap_do will be run.
        The process of shuffling events and running the pipeline  will be repeated n_bootstraps times.
        The output table will contain the mean, median, standard deviation, lower confidence interval, upper confidence
        interval, sample size for the bootstrap and the p-value.
        Confidence intervals are based on the alpha_value passed.
        :param origin_input_process: The continuous, un-epoched data that will be bootstrap
        :param before_bootstrapping_input_process: Inputprocess to be run before bootstrap begins but after the
        original statistics have been computed. If None, by default the average evoked response will be removed.
        :param at_each_bootstrap_do: The pipeline that will be bootstrapped
        :param n_events: If not none, the number of random events will be n_events
        :param event_code: the event code that will be shuffled
        :param dur: duration of the shuffled event code
        :param min_time: minimum time allowed for shuffle events. If None, the timing of the first event will be used
        :param max_time: maximum time allowed for shuffle events. If None, the timing of the last event will be used
        :param epoch_length: reference duration of epochs. This is only used to ensure that the after the last event
        there will be time enough to ensure this epoch length
        :param n_bootstraps: how many times to bootstrap the pipeline
        :param bootstrap_targets: array of BootstrapTarget indicating what tables from the different pipeline elements
        should be keep for bootstrapping and what statistics.
        :param alpha_level: alpha level of confidence intervals
        :param one_sided: bool indicating whether alpha value is one_sided or not.
        :param kwargs: extra parameters to be passed to the superclass
        """
        super(Bootstrap, self).__init__(input_process=None, **kwargs)
        self.origin_input_process = origin_input_process
        self.before_bootstrapping_input_process = before_bootstrapping_input_process
        self.at_each_bootstrap_do = at_each_bootstrap_do
        self.n_bootstraps = n_bootstraps
        self.n_events = n_events
        self.event_code = event_code
        self.dur = dur
        self.min_time = min_time
        self.max_time = max_time
        self.epoch_length = epoch_length
        self.alpha_level = alpha_level
        self.one_sided = one_sided
        self._original_events = None
        self.bootstrap_targets = bootstrap_targets

    def transform_data(self):
        # the origin input_process is copied to ensure nothing is done to the original reference process
        if self.origin_input_process is not None:
            _origin_input_process = copy.copy(self.origin_input_process)
        else:
            _origin_input_process = copy.copy(list(self.at_each_bootstrap_do.values())[0].input_process)

        # ensure that the reference process is used by the pipeline
        for _process in list(self.at_each_bootstrap_do.values()):
            if _process.input_process.name == _origin_input_process.name:
                _process = _origin_input_process

        # first run pipeline to extract actual values to be tested against bootstrapped tables
        self.at_each_bootstrap_do.run(force=True)
        # extract reference tables
        ref_table = get_tables(pipeline=self.at_each_bootstrap_do, targets=self.bootstrap_targets)
        # get event information
        _n_events = self.n_events
        _min_time = self.min_time
        _max_time = self.max_time
        if _n_events is None:
            _n_events = _origin_input_process.output_node.events.get_events_code(code=self.event_code).size
        if _min_time is None:
            _min_time = _origin_input_process.output_node.events.get_events_time(code=self.event_code).min()
        if _max_time is None:
            _max_time = _origin_input_process.output_node.events.get_events_time(code=self.event_code).max()
        # apply whatever we ask before we bootstrap. Normally we will remove the evoked data
        if self.before_bootstrapping_input_process is not None:
            self.before_bootstrapping_input_process.input_process = _origin_input_process
        else:
            self.before_bootstrapping_input_process = RemoveEvokedResponse(
                input_process=_origin_input_process,
                event_code=self.event_code,
                post_stimulus_interval=self.epoch_length)

        self.before_bootstrapping_input_process.run()
        _origin_input_process.output_node.data = self.before_bootstrapping_input_process.output_node.data
        # generate average epoch length if not given to prevent small estimations from random events
        _epoch_length = self.epoch_length
        if self.epoch_length is None:
            _epoch_length = np.mean(
                np.diff(_origin_input_process.output_node.events.get_events_time(code=self.event_code)))

        # bootstrap pipeline
        bootstrapped_tables = pd.DataFrame()
        for _i in tqdm.tqdm(range(self.n_bootstraps), desc='Bootstrapping pipeline', colour='blue'):
            # randomize events for run
            _origin_input_process.output_node.randomize_events(event_code=self.event_code,
                                                               epoch_length=_epoch_length,
                                                               min_time=_min_time,
                                                               max_time=_max_time,
                                                               n_events=_n_events
                                                               )
            # run pipeline with new events
            self.at_each_bootstrap_do.run(force=True)
            if _i == 0:
                bootstrapped_tables = get_tables(pipeline=self.at_each_bootstrap_do, targets=self.bootstrap_targets)
                bootstrapped_tables['bootstrap_number'] = _i

            else:
                _current_tables = get_tables(pipeline=self.at_each_bootstrap_do, targets=self.bootstrap_targets)
                _current_tables['bootstrap_number'] = _i
                bootstrapped_tables = pd.concat([bootstrapped_tables, _current_tables])
        # compute statistics
        ref_table = ref_table.rename(columns={'value': 'statistic_value'})
        columns_left = set(bootstrapped_tables.keys()).difference(['value', 'bootstrap_number'])
        columns_right = set(ref_table.keys()).difference(['statistic_value'])
        common_cols = list(columns_left.intersection(columns_right))
        bootstrapped_and_ref_tables = pd.merge(bootstrapped_tables,
                                               ref_table,
                                               how='left',
                                               on=common_cols
                                               )

        df_boots = bootstrapped_and_ref_tables.groupby(list(set(bootstrapped_and_ref_tables.keys()).difference(
            ['value', 'bootstrap_number'])), as_index=False).apply(
            lambda x: pd.Series({'stats': get_bootstrap_estimates(samples=x['value'],
                                                                  statistic=x['statistic_value'],
                                                                  alpha_level=self.alpha_level,
                                                                  one_sided=self.one_sided)}))

        (df_boots['mean'],
         df_boots['median'],
         df_boots['std'],
         df_boots['ci_lower'],
         df_boots['ci_upper'],
         df_boots['sample_size'],
         df_boots['p_value']) = zip(*df_boots.stats)
        df_boots['one_sided'] = self.one_sided
        df_boots = df_boots.drop(['stats'], axis=1)
        # join boot table and reference table
        self.output_node.statistical_tests = Tables(table_name=TestType.bootstrap,
                                                    data=df_boots,
                                                    data_source=self.name)


def get_bootstrap_estimates(samples: np.array = None,
                            statistic: np.array = None,
                            alpha_level: float = 0.05,
                            one_sided=True):
    # remove nan that may be present
    samples = samples[~pd.isna(samples)]
    _stat = np.unique(statistic)
    sample_size = samples.shape[0]
    sorted_samples = np.sort(samples, axis=0)
    mean = np.mean(samples, axis=0)
    median = np.median(samples, axis=0)
    std = np.std(samples, axis=0)
    _alpha = alpha_level
    if not one_sided:
        _alpha = alpha_level / 2.0

    _i_upper = np.minimum(int(samples.shape[0] * (1 - _alpha)), samples.shape[0])
    _i_lower = np.maximum(int(samples.shape[0] * _alpha), 0)
    ci_lower = sorted_samples[_i_lower]
    ci_upper = sorted_samples[_i_upper]
    diff = np.abs(_stat - sorted_samples)
    _idx_match = np.argmin(diff, axis=0) + 1
    p_value = 1 - _idx_match / sample_size
    return [mean, median, std, ci_lower, ci_upper, sample_size, p_value]


def get_tables(pipeline: PipePool = None,
               targets: [BootstrapTarget] = None):
    output = pd.DataFrame()
    for _source, _value in pipeline.items():
        for _target in targets:
            if _target.table_name in _value.output_node.statistical_tests.keys():
                _columns = list(set(_value.output_node.statistical_tests[_target.table_name].keys()) &
                                set(_target.target_values))
                if len(_columns):
                    df = _value.output_node.statistical_tests[_target.table_name]
                    df = df[_target.group_by + _target.target_values + ['data_source']]
                    df = pd.melt(df, ignore_index=False,
                                 id_vars=set(set(df.keys())).difference(_target.target_values),
                                 value_vars=_target.target_values,
                                 var_name='statistic')
                    df['table_name'] = _target.table_name
                    output = pandas.concat([output, df], ignore_index=True)
    return output
