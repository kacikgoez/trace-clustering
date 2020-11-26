

class TrainingSet:
    """
    sample_set - list of traces - the attributes of the eventlog are not changed
    """
    def __init__(self, sample_set):
        self.training_set = list()
        len_train_set = round(len(sample_set) / 2)
        for i in range(len_train_set):
            self.training_set.append(sample_set[i])

    def get_training_set(self):
        return self.training_set
