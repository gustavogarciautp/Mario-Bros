import pygame

# Colores
NEGRO    = (   0,   0,   0)
BLANCO   = ( 255, 255, 255)
AZUL     = (   0,   0, 255)
ROJO     = ( 255,   0,   0)
VERDE    = (   0, 255,   0)

# Dimensiones pantalla
ANCHO = 6800
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

class Bloque1(pygame.sprite.Sprite):    #BLOQUES DE LADRILLOS DE INTERROGACION
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

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    pygame.display.set_caption("Juego basico")

    #IMagenes de inicio
    ini1= True
    fondo= pygame.image.load('Nivel3final.png')
    fondofinal=pygame.image.load('N3.png')
    
    pantalla.blit(fondofinal,[0,0])

    #Grupos
    general=pygame.sprite.Group()
    bloques=pygame.sprite.Group()
    tubos=pygame.sprite.Group()
    fuegos=pygame.sprite.Group()

    #Recorto el suelo del muro al inicio del nivel
    suelo=recortar2(fondo,[0,49],[16],[35])

    n=9
    m=4
    x=0
    y=313.5
    for i in range(m):
        for i in range(n):
            su=Suelo(suelo)
            su.rect.x+=x
            su.rect.y+=y
            general.add(su)
            x+=15
        su=Suelo(suelo)
        su.rect.x+=x
        su.rect.y+=y
        general.add(su)
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
            general.add(su)
            x+=15
        su=Suelo(suelo)
        su.rect.x+=x
        su.rect.y+=y
        general.add(su)
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
        general.add(su)
        x+=15
    n=3
    x=150
    y=382
    for i in range(n):
        su=Suelo(suelo)
        su.rect.x+=x
        su.rect.y+=y
        general.add(su)
        x+=15
    n=3
    x=150
    y=347
    for i in range(n):
        su=Suelo(suelo)
        su.rect.x+=x
        su.rect.y+=y
        general.add(su)
        x+=15
    #segundo nivel de muro
    n=2
    x=135
    y=278.5
    for i in range(n):
        su=Suelo(suelo)
        su.rect.x+=x
        su.rect.y+=y
        general.add(su)
        x+=15
    #tercer nivel del muro
    x=120
    y=243.5
    su=Suelo(suelo)
    su.rect.x+=x
    su.rect.y+=y
    general.add(su)
    
    

    #***************RECORTO EL SUELO PRINCIPAL*************
    suelop=recortar2(fondo,[368,418],[16],[50])
    crearsuelo(suelop,368,6800,general)
    


    #recortar tubos
    #Tubo 1
    tubo1=recortar2(fondo,[634,351],[67],[116])
    tub1=Tubo(tubo1)
    tub1.rect.x=634
    tub1.rect.y=351
    tubos.add(tub1)
    general.add(tub1)
    #tubo2
    tub1=Tubo(tubo1)
    tub1.rect.x=1703
    tub1.rect.y=351
    tubos.add(tub1)
    general.add(tub1)
    #tubo3
    tubo2=recortar2(fondo,[2705,251],[67],[216])
    tub2=Tubo(tubo2)
    tub2.rect.x=2705
    tub2.rect.y=251
    tubos.add(tub2)
    general.add(tub2)
    #tubo4
    tubo3=recortar2(fondo,[3006,217],[67],[250])
    tub3=Tubo(tubo3)
    tub3.rect.x=3006
    tub3.rect.y=217
    tubos.add(tub3)
    general.add(tub3)
    #tubo5
    tub1=Tubo(tubo1)
    tub1.rect.x=3440
    tub1.rect.y=351
    tubos.add(tub1)
    general.add(tub1)
    #tubo6
    tubo4=recortar2(fondo,[3673,317],[67],[150])
    tub4=Tubo(tubo4)
    tub4.rect.x=3673
    tub4.rect.y=317
    tubos.add(tub4)
    general.add(tub4)
    #tubo7
    tub1=Tubo(tubo1)
    tub1.rect.x=4007
    tub1.rect.y=351
    tubos.add(tub1)
    general.add(tub1)
    #tubo 8
    tub4=Tubo(tubo4)
    tub4.rect.x=4341
    tub4.rect.y=317
    tubos.add(tub4)
    general.add(tub4)
    #tubo 9
    tubo5=recortar2(fondo,[4675,184],[67],[99])
    tub5=Tubo(tubo5)
    tub5.rect.x=4675
    tub5.rect.y=184
    tubos.add(tub5)
    general.add(tub5)
    #tubo10
    tub1=Tubo(tubo1)
    tub1.rect.x=5009
    tub1.rect.y=351
    tubos.add(tub1)
    general.add(tub1)
    #tubo11
    tub2=Tubo(tubo2)
    tub2.rect.x=5310
    tub2.rect.y=251
    tubos.add(tub2)
    general.add(tub2)
    #tubo12
    tub3=Tubo(tubo3)
    tub3.rect.x=5577
    tub3.rect.y=217
    tubos.add(tub3)
    general.add(tub3)
    #tubo13
    tub2=Tubo(tubo2)
    tub2.rect.x=6111
    tub2.rect.y=251
    tubos.add(tub2)
    general.add(tub2)

    #************RECORTE DE LAVA*************

    #primer segmento de lava
    fuego=recortar2(fondo,[201,418],[35],[50])
    n=5
    x=200
    y=418
    for i in range(n):
        f=Lava(fuego)
        f.rect.x+=x
        f.rect.y+=y
        fuegos.add(f)
        general.add(f)
        x+=35

    #segundo segmento de lava
    fuego2=recortar2(fondo,[202,418],[17],[50])
    n=18
    x=2205
    y=418
    for i in range(n):
        f=Lava(fuego2)
        f.rect.x+=x
        f.rect.y+=y
        fuegos.add(f)
        general.add(f)
        x+=16.7
    #tercer segmento de lava
    n=3
    x=4409
    y=418
    for i in range(n):
        f=Lava(fuego)
        f.rect.x+=x
        f.rect.y+=y
        fuegos.add(f)
        general.add(f)
        x+=35
    
    #cuarto sgmento de lava
    n=4
    x=5845
    y=418
    for i in range(n):
        f=Lava(fuego)
        f.rect.x+=x
        f.rect.y+=y
        fuegos.add(f)
        general.add(f)
        x+=33.3


    #********CREAR TECHO************
    suelot=recortar2(fondo,[0,49],[17],[35])
    creartecho(suelot,0,7040,general)

    #**********PLATAFORMA**********
    #Platafaroma1
    crearplataforma(suelot,9,2538,183,general)

    #plataforma 2
    crearplataforma(suelot,4,4675,284,general)

    

    #*************MUROS ALTOS**********
    #MURO 1
    crearplataforma(suelop,9,2069,317,general)
    crearplataforma(suelop,9,2069,367,general)

    #MURO 2
    crearplataforma(suelop,45,2504,317,general)
    crearplataforma(suelop,45,2504,367,general)

    #MURO 3
    crearplataforma(suelop,47,5109,317,general)
    crearplataforma(suelop,47,5109,367,general)

    #MURO 4
    crearplataforma(suelop,53,5978,317,general)
    crearplataforma(suelop,53,5978,367,general)

    

    



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
