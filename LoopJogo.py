from pygame.constants import *
from Classes_Funcoes import *
from constantes import *
import pygame
import random

pygame.init()  # Inicialização Pygame
pygame.mixer.init()  # Inicialização do módulo de áudio do pygame

# Criando a tela do jogo
pygame.display.set_caption('Olha o Carteiro!')

# Carregando imagens:
background = pygame.image.load('Assets/Imagens/8bitNY.jpg').convert()  # Não precisa de transparência aqui
background = pygame.transform.scale(background, (1000, 800))
carteira_sheet = pygame.image.load('Assets/Imagens/MailmanFemaleSpriteSheet.png').convert_alpha()
carteiro_sheet= pygame.image.load('Assets/Imagens/MailmanSpriteSheet.png').convert_alpha()
poste_img = pygame.image.load('Assets/Imagens/poste.png').convert_alpha()
poste_img = pygame.transform.scale(poste_img, (WIDTH_pole, HEIGHT_pole))
cone_img = pygame.image.load('Assets/Imagens/cone.png').convert_alpha()
cone_img = pygame.transform.scale(cone_img, (WIDTH_cone, HEIGHT_cone))


# Função de tela do jogo
def executar_joguinho(tela,player):
    frames = 0
    if player==0:
        carteira_andando = Carteiro(carteira_sheet)
    else:
        carteira_andando = Carteiro(carteiro_sheet)

    # Rodando o cenário
    clock = pygame.time.Clock()
    # Grupo de todas as sprites e carregando a sprite do carteiro
    todas_as_sprites = pygame.sprite.Group()
    todas_as_sprites.add(carteira_andando)
    # Grupo colisão com a carteira
    grupo_obstaculo = pygame.sprite.Group()
    obstaculo = None
    # São criados 2 fundos, um incial e outro logo após o primeiro, que aparece quando o primeiro sai da tela
    bg_e = 0
    bg_d = background.get_width()
    # Música de fundo do jogo e volume
    pygame.mixer.music.load("Assets/Som/gorgonzola_city.ogg")
    pygame.mixer.music.set_volume(volume)
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
                # Se a tecla for apertada
                if event.type == KEYDOWN:
                    # Se a tecla for a setinha para cima
                    if event.key == K_UP:
                        # Se estiver acima do chão, não pulará
                        if carteira_andando.rect.y != carteira_andando.inicial_y:
                            pass
                        # Se estiver no chão, pulará
                        else:
                            carteira_andando.pula()
            # Se colidiu com um obstáculo
            if state == MORTO:
                # Se a tecla for apertada
                if event.type == KEYDOWN:
                    # Se a tecla for o espaço
                    if event.key == K_SPACE:
                        # Zera tudo e começa novamente
                        pygame.mixer.music.play()
                        todas_as_sprites.empty()
                        todas_as_sprites.add(carteira_andando)
                        grupo_obstaculo.empty()
                        state = JOGAR
                        colisoes.clear()
                        obstaculo = None
                        frames = 0
                        acelera.acelera = 2
                    if event.key == K_q:
                        exit()

        # Para surgir os obstáculos
        if obstaculo == None or obstaculo.rect.x < (largura - 500):
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
        # Criando as colisões
        colisoes = pygame.sprite.spritecollide(carteira_andando, grupo_obstaculo, False, pygame.sprite.collide_mask)
        # Se houver uma colisão
        if len(colisoes) > 0 and state != MORTO:
            # Toca o som da colisão e seu state agora é morto
            carteira_andando.tocar_som_colisao()
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
        # Linhas importantes = Fazem a tela do cenário do jogo ficar sempre se atualizando
        tela.blit(background, (bg_e, -270))
        tela.blit(background, (bg_d, -270))
        todas_as_sprites.draw(tela)

        # Se ele estiver morto, aparecerão as seguintes mensagens na tela
        if state == MORTO:
            cabou = mensagem("ENCOMENDAS NÃO ENTREGUES :(", 30, (255, 255, 0))
            tela.blit(cabou, (70, 100))
            restart = mensagem("Pressione espaço para reiniciar!", 25, (255, 255, 0))
            tela.blit(restart, (70, 180))
            quit = mensagem("Pressione Q para sair :(", 25, (255, 255, 0))
            tela.blit(quit, (70, 210))
            Frame = mensagem("Pontuação:" f"{frames}", 30, (255, 255, 0))
            tela.blit(Frame, (410, 300))

            # Para acessar o highscore, utilizar o conhecimento sobre arquivos
            # Nessa parte, abre o arquivo e o lê
            lendo = open("highscore.txt", "r")
            highscore = lendo.read()
            # Salva o número do arquivo, que estava em string, como um número
            highscore_numero = int(highscore)
            # Fechar o arquivo
            lendo.close()
            # Se o frames for maior que o highscore
            if frames > highscore_numero:
                highscore_numero = frames
                # Abre o arquivo novamente, mas para escrever o novo máximo
                escrevendo = open("highscore.txt", "w")
                escrevendo.write(str(highscore_numero))
                # Fecha ele novamente
                escrevendo.close()
            Record = mensagem("Atual Recorde:" f"{highscore_numero}", 30, (255, 255, 0))
            tela.blit(Record, (300, 350))

        else:
            # Aparece a contagem dos frames na tela do jogo, sempre se atualizando
            contagem = mensagem(f"{frames}", 30, (255, 255, 0))
            tela.blit(contagem, (largura - 300, 10))
            frames += 5
        # A cada 5000 frames a velocidade aumenta 0.5
        if frames % 5000 == 0:
            carteira_andando.pontuacao_pontos()
            if acelera.acelera <= 8:
                acelera.acelera += 0.5

        # Atualizando o jogo
        pygame.display.update()

    return state
