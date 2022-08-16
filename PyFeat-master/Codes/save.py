def saveCSV(X, Y, type,fileName):
    global F
    if type == 'full':
        F = open(fileName+'fullDataset.csv', 'w')

    else:
        if type == 'test':
            F = open(fileName+'testDataset.csv', 'w')

        else:
            if type == 'optimum':
                F = open(fileName+'optimumDataset.csv', 'w')

            else: None

    for x, y in zip(X, Y):
        for each in x:
            F.write(str(each) + ',')
        F.write(str(int(y)) + '\n')
    F.close()


def saveBestK(K):
    F = open('selectedIndex.txt', 'w')
    ensure = True
    for i in K:
        if ensure:
            F.write(str(i))
        else:
            F.write(','+str(i))
        ensure = False
    F.close()

def saveFeatures(tracking):
    F = open('trackingFeaturesStructure.txt', 'w')
    ensure = True
    for i in tracking:
        if ensure:
            F.write(str(i))
        else:
            F.write(',' + str(i))
        ensure = False
    F.close()




