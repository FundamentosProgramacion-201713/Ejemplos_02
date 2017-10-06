# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame

# Dimensiones de la pantalla
ANCHO = 600
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)


def rebotar():
    '''
    Mueve la pelota dentro de los límites de la pantalla
    '''
    # pelota
    x = ANCHO//2
    y = ALTO//2
    radio = 20
    DX = +15    # derecha (suma), izquierda resta
    DY = 10     # abajo suma, arriba resta

    # raqueta
    ALTO_RAQUETA = ALTO//5
    ANCHO_RAQUETA = ALTO_RAQUETA//4
    yRaqueta = ALTO//2 - 50

    # Ejemplo del uso de pygame
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

            # Aquí podemos revisar el teclado y mover la raqueta

        # Borrar pantalla
        ventana.fill(VERDE_BANDERA)

        # Dibujar, aquí haces todos los trazos que requieras
        '''
        pygame.draw.rect(ventana, VERDE_BANDERA, (30, 30, ANCHO - 60, ALTO - 60), 5)
        pygame.draw.circle(ventana, ROJO, (ANCHO // 2, ALTO // 2), 200, 2)
        pygame.draw.line(ventana, VERDE_BANDERA,(0,ALTO),(ANCHO,0),10)
        '''
        # Dibujar raqueta
        pygame.draw.rect(ventana,ROJO,(0,yRaqueta,ANCHO_RAQUETA,ALTO_RAQUETA))

        # Dibujar Pelota
        pygame.draw.circle(ventana,ROJO,(x ,y),radio)
        x += DX      # x = x + 2
        y += DY

        if y>=ALTO-radio or y<=radio:
            DY = -DY

        if x>=ANCHO-radio:  # or x<=radio:
            DX = -DX

        # Prueba colisión con raqueta
        if x<=ANCHO_RAQUETA and y>=yRaqueta and y<=yRaqueta+ALTO_RAQUETA:
            DX = -DX

        # IA??? qué tal esto? :) :) :)
        yRaqueta = y - ALTO_RAQUETA//2 + radio//2

        # Después probaremos la colisión entre raqueta y pelota

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(60)  # 60 fps

    pygame.quit()  # termina pygame


def main():
    rebotar()


main()
