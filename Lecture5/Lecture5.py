import glob
from pathlib import PurePath
import fileinput

def findFiles():
    # getting a list of path to all .txt files in project
    return glob.glob('**/*txt',recursive=True)

def getWordFreqs(path):# This function creates a bag of words
    word_freq_dict = {}
    for line in fileinput.input(path,openhook=fileinput.hook_encoded("utf-8-sig")):
        word_list = line.split() # creates a list of words
        for word in word_list:
            if word in word_freq_dict: word_freq_dict[word] += 1
            else: word_freq_dict[word] = 1

    return word_freq_dict

def getWordsLine(path,search_word):
    lineno_list =[]
    for line in fileinput.input(path,openhook=fileinput.hook_encoded("utf-8-sig")):
        word_list = line.split()
        if search_word in word_list:
            lineno_list.append(fileinput.filelineno())
    return lineno_list

def main():
    path_list = findFiles()
    for path in path_list:
        path = PurePath(path)
        print('The file %s has the following bag of word: \n%s'%(path.name,getWordFreqs(path)))

    search_word = "eBook"
    for path in path_list:
        path =PurePath(path)
        print('The word %s is found in file %s at the following lines:\n%s'%(search_word,path.name,getWordsLine(path,search_word)))

if __name__ == '__main__':
    main()