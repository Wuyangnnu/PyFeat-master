def readFASTAs(fileName):
    '''
    :param fileName:
    :return: genome sequences
    '''
    with open(fileName, 'r') as file:
        v = []
        genome = ''
        for line in file:
            if line[0] != '>':
                genome += line.strip()
            else:
                v.append(genome.upper())
                genome = ''
        v.append(genome.upper())
        del v[0]
        return v


def readFASTAs_V2(fileName):
    '''
    :param fileName:
    :return: genome sequences
    '''
    with open(fileName, 'r') as file:
        x = []
        y = []
        genome = ''
        txt = ""
        for line in file:
            # 处理labels
            if line.startswith(">DEG"):
                y.append(1)
                txt += "1" + "\n"
            elif line.startswith(">DNEG"):
                y.append(0)
                txt += "0" + "\n"
            # 处理基因
            if line[0] != '>':
                genome += line.strip()
            else:
                x.append(genome.upper())
                genome = ''
        # 最后一个元素
        x.append(genome.upper())
        del x[0]
        print_log = open(fileName+"-label.txt", "w")
        print(txt, file=print_log)
        print_log.close()

        return x, y


def readLabels(fileName):
    '''
    :param fileName:
    :return: label of genome sequences
    '''
    with open(fileName, 'r') as file:
        v = []
        for line in file:
            if line != '\n':
                v.append((line.replace('\n', '')).replace(' ', ''))
        return v


def fetchXY(FASTAs, Labels):
    # print('Please, enter the full path of FASTA file:')
    # X = readFASTA(input().strip())
    #
    # print('Please, enter the full path of label file:')
    # Y = readLabel(input().strip())
    #
    # from sklearn.preprocessing import LabelEncoder
    # Y = LabelEncoder().fit_transform(Y)
    #
    # assert len(X)==len(Y), 'Numbers of FASTA and numbers of type are not equal.'
    X, Y = readFASTAs_V2(FASTAs)

    from sklearn.preprocessing import LabelEncoder
    Y = LabelEncoder().fit_transform(Y)

    assert len(X) == len(Y), 'Numbers of sequence and number of labels are not equal.'

    return X, Y
