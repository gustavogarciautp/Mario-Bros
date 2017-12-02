import pygame

# Colores
NEGRO    = (   0,   0,   0)
BLANCO   = ( 255, 255, 255)
AZUL     = (   0,   0, 255)
ROJO     = ( 255,   0,   0)
VERDE    = (   0, 255,   0)

# Dimensiones pantalla
ANCHO = 2140
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
            s+=15.5

def creartecho(imagen,principio,limite,general):
        s=principio
        while(s<limite):
            su=Bloque2(imagen)
            su.rect.x+=s
            su.rect.y=49
            general.add(su)
            s+=17

def crearplataforma(imagen,n,x,y,general):
    for i in range(n):
        pl=Suelo(imagen)
        pl.rect.x+=x
        pl.rect.y+=y
        general.add(pl)
        x+=15.5

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



if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    pygame.display.set_caption("Juego basico")

    #IMagenes de inicio
    ini1= True
    fondo= pygame.image.load('Nivelfinalprincesa.png')
    fondofinal=pygame.image.load('Nivel3princes.png')
    
    pantalla.blit(fondofinal,[0,0])
    #Grupos
    general=pygame.sprite.Group()
    bloques=pygame.sprite.Group()
    tubos=pygame.sprite.Group()
    fuegos=pygame.sprite.Group()


    #********CREAR TECHO************
    suelot=recortar2(fondo,[0,49],[17],[35])
    creartecho(suelot,0,2150,general)
    

    #********CREAR TECHO***********
    suelop=recortar2(fondo,[0,418],[16],[50])
    crearsuelo(suelop,0,2140,general)

    #*********CREAR TUBOS***********
    #tubo 1
    tubo1=recortar2(fondo,[100,351],[67],[116])
    tub1=Tubo(tubo1)
    tub1.rect.x=100
    tub1.rect.y=351
    tubos.add(tub1)
    general.add(tub1)

    #tubo 2
    tub1=Tubo(tubo1)
    tub1.rect.x=334
    tub1.rect.y=351
    tubos.add(tub1)
    general.add(tub1)
    
    #**********CREAR LAVA********
    fuego=recortar2(fondo,[702,418],[35],[50])
    n=5
    x=701
    y=418
    for i in range(n):
        f=Lava(fuego)
        f.rect.x+=x
        f.rect.y+=y
        fuegos.add(f)
        general.add(f)
        x+=33.3
    
    n=13
    x=1069
    y=418
    for i in range(n):
        f=Lava(fuego)
        f.rect.x+=x
        f.rect.y+=y
        fuegos.add(f)
        general.add(f)
        x+=33.3
    
    #*******************MUROS ALTOS**************
    #MURO 1 arriba
    crearplataforma(suelot,13,868,82,general)
    crearplataforma(suelot,13,868,117,general)
    #MURO2 ARRIBA
    crearplataforma(suelot,5,1536,82,general)
    crearplataforma(suelot,5,1536,117,general)
    crearplataforma(suelot,5,1536,152,general)

    #MURO 1 ABAJO
    crearplataforma(suelop,13,868,317,general)
    crearplataforma(suelop,13,868,367,general)
    
    #MURO 2 ABAJO
    crearplataforma(suelot,7,1503,284,general)
    crearplataforma(suelop,7,1503,319,general)
    crearplataforma(suelop,7,1503,369,general)

    #*********CREAR PUENTE************
    puente=recortar2(fondo,[1069,317],[433],[34])
    p=Puente(puente)
    p.rect.x=1069
    p.rect.y=317
    general.add(p)

    #********CREAR MARTILLO********
    martillo=recortar2(fondo,[1502,250],[36],[34])
    mart=Martillo(martillo)
    mart.rect.x=1502
    mart.rect.y=250
    general.add(mart)
    
    

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
        tubos.draw(pantalla)
        fuegos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)