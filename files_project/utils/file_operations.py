def readFile_data(filename="fileOperations_test.txt"):
    with open(filename) as fhandle:
        return fhandle.read().split('\n')


def saveFile_data(content, filename="fileOperations_test.txt"):
    with open(filename, 'a') as fhandle:
        fhandle.write(content)