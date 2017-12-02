import pygame

# Colores
NEGRO    = (   0,   0,   0)
BLANCO   = ( 255, 255, 255)
AZUL     = (   0,   0, 255)
ROJO     = ( 255,   0,   0)
VERDE    = (   0, 255,   0)

# Dimensiones pantalla
ANCHO = 7425
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
    fondo= pygame.image.load('Nivel2Final.png')
    fondofinal=pygame.image.load('N2.png')

    pantalla.blit(fondofinal,[0,0])
    #Grupos
    general=pygame.sprite.Group()
    bloques=pygame.sprite.Group()
    #Recorto el suelo
    suelo=recortar2(fondo,[0,418],[33.3],[50])
    #primer suelo
    crearsuelo(suelo,0,2650,general)
    #suelo despues del primero precipicio
    crearsuelo(suelo,2743.8,4100,general)
    #suelo despues del segundo principio
    crearsuelo(suelo,4181.8,4270,general)
    #suelo despues del tercer precipicio
    crearsuelo(suelo,4350.8,7425,general)

    #Recortar Tubos
    #Tubo1
    tubo1=recortar2(fondo,[5655,317],[67],[101])
    tub1=Tubo(tubo1)
    tub1.rect.x=5655
    tub1.rect.y=317
    general.add(tub1)

    #****************************BLOQUES DE INTERROGACION******************
    bloque1=recortar2(fondo,[2007,181],[32],[32])
    bl=Bloque1(bloque1)
    bl.rect.x=2007
    bl.rect.y=181
    general.add(bl)
    
    #****************************BLOQUES DE LADRILLO NORMAL****************
    bloque2=recortar2(fondo,[2576,284],[34],[31])

    #ubicar bloques primera fila
    n=2

    y=284
    for i in range(n):
        bl2=Bloque2(bloque2)
        bl2.rect.x=2576
        bl2.rect.y=y
        general.add(bl2)
        y-=134
    
    #ubicar segunda fila de cuadros}
    bl2=Bloque2(bloque2)
    bl2.rect.x=4216
    bl2.rect.y=183
    general.add(bl2)

    #****************BLOQUES DE PIRAMIDE*************+
    cuadro=recortar2(fondo,[2007,317],[33],[33])
    cu=Bloque3(cuadro)
    cu.rect.x=1639
    cu.rect.y=384
    general.add(cu)

    #primer pilar de blques
    n=3
    x=2007
    y=317
    for i in range(n):
        cu=Bloque3(cuadro)
        cu.rect.x+=x
        cu.rect.y+=y
        general.add(cu)
        y+=33
    
    #segundo pilar de bloques
    n=2
    x=2509
    y=351
    for i in range(n):
        cu=Bloque3(cuadro)
        cu.rect.x+=x
        cu.rect.y+=y
        general.add(cu)
        y+=33

     #tercer pilar de bloques
    n=2
    x=2643
    y=351
    for i in range(n):
        cu=Bloque3(cuadro)
        cu.rect.x+=x
        cu.rect.y+=y
        general.add(cu)
        y+=33
    
    #cuarto pilar de bloques
    n=2
    x=4216
    y=351
    for i in range(n):
        cu=Bloque3(cuadro)
        cu.rect.x+=x
        cu.rect.y+=y
        general.add(cu)
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
            general.add(cuadr)
            x-=34
        cuadr=Bloque3(cuadro)
        cuadr.rect.x+=x
        cuadr.rect.y+=y
        general.add(cuadr)
        x=6692
        y-=33
        m-=1

    cuadr=Bloque3(cuadro)
    cuadr.rect.x=6993
    cuadr.rect.y=384
    general.add(cuadr)

    #****************Recortar la bandera******************
    band=recortar2(fondo,[6977,85],[33],[33])
    b=Bandera(band)
    b.rect.x=6977
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

    