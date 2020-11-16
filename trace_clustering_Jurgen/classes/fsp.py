import os
from spmf import Spmf
import itertools

class Fsp:

    def __init__(self, algorithm_name, eventlogLabeling, arguments):
        self.writeTxtInputFile(eventlogLabeling)
        self.spmf = Spmf(algorithm_name, input_filename='../input.txt', output_filename='output.txt', arguments=arguments, spmf_bin_location_dir='/Users/lentz/PycharmProjects/trace_clustering_Jurgen')
        self.spmf.run()
        self.result = self.outputToArray('output.txt')
        os.remove('../input.txt')
        os.remove('output.txt')

    """This function writes a .txt file to"""
    def writeTxtInputFile(self, eventlogLabeling):
        file = open('../input.txt', 'w+')
        file.write('@CONVERTED_FROM_TEXT\n')
        d = self.mappingDict(eventlogLabeling)

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

    def outputToArray(self, output):
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

    def mappingDict(self, eventlogLabeling):
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

    def getResult(self):
        return self.result

    def getAmount(self):
        return len(self.result)