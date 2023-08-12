#Apartmanlar_Oyunu
from Apartmanlar_Oyunu_bilgiler import *
import pygame

def ready_to_solve():
    global dikeyleme,yataylama
    for x,y in dikeyleme:
        if x==0 or y==0:
            return False
    for q,z in yataylama:
        if q==0 or z==0:
            return False
    return True


pygame.init()
ekr=pygame.display.set_mode(ekrbyt)
pygame.display.set_caption("Apartmanlar_Oyunu")

font=pygame.font.SysFont("Corbel",35)

BASLIK_yazi=font.render("APARTMANLAR OYUNU",True,beyaz)
OYNA_yazi=font.render("Oyna",True,beyaz)
COZUCU_yazi=font.render("Cozucu",True,beyaz)
CIK_yazi=font.render("Cik",True,beyaz)
BILGI_yazi=font.render("i",True,beyaz)
GERI_yazi=font.render("Geri",True,BLACK)
COZ_yazi=font.render("Coz",True,BLACK)
SIFIRLA_yazi=font.render("Sıfırla",True,BLACK)
HAKKINDA_yazi=font.render("Proje Takım Kaptanı=Kerem_Ali",True,(255,255,255))



sayi=0
pos=(0,0)
grid = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
dikeyleme=[[0, 0], [0, 0], [0, 0], [0, 0]]
yataylama=[[0, 0], [0, 0], [0, 0], [0, 0]]

    

quite=False

yer="Menu"

while not quite:
    if yer=="Menu":
        grid = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
        dikeyleme=[[0, 0], [0, 0], [0, 0], [0, 0]]
        yataylama=[[0, 0], [0, 0], [0, 0], [0, 0]]
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quite=True
                yer="Cik"
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if (BUTON_OYNA_STARTX<=mouse[0] <=BUTON_OYNA_STARTX+BUTON_OYNA_GENISLIK) and(BUTON_OYNA_STARTY<=mouse[1] <=BUTON_OYNA_STARTY+BUTON_OYNA_UZUNLUK):
                    #quite=True
                    yer="Oyna"
                elif (BUTON_COZUCU_STARTX<=mouse[0] <=BUTON_COZUCU_STARTX+BUTON_COZUCU_GENISLIK) and(BUTON_COZUCU_STARTY<=mouse[1] <=BUTON_COZUCU_STARTY+BUTON_COZUCU_UZUNLUK):
                    #quite=True
                    yer="Cozucu"
                elif (BUTON_CIK_STARTX<=mouse[0] <=BUTON_CIK_STARTX+BUTON_CIK_GENISLIK) and(BUTON_CIK_STARTY<=mouse[1] <=BUTON_CIK_STARTY+BUTON_CIK_UZUNLUK):
                    quite=True
                    yer="Cik"
                elif (BUTON_BILGI_STARTX<=mouse[0] <=BUTON_BILGI_STARTX+BUTON_BILGI_GENISLIK) and(BUTON_BILGI_STARTY<=mouse[1] <=BUTON_BILGI_STARTY+BUTON_BILGI_UZUNLUK):
                    #quite=True
                    yer="Bilgi"


        ekr.fill(mor)
        mouse=pygame.mouse.get_pos()
        if (BUTON_OYNA_STARTX<=mouse[0] <=BUTON_OYNA_STARTX+BUTON_OYNA_GENISLIK) and(BUTON_OYNA_STARTY<=mouse[1] <=BUTON_OYNA_STARTY+BUTON_OYNA_UZUNLUK):
            pygame.draw.rect(ekr,gri,[BUTON_OYNA_STARTX,BUTON_OYNA_STARTY,BUTON_OYNA_GENISLIK,BUTON_OYNA_UZUNLUK])
        else:
            pygame.draw.rect(ekr,koyu_gri,[BUTON_OYNA_STARTX,BUTON_OYNA_STARTY,BUTON_OYNA_GENISLIK,BUTON_OYNA_UZUNLUK])


        if (BUTON_COZUCU_STARTX<=mouse[0] <=BUTON_COZUCU_STARTX+BUTON_COZUCU_GENISLIK) and(BUTON_COZUCU_STARTY<=mouse[1] <=BUTON_COZUCU_STARTY+BUTON_COZUCU_UZUNLUK):
            pygame.draw.rect(ekr,gri,[BUTON_COZUCU_STARTX,BUTON_COZUCU_STARTY,BUTON_COZUCU_GENISLIK,BUTON_COZUCU_UZUNLUK])
        else:
            pygame.draw.rect(ekr,koyu_gri,[BUTON_COZUCU_STARTX,BUTON_COZUCU_STARTY,BUTON_COZUCU_GENISLIK,BUTON_COZUCU_UZUNLUK])


        if (BUTON_CIK_STARTX<=mouse[0] <=BUTON_CIK_STARTX+BUTON_CIK_GENISLIK) and(BUTON_CIK_STARTY<=mouse[1] <=BUTON_CIK_STARTY+BUTON_CIK_UZUNLUK):
            pygame.draw.rect(ekr,gri,[BUTON_CIK_STARTX,BUTON_CIK_STARTY,BUTON_CIK_GENISLIK,BUTON_CIK_UZUNLUK])
        else:
            pygame.draw.rect(ekr,koyu_gri,[BUTON_CIK_STARTX,BUTON_CIK_STARTY,BUTON_CIK_GENISLIK,BUTON_CIK_UZUNLUK])


        if (BUTON_BILGI_STARTX<=mouse[0] <=BUTON_BILGI_STARTX+BUTON_BILGI_GENISLIK) and(BUTON_BILGI_STARTY<=mouse[1] <=BUTON_BILGI_STARTY+BUTON_BILGI_UZUNLUK):
            pygame.draw.rect(ekr,gri,[BUTON_BILGI_STARTX,BUTON_BILGI_STARTY,BUTON_BILGI_GENISLIK,BUTON_BILGI_UZUNLUK],0,10)
        else:
            pygame.draw.rect(ekr,koyu_gri,[BUTON_BILGI_STARTX,BUTON_BILGI_STARTY,BUTON_BILGI_GENISLIK,BUTON_BILGI_UZUNLUK],0,10)

        ekr.blit(OYNA_yazi , (BUTON_OYNA_STARTX+28,BUTON_OYNA_STARTY+10))
        ekr.blit(COZUCU_yazi , (BUTON_COZUCU_STARTX+15,BUTON_COZUCU_STARTY+10))
        ekr.blit(BASLIK_yazi , (LABEL_BASLIK_STARTX,LABEL_BASLIK_STARTY))
        ekr.blit(CIK_yazi , (BUTON_CIK_STARTX+30,BUTON_CIK_STARTY+5))
        ekr.blit(BILGI_yazi , (BUTON_BILGI_STARTX+15,BUTON_BILGI_STARTY+5))

        
        pygame.display.update()
    if yer=="Oyna":
        from solver_icin2 import random_getir
        board,yataylama,dikeyleme=random_getir()
        while yer=="Oyna":
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quite=True
                    yer="Cik"
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    column=(pos[0]-box_kaydirma)//(box_genislik+box_bosluk)
                    row=(pos[1]-box_kaydirma) // (box_uzunluk +box_bosluk)
                    
                    if (BUTON_GERI_STARTX<=mouse[0] <=BUTON_GERI_STARTX+BUTON_GERI_GENISLIK) and(BUTON_GERI_STARTY<=mouse[1] <=BUTON_GERI_STARTY+BUTON_GERI_UZUNLUK):
                        yer="Menu"

                    elif (BUTON_SIFIRLA_STARTX<=mouse[0] <=BUTON_SIFIRLA_STARTX+BUTON_SIFIRLA_GENISLIK) and(BUTON_SIFIRLA_STARTY<=mouse[1] <=BUTON_SIFIRLA_STARTY+BUTON_SIFIRLA_UZUNLUK):
                       grid = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
                    elif -1<row<4 and -1<column<4:
                        grid[row][column] =sayi

                    
                    

                elif event.type == pygame.KEYDOWN:
                    if(-1 < event.key - 48 <5):
                        sayi=event.key-48


            color = WHITE

            ekr.fill(mor)

            mouse=pygame.mouse.get_pos()





            if (BUTON_GERI_STARTX<=mouse[0] <=BUTON_GERI_STARTX+BUTON_GERI_GENISLIK) and(BUTON_GERI_STARTY<=mouse[1] <=BUTON_GERI_STARTY+BUTON_GERI_UZUNLUK):
                pygame.draw.rect(ekr,GREEN,[BUTON_GERI_STARTX,BUTON_GERI_STARTY,BUTON_GERI_GENISLIK,BUTON_GERI_UZUNLUK])
            else:
                pygame.draw.rect(ekr,RED,[BUTON_GERI_STARTX,BUTON_GERI_STARTY,BUTON_GERI_GENISLIK,BUTON_GERI_UZUNLUK])

            if (BUTON_SIFIRLA_STARTX<=mouse[0] <=BUTON_SIFIRLA_STARTX+BUTON_SIFIRLA_GENISLIK) and(BUTON_SIFIRLA_STARTY<=mouse[1] <=BUTON_SIFIRLA_STARTY+BUTON_SIFIRLA_UZUNLUK):
                pygame.draw.rect(ekr,gri,[BUTON_SIFIRLA_STARTX,BUTON_SIFIRLA_STARTY,BUTON_SIFIRLA_GENISLIK,BUTON_SIFIRLA_UZUNLUK])
            else:
                pygame.draw.rect(ekr,koyu_gri,[BUTON_SIFIRLA_STARTX,BUTON_SIFIRLA_STARTY,BUTON_SIFIRLA_GENISLIK,BUTON_SIFIRLA_UZUNLUK])


            for x in range(2):
                for eleman in range(4):
                    pygame.draw.rect(ekr,
                                     color,
                                     [(box_bosluk + box_genislik) * x*7+ box_bosluk+50,
                                      (box_bosluk + box_uzunluk) * eleman + box_bosluk+box_kaydirma,
                                      box_genislik,
                                      box_uzunluk],2)
                    yazi=font.render("{}".format(yataylama[eleman][x]),True,beyaz)
                    ekr.blit(yazi,((box_bosluk + box_genislik) * x*7+ box_bosluk+60,(box_bosluk + box_uzunluk) * eleman + box_bosluk+box_kaydirma))
                    

            for y in range(2):
                for eleman in range(4):
                    pygame.draw.rect(ekr,
                                     color,
                                     [(box_bosluk + box_genislik) * eleman+ box_bosluk+box_kaydirma,
                                      (box_bosluk + box_uzunluk) * y*7 + box_bosluk+50,
                                      box_genislik,
                                      box_uzunluk],2)
                    
                    yazi=font.render("{}".format(dikeyleme[eleman][y]),True,beyaz)
                    ekr.blit(yazi,((box_bosluk + box_genislik) * eleman+ box_bosluk+box_kaydirma+15,(box_bosluk + box_uzunluk) * y*7 + box_bosluk+50))
                    


            for row in range(4):
                for column in range(4):
                    color = WHITE
                    
                    pygame.draw.rect(ekr,
                                     color,
                                     [(box_bosluk + box_genislik) * column + box_bosluk+box_kaydirma,
                                      (box_bosluk + box_uzunluk) * row + box_bosluk+box_kaydirma,
                                      box_genislik,
                                      box_uzunluk],2)
                    yazi=font.render("{}".format(grid[row][column]),True,beyaz)
                    if not grid[row][column]==0:
                        ekr.blit(yazi,((box_bosluk + box_genislik) * column + box_bosluk+box_kaydirma+15,
                                      (box_bosluk + box_uzunluk) * row + box_bosluk+box_kaydirma+4))

            

            
            if grid==board:
                ekr.blit(font.render("Kazandiniz!".format(pos,sayi),True,beyaz),(25,25))
            else:
                kord_yazi=font.render("secilen sayi={}".format(sayi),True,beyaz)
                ekr.blit(kord_yazi,(25,25))
                
            ekr.blit(GERI_yazi,(BUTON_GERI_STARTX+8,BUTON_GERI_STARTY+10))
            ekr.blit(SIFIRLA_yazi,(BUTON_SIFIRLA_STARTX+8,BUTON_SIFIRLA_STARTY+10))

            pygame.display.update()

    if yer=="Cozucu":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quite=True
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if (BUTON_COZ_STARTX<=mouse[0] <=BUTON_COZ_STARTX+BUTON_COZ_GENISLIK) and(BUTON_COZ_STARTY<=mouse[1] <=BUTON_COZ_STARTY+BUTON_COZ_UZUNLUK):
                    if ready_to_solve():
                        from apartmanlar_oyunu_solver2 import solve
                        cozumler=solve(dikeyleme,yataylama)
                        if len(cozumler)>0:
                            grid=cozumler[0]
                        else:
                            print("cozumu yok")
                            print("cozum sayisi={}".format(len(cozumler)))
                elif (BUTON_GERI_STARTX<=mouse[0] <=BUTON_GERI_STARTX+BUTON_GERI_GENISLIK) and(BUTON_GERI_STARTY<=mouse[1] <=BUTON_GERI_STARTY+BUTON_GERI_UZUNLUK):
                    yer="Menu"

                pos=pygame.mouse.get_pos()
                column=(pos[0]-box_kaydirma)//(box_genislik+box_bosluk)
                row=(pos[1]-box_kaydirma) // (box_uzunluk +box_bosluk)
                if (-1<row<4 and (column==-2 or column==5)) or  (-1<column<4 and (row==-2 or row==5)):
                    if (-1<row<4 and (column==-2 or column==5)):
                        if column==-2:
                            yataylama[row][0]=sayi
                        elif column==5:
                            yataylama[row][1]=sayi
                    elif (-1<column<4 and (row==-2 or row==5)):
                        if row==-2:
                            dikeyleme[column][0]=sayi
                        elif row==5:
                            dikeyleme[column][1]=sayi

                    

        


                
                

            elif event.type == pygame.KEYDOWN:
                if(-1 < event.key - 48 <5):
                    sayi=event.key-48




        color = WHITE

        ekr.fill(mor)

        mouse=pygame.mouse.get_pos()

        if (BUTON_COZ_STARTX<=mouse[0] <=BUTON_COZ_STARTX+BUTON_COZ_GENISLIK) and(BUTON_COZ_STARTY<=mouse[1] <=BUTON_COZ_STARTY+BUTON_COZ_UZUNLUK):
            pygame.draw.rect(ekr,GREEN,[BUTON_COZ_STARTX,BUTON_COZ_STARTY,BUTON_COZ_GENISLIK,BUTON_COZ_UZUNLUK])
        else:
            pygame.draw.rect(ekr,RED,[BUTON_COZ_STARTX,BUTON_COZ_STARTY,BUTON_COZ_GENISLIK,BUTON_COZ_UZUNLUK])
        if (BUTON_GERI_STARTX<=mouse[0] <=BUTON_GERI_STARTX+BUTON_GERI_GENISLIK) and(BUTON_GERI_STARTY<=mouse[1] <=BUTON_GERI_STARTY+BUTON_GERI_UZUNLUK):
            pygame.draw.rect(ekr,GREEN,[BUTON_GERI_STARTX,BUTON_GERI_STARTY,BUTON_GERI_GENISLIK,BUTON_GERI_UZUNLUK])
        else:
            pygame.draw.rect(ekr,RED,[BUTON_GERI_STARTX,BUTON_GERI_STARTY,BUTON_GERI_GENISLIK,BUTON_GERI_UZUNLUK])



        for x in range(2):
            for eleman in range(4):
                pygame.draw.rect(ekr,
                                 color,
                                 [(box_bosluk + box_genislik) * x*7+ box_bosluk+50,
                                  (box_bosluk + box_uzunluk) * eleman + box_bosluk+box_kaydirma,
                                  box_genislik,
                                  box_uzunluk],2)
                yazi=font.render("{}".format(yataylama[eleman][x]),True,beyaz)
                ekr.blit(yazi,((box_bosluk + box_genislik) * x*7+ box_bosluk+60,(box_bosluk + box_uzunluk) * eleman + box_bosluk+box_kaydirma))
                

        for y in range(2):
            for eleman in range(4):
                pygame.draw.rect(ekr,
                                 color,
                                 [(box_bosluk + box_genislik) * eleman+ box_bosluk+box_kaydirma,
                                  (box_bosluk + box_uzunluk) * y*7 + box_bosluk+50,
                                  box_genislik,
                                  box_uzunluk],2)
                
                yazi=font.render("{}".format(dikeyleme[eleman][y]),True,beyaz)
                ekr.blit(yazi,((box_bosluk + box_genislik) * eleman+ box_bosluk+box_kaydirma+15,(box_bosluk + box_uzunluk) * y*7 + box_bosluk+50))
                


        for row in range(4):
            for column in range(4):
                color = WHITE
                
                pygame.draw.rect(ekr,
                                 color,
                                 [(box_bosluk + box_genislik) * column + box_bosluk+box_kaydirma,
                                  (box_bosluk + box_uzunluk) * row + box_bosluk+box_kaydirma,
                                  box_genislik,
                                  box_uzunluk],2)
                yazi=font.render("{}".format(grid[row][column]),True,beyaz)
                if not grid[row][column]==0:
                    ekr.blit(yazi,((box_bosluk + box_genislik) * column + box_bosluk+box_kaydirma+15,
                                  (box_bosluk + box_uzunluk) * row + box_bosluk+box_kaydirma+4))

        kord_yazi=font.render("secilen sayi={}".format(sayi),True,beyaz)

        ekr.blit(kord_yazi,(25,25))
        ekr.blit(COZ_yazi,(BUTON_COZ_STARTX+15,BUTON_COZ_STARTY+15))
        ekr.blit(GERI_yazi,(BUTON_GERI_STARTX+8,BUTON_GERI_STARTY+10))

        pygame.display.update()

    if yer=="Bilgi":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quite=True
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if (BUTON_GERI_STARTX<=mouse[0] <=BUTON_GERI_STARTX+BUTON_GERI_GENISLIK) and(BUTON_GERI_STARTY<=mouse[1] <=BUTON_GERI_STARTY+BUTON_GERI_UZUNLUK):
                    #quite=True
                    yer="Menu"

        ekr.fill(mor)
        mouse=pygame.mouse.get_pos()

        if (BUTON_GERI_STARTX<=mouse[0] <=BUTON_GERI_STARTX+BUTON_GERI_GENISLIK) and(BUTON_GERI_STARTY<=mouse[1] <=BUTON_GERI_STARTY+BUTON_GERI_UZUNLUK):
            pygame.draw.rect(ekr,GREEN,[BUTON_GERI_STARTX,BUTON_GERI_STARTY,BUTON_GERI_GENISLIK,BUTON_GERI_UZUNLUK])
        else:
            pygame.draw.rect(ekr,RED,[BUTON_GERI_STARTX,BUTON_GERI_STARTY,BUTON_GERI_GENISLIK,BUTON_GERI_UZUNLUK])
        
        ekr.blit(HAKKINDA_yazi,(LABEL_HAKKINDA_STARTX+8,LABEL_HAKKINDA_STARTY+10))
        ekr.blit(GERI_yazi,(BUTON_GERI_STARTX+8,BUTON_GERI_STARTY+10))
        pygame.display.update()

        
        
        

pygame.quit()
