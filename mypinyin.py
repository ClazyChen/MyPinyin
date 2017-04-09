import queue
INF = 99.0

def loadIn(vStr):
    vDict = {}
    with open(vStr, 'r', encoding = 'utf-8') as f:
        for s in f.readlines():
            t = s.strip('\n').split(' ')
            vDict[t[0]] = t[1:]
    return vDict

def changeValueType(vDict):
    for key in vDict.keys():
        vDict[key] = float(vDict[key][0])
    return vDict

pinyinDict = loadIn('pinyin.txt')
characterDict = changeValueType(loadIn('character.txt'))
wordDict = changeValueType(loadIn('word.txt'))

answerList = []

while True:
#with open('input.txt', 'r', encoding = 'utf-8') as f:
    #sentence = input().split(' ')
    #for s in f.readlines():
    s = input()
    if True:
        s = s.lower()
        sentence = s.strip('\n').split(' ')
        length = len(sentence)
        graph = [[['', INF] for j in range(length + 1)] for i in range(length + 1)]
        for i in range(length):
            character = sentence[i]
            try:
                possibleCharacterList = pinyinDict[character]
                weight = INF + 1
                word = ''
                for char in possibleCharacterList:
                    tempWeight = characterDict.get(char, INF)
                    if weight > tempWeight:
                        weight = tempWeight
                        word = char
                graph[i][i + 1] = [word, weight]
            except:
                print('wrong input')
                exit()
        for i in range(length):
            for j in range(i, min(i + 3, length)):
                try:
                    pinyinList = [pinyinDict[character] for character in sentence[i:j+1]]
                    possibleWordList = ['']
                    for k in range(len(pinyinList)):
                        possibleWordList = [old + new for old in possibleWordList for new in pinyinList[k]]
                    weight = INF + 1
                    word = ''
                    for singleWord in possibleWordList:
                        tempWeight = wordDict.get(singleWord, INF)
                        if weight > tempWeight:
                            weight = tempWeight
                            word = singleWord
                    if weight < INF - 1:
                        graph[i][j + 1] = [word, weight]
                except:
                    print('wrong input')
                    exit()
        visitList = [[-1, INF * 100] for i in range(length + 1)]
        #[last, minDist]
        nowPoint = 0
        visitList[0] = [-1, 0]
        remainList = list(range(length + 1))
        while len(remainList) > 0:
            minLength = INF * 101
            for i in remainList:
                if visitList[i][1] < minLength:
                    nowPoint = i
                    minLength = visitList[i][1]
            for i in remainList:
                if i > nowPoint and graph[nowPoint][i][1] + visitList[nowPoint][1] < visitList[i][1]:
                    visitList[i] = [nowPoint, graph[nowPoint][i][1] + visitList[nowPoint][1]]
            remainList.remove(nowPoint)
        nowPoint = length;
        answer = ''
        while nowPoint > 0:
            answer = graph[visitList[nowPoint][0]][nowPoint][0] + answer
            nowPoint = visitList[nowPoint][0]
        #answerList.append(answer)
        print(answer)

#with open('output.txt', 'w', encoding = 'utf-8') as f:
#    for x in answerList:
#        f.write(x + '\n')

    
