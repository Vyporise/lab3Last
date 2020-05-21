def Huffman(signs,weights):
    way = sort(signs,weights)
    left0=''
    right0=''
    word=''
    while len(way)>1:
        treemap[way[0] + way[1]+'0'] = way[0]
        treemap[way[0] + way[1] + '1'] = way[1]
        weights[way[0] + way[1]] = weights[way[0]] + weights[way[1]]
        word = way[0]+way[1]
        way[0] += way[1]
        way.pop(1)
        way = sort(way, weights)
    treemapNumbers('0',treemap[word+'0'])
    treemapNumbers('1',treemap[word+'1'])

def treemapNumbers(code,word):

    treemapNums[code]=word
    codes[word]=code
    if(treemap.get(word+'0') != None):
        treemapNumbers(code+'0',treemap[word+'0'])
    if(treemap.get(word+'1') != None):
        treemapNumbers(code + '1', treemap[word + '1'])

def sort(signs,weights):
    result = []
    temp = {}
    for i in range(0,len(signs)):
        temp[signs[i]]=weights.get(signs[i])
    for i in sorted(weights.values()):
        for j in range(0,len(signs)):
            if i == temp.get(signs[j]):
                temp.pop(signs[j])
                result.append(signs[j])
    return result

def codMessage(string,codes):
    result = ''
    for i in range (0,len(string)):
        result += str(codes.get(string[i]))
    return result

def deCoding(message):
    print(treemap)
    print(treemapNums)
    result=''
    i=''
    j=0
    while message[0]!='|':
        i += message[j]
        while ( j<len(message)):
            j += 1
            if treemapNums.get(i) == None:
                result += treemapNums.get(i[:len(i)-1])
                i=''
                message = message[j-1:]
                j=0
                break
            if (j < len(message)):
                i += message[j]
    return result

def tree(codes,signs):
    result = {}
    for i in range(0,len(signs)):
        result[codes.get(signs[i])]=signs[i]
    return result

def sortByLength(signs, codes):
    length = 0
    max = 0
    result=[]
    buf=''
    for i in range(0,len(signs)):
        for j in range(i,len(signs)):
            if(len(codes[signs[j]])>length):
                length=len(codes[signs[j]])
                max = j

        result.append(signs[max])
        signs.pop(max)
        max=0
        length=0

    return result

inputString='aa'
f = open('1.txt','r',encoding='utf-8')
inputString = f.read()
f.close()
input1 = inputString

signs=[]
weights={}
fl = True
for i in range(0,len(inputString)):
    fl = True
    for j in range(0,len(signs)):
        if(signs[j]==inputString[i]):
            weights[signs[j]]=weights[signs[j]]+1
            fl = False
            break
    if (fl):
        signs.append(inputString[i])
        weights[inputString[i]] = 1

print(signs)
print(weights)

treemap = {}
codes = {}

treemapNums = {}
Huffman(signs, weights)
message =''
for i in range(0,len(signs)):
    print(signs[i] + ': ' +codes.get(signs[i]))
for i in range(0,len(inputString)):
    message += codes[inputString[i]]
f = open('2.txt','w',encoding='utf-8')
f.write(message)
f.close()
f = open('2.txt','r',encoding='utf-8')
message = f.read()
f.close()
message+='|'
print(message)
print('there')
messageDecoded = deCoding(message)
print('here')
print(inputString)
print(messageDecoded)
f = open('3.txt','w',encoding='utf-8')
f.write(messageDecoded)
f.close()
print('cortezhik')
a = (1,2,3)
print(a[0])
print(a[2])
print("Eto2Commit")