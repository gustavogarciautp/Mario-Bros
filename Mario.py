import pygame
import math
#from nivel1 import *
#from nivel2 import *
#from nivel3 import *
#from nivel3princesa import *
from bonusNivel1 import *

#Contantes globales
# Colores
NEGRO    = (   0,   0,   0)
BLANCO   = ( 255, 255, 255)
AZUL     = (   0,   0, 255)
ROJO     = ( 255,   0,   0)
VERDE    = (   0, 255,   0)

# Dimensiones pantalla
ANCHO = 600
ALTO  = 470
C=[(ANCHO/2)-20,0]


def recortar2(imagen, inicio, anchos, altos):
    
    sp_col = len(anchos)
    sp_fil = len(altos)
    x1, y1 = inicio
    temp = []
    for y in range(sp_fil):
        temp.append([])
        for x in range(sp_col):
            cuadro = (x1, y1, anchos[x], altos[y]) # posicion de una imagen
            recorte = imagen.subsurface(cuadro)
            temp[y].append(recorte)
            x1 += anchos[x]
        y1 += altos[y]
        x1 = inicio[0]
    return temp



def crearsuelo1(imagen,principio,limite,general):
        s=principio
        while(s<limite):
            su=Suelo(imagen)
            su.rect.x+=s
            su.rect.y=418
            general.add(su)
            s+=33.3

def crearsuelo3(imagen,principio,limite,general):
        s=principio
        while(s<limite):
            su=Suelo(imagen)
            su.rect.x+=s
            su.rect.y=418
            general.add(su)
            s+=15.5

def creartecho3(imagen,principio,limite,general):
        s=principio
        while(s<limite):
            su=Bloque2(imagen)
            su.rect.x+=s
            su.rect.y=49
            general.add(su)
            s+=17

def crearplataforma3(imagen,n,x,y,general):
    for i in range(n):
        pl=Suelo(imagen)
        pl.rect.x+=x
        pl.rect.y+=y
        general.add(pl)
        x+=15.5

def crearsuelob1(imagen,principio,limite,generalb1):   #SUELO DEL BONUS 1
        s=principio
        while(s<limite):
            su=Suelo(imagen)
            su.rect.x+=s
            su.rect.y=412
            generalb1.add(su)
            s+=36.6
def crearparedb1(imagen,principio,limite,generalb1):
    s=principio
    while(s<limite):
        p=Pared(imagen)
        p.rect.x=0
        p.rect.y+=s
        generalb1.add(p)
        s+=36.6

def crearsuelob3(imagen,principio,limite,general): #Suelos del BONUS 3
        s=principio
        while(s<limite):
            su=Suelo(imagen)
            su.rect.x+=s
            su.rect.y=418.5
            general.add(su)
            s+=20
def crearparedb3(imagen,principio,limite,general):
    s=principio
    while(s<limite):
        p=Pared(imagen)
        p.rect.x=0
        p.rect.y+=s
        general.add(p)
        s+=36.6

def crearsuelo1(imagen,principio,limite,general):
        s=principio
        while(s<limite):
            su=Suelo(imagen)
            su.rect.x+=s
            su.rect.y=418
            general.add(su)
            s+=33.3

def recorte(imagen,sp_fil,sp_col):
    #CARGA LA IMAGEN
    imagen=pygame.image.load(imagen).convert_alpha()#convert es para que se adapte al sistema
    ancho_img,alto_img= imagen.get_size()#get_size me develve el ancho y el alto de la imagen
    an_corte=ancho_img/sp_col
    al_corte=alto_img/sp_fil
    matriz=[]
    for i in range(sp_fil):
        fila=[]
        for j in range(sp_col):
            cuadro=((j*an_corte),(i*al_corte),an_corte,al_corte)#pide una posicion con los dos primeros y un ancho y un alto
            fila.append(imagen.subsurface(cuadro))
        matriz.append(fila)
    return matriz


class Suelo(pygame.sprite.Sprite):
    def __init__ (self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m= m
        self.dir=0
        self.x=0
        self.moviendo= False
        self.image=m[self.x][self.dir]
        self.rect= self.image.get_rect()
        self.var_x=0

    def update(self):
        self.rect.x+= self.var_x

class Tubo(pygame.sprite.Sprite):
    def __init__ (self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m= m
        self.dir=0
        self.x=0
        self.moviendo= False
        self.image=m[self.x][self.dir]
        self.rect= self.image.get_rect()
        self.var_x=0

    def update(self):
        self.rect.x+= self.var_x

class Bloque1(pygame.sprite.Sprite):
    def __init__ (self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m= m
        self.dir=0
        self.x=0
        self.moviendo= False
        self.image=m[self.x][self.dir]
        self.rect= self.image.get_rect()
        self.var_x=0

    def update(self):
        self.rect.x+= self.var_x

class Bloque2(pygame.sprite.Sprite):
    def __init__ (self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m= m
        self.dir=0
        self.x=0
        self.moviendo= False
        self.image=m[self.x][self.dir]
        self.rect= self.image.get_rect()
        self.var_x=0

    def update(self):
        self.rect.x+= self.var_x
        
class Bloque3(pygame.sprite.Sprite): #Piramide
    def __init__ (self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m= m
        self.dir=0
        self.x=0
        self.moviendo= False
        self.image=m[self.x][self.dir]
        self.rect= self.image.get_rect()
        self.var_x=0

    def update(self):
        self.rect.x+= self.var_x
class Bandera(pygame.sprite.Sprite):
    def __init__ (self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m= m
        self.dir=0
        self.x=0
        self.moviendo= False
        self.image=m[self.x][self.dir]
        self.rect= self.image.get_rect()
        self.var_x=0

    def update(self):
        self.rect.x+= self.var_x


class Lava(pygame.sprite.Sprite): 
    def __init__ (self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m= m
        self.dir=0
        self.x=0
        self.moviendo= False
        self.image=m[self.x][self.dir]
        self.rect= self.image.get_rect()
        self.var_x=0

    def update(self):
        self.rect.x+= self.var_x


class Puente(pygame.sprite.Sprite): 
    def __init__ (self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m= m
        self.dir=0
        self.x=0
        self.moviendo= False
        self.image=m[self.x][self.dir]
        self.rect= self.image.get_rect()
        self.var_x=0

    def update(self):
        self.rect.x+= self.var_x

class Martillo(pygame.sprite.Sprite): 
    def __init__ (self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m= m
        self.dir=0
        self.x=0
        self.moviendo= False
        self.image=m[self.x][self.dir]
        self.rect= self.image.get_rect()
        self.var_x=0

    def update(self):
        self.rect.x+= self.var_x

class Pared(pygame.sprite.Sprite):
    def __init__ (self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m= m
        self.dir=0
        self.x=0
        self.moviendo= False
        self.image=m[self.x][self.dir]
        self.rect= self.image.get_rect()
        self.var_x=0

    def update(self):
        self.rect.x+= self.var_x

class Plataforma(pygame.sprite.Sprite):
    def __init__ (self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m= m
        self.dir=0
        self.x=0
        self.moviendo= False
        self.image=m[self.x][self.dir]
        self.rect= self.image.get_rect()
        self.var_x=0

    def update(self):
        self.rect.x+= self.var_x

class Techo(pygame.sprite.Sprite):
    def __init__ (self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m= m
        self.dir=0
        self.x=0
        self.moviendo= False
        self.image=m[self.x][self.dir]
        self.rect= self.image.get_rect()
        self.var_x=0

    def update(self):
        self.rect.x+= self.var_x

class Jugador(pygame.sprite.Sprite):
	var_x = 0
	var_y = 0
	def __init__(self):
	    pygame.sprite.Sprite.__init__(self)
	    ancho = 40
	    alto = 60
	    self.image = pygame.Surface([ancho, alto])
	    self.tubos= []
	    self.image.fill(ROJO)
	    self.rect = self.image.get_rect()
	    self.salto=False

	def gravedad(self):
		if self.var_y==0:
			self.var_y=1
		else:
			self.var_y+=1.5

	def update(self):
		self.gravedad()
		self.rect.x+=self.var_x
		self.rect.y+=self.var_y
		ls_coltub=pygame.sprite.spritecollide(self,self.tubos,False)
		for elemen in ls_coltub:
			self.salto=False
			if (self.rect.y<elemen.rect.y) and (self.rect.x+self.rect[2]>elemen.rect.x) and (self.rect.x<elemen.rect.x+elemen.rect[2] and self.var_y>0):
				self.rect.y=elemen.rect.y-self.rect[3]
				self.var_y=0
			elif self.rect.x+self.rect[3]>elemen.rect.x:
				if self.rect.x<elemen.rect.x:
					self.rect.x=elemen.rect.x-self.rect[2]
				else:
					self.rect.x=elemen.rect.x+elemen.rect[2]
		if self.rect.y>ALTO-120:
			self.var_y=0
			self.rect.y=ALTO-120
			self.salto=False
		if self.rect.x<0:
			self.rect.x=0

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    pygame.display.set_caption("Mario Bros")
    fondo = pygame.image.load("NivelFinal.png")
    #m=recorte('Mariossolo2.png',1,21)

    #CARGAR IMAGENES DE TODOS LOS NIVELES
    fondon1= pygame.image.load('NivelFinal.png')
    fondofinaln1=pygame.image.load('N1.png')

    fondon2= pygame.image.load('Nivel2Final.png')
    fondofinaln2=pygame.image.load('N2.png')

    fondon3= pygame.image.load('Nivel3final.png')
    fondofinaln3=pygame.image.load('N3.png')

    fondob1= pygame.image.load('Nivelbonusn1.png')
    fondofinalb1=pygame.image.load('N1BONUS.png')

    fondob3= pygame.image.load('Nivelbonusn2.png')
    fondofinalb3=pygame.image.load('N2bonus.png')

    fondon3p= pygame.image.load('Nivelfinalprincesa.png')
    fondofinaln3p=pygame.image.load('Nivel3princes.png')

    fondob3= pygame.image.load('Nivelbonusn2.png')
    fondofinalb3=pygame.image.load('N1BONUS.png')
    
    #pantalla.blit(fondofinaln3,[0,0])
    #CREAR GRUPOS :)
    generaln1=pygame.sprite.Group()
    generaln2=pygame.sprite.Group()
    generaln3=pygame.sprite.Group()
    generalb1=pygame.sprite.Group()
    generalb3=pygame.sprite.Group()
    generaln3p=pygame.sprite.Group()

    suelosn1=pygame.sprite.Group()
    suelosn2=pygame.sprite.Group()
    suelosn3=pygame.sprite.Group()
    suelosb1=pygame.sprite.Group()
    suelosb3=pygame.sprite.Group()
    suelosn3p=pygame.sprite.Group()

    tubosn1=pygame.sprite.Group()
    tubosn2=pygame.sprite.Group()
    tubosn3=pygame.sprite.Group()
    tubosb1=pygame.sprite.Group()
    tubosb3=pygame.sprite.Group()
    tubosn3p=pygame.sprite.Group()

    bloques1n1=pygame.sprite.Group()
    bloques1n2=pygame.sprite.Group()
    bloques1n3=pygame.sprite.Group()
    bloques1b1=pygame.sprite.Group()
    bloques1b3=pygame.sprite.Group()
    bloques1n3p=pygame.sprite.Group()

    bloques2n1=pygame.sprite.Group()
    bloques2n2=pygame.sprite.Group()
    bloques2n3=pygame.sprite.Group()
    bloques2b1=pygame.sprite.Group()
    bloques2b3=pygame.sprite.Group()
    bloques2n3p=pygame.sprite.Group()

    bloques3n1=pygame.sprite.Group()
    bloques3n2=pygame.sprite.Group()
    bloques3n3=pygame.sprite.Group()
    bloques3b1=pygame.sprite.Group()
    bloques3b3=pygame.sprite.Group()
    bloques3n3p=pygame.sprite.Group()

    banderasn1=pygame.sprite.Group()
    banderasn2=pygame.sprite.Group()

    fuegosn3=pygame.sprite.Group()
    fuegosn3p=pygame.sprite.Group()

    #**********************************************************RECORTES NIVEL1********************************************************

    #Recorto el suelo
    suelo=recortar2(fondon1,[0,418],[33.3],[50])
    #primer suelo
    crearsuelo1(suelo,0,2290,generaln1)
    #suelo despues del primero precipicio
    crearsuelo1(suelo,2370.8,2870,generaln1)
    #suelo despues del segundo principio
    crearsuelo1(suelo,2972.8,5100,generaln1)
    #suelo despues del tercer precipicio
    crearsuelo1(suelo,5175.8,7060,generaln1)

    #Recortar Tubos
    #Tubo1
    tubo1=recortar2(fondon1,[935,350],[67],[67])
    tub1=Tubo(tubo1)
    tub1.rect.x=935
    tub1.rect.y=350
    tubosn1.add(tub1)
    generaln1.add(tub1)
    #Tubo 2
    tubo2=recortar2(fondon1,[1268, 317],[67],[101])
    tub2=Tubo(tubo2)
    tub2.rect.x=1268
    tub2.rect.y=317
    tubosn1.add(tub2)
    generaln1.add(tub2)
    #Tubo3
    tubo3=recortar2(fondon1,[1535,283],[67],[135])
    tub3=Tubo(tubo3)
    tub3.rect.x=1535
    tub3.rect.y=283
    tubosn1.add(tub3)
    generaln1.add(tub3)
    #tubo4
    tub4=Tubo(tubo3)
    tub4.rect.x=1902
    tub4.rect.y=283
    tubosn1.add(tub4)
    generaln1.add(tub4)
    #tubo5
    tub5=Tubo(tubo1)
    tub5.rect.x=5442
    tub5.rect.y=350
    tubosn1.add(tub5)
    generaln1.add(tub5)
    #tubo6
    tub6=Tubo(tubo1)
    tub6.rect.x=5976
    tub6.rect.y=350
    tubosn1.add(tub6)
    generaln1.add(tub6)

    #*******************************BLOQUES DE INTERROGACION************************
    bloque1=recortar2(fondon1,[534,283],[34],[35])
    #Ubicar bloques de primera fila
    bl=Bloque1(bloque1)
    bl.rect.x=533
    bl.rect.y=283
    generaln1.add(bl)


    bl1=Bloque1(bloque1)
    bl1.rect.x=734
    bl1.rect.y=150
    generaln1.add(bl1)

    n=2
    x=702
    for i in range(n):
        bl1=Bloque1(bloque1)
        bl1.rect.x+=x
        bl1.rect.y=283
        generaln1.add(bl1)
        x+=67.1

    #ubicar bloques segunda fila
    bl1=Bloque1(bloque1)
    bl1.rect.x=2604
    bl1.rect.y=283
    generaln1.add(bl1)

    #bloques arriba despues del segundo precipicio
    bl1=Bloque1(bloque1)
    bl1.rect.x=3140
    bl1.rect.y=149
    generaln1.add(bl1)

    #CUARTA FILA DE BLOQUES
    n=3
    x=3539
    for i in range(n):
        bl1=Bloque1(bloque1)
        bl1.rect.x+=x
        bl1.rect.y=283
        generaln1.add(bl1)
        x+=100.5
    bl1=Bloque1(bloque1)
    bl1.rect.x= 3639
    bl1.rect.y=150
    generaln1.add(bl1)

    #SEXTA FILA DE BLOQUES
    n=2
    x=4307
    for i in range(n):
        bl1=Bloque1(bloque1)
        bl1.rect.x+=x
        bl1.rect.y=150
        generaln1.add(bl1)
        x+=34
    #SEPTIMA FILA DE BLOQUES
    bl1=Bloque1(bloque1)
    bl1.rect.x=5677
    bl1.rect.y=283
    generaln1.add(bl1)





    #****************************BLOQUES DE LADRILLO NORMAL****************
    bloque2=recortar2(fondon1,[668,283],[35],[35])
    #ubicar bloques primera fila
    n=3
    x=667
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x+=x
        bl2.rect.y=283
        generaln1.add(bl2)
        x+=67

    #ubicar bloques segunda fila
    n=2
    x=2570
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x+=x
        bl2.rect.y=283
        generaln1.add(bl2)
        x+=67

    x=2670
    n=8
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x+=x
        bl2.rect.y=149
        generaln1.add(bl2)
        x+=34

    #bloques arriba despues del segundo precipicio
    n=3
    x=3038
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x+=x
        bl2.rect.y=149
        generaln1.add(bl2)
        x+=34

    bl2=Bloque2(bloque2)
    bl2.rect.x=3138
    bl2.rect.y=283
    generaln1.add(bl2)

    #CUARTA FILA DE BLOQUES
    n=3
    x=3338
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x+=x
        bl2.rect.y=283
        generaln1.add(bl2)
        x+=34

    #QUINTA FILA DE BLOQUES
    l2=Bloque2(bloque2)
    bl2.rect.x=3939
    bl2.rect.y=283
    generaln1.add(bl2)

    n=3
    x=4039
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x+=x
        bl2.rect.y=150
        generaln1.add(bl2)
        x+=34

    #SEXTA FILA DE BLOQUES
    n=2
    x=4273
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x+=x
        bl2.rect.y=150
        generaln1.add(bl2)
        x+=102

    n=2
    x=4307
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x+=x
        bl2.rect.y=283
        generaln1.add(bl2)
        x+=34

    #SEPTIMA FILA DE BLOQUES 
    n=2
    x=5609
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x+=x
        bl2.rect.y=283
        generaln1.add(bl2)
        x+=34
    bl2=Bloque2(bloque2)
    bl2.rect.x=5711
    bl2.rect.y=283
    generaln1.add(bl2)

    #********************************PIRAMIDES DE BLOQUES*************************

    cuadro=recortar2(fondon1,[4574,283],[34],[33])
    #**Piramide hacia la izquierda
    n=4
    m=4
    x=4574
    y=385
    for i in range(n):
        for i in range(m):
            cuadr=Bloque3(cuadro)
            cuadr.rect.x+=x
            cuadr.rect.y+=y
            generaln1.add(cuadr)
            x-=34
        x=4574
        y-=33
        m-=1

    #piramide hacia la derecha
    n=4
    m=4
    x=4674
    y=385
    for i in range(n):
        for i in range(m):
            cuadr=Bloque3(cuadro)
            cuadr.rect.x+=x
            cuadr.rect.y+=y
            generaln1.add(cuadr)
            x+=34
        x=4674
        y-=33
        m-=1
    n=4
    m=4
    x=5175
    y=385
    for i in range(n):
        for i in range(m):
            cuadr=Bloque3(cuadro)
            cuadr.rect.x+=x
            cuadr.rect.y+=y
            generaln1.add(cuadr)
            x+=34
        x=5175
        y-=33
        m-=1

    #Piramide con bloque doble
    n=4
    m=4
    x=5075
    y=385
    for i in range(n):
        for i in range(m):
            cuadr=Bloque3(cuadro)
            cuadr.rect.x+=x
            cuadr.rect.y+=y
            generaln1.add(cuadr)
            x-=34
        cuadr=Bloque3(cuadro)
        cuadr.rect.x+=x
        cuadr.rect.y+=y
        generaln1.add(cuadr)
        x=5075
        y-=33
        m-=1

    n=8
    m=8
    x=6311
    y=385
    for i in range(n):
        for i in range(m):
            cuadr=Bloque3(cuadro)
            cuadr.rect.x+=x
            cuadr.rect.y+=y
            generaln1.add(cuadr)
            x-=34
        cuadr=Bloque3(cuadro)
        cuadr.rect.x+=x
        cuadr.rect.y+=y
        generaln1.add(cuadr)
        x=6311
        y-=33
        m-=1
    cuadr=Bloque3(cuadro)
    cuadr.rect.x=6611
    cuadr.rect.y=383
    generaln1.add(cuadr)

    #****************Recortar la bandera******************
    band=recortar2(fondon1,[6594,85],[33],[33])
    b=Bandera(band)
    b.rect.x=6594
    b.rect.y=85
    generaln1.add(b)


    #******************************************************RECORTES NIVEL2***************************************************************
    #Recorto el suelo
    suelo=recortar2(fondon2,[0,418],[33.3],[50])
    #primer suelo
    crearsuelo1(suelo,0,2650,generaln2)
    #suelo despues del primero precipicio
    crearsuelo1(suelo,2743.8,4100,generaln2)
    #suelo despues del segundo principio
    crearsuelo1(suelo,4181.8,4270,generaln2)
    #suelo despues del tercer precipicio
    crearsuelo1(suelo,4350.8,7425,generaln2)

    #Recortar Tubos
    #Tubo1
    tubo1=recortar2(fondon2,[5655,317],[67],[101])
    tub1=Tubo(tubo1)
    tub1.rect.x=5655
    tub1.rect.y=317
    generaln2.add(tub1)

    #****************************BLOQUES DE INTERROGACION******************
    bloque1=recortar2(fondon2,[2007,181],[32],[32])
    bl=Bloque1(bloque1)
    bl.rect.x=2007
    bl.rect.y=181
    generaln2.add(bl)

    #****************************BLOQUES DE LADRILLO NORMAL****************
    bloque2=recortar2(fondon2,[2576,284],[34],[31])

    #ubicar bloques primera fila
    n=2

    y=284
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x=2576
        bl2.rect.y=y
        generaln2.add(bl2)
        y-=134

    #ubicar segunda fila de cuadros}
    bl2=Bloque2(bloque2)
    bl2.rect.x=4216
    bl2.rect.y=183
    generaln2.add(bl2)

    #****************BLOQUES DE PIRAMIDE*************+
    cuadro=recortar2(fondon2,[2007,317],[33],[33])
    cu=Bloque3(cuadro)
    cu.rect.x=1639
    cu.rect.y=384
    generaln2.add(cu)

    #primer pilar de blques
    n=3
    x=2007
    y=317
    for i in range(n):
        cu=Bloque3(cuadro)
        cu.rect.x+=x
        cu.rect.y+=y
        generaln2.add(cu)
        y+=33

    #segundo pilar de bloques
    n=2
    x=2509
    y=351
    for i in range(n):
        cu=Bloque3(cuadro)
        cu.rect.x+=x
        cu.rect.y+=y
        generaln2.add(cu)
        y+=33

        #tercer pilar de bloques
    n=2
    x=2643
    y=351
    for i in range(n):
        cu=Bloque3(cuadro)
        cu.rect.x+=x
        cu.rect.y+=y
        generaln2.add(cu)
        y+=33

    #cuarto pilar de bloques
    n=2
    x=4216
    y=351
    for i in range(n):
        cu=Bloque3(cuadro)
        cu.rect.x+=x
        cu.rect.y+=y
        generaln2.add(cu)
        y+=33

    #piramide con bloque doble
    n=8
    m=8
    x=6692
    y=385
    for i in range(n):
        for i in range(m):
            cuadr=Bloque3(cuadro)
            cuadr.rect.x+=x
            cuadr.rect.y+=y
            generaln2.add(cuadr)
            x-=34
        cuadr=Bloque3(cuadro)
        cuadr.rect.x+=x
        cuadr.rect.y+=y
        generaln2.add(cuadr)
        x=6692
        y-=33
        m-=1

    cuadr=Bloque3(cuadro)
    cuadr.rect.x=6993
    cuadr.rect.y=384
    generaln2.add(cuadr)

    #****************Recortar la bandera******************
    band=recortar2(fondon2,[6977,85],[33],[33])
    b=Bandera(band)
    b.rect.x=6977
    b.rect.y=85
    generaln2.add(b)



    #********************************************************************************RECORTES NIVEL 3*******************************************
    #Recorto el suelo del muro al inicio del nivel
    suelo=recortar2(fondon3,[0,49],[16],[35])
    n=9
    m=4
    x=0
    y=313.5
    for i in range(m):
        for i in range(n):
            su=Suelo(suelo)
            su.rect.x+=x
            su.rect.y+=y
            generaln3.add(su)
            x+=15
        su=Suelo(suelo)
        su.rect.x+=x
        su.rect.y+=y
        generaln3.add(su)
        x+=15
        y-=35
        x=0
        n-=1
    
    #esto es para completar la parte de abajo del muro
    m=2
    n=9
    y=382
    for i in range(m):
        for i in range(n):
            su=Suelo(suelo)
            su.rect.x+=x
            su.rect.y+=y
            generaln3.add(su)
            x+=15
        su=Suelo(suelo)
        su.rect.x+=x
        su.rect.y+=y
        generaln3.add(su)
        x+=15
        y-=35
        x=0

    #primer nivel del muro
    n=3
    x=150
    y=313.5
    for i in range(n):
        su=Suelo(suelo)
        su.rect.x+=x
        su.rect.y+=y
        generaln3.add(su)
        x+=15
    n=3
    x=150
    y=382
    for i in range(n):
        su=Suelo(suelo)
        su.rect.x+=x
        su.rect.y+=y
        generaln3.add(su)
        x+=15
    n=3
    x=150
    y=347
    for i in range(n):
        su=Suelo(suelo)
        su.rect.x+=x
        su.rect.y+=y
        generaln3.add(su)
        x+=15
    #segundo nivel de muro
    n=2
    x=135
    y=278.5
    for i in range(n):
        su=Suelo(suelo)
        su.rect.x+=x
        su.rect.y+=y
        generaln3.add(su)
        x+=15
    #tercer nivel del muro
    x=120
    y=243.5
    su=Suelo(suelo)
    su.rect.x+=x
    su.rect.y+=y
    generaln3.add(su)
    
    

    #***************RECORTO EL SUELO PRINCIPAL*************
    suelop=recortar2(fondon3,[368,418],[16],[50])
    crearsuelo3(suelop,368,6800,generaln3)
    


    #recortar tubosn3
    #Tubo 1
    tubo1=recortar2(fondon3,[634,351],[67],[116])
    tub1=Tubo(tubo1)
    tub1.rect.x=634
    tub1.rect.y=351
    tubosn3.add(tub1)
    generaln3.add(tub1)
    #tubo2
    tub1=Tubo(tubo1)
    tub1.rect.x=1703
    tub1.rect.y=351
    tubosn3.add(tub1)
    generaln3.add(tub1)
    #tubo3
    tubo2=recortar2(fondon3,[2705,251],[67],[216])
    tub2=Tubo(tubo2)
    tub2.rect.x=2705
    tub2.rect.y=251
    tubosn3.add(tub2)
    generaln3.add(tub2)
    #tubo4
    tubo3=recortar2(fondon3,[3006,217],[67],[250])
    tub3=Tubo(tubo3)
    tub3.rect.x=3006
    tub3.rect.y=217
    tubosn3.add(tub3)
    generaln3.add(tub3)
    #tubo5
    tub1=Tubo(tubo1)
    tub1.rect.x=3440
    tub1.rect.y=351
    tubosn3.add(tub1)
    generaln3.add(tub1)
    #tubo6
    tubo4=recortar2(fondon3,[3673,317],[67],[150])
    tub4=Tubo(tubo4)
    tub4.rect.x=3673
    tub4.rect.y=317
    tubosn3.add(tub4)
    generaln3.add(tub4)
    #tubo7
    tub1=Tubo(tubo1)
    tub1.rect.x=4007
    tub1.rect.y=351
    tubosn3.add(tub1)
    generaln3.add(tub1)
    #tubo 8
    tub4=Tubo(tubo4)
    tub4.rect.x=4341
    tub4.rect.y=317
    tubosn3.add(tub4)
    generaln3.add(tub4)
    #tubo 9
    tubo5=recortar2(fondon3,[4675,184],[67],[99])
    tub5=Tubo(tubo5)
    tub5.rect.x=4675
    tub5.rect.y=184
    tubosn3.add(tub5)
    generaln3.add(tub5)
    #tubo10
    tub1=Tubo(tubo1)
    tub1.rect.x=5009
    tub1.rect.y=351
    tubosn3.add(tub1)
    generaln3.add(tub1)
    #tubo11
    tub2=Tubo(tubo2)
    tub2.rect.x=5310
    tub2.rect.y=251
    tubosn3.add(tub2)
    generaln3.add(tub2)
    #tubo12
    tub3=Tubo(tubo3)
    tub3.rect.x=5577
    tub3.rect.y=217
    tubosn3.add(tub3)
    generaln3.add(tub3)
    #tubo13
    tub2=Tubo(tubo2)
    tub2.rect.x=6111
    tub2.rect.y=251
    tubosn3.add(tub2)
    generaln3.add(tub2)

    #************RECORTE DE LAVA*************

    #primer segmento de lava
    fuego=recortar2(fondon3,[201,418],[35],[50])
    n=5
    x=200
    y=418
    for i in range(n):
        f=Lava(fuego)
        f.rect.x+=x
        f.rect.y+=y
        fuegosn3.add(f)
        generaln3.add(f)
        x+=35

    #segundo segmento de lava
    fuego2=recortar2(fondon3,[202,418],[17],[50])
    n=18
    x=2205
    y=418
    for i in range(n):
        f=Lava(fuego2)
        f.rect.x+=x
        f.rect.y+=y
        fuegosn3.add(f)
        generaln3.add(f)
        x+=16.7
    #tercer segmento de lava
    n=3
    x=4409
    y=418
    for i in range(n):
        f=Lava(fuego)
        f.rect.x+=x
        f.rect.y+=y
        fuegosn3.add(f)
        generaln3.add(f)
        x+=35
    
    #cuarto sgmento de lava
    n=4
    x=5845
    y=418
    for i in range(n):
        f=Lava(fuego)
        f.rect.x+=x
        f.rect.y+=y
        fuegosn3.add(f)
        generaln3.add(f)
        x+=33.3


    #********CREAR TECHO************
    suelot=recortar2(fondon3,[0,49],[17],[35])
    creartecho3(suelot,0,7040,generaln3)

    #**********PLATAFORMA**********
    #Platafaroma1
    crearplataforma3(suelot,9,2538,183,generaln3)

    #plataforma 2
    crearplataforma3(suelot,4,4675,284,generaln3)

    

    #*************MUROS ALTOS**********
    #MURO 1
    crearplataforma3(suelop,9,2069,317,generaln3)
    crearplataforma3(suelop,9,2069,367,generaln3)

    #MURO 2
    crearplataforma3(suelop,45,2504,317,generaln3)
    crearplataforma3(suelop,45,2504,367,generaln3)

    #MURO 3
    crearplataforma3(suelop,47,5109,317,generaln3)
    crearplataforma3(suelop,47,5109,367,generaln3)

    #MURO 4
    crearplataforma3(suelop,53,5978,317,generaln3)
    crearplataforma3(suelop,53,5978,367,generaln3)

    #***************************************************+CREAR NIVEL BONUS 3*******************
    #*****CREAR SUELO*****
    suelo=recortar2(fondob3,[0,418],[20],[50])
    crearsuelob3(suelo,0,2504,generalb3)
    
    #suelo que sobresale (muro)
    suelo=recortar2(fondob3,[199,317],[403],[99])
    mu=Suelo(suelo)
    mu.rect.x=199
    mu.rect.y=317
    generalb3.add(mu)

    suel=recortar2(fondob3,[366,284],[235],[32])
    mu=Suelo(suel)
    mu.rect.x=366
    mu.rect.y=284
    generalb3.add(mu)

    #MURO ARRIBA EN LA MITAD
    mur=recortar2(fondob3,[1302,82],[100],[100])
    mur=Techo(mur)
    mur.rect.x=1302
    mur.rect.y=82  
    generalb3.add(mur)

    #MURO ABAJO EN LA MITAD
    mur=recortar2(fondob3,[1302,317],[100],[100])
    mur=Techo(mur)
    mur.rect.x=1302
    mur.rect.y=317
    generalb3.add(mur)

    #creo paredes izquierda y derecha
    paredizq=recortar2(fondob3,[0,50],[65],[366])
    p=Pared(paredizq)
    p.rect.x=0
    p.rect.y=50
    generalb3.add(p)

    paredder=recortar2(fondob3,[2304,50],[101],[366])
    p=Pared(paredder)
    p.rect.x=2304
    p.rect.y=50
    generalb3.add(p)

    #Pared derecha abajo del tubo verde
    paredder=recortar2(fondob3,[2237,283],[35],[134])
    p=Pared(paredder)
    p.rect.x=2237
    p.rect.y=283
    generalb3.add(p)

    #Pared derecha arriba del tubo verde
    paredder=recortar2(fondob3,[2237,82],[66],[100])
    p=Pared(paredder)
    p.rect.x=2237
    p.rect.y=82
    generalb3.add(p)


    #********CREAR TECHO*******
    techo=recortar2(fondob3,[200,49],[2205],[33])
    tc=Techo(techo)
    tc.rect.x=66
    tc.rect.y=49
    generalb3.add(tc)

    techo2=recortar2(fondob3,[200,82],[400],[67])
    tc=Techo(techo2)
    tc.rect.x=200
    tc.rect.y=82
    generalb3.add(tc)

    techo=recortar2(fondob3,[366,149],[234],[33])
    tc=Techo(techo)
    tc.rect.x=366
    tc.rect.y=149
    generalb3.add(tc)

    #******CREAR TUBOS********
    tubo1=recortar2(fondob3,[100,351],[66],[116])
    tub=Tubo(tubo1)
    tub.rect.x=100
    tub.rect.y=351
    tubosb3.add(tub)
    generalb3.add(tub)



    Mario=Jugador()
    Mario.tubos=tubosn1
    Mario.rect.x=100
    Mario.rect.y=300

    generalsinMario=pygame.sprite.Group()

    for e in generaln1:
    	generalsinMario.add(e)

    generaln1.add(Mario)
    
    fin=False
    mov=False
    mov1=False
    varp_x=0
    posx_p=0
    reloj=pygame.time.Clock()
    print len(tubosn1)
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Mario.var_x=-6
                    mov1=True
                if event.key == pygame.K_RIGHT:
                    Mario.var_x=6
                    mov=True 
                if event.key == pygame.K_SPACE:
                    if not Mario.salto:
                        Mario.salto=True
                        Mario.var_y=-21
            if event.type== pygame.KEYUP:
                if (event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
                    if event.key==pygame.K_LEFT:
                        mov1=False
                    else:
                        mov=False
                    if (mov or mov1):
                        if mov==True and mov1==False:
                            Mario.var_x=5
                        elif mov==False and mov1==True:
                            Mario.var_x=-5
                    else:
                        Mario.var_x=0
        if Mario.rect.x>ANCHO/2 and mov:
        	Mario.var_x=0
        	varp_x=-6        	
        else:
        	varp_x=0
        posx_p+=varp_x                
        pantalla.fill(NEGRO)               
        pantalla.blit(fondofinaln1,[posx_p,0])
        for e in generalsinMario:
        	e.var_x=varp_x
        generaln1.update()            
        generaln1.draw(pantalla)
        #tubosn3.draw(pantalla)
        #fuegosn3.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)