

def compare_patter(pattern, trace):
    """
    Verification if a pattern occurs in a trace.
    :param pattern: a pattern of labeling events (1-dimensional list)
    :param trace: list of labeling events of a trace (1-dimensional list)
    :return: boolean True iff pattern occurs in trace regarding its ordering in pattern (bool)
    """
    start = 0
    for y in pattern:
        try:
            start = trace.index(y, start) + 1
        except ValueError:
            return False
    else:
        return True


def compare_pattern(pattern_list, trace):
    """
    The function counts the amount of patterns that occur in the trace.
    :param pattern_list: a list of pattern of labeling events (2-dimensional list)
    :param trace: list of labeling events of a trace (1-dimensional list)
    :return: how many pattern in pattern_list occurs in trace (int)
    """
    count = 0
    for i in pattern_list:
        if compare_patter(i, trace):
            count += 1
    return count


def compare_mult_pattern(mult_pattern_list, trace):
    """
    The function counts the amount of pattern of each pattern list that occur in the trace.
    :param mult_pattern_list: a list of multiple lists of pattern of labeling events (3-dimensional list)
    :param trace: list of labeling events of a trace (1-dimensional list)
    :return: how many pattern of each multiple lists of pattern occurs in trace (1-dimensional list of ints)
    """
    help_list = list()
    for i in mult_pattern_list:
        help_list.append(compare_pattern(i, trace))
    return help_list


def compare_all(mult_pattern_list, traces):
    """
    The function counts the amount of pattern of each pattern list that occur in each trace of the list traces.
    :param mult_pattern_list: a list of multiple lists of pattern of labeling events (3-dimensional list)
    :param traces: list of traces of labeling events of a trace (2-dimensional list)
    :return: how man pattern of each multiple lists of pattern occurs in each trace of the list traces
            (2-dimensional list of ints)
    """
    help_list = list()
    for i in traces:
        help_list.append(compare_mult_pattern(mult_pattern_list, i))
    return help_list


def in_cluster(mult_pattern_list, traces, thresholds):
    """
    Return True for each trace in the list traces iff it satisfies the thresholds.
    :param mult_pattern_list: a list of multiple lists of pattern of labeling events (3-dimensional list)
    :param traces: list of traces of labeling events of a trace (2-dimensional list)
    :param thresholds: amount of patterns of each pattern list that should at least occur in each trace of
                       traces (1-dimensional list of ints)
    :return: if trace of the list traces satisfies the thresholds (1-dimensional list of bool)
    """
    pattern_amount = compare_all(mult_pattern_list, traces)
    help_list = list()
    for i in pattern_amount:
        for j in range(len(i)):
            if i[j] < thresholds[j]:
                help_list.append(False)
                break
            elif j == len(i) - 1:
                help_list.append(True)
    return help_list
