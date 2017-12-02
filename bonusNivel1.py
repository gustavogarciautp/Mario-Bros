import pygame

# Colores
NEGRO    = (   0,   0,   0)
BLANCO   = ( 255, 255, 255)
AZUL     = (   0,   0, 255)
ROJO     = ( 255,   0,   0)
VERDE    = (   0, 255,   0)

# Dimensiones pantalla
ANCHO = 596
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
            su.rect.y=412
            general.add(su)
            s+=36.6
def crearpared(imagen,principio,limite,general):
    s=principio
    while(s<limite):
        p=Pared(imagen)
        p.rect.x=0
        p.rect.y+=s
        general.add(p)
        s+=36.6

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

class Bloque2(pygame.sprite.Sprite):   #BLOQUES DE LADRILLOS NOMRALES
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
    fondo= pygame.image.load('Nivelbonusn1.png')
    fondofinal=pygame.image.load('N1BONUS.png')
    
    pantalla.blit(fondofinal,[0,0])
    #Grupos
    general=pygame.sprite.Group()
    bloques=pygame.sprite.Group()

    #Recorto el suelo
    suelo=recortar2(fondo,[0,412],[36],[56])
    crearsuelo(suelo,0,600,general)

    #********RECORTO PARED*******
    pared=recortar2(fondo,[0,0],[36],[36])
    crearpared(pared,0,409,general)

    #*******Creo Techo*****
    techo=recortar2(fondo,[149,2],[260],[34])
    tc=Techo(techo)
    tc.rect.x=149
    tc.rect.y=2
    general.add(tc)

    #******CREAR PLATAFORMA PRINCIPAL******
    plataf=recortar2(fondo,[149,301],[260],[110])
    pl=Plataforma(plataf)
    pl.rect.x=149
    pl.rect.y=301
    general.add(pl)

    #******CREAR TUBO HORIZONTAL**********
    tubo1=recortar2(fondo,[484,338],[112],[72])
    tub=Tubo(tubo1)
    tub.rect.x=484
    tub.rect.y=338
    general.add(tub)

    #******CREAR TUBO VERTICAL********
    tubo2=recortar2(fondo,[564,2],[32],[336])
    tub=Tubo(tubo2)
    tub.rect.x=564
    tub.rect.y=2
    general.add(tub)
 

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


