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
    DX = +17    # derecha (suma), izquierda resta
    DY = 12     # abajo suma, arriba resta

    # raqueta
    ALTO_RAQUETA = ALTO//5
    ANCHO_RAQUETA = ALTO_RAQUETA//4
    yRaqueta = ALTO//2 - 50
    moverRaqueta = False
    DY_RAQUETA = 20

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
            # Pregunta si se oprimió alguna tecla
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:   # flecha arriba
                    moverRaqueta = True
                    DY_RAQUETA = -20
                elif evento.key == pygame.K_DOWN:   # flecha abajo
                    moverRaqueta = True
                    DY_RAQUETA = +20
            if evento.type == pygame.KEYUP:     # se liberó la tecla
                moverRaqueta = False

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

        # Actualizar la posición de la pelota
        x += DX      # x = x + DX
        y += DY
        # Prueba colisión
        if y>=ALTO-radio or y<=radio:
            DY = -DY
        if x>=ANCHO-radio:  # or x<=radio:
            DX = -DX

        # Prueba colisión con raqueta
        if x>=0 and x<=ANCHO_RAQUETA and y>=yRaqueta and y<=yRaqueta+ALTO_RAQUETA:
            DX = -DX

        # IA??? qué tal esto? :) :) :)
        # yRaqueta = y - ALTO_RAQUETA//2 + radio//2
        # Si es necesario, mueve la raqueta
        if moverRaqueta:
            yRaqueta += DY_RAQUETA

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame


def main():
    rebotar()


main()
