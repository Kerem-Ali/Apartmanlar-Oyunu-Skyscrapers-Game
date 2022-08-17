#Apartmanlar Oyunu
import random


def random_getir():
    board=[]
    sayilar=[1,2,3,4]


    def listele(*args):
        liste=[]
        for a in args:
            liste.append(a)
        return liste

    def fadc(l1,l2,l3,l4):
        frees=[]
        for j in range(0,len(l1)):
            for k in range(0,len(l2)):
                for l in range(0,len(l3)):
                    for m in range(0,len(l4)):
                        if len(set(listele(l1[j],l2[k],l3[l],l4[m])))==4:
                            frees.append([l1[j],l2[k],l3[l],l4[m]])
        return frees

    def dikeyleme(board,index):
        fr=[1,2,3,4]
        for satir in range(len(board)):
            if board[satir][index] in fr:
                fr.remove(board[satir][index])
        return fr








    def yataylar_dikeyler(board):
        yataylar=[]
        dikeyler=[]

        def yukari():
            global listw
            listw=[]
            sayi=0
            eb=0
            for q in range (4):
                sayi=0
                eb=0
                for s in range(4): 
                    if board[s][q]>eb:
                        eb=int(board[s][q])
                        sayi+=1
                listw.append(sayi)

            lisq="  "
            for eleman in listw:
            
                lisq+=str(eleman)
                lisq+="  "
            return lisq

        def asagi():
            global lista
            lista=[]
            sayi=0
            eb=0
            for satir in range (4):
                sayi=0
                eb=0
                for s in range(3,-1,-1): 
                    if board[s][satir]>eb:
                        eb=int(board[s][satir])
                        sayi+=1
                lista.append(sayi)

            lisz="  "
            for eleman in lista:
            
                lisz+=str(eleman)
                lisz+="  "
            return lisz

            
        
        def soldan(index):
            sayi=0
            eb=0
            for eleman in board[index]:
                if eleman>eb:
                    eb=int(eleman)
                    sayi+=1
            return sayi

        def sagdan(index):
            brd=board[index][::-1]
            syi=0
            ebu=0
            for elemn in brd:
                if elemn>ebu:
                    ebu=int(elemn)
                    syi+=1
            return syi

        solda=[]
        sagda=[]
        for x in range(4):
            solda.append(soldan(x))
            sagda.append(sagdan(x))

        for q in range(4):
            yataylar.append([solda[q],sagda[q]])
        yukari()
        asagi()

        for q in range(4):
            dikeyler.append([listw[q],lista[q]])

        return yataylar,dikeyler




    from apartmanlar_oyunu_solver2 import solve


    def random_olustur():
        board=[]
        for q in range(4-len(board)):
            frees=[]
            for ys in range(4):
                free=dikeyleme(board,ys)
                frees.append(free)
            lis1=frees[0]
            lis2=frees[1]
            lis3=frees[2]
            lis4=frees[3]
            a=fadc(lis1,lis2,lis3,lis4)
            board.append(random.choice(a))
        return board

    secim=random_olustur()
    yataylar=yataylar_dikeyler(secim)[0]
    dikeyler=yataylar_dikeyler(secim)[1]
    while len(solve(yataylar,dikeyler))!=1:
        secim=random_olustur()
        yataylar=yataylar_dikeyler(secim)[0]
        dikeyler=yataylar_dikeyler(secim)[1]
    return secim,yataylar,dikeyler



    

                
        


    
