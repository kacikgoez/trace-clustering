class Labeling:

    def __init__(self, eventlog, list_of_attributes):
        self.eventlog_label = self.labeling_eventlog(self, eventlog, list_of_attributes)

    def get_eventlog_label(self):
        return self.eventlog_label

    @staticmethod
    def labeling_trace(eventlog, trace_index, list_of_attributes):
        labeling_list = list()
        for i in range(len(eventlog[trace_index])):
            help_string = ''
            for j in range(len(list_of_attributes)):
                help_string = help_string + str(eventlog[trace_index][i][list_of_attributes[j]])
                if j != len(list_of_attributes) - 1:
                    help_string = help_string + '-'
            labeling_list.append(help_string)

        return labeling_list

    @staticmethod
    def labeling_eventlog(self, eventlog, list_of_attributes):
        labeling_list = list()
        for trace_index in range(len(eventlog)):
            labeling_list.append(self.labeling_trace(eventlog, trace_index, list_of_attributes))
        return labeling_list
