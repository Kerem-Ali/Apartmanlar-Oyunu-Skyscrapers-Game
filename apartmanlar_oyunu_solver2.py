#Apartmanlar Oyunu Solver

dikeyleme=[[2, 2], [2, 2], [3, 1], [1, 3]]
yataylama=[[3, 1], [1, 2], [2, 3], [2, 2]]

def solve(dikeyleme,yataylama):
    def perm2(lst):
        if len(lst)==0:
            yield []
        elif len(lst)==1:
            yield lst
        else:
            for i in range(len(lst)):
                x=lst[i]
                xs=lst[:i]+lst[i+1:]
                for p in perm2(xs):
                    yield ([x]+p)

    def soldan(board):
            sayi=0
            eb=0
            for eleman in board:
                if eleman>eb:
                    eb=int(eleman)
                    sayi+=1
            return sayi
        
    def sagdan(board):
            brd=board[::-1]
            syi=0
            ebu=0
            for elemn in brd:
                if elemn>ebu:
                    ebu=int(elemn)
                    syi+=1
            return syi
    liste=[]
    for x in range(4):
        
        bos=[]
        for perm in perm2([1,2,3,4]):
            if soldan(perm)==yataylama[x][0] and sagdan(perm)==yataylama[x][1]:
                bos.append(perm)
        liste.append(bos)




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
                            frees.append([l1[j],l2[k],l3[l],l4[m]])
        return frees



    def check_board(board):
        a=True

        def yukari():
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

            return listw

        def asagi():
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

            return lista

        for y in range(4):
            if dikeyleme[y][0]!=yukari()[y]:
                a= False
            elif dikeyleme[y][1]!=asagi()[y]:
                a= False
        return a
        

    def check_real(board):
        for sira in board:
            if len(set(sira))!=4:
                return False
        for q in range(4):
            li=board[0][q],board[1][q],board[2][q],board[3][q]
            if len(set(li))!=4:
                return False
        return True
            



    cozumler=[]
    for q in (fadc(liste[0],liste[1],liste[2],liste[3])):
        if check_board(q) and check_real(q):
            cozumler.append(q)
    return cozumler
            
        

    
