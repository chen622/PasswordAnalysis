
#分析 中文英文top10
with open("letter_analyze.txt", encoding='utf-8') as file_obj:
    line = file_obj.readline()
    line = line[2:]
    line = line[:-2]
    # print(line)
    kk = line.split("}, {")
    # print(kk[0])
    # print(kk[1])
    name = list()
    password= list()
    email= list()
    typ = list()
    tt = dict()
    pinyin = dict()
    english = dict()
    other = dict()
    Sum = 0
    for p in range(0,max(len(kk),10)):
        # print(kk[p])
        sp = kk[p].split(", ")
        o = sp[0].split(": ")
        if (sp[0] == "\'name\': \'191569\'"):
            continue
        if (sp[0] == "\'name\': \'threeboy\'"):
            continue
        if (sp[0] == "\'name\': \'quickball\'"):
            continue
        if (sp[0]== "\'name\': \'2547\'"):
            # print(o[1].strip("\'"))
            kk[p] = kk[p].replace("tjhussain@msn.com, tjhussain@gmail.com","tjhussain@msn.com")
            # print(kk[p])
            sp = kk[p].split(", ")
        elif(sp[0] == "\'name\': \'1196\'"):
            kk[p] = kk[p].replace("ramanindu@yahoo.com, ramanindu@hotmail.com", "ramanindu@yahoo.com")
            sp = kk[p].split(", ")
        # print(sp)
        a1 = sp[0].split(":")[1].lstrip().strip("\'")
        a2 = sp[1].split(":")[1].lstrip().strip("\'")
        a3 = sp[2].split(":")[1].lstrip().strip("\'")
        a4 = sp[3].split(":")[1].lstrip().strip("\'")

        name.append(a1)
        password.append(a2)
        email.append(a3)
        typ.append(a4)

        # print(a1,a2,a3,a4)

        # if(sp[3]!=None):
        if(len(sp)!=4):
            print(kk[p])
        tt[a4] = tt.get(a4, 0) + 1
        Sum = Sum + 1
        if(a4=="Pinyin"):
            # print(/"ok")
            pinyin[a2] = pinyin.get(a2,0) + 1
        elif(a4=="English"):
            # print("okok")
            english[a2] = english.get(a2,0) + 1
        else:
            other[a2] = other.get(a2,0) + 1
        # print(sp[0])
        # print(sp[1])
        # print("\n")

    print(tt)
    print(Sum)
    epoch = 10

    f = open("top1000.txt", 'w', encoding='utf-8')

    p = sorted(pinyin.items(), key=lambda item:item[1], reverse=True)
    pp = sorted(english.items(), key=lambda item:item[1], reverse=True)
    ppp = sorted(other.items(), key=lambda item:item[1], reverse=True)
    print("--top10:Pinyin--")
    for i in range(0,epoch):
        a1 = str(p[i]).strip('(').strip(')').split(',')[0].strip('\'').strip()
        a2 = str(p[i]).strip('(').strip(')').split(',')[1].strip()
        a3 = int(a2) / Sum
        a3 = format(a3, '.6f')
        ll = len(a1)
        print('L '+str(a1)+' '+str(a2)+' '+str(a3)+' '+str(ll))
        S = 'L '+str(a1)+' '+str(a2)+' '+str(a3)+' '+str(ll)+'\n'
        f.write(S)
        # print()
    print("--top10:Endlish--")
    for i in range(0,epoch):
        a1 = str(pp[i]).strip('(').strip(')').split(',')[0].strip('\'').strip()
        a2 = str(pp[i]).strip('(').strip(')').split(',')[1].strip()
        a3 = int(a2)/Sum
        a3 = format(a3, '.6f')
        ll = len(a1)
        print('L ' + str(a1) + ' ' + str(a2) + ' ' + str(a3) + ' ' + str(ll))
        S = 'L ' + str(a1) + ' ' + str(a2) + ' ' + str(a3) + ' ' + str(ll) + '\n'
        f.write(S)
    print("--top10:Other--")
    for i in range(1,epoch):
        a1 = str(ppp[i]).strip('(').strip(')').split(',')[0].strip('\'').replace(' ','').strip()
        a2 = str(ppp[i]).strip('(').strip(')').split(',')[1].strip()
        ll = len(a1)
        a3 = int(a2) / Sum
        a3 = format(a3, '.6f')
        type1 = 0
        type2 = 0
        type3 = 0
        for test in a1:
            if test.isalpha():
                type1 = 1
            elif test.isalnum():
                type2 = 1
            else:
                type3 = 1
        if type1 == 1 and type2 == 0 and type3 == 0:
            TT = 'L'
        elif type1 == 0 and type2 == 1 and type3 == 0:
            TT = 'D'
        elif type1 == 0 and type2 == 1 and type3 == 0:
            TT = 'O'
        else: TT = 'U'
        # else: continue
        print(TT+' ' + str(a1) + ' ' + str(a2) + ' ' + str(a3) + ' ' + str(ll))
        S = TT+' ' + str(a1) + ' ' + str(a2) + ' ' + str(a3) + ' ' + str(ll) + '\n'
        f.write(S)
    # while line != '':
    #     print(line)
    #     line = file_obj.readline()
    f.close()