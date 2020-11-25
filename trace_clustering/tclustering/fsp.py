import os
from pathlib import Path
from spmf import Spmf
from pm4py.objects.log.importer.xes import importer as xes_importer
import itertools

class FSP:
    #filename without ext
    def __init__(self, file_path, supportThreshold):
        global fpath
        global log
        spmf_path = Path(file_path)
        fpath = os.path.join(str(spmf_path.parent), "processed")
        log = xes_importer.apply(file_path)
        filename = os.path.basename(file_path)
        self.file_format_to_pm4py_input("Activity", (filename + ".txt"))
        spmf = Spmf("CloFast", input_filename=(os.path.join(fpath, (filename + ".txt"))),
                output_filename=(os.path.join(fpath, "output", (filename + ".txt"))), arguments=[supportThreshold])
        spmf.run()


    """This function writes a .txt file to"""
    def write_text_input_file(self, eventlogLabeling):
        file = open('../input.txt', 'w+')
        file.write('@CONVERTED_FROM_TEXT\n')
        d = self.mapping_dict(eventlogLabeling)

        for i in list(d.keys()):
            string = '@ITEM=' + str(d[i]) + '=' + str(i) + '\n'
            file.write(string)

        file.write('@ITEM=-1=|\n')

        helpList = self.mapping(eventlogLabeling)
        for i in range(len(helpList)):
            helpString = ''
            for j in range(len(helpList[i])):
                helpString = helpString + str(helpList[i][j]) + ' -1 '
            helpString = helpString + '-2 \n'
            file.write(helpString)

        return file

    def output_to_array(self, output):
        a_file = open(output, 'r')

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

    def mapping_dict(self, eventlogLabeling):
        merged = list(itertools.chain.from_iterable(eventlogLabeling))
        d = dict([(y, x + 1) for x, y in enumerate(sorted(set(merged)))])
        return d


    def mapping(self, eventlogLabeling):
        helpList = list()
        merged = list(itertools.chain.from_iterable(eventlogLabeling))
        d = dict([(y, x + 1) for x, y in enumerate(sorted(set(merged)))])
        for i in range(len(eventlogLabeling)):
            helpList.append([d[x] for x in eventlogLabeling[i]])
        return helpList

    def get_result(self):
        return self.result

    def get_amount(self):
        return len(self.result)

    #Returns a list with the corresponding match of attribute value to integer
    def file_numerize_attribute(self, attrName):
        res_list = {}
        count = 0
        for trace in log:
            for entry in trace:
                if entry[attrName] not in res_list:
                    res_list[entry[attrName]] = count
                    count += 1
        return res_list

    #Turns attributes into numbers and keeps them in sequence
    #Example: move left -> move right -> move left -> move up
    #Output: 0 -> 1 -> 0 -> 2 
    def file_trace_to_numbers(self, attrName):
        res_array = []
        num_dict = self.file_numerize_attribute(attrName)
        for i in range (len(log)):
            res_array.append([])
            for j in range(len(log[i])):
                entry = log[i][j]
                res_array[i].append(num_dict[entry[attrName]])
        return res_array

    def file_numerize_attribute(self, attrName):
        res_list = {}
        count = 0
        for trace in log:
            for entry in trace:
                if entry[attrName] not in res_list:
                    res_list[entry[attrName]] = count
                    count += 1
        return res_list

    def file_format_to_pm4py_input(self, attrName, filename_out):
        inpt = self.file_trace_to_numbers(attrName)
        result = ""
        for i in inpt:
            for j in i:
                result += str(j) + " "
            result += "-2\n"
        with open(os.path.join(fpath, filename_out), "w") as f:
            f.write(result)
            f.close()
