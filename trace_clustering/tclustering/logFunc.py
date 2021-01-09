from pm4py.objects.log.util import func


class LogFunc:

    @staticmethod
    def choose(eventlog, cluster_bool):
        log = func.filter_(lambda t: cluster_bool[LogFunc.trace_to_index(eventlog, t)], eventlog)
        return log

    @staticmethod
    def trace_to_index(eventlog, trace):
        for i in range(len(eventlog)):
            if eventlog[i] == trace:
                return i
        return -1

    @staticmethod
    def get_log_as_array(log):
        traces = list()
        for trace in log:
            inner = []
            for event in trace:
                events = {}
                for action in event:
                    events[action] = str(event[action])
                inner.append(events)
            traces.append(inner)
        return traces
