import os
from spmf import Spmf
import itertools
from pathlib import Path


class FSP:

    def __init__(self, file_path, algorithm_name, sample_set_labeling, xes_file_name, arguments):
        """
        Runs the algorithm and stores the pattern in self.result.
        :param file_path: path where to store the input and output files as string
        :param algorithm_name: algorithm that should be used as string
        :param sample_set_labeling: list of traces as the corresponding labeling
        :param xes_file_name: the xes file name of the sample_set_labeling e.g. 'example.xes' as string
        :param arguments: arguments that are needed for the algorithm as list
        """
        self.cur_path = Path(file_path)
        extension = [algorithm_name] + arguments
        self.input_file = FSP.write_text_input_file(sample_set_labeling, file_path, xes_file_name, extension)
        self.output_file = os.path.join(file_path, FSP.file_name('output', xes_file_name, extension))
        os.path.join(file_path, 'output.txt')
        self.spmf = Spmf(algorithm_name,
                         input_filename=self.input_file,
                         output_filename=self.output_file, arguments=arguments,
                         spmf_bin_location_dir=str(self.cur_path.parent.parent.parent))
        self.spmf.run()
        self.result = self.output_to_array(self.output_file)

    @staticmethod
    def write_text_input_file(sample_set_labeling, file_path, xes_file_name, extension):
        """
        Create a input txt file for the spmf.
        :param sample_set_labeling: the sample_set_labeling
        :param file_path: file_path where to store the input file
        :param xes_file_name: the xes file name of the sample_set_labeling
        :param extension: algorithm name and arguments that will be used in the fsp
        :return: it returns the input file path
        """
        filename = FSP.file_name('input', xes_file_name, extension)

        with open(os.path.join(file_path, filename), "w+") as file:
            file.write('@CONVERTED_FROM_TEXT\n')
            d = FSP.mapping_dict(sample_set_labeling)

            for i in list(d.keys()):
                temp_string = '@ITEM=' + str(d[i]) + '=' + str(i) + '\n'
                file.write(temp_string)

            file.write('@ITEM=-1=|\n')

            help_list = FSP.mapping(sample_set_labeling)
            for i in range(len(help_list)):
                help_string = ''
                for j in range(len(help_list[i])):
                    help_string = help_string + str(help_list[i][j]) + ' -1 '
                help_string = help_string + '-2 \n'
                file.write(help_string)

            file.close()

        return os.path.join(file_path, filename)

    @staticmethod
    def mapping_dict(eventlog_labeling):
        """
        Every element (e.g. activity) is mapped sorted through a dict to an int starting from 1 and increased
        by 1.
        :param eventlog_labeling: list of traces, every trace is a sequence of event labeling
        :return: a dict that maps every element (e.g. activity) of the eventlog_labeling to an int
        """
        merged = list(itertools.chain.from_iterable(eventlog_labeling))
        d = dict([(y, x + 1) for x, y in enumerate(sorted(set(merged)))])
        return d

    @staticmethod
    def mapping(eventlog_labeling):
        """
        The eventlog_labeling is switched to a representation of int by the its mapping_dict.
        :param eventlog_labeling: list of traces, every trace is a sequence of event labeling
        :return: same as eventlog_labeling only that every event labeling is illustrated by its mapping_dict
                 representation
        """
        help_list = list()
        merged = list(itertools.chain.from_iterable(eventlog_labeling))
        d = dict([(y, x + 1) for x, y in enumerate(sorted(set(merged)))])
        for i in range(len(eventlog_labeling)):
            help_list.append([d[x] for x in eventlog_labeling[i]])
        return help_list

    @staticmethod
    def output_to_array(output):
        """
        Returns the output as list of lists.
        :param output: full path of the output txt file
        :return: returns the corresponding output as a 2-dimensional list
        """
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
        """
        Returns the Result of the FSP.
        :return: a list of patterns
        """
        return self.result

    def get_amount(self):
        """
        Counts the amount of patterns of the result.
        :return: amount of patterns of the result as int
        """
        return len(self.result)

    @staticmethod
    def file_name(in_or_output, xes_file_name, extension):
        """
        Returns an input or output file as string.
        :param in_or_output: is it an input or output as string
        :param xes_file_name: the xes file name of the sample_set_labeling e.g. 'example.xes' as string
        :param extension: algorithm name and arguments that will be used in the fsp as list
        :return: filename as string
        """
        filename = in_or_output + '_' + xes_file_name.replace('.', '_') + '_'
        for i in range(len(extension)):
            if i == len(extension) - 1:
                filename = filename + str(extension[i]) + '.txt'
            else:
                filename = filename + str(extension[i]) + '_'
        return filename
