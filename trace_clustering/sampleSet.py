class SampleSet:

    # by specifying an array traces we select specific traces into the sampleSet
    # eventlog should be imported as xes_importer.apply(eventlog)
    def __init__(self, eventlog, traces):
        self.eventlog = eventlog
        self.sampleSet = self.sample(traces, eventlog)

    def get_sample_set(self):
        return self.sampleSet

    # eventlog should be imported as xes_importer.apply(eventlog)
    @staticmethod
    def sample(list_traces_num, eventlog):
        sample_log = list()
        for i in list_traces_num:
            sample_log.append(eventlog[i])
        return sample_log
