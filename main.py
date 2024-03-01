import pygame, sys, random
import cesta, objetos

pygame.init()
ventana = pygame.display.set_mode((300,600))
sprites = pygame.sprite.Group()

posibles_objetos = ['cura','daño','monedas']

def mostrar_numero(numeros,x,y):
    font = pygame.font.Font(None, 50)  

    # Renderizar el texto
    text = font.render(str(numeros), True, (255,0,0))

    # Obtener el rectángulo del texto para posicionarlo en la pantalla
    text_rect = text.get_rect()
    text_rect.topleft = (x,y)


    ventana.blit(text, text_rect)

def run():
    tiempo_desde_creo_objeto = 0
    objeto_colisionador = cesta.cesta(100,500) # x y
    sprites.add(objeto_colisionador)
    while True:
        tiempo_actual = pygame.time.get_ticks()

        if tiempo_actual - tiempo_desde_creo_objeto >= 500: 
            posibilidad_objetos = random.randint(1,250)
            if 100 > posibilidad_objetos > 0:
                moneda = objetos.objeto(posibles_objetos[2])
                sprites.add(moneda)
            elif 200 > posibilidad_objetos > 100:
                daño = objetos.objeto(posibles_objetos[1])
                sprites.add(daño)
            elif 251 > posibilidad_objetos > 200:
                cura = objetos.objeto(posibles_objetos[0])
                sprites.add(cura)
            tiempo_desde_creo_objeto = tiempo_actual

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            objeto_colisionador.movement(keys,tiempo_actual)
                
        ventana.fill((0,0,0))

        # Dibujar los objetos despues de limpiar la pantalla
        sprites.draw(ventana)
        for objeto in sprites:
            if not objeto.tipo == 'cesta':
                objeto.avanzar(tiempo_actual)
                if not objeto.mover_abajo:
                    objeto.kill()
            
                if objeto.rect.colliderect(objeto_colisionador.rect):
                    if objeto.tipo == 'monedas':
                        objeto_colisionador.monedas += 1
                    elif objeto.tipo == 'daño':
                        objeto_colisionador.vida -= 1
                    elif objeto.tipo == 'cura':
                        if objeto_colisionador.vida < 5:
                            objeto_colisionador.vida += 1
                    objeto.rect.x = 600
                    objeto.kill()

        mostrar_numero(objeto_colisionador.monedas,0,0)
        mostrar_numero(objeto_colisionador.vida,0,50)
        pygame.display.flip()

if __name__ == '__main__':
   run()