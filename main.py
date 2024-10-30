import pygame, random
pygame.init()
tamanho = (1000,592)
tela = pygame.display.set_mode( tamanho )
clock = pygame.time.Clock()
pygame.display.set_caption('Corrida Maluca')
branco = (255,255,255)
preto = (0,0,0)
fundo = pygame.image.load("assets/assets/fundo.png")
carro1 = pygame.image.load("assets/assets/carro1.png")
carro2 = pygame.image.load("assets/assets/carro2.png")
movxcar1 = 0
movxcar2 = 0
posYCar1 = 50
posYCar2 = 180
vitoria = pygame.mixer.Sound("assets/assets/vitoria.mp3")
pygame.mixer.music.load("assets/assets/trilha.mp3")
pygame.mixer.music.play(-1)
acabou = False
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()

    tela.fill(branco)
    tela.blit(fundo, (0,0))
    tela.blit(carro1, (movxcar1,posYCar1))
    tela.blit(carro2, (movxcar2,posYCar2))
    
    if not acabou:
        movxcar1 = movxcar1 + random.randint(0,10)
        movxcar2 = movxcar2 + random.randint(0,10)

    if movxcar1 > 1000:
        movxcar1 = 0
        posYCar1 = 350

    if movxcar2 > 1000:
        movxcar2 = 0
        posYCar2 = 480


    fonte = pygame.font.Font("freesansbold.ttf",60)
    texto_vermelho = fonte.render('Vermelho Ganhou', True, branco)
    texto_amarelo = fonte.render('Amarelo Ganhou', True, branco)

    if posYCar1 == 350 and movxcar1 >= 900 and movxcar1 > movxcar2:
        tela.blit(texto_vermelho, (270,70))
        acabou = True
        pygame.mixer.music.stop()
        pygame.mixer.Sound(vitoria)
    
    elif posYCar2 == 480 and movxcar2 >= 900 and movxcar2 > movxcar1:
        tela.blit(texto_amarelo, (270,180))
        acabou = True
        pygame.mixer.music.stop()
        pygame.mixer.Sound(vitoria)
    
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
