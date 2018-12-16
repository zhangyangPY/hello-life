def IpExe():
    stra = '25525'
    length = len(stra)
    # print(length)

    lista = []
    for a in range(1, 4):
        # print(a)
        for b in range(1, 4):
            for c in range(1, 4):
                for d in range(1, 4):
                    if a + b + c + d == length:
                        lista.append([a, b, c, d])
                        # print(lista)

    listb = []

    for item in lista:
        a, b, c, d = item
        str1 = stra[:a]
        str2 = stra[a:a+b]
        str3 = stra[a+b:a+b+c]
        str4 = stra[a+b+c:]

        if int(str1) in range(256) and int(str2) in range(256) and int(str3) in range(256) and int(str4) in range(256):
            listb.append(".".join([str1, str2, str3, str4]))

    print(listb)




