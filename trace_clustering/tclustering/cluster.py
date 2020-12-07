import os
from pathlib import Path
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.log.util import func
from tclustering.fsp import FSP
from tclustering.labeling import Labeling
from tclustering.sampleSet import SampleSet
from tclustering.trainingSet import TrainingSet
from tclustering.frequency import in_cluster


class Cluster:

    """
    eventlog - .xes file
    traces - list of traces id
    labeling_attributes - list of attribute names on which the algorithm will run on
    support - number of [0, 1]
    algorithm_names - list with len(algorithm_names) = 3 with strings in it
                    first element - algorithm for the sequence pattern of length 1
                    second element - algorithm for the sequence pattern of length 2
                    third element - algorithm for the closed sequence pattern
    threshold_score - list with len(threshold_score) = 3 with integers in it
                    first element - threshold of the sequence pattern of length 1
                    second element - threshold of the sequence pattern of length 2
                    third element - threshold of the closed sequence pattern
    """

    def __init__(self, log, traces, file_path, labeling_attributes, support, algorithm_names):
        self.eventlog = xes_importer.apply(log)
        sample_set = SampleSet(self.eventlog, traces)
        training_set = TrainingSet(sample_set.get_sample_set())
        self.labeling_training_set = Labeling(training_set.get_training_set(), labeling_attributes)
        self.labeling_eventlog = Labeling(self.eventlog, labeling_attributes)
        sp_len_one = FSP(file_path, algorithm_names[0],
                         self.labeling_training_set.get_eventlog_label(), Path(log).name, [support, 1, 1])
        sp_len_two = FSP(file_path, algorithm_names[1],
                         self.labeling_training_set.get_eventlog_label(), Path(log).name, [support, 2, 2])
        sp_clo = FSP(file_path, algorithm_names[2],
                     self.labeling_training_set.get_eventlog_label(), Path(log).name, [support])
        self.pattern_len_one = sp_len_one.get_result()
        self.pattern_len_two = sp_len_two.get_result()
        self.pattern_clo = sp_clo.get_result()
        self.pattern = [self.pattern_len_one, self.pattern_len_two, self.pattern_clo]

    def get_clustering(self, threshold_score):
        clustering = self.choose(self.eventlog, in_cluster(self.pattern, self.labeling_eventlog.get_eventlog_label(),
                                                           threshold_score))
        return clustering

    @staticmethod
    def get_log_as_array(path):
        if os.path.isfile(path):
            traces = []
            log = xes_importer.apply(path)
            for trace in log:
                inner = []
                for event in trace:
                    events = {}
                    for action in event:
                        events[action] = str(event[action])
                    inner.append(events)
                traces.append(inner)
            return traces
        else:
            raise Exception("LogNotFound", "Log was not found")

    @staticmethod
    def choose(eventlog, cluster_bool):
        log = func.filter_(lambda t: cluster_bool(t), eventlog)
        return log
