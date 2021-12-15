import pygame
import os

# definisco la funzione per avviare il programma
def avvio():
    # definisco le variabili globali
    global main_dir, eseguendo_menu

    # trovo la cartella da dove viene eseguito il file
    main_dir = os.path.dirname(os.path.abspath(__file__))
    # avvio il modulo pygame
    pygame.init()
    # definisco lo stato del programma
    eseguendo_menu = True

# definisco la funzione che raccoglie le immagini
def aquisisci_immagini(main_dir):
    # definisco le variabili per le immagini
    global sfondo_menu, multiplayer_locale_sfondo, multiplayer_online_sfondo, x, o, x_ha_vinto, o_ha_vinto, icona, crediti_sfondo, turno_o, turno_x, pareggio

    # raccolgo gli oggetti (immagini)
    sfondo_menu = pygame.image.load(f"{main_dir}/Immagini/Menu_Sfondo.png")
    multiplayer_locale_sfondo = pygame.image.load(f"{main_dir}/Immagini/Multiplayer_Locale.png")
    multiplayer_online_sfondo = pygame.image.load(f"{main_dir}/Immagini/Multiplayer_Online.png")
    x = pygame.image.load(f"{main_dir}/Immagini/X.png")
    o = pygame.image.load(f"{main_dir}/Immagini/O.png")
    x_ha_vinto = pygame.image.load(f"{main_dir}/Immagini/X_ha_vinto.png")
    o_ha_vinto = pygame.image.load(f"{main_dir}/Immagini/O_ha_vinto.png")
    icona = pygame.image.load(f"{main_dir}/Immagini/Icona.png")
    crediti_sfondo = pygame.image.load(f"{main_dir}/Immagini/Crediti.png")
    turno_o = pygame.image.load(f"{main_dir}/Immagini/Turno_O.png")
    turno_x = pygame.image.load(f"{main_dir}/Immagini/Turno_X.png")
    pareggio = pygame.image.load(f"{main_dir}/Immagini/Pareggio.png")

# definisco la funzione per le impostazioni della finestra
def impostazioni(icona, main_dir):
    # definisco le variabili e le costanti globali
    global SCHERMO, FPS, NOME, ICONA, larghezza, altezza, font
    
    # definisco le costanti per l'area della finestra del programma, per i fotogrammi al secondo
    SCHERMO = pygame.display.set_mode((889,500))
    FPS = 60

    #definisco il nome della finestra e l'icona dell'applicazione
    NOME = pygame.display.set_caption("Tris - Menu Principale")
    ICONA = pygame.display.set_icon(icona)
    
    # definisco la larghezza e l'altezza della finestra
    larghezza = SCHERMO.get_width()
    altezza = SCHERMO.get_height() 
    
    # definisco il font da utilizzare
    font = pygame.font.Font(f"{main_dir}/Font/MyUnderwood.ttf",28)

# definisco la funzione per renderizzare il testo
def renderizza_testo(font):
    # definisco le variabili globali
    global esci, online_multiplayer, local_multiplayer, crediti

    # renderizzo le stringhe da mostrare 
    esci = font.render("esci", True , (0,0,0))
    online_multiplayer = font.render("multiplayer online", True, (0,0,0))
    local_multiplayer = font.render("multiplayer locale", True, (0,0,0))
    crediti = font.render("crediti", True, (0,0,0))

# aggiungo la x alle coordinate del quadrante selezionato
def disegna_x(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno):    
    if quadrante == "alto a sinistra":
        if quadrante1 == True:
            SCHERMO.blit(x, (quadratox,quadratoy))
            quadrante1 = False
            turno = turno + 1
            rigaA = rigaA + 1
            colonnaA = colonnaA + 1
            diagonaleA = diagonaleA + 1
            return quadrante1, rigaA, colonnaA, diagonaleA, turno
        elif quadrante1 == False:
            return quadrante1, rigaA, colonnaA, diagonaleA, turno
    elif quadrante == "centro a sinistra":
        if quadrante4 == True:
            SCHERMO.blit(x, (quadratox,quadratoy))
            quadrante4 = False
            turno = turno + 1
            rigaB = rigaB + 1
            colonnaA = colonnaA + 1
            return quadrante4, rigaB, colonnaA, turno
        elif quadrante4 == False:
            return quadrante4, rigaB, colonnaA, turno
    elif quadrante == "basso a sinistra":
        if quadrante7 == True:
            SCHERMO.blit(x, (quadratox,quadratoy))
            quadrante7 = False
            turno = turno + 1
            rigaC = rigaC + 1
            colonnaA = colonnaA + 1
            diagonaleB = diagonaleB + 1
            return quadrante7, rigaC, colonnaA, diagonaleB, turno
        elif quadrante7 == False:
            return quadrante7, rigaC, colonnaA, diagonaleB, turno
    elif quadrante == "alto in centro":
        if quadrante2 == True:
            SCHERMO.blit(x, (quadratox,quadratoy))
            quadrante2 = False
            turno = turno + 1
            rigaA = rigaA + 1
            colonnaB = colonnaB + 1
            return quadrante2, rigaA, colonnaB, turno
        elif quadrante2 == False:
            return quadrante2, rigaA, colonnaB, turno
    elif quadrante == "centro":
        if quadrante5 == True:
            SCHERMO.blit(x, (quadratox,quadratoy))
            quadrante5 = False
            turno = turno + 1
            rigaB = rigaB + 1
            colonnaB = colonnaB + 1
            diagonaleA = diagonaleA + 1
            diagonaleB = diagonaleB + 1
            return quadrante5, rigaB, colonnaB, diagonaleA, diagonaleB, turno
        elif quadrante5 == False:
            return quadrante5, rigaB, colonnaB, diagonaleA, diagonaleB, turno
    elif quadrante == "basso in centro":
        if quadrante8 == True:
            SCHERMO.blit(x, (quadratox,quadratoy))
            quadrante8 = False
            turno = turno + 1
            rigaC = rigaC + 1
            colonnaB = colonnaB + 1
            return quadrante8, rigaC, colonnaB, turno
        elif quadrante8 == False:
            return quadrante8, rigaC, colonnaB, turno
    elif quadrante == "alto a destra":
        if quadrante3 == True:
            SCHERMO.blit(x, (quadratox,quadratoy))
            quadrante3 = False
            turno = turno + 1
            rigaA = rigaA + 1
            colonnaC = colonnaC + 1
            diagonaleB = diagonaleB + 1
            return quadrante3, rigaA, colonnaC, diagonaleB, turno
        elif quadrante3 == False:
            return quadrante3, rigaA, colonnaC, diagonaleB, turno
    elif quadrante == "centro a destra":
        if quadrante6 == True:
            SCHERMO.blit(x, (quadratox,quadratoy))
            quadrante6 = False
            turno = turno + 1
            rigaB = rigaB + 1
            colonnaC = colonnaC + 1
            return quadrante6, rigaB, colonnaC, turno
        elif quadrante6 == False:
            return quadrante6, rigaB, colonnaC, turno
    elif quadrante == "basso a destra":
        if quadrante9 == True:
            SCHERMO.blit(x, (quadratox,quadratoy))
            quadrante9 = False
            turno = turno + 1
            rigaC = rigaC + 1
            colonnaC = colonnaC + 1
            diagonaleA = diagonaleA + 1
            return quadrante9, rigaC, colonnaC, diagonaleA, turno
        elif quadrante9 == False:
            return quadrante9, rigaC, colonnaC, diagonaleA, turno

# aggiungo la o alle coordinate del quadrante selezionato
def disegna_o(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno):
    if quadrante == "alto a sinistra":
        if quadrante1 == True:
            SCHERMO.blit(o, (quadratox,quadratoy))
            quadrante1 = False
            turno = turno - 1
            rigaA = rigaA - 1
            colonnaA = colonnaA - 1
            diagonaleA = diagonaleA - 1
            return quadrante1, rigaA, colonnaA, diagonaleA, turno
        elif quadrante1 == False:
            return quadrante1, rigaA, colonnaA, diagonaleA, turno
    elif quadrante == "centro a sinistra":
        if quadrante4 == True:
            SCHERMO.blit(o, (quadratox,quadratoy))
            quadrante4 = False
            turno = turno - 1
            rigaB = rigaB - 1
            colonnaA = colonnaA - 1
            return quadrante4, rigaB, colonnaA, turno
        elif quadrante4 == False:
            return quadrante4, rigaB, colonnaA, turno
    elif quadrante == "basso a sinistra":
        if quadrante7 == True:
            SCHERMO.blit(o, (quadratox,quadratoy))
            quadrante7 = False
            turno = turno - 1
            rigaC = rigaC - 1
            colonnaA = colonnaA - 1
            diagonaleB = diagonaleB - 1
            return quadrante7, rigaC, colonnaA, diagonaleB, turno
        elif quadrante7 == False:
            return quadrante7, rigaC, colonnaA, diagonaleB, turno
    elif quadrante == "alto in centro":
        if quadrante2 == True:
            SCHERMO.blit(o, (quadratox,quadratoy))
            quadrante2 = False
            turno = turno - 1
            rigaA = rigaA - 1
            colonnaB = colonnaB - 1
            return quadrante2, rigaA, colonnaB, turno
        elif quadrante2 == False:
            return quadrante2, rigaA, colonnaB, turno
    elif quadrante == "centro":
        if quadrante5 == True:
            SCHERMO.blit(o, (quadratox,quadratoy))
            quadrante5 = False
            turno = turno - 1
            rigaB = rigaB - 1
            colonnaB = colonnaB - 1
            diagonaleA = diagonaleA - 1
            diagonaleB = diagonaleB - 1
            return quadrante5, rigaB, colonnaB, diagonaleA, diagonaleB, turno
        elif quadrante5 == False:
            return quadrante5, rigaB, colonnaB, diagonaleA, diagonaleB, turno
    elif quadrante == "basso in centro":
        if quadrante8 == True:
            SCHERMO.blit(o, (quadratox,quadratoy))
            quadrante8 = False
            turno = turno - 1
            rigaC = rigaC - 1
            colonnaB = colonnaB - 1
            return quadrante8, rigaC, colonnaB, turno
        elif quadrante8 == False:
            return quadrante8, rigaC, colonnaB, turno
    elif quadrante == "alto a destra":
        if quadrante3 == True:
            SCHERMO.blit(o, (quadratox,quadratoy))
            quadrante3 = False
            turno = turno - 1
            rigaA = rigaA - 1
            colonnaC = colonnaC - 1
            diagonaleB = diagonaleB - 1
            return quadrante3, rigaA, colonnaC, diagonaleB, turno
        elif quadrante3 == False:
            return quadrante3, rigaA, colonnaC, diagonaleB, turno
    elif quadrante == "centro a destra":
        if quadrante6 == True:
            SCHERMO.blit(o, (quadratox,quadratoy))
            quadrante6 = False
            turno = turno - 1
            rigaB = rigaB - 1
            colonnaC = colonnaC - 1
            return quadrante6, rigaB, colonnaC, turno
        elif quadrante6 == False:
            return quadrante6, rigaB, colonnaC, turno
    elif quadrante == "basso a destra":
        if quadrante9 == True:
            SCHERMO.blit(o, (quadratox,quadratoy))
            quadrante9 = False
            turno = turno - 1
            rigaC = rigaC - 1
            colonnaC = colonnaC - 1
            diagonaleA = diagonaleA - 1
            return quadrante9, rigaC, colonnaC, diagonaleA, turno
        elif quadrante9 == False:
            return quadrante9, rigaC, colonnaC, diagonaleA, turno

# definisco la funzione inizializza() per i dati necessari al multiplayer
def inizializza():
    global turno
    global quadratox, quadratoy
    global quadrante
    global quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9

    global rigaA, rigaB, rigaC
    global colonnaA, colonnaB, colonnaC
    global diagonaleA, diagonaleB

    rigaA = 0
    rigaB = 0
    rigaC = 0
    colonnaA = 0
    colonnaB = 0
    colonnaC = 0
    diagonaleA = 0
    diagonaleB = 0

    quadrante1 = True
    quadrante2 = True   
    quadrante3 = True
    quadrante4 = True
    quadrante5 = True
    quadrante6 = True
    quadrante7 = True
    quadrante8 = True
    quadrante9 = True

    quadrante = 0
    quadratox = 0
    quadratoy = 0
    turno = 0

# definisco la funzione per disegnare gli elementi sfondo e testi sullo schermo
def disegna_sfondo_e_testi():
    # disegno lo sfondo sullo schermo
    SCHERMO.blit(sfondo_menu, (0,0))
    
    # disegno i testi sullo schermo
    SCHERMO.blit(local_multiplayer, (larghezza/2+62, altezza/2+25))
    SCHERMO.blit(esci, (larghezza/2+170, altezza/2+136))
    SCHERMO.blit(crediti, (195, altezza/2+136))
    SCHERMO.blit(online_multiplayer, (103, altezza/2+25))
    
    #aggiorno lo schermo
    pygame.display.update() 

def hai_perso(vincente):
    # mostro chi ha vinto
    if vincente == "x":
        SCHERMO.blit(x_ha_vinto, (0,0))
    elif vincente == "o":
        SCHERMO.blit(o_ha_vinto, (0,0))
    # aggiorno lo schermo
    pygame.display.update()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if ( event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE ):
                # riporta lo schermo alla schermata iniziale del multiplayer locale
                SCHERMO.blit(multiplayer_locale_sfondo, (0,0))
                SCHERMO.blit(turno_x, (561,0))
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:
                    pygame.quit()



# chiamo la funzione per avviare il programma
avvio()

# chiamo la funzione per inizializzare le immagini
aquisisci_immagini(main_dir)

# chiamo la funzione per le impostazioni della finestra
impostazioni(icona, main_dir)

# chiamo la funzione per renderizzare il testo
renderizza_testo(font)

# chiamo la funzione per disegnare gli elementi sfondo e testi sullo schermo
disegna_sfondo_e_testi()

# azioni che avvengono quando il menu sta venendo mostrato
while eseguendo_menu:
    for event in pygame.event.get():
        # verifico se l'utente chiude l'applicazione
        if event.type == pygame.QUIT:
            pygame.quit()
        # verifico se l'utente sta cliccando un tasto del mouse
        if event.type == pygame.MOUSEBUTTONUP:
            # definisco le coordinate del cursore
            coordinate_cursore = pygame.mouse.get_pos()
            #verifico in che zona del menu si trova il click
            if 484 <= coordinate_cursore[0] <= larghezza-80 and 365 <= coordinate_cursore[1] <= altezza-65:
                # esci
                pygame.quit()
            if 484 <= coordinate_cursore[0] <= larghezza-80 and 255 <= coordinate_cursore[1] <= altezza-175:
                # multiplayer locale
                # cambio schermata
                SCHERMO.blit(multiplayer_locale_sfondo, (0,0))
                # mostro il turno
                SCHERMO.blit(turno_x, (561,0))
                # aggiorno lo schermo
                pygame.display.update()
                # cambio il nome della finestra
                NOME = pygame.display.set_caption("Tris - Multiplayer Locale")
                # aggiorno lo stato dell'applicazione
                eseguendo_menu = False
                # verifico se l'utente clicca il tasto per tornare indietro
                inizializza()
                while not eseguendo_menu:
                    for event in pygame.event.get():

                        # controllo se l'utente clicca il tasto per tornare indietro
                        if event.type == pygame.MOUSEBUTTONUP:

                            # definisco le coordinate del cursore
                            posizione_cursore_x, posizione_cursore_y = pygame.mouse.get_pos()

                            #verifico in che zona del menu si trova il click
                            if 8 <= posizione_cursore_x <= 49 and 8 <= posizione_cursore_y <= altezza-451:
                                # cambio schermata e aggiorno lo schermo
                                disegna_sfondo_e_testi()
                                pygame.display.update()
                                # cambio il nome della finestra
                                NOME = pygame.display.set_caption("Tris - Menu Principale")
                                # aggiorno lo stato dell'applicazione
                                eseguendo_menu = True
                            
                            # verifico in area si trova il click
                            if 60 <= posizione_cursore_x <= 560 and 0 <= posizione_cursore_y <= 500:
                                
                                # verifico in che colonna si trova il click
                                if ( posizione_cursore_x >= 60 and posizione_cursore_x <= 224 ):
                                    # verifico in che riga si trova il click
                                    if ( posizione_cursore_y >= 0 and posizione_cursore_y <= 164 ):
                                        quadrante = "alto a sinistra"
                                    elif ( posizione_cursore_y >= 168 and posizione_cursore_y <= 331 ):
                                        quadrante = "centro a sinistra"
                                    elif ( posizione_cursore_y >= 336 and posizione_cursore_y <= 500 ):
                                        quadrante = "basso a sinistra"
                                elif ( posizione_cursore_x >= 229 and posizione_cursore_x <= 393 ):
                                    if ( posizione_cursore_y >= 0 and posizione_cursore_y <= 164 ):
                                        quadrante = "alto in centro"
                                    elif ( posizione_cursore_y >= 168 and posizione_cursore_y <= 331 ):
                                        quadrante = "centro"
                                    elif ( posizione_cursore_y >= 336 and posizione_cursore_y <= 500 ):
                                        quadrante = "basso in centro"
                                elif ( posizione_cursore_x >= 398 and posizione_cursore_x <= 560 ):
                                    if ( posizione_cursore_y >= 0 and posizione_cursore_y <= 164 ):
                                        quadrante = "alto a destra"
                                    elif ( posizione_cursore_y >= 168 and posizione_cursore_y <= 331 ):
                                        quadrante = "centro a destra"
                                    elif ( posizione_cursore_y >= 336 and posizione_cursore_y <= 500 ):
                                        quadrante = "basso a destra"
                                
                                # definisco le coordinate del quadrante
                                if quadrante == "alto a sinistra":
                                    quadratox = 60
                                    quadratoy = 0
                                elif quadrante == "centro a sinistra":
                                    quadratox = 60
                                    quadratoy = 168
                                elif quadrante == "basso a sinistra":
                                    quadratox = 60
                                    quadratoy = 336
                                elif quadrante == "alto in centro":
                                    quadratox = 229
                                    quadratoy = 0
                                elif quadrante == "centro":
                                    quadratox = 229
                                    quadratoy = 168
                                elif quadrante == "basso in centro":
                                    quadratox = 229
                                    quadratoy = 336
                                elif quadrante == "alto a destra":
                                    quadratox = 398
                                    quadratoy = 0
                                elif quadrante == "centro a destra":
                                    quadratox = 398
                                    quadratoy = 168
                                elif quadrante == "basso a destra":
                                    quadratox = 398
                                    quadratoy = 336
                                
                                # verifica il turno
                                if turno == 0:
                                    if quadrante == "alto a sinistra":
                                        quadrante1, rigaA, colonnaA, diagonaleA, turno = disegna_x(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno)
                                    elif quadrante == "centro a sinistra":
                                        quadrante4, rigaB, colonnaA, turno = disegna_x(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno)
                                    elif quadrante == "basso a sinistra":
                                        quadrante7, rigaC, colonnaA, diagonaleB, turno = disegna_x(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno)
                                    elif quadrante == "alto in centro":
                                        quadrante2, rigaA, colonnaB, turno = disegna_x(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno)
                                    elif quadrante == "centro":
                                        quadrante5, rigaB, colonnaB, diagonaleA, diagonaleB, turno = disegna_x(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno)
                                    elif quadrante == "basso in centro":
                                        quadrante8, rigaC, colonnaB, turno = disegna_x(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno)
                                    elif quadrante == "alto a destra":
                                        quadrante3, rigaA, colonnaC, diagonaleB, turno = disegna_x(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno)
                                    elif quadrante == "centro a destra":
                                        quadrante6, rigaB, colonnaC, turno = disegna_x(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno)
                                    elif quadrante == "basso a destra":
                                        quadrante9, rigaC, colonnaC, diagonaleA, turno = disegna_x(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno)
                                    
                                    # mostro il turno sullo schermo
                                    if turno == 0:
                                        SCHERMO.blit(turno_x, (561,0))
                                    elif turno == 1:
                                        SCHERMO.blit(turno_o, (561,0))
                                elif turno == 1:
                                    if quadrante == "alto a sinistra":
                                        quadrante1, rigaA, colonnaA, diagonaleA, turno = disegna_o(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno)
                                    elif quadrante == "centro a sinistra":
                                        quadrante4, rigaB, colonnaA, turno = disegna_o(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno)
                                    elif quadrante == "basso a sinistra":
                                        quadrante7, rigaC, colonnaA, diagonaleB, turno = disegna_o(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno)
                                    elif quadrante == "alto in centro":
                                        quadrante2, rigaA, colonnaB, turno = disegna_o(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno)
                                    elif quadrante == "centro":
                                        quadrante5, rigaB, colonnaB, diagonaleA, diagonaleB, turno = disegna_o(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno)
                                    elif quadrante == "basso in centro":
                                        quadrante8, rigaC, colonnaB, turno = disegna_o(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno)
                                    elif quadrante == "alto a destra":
                                        quadrante3, rigaA, colonnaC, diagonaleB, turno = disegna_o(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno)
                                    elif quadrante == "centro a destra":
                                        quadrante6, rigaB, colonnaC, turno = disegna_o(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno)
                                    elif quadrante == "basso a destra":
                                        quadrante9, rigaC, colonnaC, diagonaleA, turno = disegna_o(quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno)
                                    
                                    # mostro il turno sullo schermo
                                    if turno == 0:
                                        SCHERMO.blit(turno_x, (561,0))
                                    elif turno == 1:
                                        SCHERMO.blit(turno_o, (561,0))

                                # controllo chi ha perso
                                if rigaA == 3 or colonnaA == 3 or diagonaleA == 3 or rigaB == 3 or colonnaB == 3 or diagonaleB == 3 or rigaC == 3 or colonnaC == 3:
                                    vincente = "x"
                                    hai_perso(vincente)
                                elif rigaA == -3 or colonnaA == -3 or diagonaleA == -3 or rigaB == -3 or colonnaB == -3 or diagonaleB == -3 or rigaC == -3 or colonnaC == -3:
                                    vincente = "o"
                                    hai_perso(vincente)
                                
                                # verifico se i quadranti sono tutti pieni
                                if quadrante1 == False and quadrante2 == False and quadrante3 == False and quadrante4 == False and quadrante5 == False and quadrante6 == False and quadrante7 == False and quadrante8 == False and quadrante9 == False:
                                    # mostro la schermata di pareggio
                                    SCHERMO.blit(pareggio, (0,0))
                                    # aggiorno lo schermo
                                    pygame.display.update()
                                    ricominciamo = False
                                    while not ricominciamo:
                                        for event in pygame.event.get():
                                            if ( event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE ):
                                                # riporta lo schermo alla schermata iniziale del multiplayer locale
                                                SCHERMO.blit(multiplayer_locale_sfondo, (0,0))
                                                SCHERMO.blit(turno_x, (561,0))
                                                inizializza()
                                                ricominciamo = True
                                            if event.type == pygame.QUIT:
                                                    pygame.quit()

                                # aggiorno lo schermo
                                pygame.display.update()

                    # controllo se l'utente clicca il tasto per uscire
                    if event.type == pygame.QUIT:
                        pygame.quit()
            elif 85 <= coordinate_cursore[0] <= larghezza-484 and 365 <= coordinate_cursore[1] <= altezza-65:
                # crediti
                # cambio schermata e aggiorno lo schermo
                SCHERMO.blit(crediti_sfondo, (0,0))
                pygame.display.update()
                # cambio il nome della finestra
                NOME = pygame.display.set_caption("Tris - Crediti")
                # aggiorno lo stato dell'applicazione
                eseguendo_menu = False
                # verifico se l'utente clicca il tasto per tornare indietro
                while eseguendo_menu == False:
                    for event in pygame.event.get():
                        # controllo se l'utente clicca il tasto per uscire
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            # definisco le coordinate del cursore
                            coordinate_cursore = pygame.mouse.get_pos()
                            #verifico in che zona del menu si trova il click
                            if 68 <= coordinate_cursore[0] <= larghezza-769 and 68 <= coordinate_cursore[1] <= altezza-381:
                                # cambio schermata e aggiorno lo schermo
                                disegna_sfondo_e_testi()
                                pygame.display.update()
                                # cambio il nome della finestra
                                NOME = pygame.display.set_caption("Tris - Menu Principale")
                                # aggiorno lo stato dell'applicazione
                                eseguendo_menu = True
            elif 85 <= coordinate_cursore[0] <= larghezza-484 and 255 <= coordinate_cursore[1] <= altezza-175:
                # multiplayer online
                # aggiorno lo stato dell'applicazione
                eseguendo_menu = False