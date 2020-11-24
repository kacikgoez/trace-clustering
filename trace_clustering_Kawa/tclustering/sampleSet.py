from pm4py.objects.log.importer.xes import importer as xes_importer
import itertools

class SampleSet:

    # by specifing an array traces we select specific traces into the sampleSet
    def __init__(self, eventlog, traces):
        self.eventlog = xes_importer.apply(eventlog)
        self.sampleSet = self.sample(traces, self.eventlog)

    def sample(self, n, eventlog):
        sampleLog = list()
        for i in n:
            sampleLog.append(eventlog[i])
        return sampleLog

    def labelingTrace(self, eventlog, traceIndex, listOfAttributes):
        labelingList = list()
        for i in range(len(eventlog[traceIndex])):
            helpString = ''
            for j in range(len(listOfAttributes)):
                helpString = helpString + str(eventlog[traceIndex][i][listOfAttributes[j]])
                if j != len(listOfAttributes) - 1:
                    helpString = helpString + '-'
            labelingList.append(helpString)

        return labelingList

    def labelingEventlog(self, eventlog, listOfAttributes):
        labelingList = list()
        for i in range(len(eventlog)):
            labelingList.append(self.labelingTrace(eventlog, i, listOfAttributes))
        return labelingList


