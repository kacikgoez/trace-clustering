import random


class TrainingSet:
    def __init__(self, sample_set):
        """
        :param sample_set: list of traces - the attributes of the eventlog are not changed
        """
        training_set_help = list()
        self.training_set = list()
        len_train_set = round(len(sample_set) * 0.5)
        i = 0
        while i < len_train_set:
            help_var = random.randint(0, len(sample_set) - 1)
            if help_var not in training_set_help:
                training_set_help.append(help_var)
                i += 1
        for i in training_set_help:
            self.training_set.append(sample_set[i])

    def get_training_set(self):
        """
        :return: Returns the training set.
        """
        return self.training_set
