# -*- coding: utf-8 -*-
def loadDict():
    file_dict = open('dir.txt','rb')
    Dict = {}
    for line in file_dict.readlines():
        tmp=[]
        lineVec = str(line).strip().split('\\xef\\xa3\\xb5')
        for content in lineVec[1:-1]:
            if '.' in str(content) :#and len(content)<=6:
                tmp.append(content)
        Dict[lineVec[0]] = tmp
    Dict_final ={}
    for key in Dict.keys():
        Dict_final[key.replace("b'",'')] = Dict[key]
    return Dict_final

def htmlParse():
    import re
    from bs4 import BeautifulSoup
    file_html = open('HTML.html','rb')
    file_txt = open('irregular verbs.txt','w+')

    soup = BeautifulSoup(file_html,'html.parser')
    tr = soup.find_all('tr')
    for i in range(1,len(tr)):
        tmpStr = ''
        tds = tr[i].find_all('td')
        #print(tds[1])
        L1 = tds[1].text.strip().split(',')
        L2 = tds[2].text.strip().split(',')
        tmpStr = tmpStr + str(tds[0].text.strip())
        for content in L1:
            tmpStr = tmpStr +'\t'+ str(content)
        for content in L2:
            tmpStr = tmpStr + '\t' + str(content)
        tmpStr = tmpStr + '\n'
        file_txt.write(tmpStr)


def loadIrVerb():    # 读入不规则动词表
    file_dict = open('irregular verbs.txt','rb')
    Dict = {}
    for line in file_dict.readlines():
        lineVec = str(line).replace('\\r\\n','').split('\\t')
        for word in lineVec[1:-1]:
            Dict[str(word)] = str(lineVec[0])
    return Dict

def loadIrNoun():
    file_dict = open('irregular nouns.txt','rb')
    Dict = {}
    for line in file_dict.readlines():
        lineVec = str(line).strip().split('\\t')
        #print(lineVec[1],lineVec[3])
        Dict[lineVec[3]] = lineVec[1]
    return Dict

def verbJudge(word,wholeDict):
    flag = False
    if 'ies' == word[-3:len(word)]:
        tmp = word[0:-3]+'y'
        if tmp in wholeDict.keys():
            print("original form: " + tmp)
            tmpStr = ''
            for inst in wholeDict[tmp]:
                tmpStr += (inst + '\t')
            print("part of speech: " + tmpStr)
            flag = True
    if not flag:
        if 'es' == word[-2:len(word)]:
            tmp = word[0:-2]
            if tmp in wholeDict.keys():
                print("original form: " + tmp)
                tmpStr = ''
                for inst in wholeDict[tmp]:
                    tmpStr += (inst + '\t')
                print("part of speech: " + tmpStr)
                flag = True
    if not flag:
        if 's' == word[-1:len(word)]:
            tmp = word[0:-1]
            if tmp in wholeDict.keys():
                print("original form: " + tmp)
                tmpStr = ''
                for inst in wholeDict[tmp]:
                    tmpStr += (inst + '\t')
                print("part of speech: " + tmpStr)
                flag = True
    if not flag:
        if 'ing' == word[-3:len(word)] and word[-4] == word[-5]:
            tmp = word[0:-4]
            if tmp in wholeDict.keys():
                print("original form: " + tmp)
                tmpStr = ''
                for inst in wholeDict[tmp]:
                    tmpStr += (inst + '\t')
                print("part of speech: " + tmpStr)
                flag = True
    if not flag:
        if 'ying' == word[-4:len(word)]:
            tmp = word[0:-4] + 'ie'
            if tmp in wholeDict.keys():
                print("original form: " + tmp)
                tmpStr = ''
                for inst in wholeDict[tmp]:
                    tmpStr += (inst + '\t')
                print("part of speech: " + tmpStr)
                flag = True
    if not flag:
        if 'ing' == word[-3:len(word)]:
            if word[0:-3] in wholeDict.keys():
                tmp = word[0:-3]
                print("original form: " + tmp)
                tmpStr = ''
                for inst in wholeDict[tmp]:
                    tmpStr += (inst + '\t')
                print("part of speech: " + tmpStr)
                flag = True
            elif word[0:-3]+'e' in wholeDict.keys():
                tmp = word[0:-3]+'e'
                print("original form: " + tmp)
                tmpStr = ''
                for inst in wholeDict[tmp]:
                    tmpStr += (inst + '\t')
                print("part of speech: " + tmpStr)
                flag = True
    if not flag:
        if 'ed' == word[-2:len(word)] and word[-3]==word[-4]:
            tmp = word[0:-2] + word[-3]
            if tmp in wholeDict.keys():
                print("original form: " + tmp)
                tmpStr = ''
                for inst in wholeDict[tmp]:
                    tmpStr += (inst + '\t')
                print("part of speech: " + tmpStr)
                flag = True
    if not flag:
        if 'ied' == word[-3:len(word)]:
            tmp = word[0:-3] + 'y'
            if tmp in wholeDict.keys():
                print("original form: " + tmp)
                tmpStr = ''
                for inst in wholeDict[tmp]:
                    tmpStr += (inst + '\t')
                print("part of speech: " + tmpStr)
                flag = True
    if not flag:
        if 'ed' == word[-2:len(word)]:
            if word[0:-2] in wholeDict.keys():
                tmp = word[0:-2]
                print("original form: " + tmp)
                tmpStr = ''
                for inst in wholeDict[tmp]:
                    tmpStr += (inst + '\t')
                print("part of speech: " + tmpStr)
                flag = True
            elif word[0:-2]+'e' in wholeDict.keys():
                tmp = word[0:-2]+'e'
                print("original form: " + tmp)
                tmpStr = ''
                for inst in wholeDict[tmp]:
                    tmpStr += (inst + '\t')
                print("part of speech: " + tmpStr)
                flag = True
    return flag

def nounJudge(word,wholeDict):
    flag = False
    if 'ves' == word[-3:len(word)]:
        if word[0:-3]+'f' in wholeDict.keys():
            tmp = word[0:-3]+'f'
            print("original form: " + tmp)
            tmpStr = ''
            for inst in wholeDict[tmp]:
                tmpStr += (inst + '\t')
            print("part of speech: " + tmpStr)
            flag = True
        elif word[0:-3] + 'fe' in wholeDict.keys():
            tmp = word[0:-3]+'fe'
            print("original form: " + tmp)
            tmpStr = ''
            for inst in wholeDict[tmp]:
                tmpStr += (inst + '\t')
            print("part of speech: " + tmpStr)
            flag = True
    if not flag and 'ies' == word[-3:len(word)]:
        if word[0:-3]+'y' in wholeDict.keys():
            tmp = word[0:-3]+'y'
            print("original form: " + tmp)
            tmpStr = ''
            for inst in wholeDict[tmp]:
                tmpStr += (inst + '\t')
            print("part of speech: " + tmpStr)
            flag = True
    if not flag and 'es' == word[-2:len(word)]:
        if word[0:-2] in wholeDict.keys():
            tmp = word[0:-2]
            print("original form: " + tmp)
            tmpStr = ''
            for inst in wholeDict[tmp]:
                tmpStr += (inst + '\t')
            print("part of speech: " + tmpStr)
            flag = True
    if not flag and 's'==word[len(word)-1]:
        if word[0:-1] in wholeDict.keys():
            tmp = word[0:-1]
            print("original form: " + tmp)
            tmpStr = ''
            for inst in wholeDict[tmp]:
                tmpStr += (inst + '\t')
            print("part of speech: " + tmpStr)
            flag = True
    return flag

def otherJudge(word,wholeDict):
    flag = False
    flag = verbJudge(word, wholeDict)
    if not flag:
        flag = nounJudge(word, wholeDict)
    return flag

def main():
    irVerbDict = loadIrVerb()
    irNounDict = loadIrNoun()
    wholeDict = loadDict()

    #print(irNounDict)
    wordInput = input("Input an English word: ")
    if wordInput in wholeDict.keys():
        #print("1")
        print("original form: " + wordInput)
        tmpStr = ''
        for inst in wholeDict[wordInput]:
            tmpStr += (inst+'\t')
        print("part of speech: " + tmpStr)
    elif wordInput in irVerbDict.keys():
        #print("2")
        print("original form: " + irVerbDict[wordInput])
        tmpStr = ''
        for inst in wholeDict[irVerbDict[wordInput]]:
            tmpStr += (inst + '\t')
        print("part of speech: " + tmpStr)
    elif wordInput in irNounDict.keys():
        #print("3")
        print("original form: " + irNounDict[wordInput])
        tmpStr = ''
        for inst in wholeDict[irNounDict[wordInput]]:
            tmpStr += (inst + '\t')
        print("part of speech: " + tmpStr)
    else:
        #print("4")
        flag = otherJudge(wordInput,wholeDict)
        if not flag:
            print("Transformation Failure......")

if __name__ == '__main__':
    while 1:
        main()