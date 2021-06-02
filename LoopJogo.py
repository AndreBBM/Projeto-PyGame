from pygame.constants import *
from Classes import *
from constantes import *
import pygame
import random
from Funcoes import *

pygame.init()  # Inicialização Pygame
pygame.mixer.init()  # Inicialização do módulo de áudio do pygame

# Criando a tela do jogo
pygame.display.set_caption('Olha o Carteiro!')

# Carregando imagens:
background = pygame.image.load('Imagens/8bitNY.jpg').convert()  # Não precisa de transparência aqui
background = pygame.transform.scale(background, (1000, 800))
carteiro_sheet = pygame.image.load('Imagens/MailmanFemaleSpriteSheet.png').convert_alpha()
carteiro_img = pygame.image.load('Imagens/MailmanFemale.png').convert_alpha()
carteiro_img = pygame.transform.scale(carteiro_img, (WIDTH_cart, HEIGHT_cart))
poste_img = pygame.image.load('Imagens/poste.png').convert_alpha()
poste_img = pygame.transform.scale(poste_img, (WIDTH_pole, HEIGHT_pole))
caixas_img = pygame.image.load('Imagens/Caixa.png').convert_alpha()
caixas_img = pygame.transform.scale(caixas_img, (WIDTH_caixa, HEIGHT_caixa))
cone_img = pygame.image.load('Imagens/cone.png').convert_alpha()
cone_img = pygame.transform.scale(cone_img, (WIDTH_cone, HEIGHT_cone))

def executar_joguinho(tela):
    frames = 0
    pygame.mixer.music.load("Som/gorgonzola_city.ogg")
    # Volume: 
    pygame.mixer.music.set_volume(volume)

    # Rodando o cenário
    clock = pygame.time.Clock()

    todas_as_sprites = pygame.sprite.Group()
    carteiro_andando = Carteiro(carteiro_sheet)
    todas_as_sprites.add(carteiro_andando)

    # Grupo colisão com a carteira
    grupo_obstaculo = pygame.sprite.Group()
    obstaculo = None
    obstaculo_invisivel = None

    # São criados 2 fundos, um incial e outro logo após o primeiro, que aparece quando o primeiro sai da tela
    bg_e = 0
    bg_d = background.get_width()

    # Música de fundo do jogo começa a tocar
    pygame.mixer.music.play(loops=-1)

    state = JOGAR
    # Loop Principal!
    while state != ACABOU:
        clock.tick(FramePerSecond)
        # Tratando eventos
        for event in pygame.event.get():
            # Para sair do jogo
            if event.type == QUIT:
                state = ACABOU
                exit()
            # Estando no jogo
            if state == JOGAR:
                # Para pular
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        if carteiro_andando.rect.y != carteiro_andando.inicial_y:
                            pass
                        else:
                            carteiro_andando.pula()
            # Se colidiu com um obstáculo
            if state == MORTO:
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        pygame.mixer.music.play()
                        todas_as_sprites.empty()
                        todas_as_sprites.add(carteiro_andando)
                        grupo_obstaculo.empty()
                        state = JOGAR
                        colisoes.clear()
                        obstaculo = None
                        frames = 0
                    elif event.key == QUIT or event.key == K_q:
                        state = MORTO

        # Para surgir os obstáculos
        if obstaculo == None or obstaculo.rect.x < (largura - 400):
            # Aleatoriamente
            opcao = random.randint(1, 2)
            # Surgirá um cone
            if opcao == 1:
                obstaculo = Cone(cone_img)
            # Surgirá um poste
            if opcao == 2:
                referencia = Poste(poste_img)
                obstaculo = Lampada(poste_img, referencia)
                todas_as_sprites.add(referencia)

            todas_as_sprites.add(obstaculo)
            grupo_obstaculo.add(obstaculo)

        # Caso colida com algum dos obstáculos, o fundo para de andar    
        if state == MORTO:
            velocidade_tela = 0
            # Do contrário, o fundo continua a andar e atualizar as sprites
        else:
            velocidade_tela = 2
            todas_as_sprites.update()
        colisoes = pygame.sprite.spritecollide(carteiro_andando, grupo_obstaculo, False, pygame.sprite.collide_mask)

        if len(colisoes) > 0 and state != MORTO:
            carteiro_andando.tocar_som_colisao()
            pygame.mixer.music.stop()
            state = MORTO

        # Velocidade com que o fundo se mexe
        bg_e -= velocidade_tela
        bg_d -= velocidade_tela
        # Quando os fundos saem completamente da tela, eles voltam para o início para passarem novamente
        if bg_e < background.get_width() * -1:
            bg_e = background.get_width()
        if bg_d < background.get_width() * -1:
            bg_d = background.get_width()

        # Linhas importantes = Fazem a tela do jogo ficar sempre se atualizando
        tela.blit(background, (bg_e, -270))
        tela.blit(background, (bg_d, -270))

        if state == MORTO:
            cabou = mensagem("ENCOMENDAS NÃO ENTREGUES :(", 30, (255, 255, 0))
            tela.blit(cabou, (70, 100))
            restart = mensagem("Pressione espaço para reiniciar!", 25, (255, 255, 0))
            tela.blit(restart, (70, 180))
            Frame = mensagem(f"{frames}", 30, (255, 255, 0))
            tela.blit(Frame, (70, 300))
        else:
            # Teste contagem quadros
            contagem = mensagem(f"{frames}", 30, (255, 255, 0))
            tela.blit(contagem, (largura-200, 10))
            frames+=5

        if frames % 3000==0:
            carteiro_andando.pontuacao_pontos()
            #carteiro_andando.para()
            
        todas_as_sprites.draw(tela)
        # Atualizando o jogo
        pygame.display.update()

    return state
