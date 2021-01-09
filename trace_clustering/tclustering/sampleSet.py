from tclustering.logFunc import LogFunc


class SampleSet:

    # by specifying an array traces we select specific traces into the sampleSet
    # eventlog should be imported as xes_importer.apply(eventlog)
    def __init__(self, eventlog, traces):
        self.eventlog = eventlog
        self.sampleSet = self.sample(traces, eventlog)
        self.sampleLog = self.sample_as_log(eventlog, traces)

    def get_sample_set(self):
        return self.sampleSet

    def get_sample_log(self):
        return self.sampleLog

    # eventlog should be imported as xes_importer.apply(eventlog)
    @staticmethod
    def sample(list_traces_num, eventlog):
        sample_log = list()
        for i in list_traces_num:
            sample_log.append(eventlog[i])
        return sample_log

    @staticmethod
    def sample_as_log(eventlog, traces):
        cluster_bool = list()
        for i in range(len(eventlog)):
            if i in traces:
                cluster_bool.append(True)
            else:
                cluster_bool.append(False)
        return LogFunc.choose(eventlog, cluster_bool)
