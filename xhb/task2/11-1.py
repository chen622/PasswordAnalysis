def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if [item] not in C1:
                C1.append([item])
    C1.sort()
    return map(frozenset, C1)


def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                ssCnt[can] = ssCnt.get(can, 0) + 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key] / numItems
        if support >= minSupport:
            retList.insert(0, key)
        supportData[key] = support
    return retList, supportData


def aprioriGen(Lk, k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(Lk[i])[: k - 2];
            L2 = list(Lk[j])[: k - 2];
            L1.sort();
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList


def apriori(dataSet, minSupport=0.5):
    C1 = createC1(dataSet)
    D = map(set, dataSet)
    L1, suppData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2

    while (len(L[k - 2]) > 0):
        Ck = aprioriGen(L[k - 2], k)
        Lk, supK = scanD(D, Ck, minSupport)
        suppData.update(supK)
        L.append(Lk)
        k += 1
    return L, suppData

def txt_wrap_by(start_str, end, html):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()

def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet] / supportData[freqSet - conseq]
        if conf >= minConf:
            # print(type(freqSet - conseq))
            # print(freqSet - conseq)
            new1 = txt_wrap_by("[", "]", str(freqSet - conseq))
            new2 = txt_wrap_by("[", "]", str(conseq))
            # print(Hash[int(new1)])
            print(Hash[int(new1)], '-->', Hash[int(new2)], 'conf:', conf)
            brl.append((Hash[int(new1)], '-->', Hash[int(new2)], conf))
            # brl.append((freqSet - conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH


def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    m = len(H[0])

    if len(freqSet) > m + 1:
        Hmp1 = aprioriGen(H, m + 1)
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)

        if len(Hmp1) > 1:
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)


def generateRules(L, supportData, minConf=0.7):
    bigRuleList = []
    for i in range(1, len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]

            if i > 1:
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList

if __name__ == '__main__':
    myDat = []
    my = [[1,1],[2,2]]
    print(type(my))
    import  os

    Hash = {}
    i = 1
    with open('id.txt') as file_obj:
        contents = file_obj.readlines()
        for content in contents:
            spp = content.split(" ")
            if(spp is None):break
            for dd in spp:
                if(dd == ""):break
                Hash[i] = dd
                i = i + 1

    # for key in Hash.keys():
    #     print(str(key) + ':' + Hash[key])
    #
    # print("ok\n")
    with open('Password_number3.txt') as file_obj:
        contents = file_obj.readlines()
        for u in contents:
            u = u.strip('\n')
            u = u.strip(' ')
            # print(contents)
            sp = u.split(' ')
            tmp_a = list()
            # print(sp)
            for o in sp:
                # print(type(o))
                tmp_a.append( int(o) );
            myDat.append(tmp_a)
    print(type(myDat))
    # print(myDat)
    L, suppData = apriori(myDat, 0.05)
    rules = generateRules(L, suppData, minConf=0.05)
    # L, suppData = apriori(myDat, 0.5)
    # rules = generateRules(L, suppData, minConf=0.7)
    # print 'rules:\n', rules
    print("\n".join(str(i) for i in rules))