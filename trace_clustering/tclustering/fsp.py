import os
from spmf import Spmf
import itertools
from pathlib import Path


class FSP:

    """
    file_path - path of one of the sequence_pattern_dir
    """
    def __init__(self, file_path, algorithm_name, sample_set_labeling, arguments):
        self.cur_path = Path(file_path)
        self.spmf_jar_path = Path(file_path)
        self.input_file = self.write_text_input_file(sample_set_labeling, file_path)
        self.spmf = Spmf(algorithm_name, input_filename=self.input_file,
                         output_filename=os.path.join(file_path, 'output.txt'), arguments=arguments,
                         spmf_bin_location_dir=str(self.spmf_jar_path.parent))
        self.spmf.run()
        self.result = self.output_to_array(os.path.join(file_path, 'output.txt'))

    """This function writes a .txt file to"""
    def write_text_input_file(self, sample_set_labeling, file_path):
        with open(os.path.join(file_path, "input.txt"), "w+") as file:
            file.write('@CONVERTED_FROM_TEXT\n')
            d = self.mapping_dict(sample_set_labeling)

            for i in list(d.keys()):
                temp_string = '@ITEM=' + str(d[i]) + '=' + str(i) + '\n'
                file.write(temp_string)

            file.write('@ITEM=-1=|\n')

            help_list = self.mapping(sample_set_labeling)
            for i in range(len(help_list)):
                help_string = ''
                for j in range(len(help_list[i])):
                    help_string = help_string + str(help_list[i][j]) + ' -1 '
                help_string = help_string + '-2 \n'
                file.write(help_string)

            file.close()

        return os.path.join(file_path, "input.txt")

    @staticmethod
    def mapping_dict(eventlog_labeling):
        merged = list(itertools.chain.from_iterable(eventlog_labeling))
        d = dict([(y, x + 1) for x, y in enumerate(sorted(set(merged)))])
        return d

    @staticmethod
    def mapping(eventlog_labeling):
        help_list = list()
        merged = list(itertools.chain.from_iterable(eventlog_labeling))
        d = dict([(y, x + 1) for x, y in enumerate(sorted(set(merged)))])
        for i in range(len(eventlog_labeling)):
            help_list.append([d[x] for x in eventlog_labeling[i]])
        return help_list

    @staticmethod
    def output_to_array(output):
        with open(output, "r") as a_file:
            list_of_list = []
            for line in a_file:
                stripped_line = line.strip()
                if '-2' not in stripped_line:
                    res = stripped_line.partition(' | #SUP:')[0]
                else:
                    res = stripped_line.partition(' | -2')[0]
                line_list = res.split(' | ')
                list_of_list.append(line_list)

            a_file.close()
            return list_of_list

    def get_result(self):
        return self.result

    def get_amount(self):
        return len(self.result)

