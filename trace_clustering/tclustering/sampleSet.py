class SampleSet:

    # by specifying a list of traces we select specific traces into the sample set
    def __init__(self, eventlog, traces):
        self.eventlog = eventlog
        self.sampleSet = self.sample(traces, self.eventlog)

    def get_sample_set(self):
        return self.sampleSet

    @staticmethod
    def sample(n, eventlog):
        sample_log = list()
        for i in n:
            sample_log.append(eventlog[i])
        return sample_log
