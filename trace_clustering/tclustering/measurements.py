class Measurements:

    def __init__(self, sample_set, computed_log):
        self.recall = Measurements.recall(sample_set, computed_log)
        self.precision = Measurements.precision(sample_set, computed_log)
        self.f1measure = Measurements.f1measure(sample_set, computed_log)

    @staticmethod
    def recall(sample_set, computed_log):
        """
            @param sample_set: Sample Set selected by user
            @param computed_log: Cluster computed by the Algorithm
            returns the recall value of the computed log
        """
        intsct = Measurements.intersection(sample_set, computed_log)
        return len(intsct)/len(sample_set)

    @staticmethod
    def intersection(sample_set, computed_log):
        """
            @param sample_set: Sample Set selected by user
            @param computed_log: Cluster computed by the Algorithm
            returns mutual traces found in both logs
        """
        result = list()
        for i in computed_log:
            for j in sample_set:
                if i == j:
                    result.append(i)
        return result

    @staticmethod
    def precision(sample_set, computed_log):
        """
            @param sample_set: Sample Set selected by user
            @param computed_log: Cluster computed by the Algorithm
            returns the precision value of the computed log
        """
        intsct = Measurements.intersection(sample_set, computed_log)
        return len(intsct) / len(computed_log)

    @staticmethod
    def f1measure(sample_set, computed_log):
        """
            @param sample_set: Sample Set selected by user
            @param computed_log: Cluster computed by the Algorithm
            returns the f1measure value of the computed log
        """
        numerator = Measurements.precision(sample_set, computed_log) * Measurements.recall(sample_set, computed_log)
        denominator = Measurements.recall(sample_set, computed_log) + Measurements.precision(sample_set, computed_log)
        return 2*numerator / denominator
