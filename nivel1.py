import pygame

# Colores
NEGRO    = (   0,   0,   0)
BLANCO   = ( 255, 255, 255)
AZUL     = (   0,   0, 255)
ROJO     = ( 255,   0,   0)
VERDE    = (   0, 255,   0)

# Dimensiones pantalla
ANCHO = 7100
ALTO  = 470


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

def crearsuelo(imagen,principio,limite,general):
        s=principio
        while(s<limite):
            su=Suelo(imagen)
            su.rect.x+=s
            su.rect.y=418
            general.add(su)
            s+=33.3

class Jugador(pygame.sprite.Sprite):

    var_x = 0
    var_y = 0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ancho = 40
        alto = 60
        self.image = pygame.Surface([ancho, alto])
        self.bl= []
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x+=self.var_x
        self.rect.y+=self.var_y

        for b in self.bl:
            if pygame.sprite.collide_rect(self,b):
                print 'colision'


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

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    pygame.display.set_caption("Juego basico")

    #IMagenes de inicio
    ini1= True
    fondo= pygame.image.load('NivelFinal.png')
    fondofinal=pygame.image.load('N1.png')
    
    pantalla.blit(fondofinal,[0,0])

    #Grupos
    general=pygame.sprite.Group()
    bloques=pygame.sprite.Group()

    #Recorto el suelo
    suelo=recortar2(fondo,[0,418],[33.3],[50])
    #primer suelo
    crearsuelo(suelo,0,2290,general)
    #suelo despues del primero precipicio
    crearsuelo(suelo,2370.8,2870,general)
    #suelo despues del segundo principio
    crearsuelo(suelo,2972.8,5100,general)
    #suelo despues del tercer precipicio
    crearsuelo(suelo,5175.8,7060,general)
    
    #Recortar Tubos
    #Tubo1
    tubo1=recortar2(fondo,[935,350],[67],[67])
    tub1=Tubo(tubo1)
    tub1.rect.x=935
    tub1.rect.y=350
    general.add(tub1)
    #Tubo 2
    tubo2=recortar2(fondo,[1268, 317],[67],[101])
    tub2=Tubo(tubo2)
    tub2.rect.x=1268
    tub2.rect.y=317
    general.add(tub2)
    #Tubo3
    tubo3=recortar2(fondo,[1535,283],[67],[135])
    tub3=Tubo(tubo3)
    tub3.rect.x=1535
    tub3.rect.y=283
    general.add(tub3)
    #tubo4
    tub4=Tubo(tubo3)
    tub4.rect.x=1902
    tub4.rect.y=283
    general.add(tub4)
    #tubo5
    tub5=Tubo(tubo1)
    tub5.rect.x=5442
    tub5.rect.y=350
    general.add(tub5)
    #tubo6
    tub6=Tubo(tubo1)
    tub6.rect.x=5976
    tub6.rect.y=350
    general.add(tub6)

    #*******************************BLOQUES DE INTERROGACION************************
    bloque1=recortar2(fondo,[534,283],[34],[35])
    #Ubicar bloques de primera fila
    bl=Bloque1(bloque1)
    bl.rect.x=533
    bl.rect.y=283
    general.add(bl)


    bl1=Bloque1(bloque1)
    bl1.rect.x=734
    bl1.rect.y=150
    general.add(bl1)

    n=2
    x=702
    for i in range(n):
        bl1=Bloque1(bloque1)
        bl1.rect.x+=x
        bl1.rect.y=283
        general.add(bl1)
        x+=67.1

    #ubicar bloques segunda fila
    bl1=Bloque1(bloque1)
    bl1.rect.x=2604
    bl1.rect.y=283
    general.add(bl1)

    #bloques arriba despues del segundo precipicio
    bl1=Bloque1(bloque1)
    bl1.rect.x=3140
    bl1.rect.y=149
    general.add(bl1)

    #CUARTA FILA DE BLOQUES
    n=3
    x=3539
    for i in range(n):
        bl1=Bloque1(bloque1)
        bl1.rect.x+=x
        bl1.rect.y=283
        general.add(bl1)
        x+=100.5
    bl1=Bloque1(bloque1)
    bl1.rect.x= 3639
    bl1.rect.y=150
    general.add(bl1)

    #SEXTA FILA DE BLOQUES
    n=2
    x=4307
    for i in range(n):
        bl1=Bloque1(bloque1)
        bl1.rect.x+=x
        bl1.rect.y=150
        general.add(bl1)
        x+=34
    #SEPTIMA FILA DE BLOQUES
    bl1=Bloque1(bloque1)
    bl1.rect.x=5677
    bl1.rect.y=283
    general.add(bl1)
    



    
    #****************************BLOQUES DE LADRILLO NORMAL****************
    bloque2=recortar2(fondo,[668,283],[35],[35])
    #ubicar bloques primera fila
    n=3
    x=667
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x+=x
        bl2.rect.y=283
        general.add(bl2)
        x+=67

    #ubicar bloques segunda fila
    n=2
    x=2570
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x+=x
        bl2.rect.y=283
        general.add(bl2)
        x+=67
    
    x=2670
    n=8
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x+=x
        bl2.rect.y=149
        general.add(bl2)
        x+=34

    #bloques arriba despues del segundo precipicio
    n=3
    x=3038
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x+=x
        bl2.rect.y=149
        general.add(bl2)
        x+=34
    
    bl2=Bloque2(bloque2)
    bl2.rect.x=3138
    bl2.rect.y=283
    general.add(bl2)

    #CUARTA FILA DE BLOQUES
    n=3
    x=3338
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x+=x
        bl2.rect.y=283
        general.add(bl2)
        x+=34

    #QUINTA FILA DE BLOQUES
    l2=Bloque2(bloque2)
    bl2.rect.x=3939
    bl2.rect.y=283
    general.add(bl2)

    n=3
    x=4039
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x+=x
        bl2.rect.y=150
        general.add(bl2)
        x+=34
    
    #SEXTA FILA DE BLOQUES
    n=2
    x=4273
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x+=x
        bl2.rect.y=150
        general.add(bl2)
        x+=102
    
    n=2
    x=4307
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x+=x
        bl2.rect.y=283
        general.add(bl2)
        x+=34

    #SEPTIMA FILA DE BLOQUES 
    n=2
    x=5609
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x+=x
        bl2.rect.y=283
        general.add(bl2)
        x+=34
    bl2=Bloque2(bloque2)
    bl2.rect.x=5711
    bl2.rect.y=283
    general.add(bl2)

    #********************************PIRAMIDES DE BLOQUES*************************
    
    cuadro=recortar2(fondo,[4574,283],[34],[33])
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
            general.add(cuadr)
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
            general.add(cuadr)
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
            general.add(cuadr)
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
            general.add(cuadr)
            x-=34
        cuadr=Bloque3(cuadro)
        cuadr.rect.x+=x
        cuadr.rect.y+=y
        general.add(cuadr)
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
            general.add(cuadr)
            x-=34
        cuadr=Bloque3(cuadro)
        cuadr.rect.x+=x
        cuadr.rect.y+=y
        general.add(cuadr)
        x=6311
        y-=33
        m-=1
    cuadr=Bloque3(cuadro)
    cuadr.rect.x=6611
    cuadr.rect.y=383
    general.add(cuadr)

    #****************Recortar la bandera******************
    band=recortar2(fondo,[6594,85],[33],[33])
    b=Bandera(band)
    b.rect.x=6594
    b.rect.y=85
    general.add(b)


    fin=False
    reloj=pygame.time.Clock()
    x=0
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

        general.update()

        '''if(x<7000):
            x-=2
            pantalla.blit(fondo,[x,0])
        else:
            pantalla.blit[0,0]
            x=0'''
            

        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
