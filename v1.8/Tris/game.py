import os
import pygame
import socket
from _thread import *

class Menu():
    # definisco la funzione per inizializzare
    def __init__(self):
        # avvio il modulo pygame
        pygame.init()

        # trovo la cartella da dove viene eseguito il file
        self.main_dir = os.path.dirname(os.path.abspath(__file__))

        # definisci la dimensione dello schermo e la frequenza di aggiornamento delle immagini
        self.SCHERMO = pygame.display.set_mode((889,500))
        self.FPS = 60

        # raccolgo gli oggetti (immagini)
        self.sfondo_menu = pygame.image.load(f"{self.main_dir}/Immagini/Menu_Sfondo.png")
        self.multiplayer_locale_sfondo = pygame.image.load(f"{self.main_dir}/Immagini/Multiplayer_Locale.png")
        self.multiplayer_online_sfondo = pygame.image.load(f"{self.main_dir}/Immagini/Multiplayer_Online.png")
        self.x = pygame.image.load(f"{self.main_dir}/Immagini/X.png")
        self.o = pygame.image.load(f"{self.main_dir}/Immagini/O.png")
        self.x_ha_vinto = pygame.image.load(f"{self.main_dir}/Immagini/X_ha_vinto.png")
        self.o_ha_vinto = pygame.image.load(f"{self.main_dir}/Immagini/O_ha_vinto.png")
        self.icona = pygame.image.load(f"{self.main_dir}/Immagini/Icona.png")
        self.crediti_sfondo = pygame.image.load(f"{self.main_dir}/Immagini/Crediti.png")
        self.turno_o = pygame.image.load(f"{self.main_dir}/Immagini/Turno_O.png")
        self.turno_x = pygame.image.load(f"{self.main_dir}/Immagini/Turno_X.png")
        self.pareggio = pygame.image.load(f"{self.main_dir}/Immagini/Pareggio.png")

        self.turno = 0

        # definisco la larghezza e l'altezza della finestra
        self.larghezza = self.SCHERMO.get_width()
        self.altezza = self.SCHERMO.get_height()

        #definisco il nome della finestra e l'icona dell'applicazione
        self.NOME = pygame.display.set_caption("Tris - Menu Principale")
        self.ICONA = pygame.display.set_icon(self.icona)

        # definisco il font da utilizzare
        self.font = pygame.font.Font(f"{self.main_dir}/Font/MyUnderwood.ttf",28)

        # renderizzo le stringhe da mostrare 
        self.esci = self.font.render("esci", True , (0,0,0))
        self.online_multiplayer = self.font.render("multiplayer online", True, (0,0,0))
        self.local_multiplayer = self.font.render("multiplayer locale", True, (0,0,0))
        self.crediti = self.font.render("crediti", True, (0,0,0))

        # impostazione iniziale della variabile eseguendo_menu
        self.eseguendo_menu = True

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.PORT = 5050

        self.informazioni = []

    # definisco la funzione per disegnare gli elementi sfondo e testi sullo schermo
    def disegna_sfondo_e_testi(self):
        # disegno lo sfondo sullo schermo
        self.SCHERMO.blit(self.sfondo_menu, (0,0))
        
        # disegno i testi sullo schermo
        self.SCHERMO.blit(self.local_multiplayer, (self.larghezza/2+62, self.altezza/2+25))
        self.SCHERMO.blit(self.esci, (self.larghezza/2+170, self.altezza/2+136))
        self.SCHERMO.blit(self.crediti, (195, self.altezza/2+136))
        self.SCHERMO.blit(self.online_multiplayer, (103, self.altezza/2+25))
        
        #aggiorno lo schermo
        pygame.display.update() 

    # definisco la funzione inizializza() per i dati necessari al multiplayer
    def inizializza(self):
        # riporto alle impostazioni iniziali le variabili del programma
        self.rigaA = 0
        self.rigaB = 0
        self.rigaC = 0
        self.colonnaA = 0
        self.colonnaB = 0
        self.colonnaC = 0
        self.diagonaleA = 0
        self.diagonaleB = 0

        self.quadrante1 = True
        self.quadrante2 = True   
        self.quadrante3 = True
        self.quadrante4 = True
        self.quadrante5 = True
        self.quadrante6 = True
        self.quadrante7 = True
        self.quadrante8 = True
        self.quadrante9 = True

        self.quadrante = 0
        self.quadratox = 0
        self.quadratoy = 0
        self.turno = 0

    # definisco la funzine che viene eseguita quando uno dei due perde
    def hai_perso(self, vincente):
        # mostro chi ha vinto
        if vincente == "x":
            self.SCHERMO.blit(self.x_ha_vinto, (0,0))
        elif vincente == "o":
            self.SCHERMO.blit(self.o_ha_vinto, (0,0))
        # aggiorno lo schermo
        pygame.display.update()
        ricominciamo = False
        while not ricominciamo:
            for event in pygame.event.get():
                if ( event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE ):
                    # riporta lo schermo alla schermata iniziale del multiplayer locale
                    self.SCHERMO.blit(self.multiplayer_locale_sfondo, (0,0))
                    self.SCHERMO.blit(self.turno_x, (561,0))
                    self.inizializza()
                    ricominciamo = True
                if event.type == pygame.QUIT:
                        pygame.quit()

    # aggiungo la x alle coordinate del quadrante selezionato
    def disegna_x(self, quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno):    
        if quadrante == "alto a sinistra":
            if quadrante1 == True:
                self.informazioni = [bytes(f"{quadratox}", "utf-8"), bytes(f"{quadratoy}", "utf-8"), bytes("x", "utf-8")]
                self.s.send(self.informazioni[0])
                self.s.send(self.informazioni[1])
                self.s.send(self.informazioni[2])
                self.SCHERMO.blit(self.x, (quadratox,quadratoy))
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
                self.SCHERMO.blit(self.x, (quadratox,quadratoy))
                quadrante4 = False
                turno = turno + 1
                rigaB = rigaB + 1
                colonnaA = colonnaA + 1
                return quadrante4, rigaB, colonnaA, turno
            elif quadrante4 == False:
                return quadrante4, rigaB, colonnaA, turno
        elif quadrante == "basso a sinistra":
            if quadrante7 == True:
                self.SCHERMO.blit(self.x, (quadratox,quadratoy))
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
                self.SCHERMO.blit(self.x, (quadratox,quadratoy))
                quadrante2 = False
                turno = turno + 1
                rigaA = rigaA + 1
                colonnaB = colonnaB + 1
                return quadrante2, rigaA, colonnaB, turno
            elif quadrante2 == False:
                return quadrante2, rigaA, colonnaB, turno
        elif quadrante == "centro":
            if quadrante5 == True:
                self.SCHERMO.blit(self.x, (quadratox,quadratoy))
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
                self.SCHERMO.blit(self.x, (quadratox,quadratoy))
                quadrante8 = False
                turno = turno + 1
                rigaC = rigaC + 1
                colonnaB = colonnaB + 1
                return quadrante8, rigaC, colonnaB, turno
            elif quadrante8 == False:
                return quadrante8, rigaC, colonnaB, turno
        elif quadrante == "alto a destra":
            if quadrante3 == True:
                self.SCHERMO.blit(self.x, (quadratox,quadratoy))
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
                self.SCHERMO.blit(self.x, (quadratox,quadratoy))
                quadrante6 = False
                turno = turno + 1
                rigaB = rigaB + 1
                colonnaC = colonnaC + 1
                return quadrante6, rigaB, colonnaC, turno
            elif quadrante6 == False:
                return quadrante6, rigaB, colonnaC, turno
        elif quadrante == "basso a destra":
            if quadrante9 == True:
                self.SCHERMO.blit(self.x, (quadratox,quadratoy))
                quadrante9 = False
                turno = turno + 1
                rigaC = rigaC + 1
                colonnaC = colonnaC + 1
                diagonaleA = diagonaleA + 1
                return quadrante9, rigaC, colonnaC, diagonaleA, turno
            elif quadrante9 == False:
                return quadrante9, rigaC, colonnaC, diagonaleA, turno

    # aggiungo la o alle coordinate del quadrante selezionato
    def disegna_o(self, quadrante, quadrante1, quadrante2, quadrante3, quadrante4, quadrante5, quadrante6, quadrante7, quadrante8, quadrante9, quadratox, quadratoy, rigaA, rigaB, rigaC, colonnaA, colonnaB, colonnaC, diagonaleA, diagonaleB, turno):
        if quadrante == "alto a sinistra":
            if quadrante1 == True:
                self.SCHERMO.blit(self.o, (quadratox,quadratoy))
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
                self.SCHERMO.blit(self.o, (quadratox,quadratoy))
                quadrante4 = False
                turno = turno - 1
                rigaB = rigaB - 1
                colonnaA = colonnaA - 1
                return quadrante4, rigaB, colonnaA, turno
            elif quadrante4 == False:
                return quadrante4, rigaB, colonnaA, turno
        elif quadrante == "basso a sinistra":
            if quadrante7 == True:
                self.SCHERMO.blit(self.o, (quadratox,quadratoy))
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
                self.SCHERMO.blit(self.o, (quadratox,quadratoy))
                quadrante2 = False
                turno = turno - 1
                rigaA = rigaA - 1
                colonnaB = colonnaB - 1
                return quadrante2, rigaA, colonnaB, turno
            elif quadrante2 == False:
                return quadrante2, rigaA, colonnaB, turno
        elif quadrante == "centro":
            if quadrante5 == True:
                self.SCHERMO.blit(self.o, (quadratox,quadratoy))
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
                self.SCHERMO.blit(self.o, (quadratox,quadratoy))
                quadrante8 = False
                turno = turno - 1
                rigaC = rigaC - 1
                colonnaB = colonnaB - 1
                return quadrante8, rigaC, colonnaB, turno
            elif quadrante8 == False:
                return quadrante8, rigaC, colonnaB, turno
        elif quadrante == "alto a destra":
            if quadrante3 == True:
                self.SCHERMO.blit(self.o, (quadratox,quadratoy))
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
                self.SCHERMO.blit(self.o, (quadratox,quadratoy))
                quadrante6 = False
                turno = turno - 1
                rigaB = rigaB - 1
                colonnaC = colonnaC - 1
                return quadrante6, rigaB, colonnaC, turno
            elif quadrante6 == False:
                return quadrante6, rigaB, colonnaC, turno
        elif quadrante == "basso a destra":
            if quadrante9 == True:
                self.SCHERMO.blit(self.o, (quadratox,quadratoy))
                quadrante9 = False
                turno = turno - 1
                rigaC = rigaC - 1
                colonnaC = colonnaC - 1
                diagonaleA = diagonaleA - 1
                return quadrante9, rigaC, colonnaC, diagonaleA, turno
            elif quadrante9 == False:
                return quadrante9, rigaC, colonnaC, diagonaleA, turno

    def menu(self):
        while self.eseguendo_menu:
            for event in pygame.event.get():
                # verifico se l'utente chiude l'applicazione
                if event.type == pygame.QUIT:
                    pygame.quit()
                # verifico se l'utente sta cliccando un tasto del mouse
                if event.type == pygame.MOUSEBUTTONUP:
                    # definisco le coordinate del cursore
                    coordinate_cursore = pygame.mouse.get_pos()
                    #verifico in che zona del menu si trova il click
                    # esci
                    if 484 <= coordinate_cursore[0] <= self.larghezza-80 and 365 <= coordinate_cursore[1] <= self.altezza-65:
                        # esci
                        pygame.quit()
                    # multiplayer locale
                    if 484 <= coordinate_cursore[0] <= self.larghezza-80 and 255 <= coordinate_cursore[1] <= self.altezza-175:
                        Locale().gioco()
                    # crediti
                    elif 85 <= coordinate_cursore[0] <= self.larghezza-484 and 365 <= coordinate_cursore[1] <= self.altezza-65:
                        Crediti().mostra()
                    # multiplayer online
                    elif 85 <= coordinate_cursore[0] <= self.larghezza-484 and 255 <= coordinate_cursore[1] <= self.altezza-175:
                        Online().gioco()

class Crediti(Menu):
    def mostra(self):
        # crediti
        # cambio schermata e aggiorno lo schermo
        self.SCHERMO.blit(self.crediti_sfondo, (0,0))
        pygame.display.update()
        # cambio il nome della finestra
        self.NOME = pygame.display.set_caption("Tris - Crediti")
        # aggiorno lo stato dell'applicazione
        self.eseguendo_menu = False
        # verifico se l'utente clicca il tasto per tornare indietro
        while self.eseguendo_menu == False:
            for event in pygame.event.get():
                # controllo se l'utente clicca il tasto per uscire
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # definisco le coordinate del cursore
                    coordinate_cursore = pygame.mouse.get_pos()
                    #verifico in che zona del menu si trova il click
                    if 68 <= coordinate_cursore[0] <= self.larghezza-769 and 68 <= coordinate_cursore[1] <= self.altezza-381:
                        # cambio schermata e aggiorno lo schermo
                        self.disegna_sfondo_e_testi()
                        pygame.display.update()
                        # cambio il nome della finestra
                        NOME = pygame.display.set_caption("Tris - Menu Principale")
                        # aggiorno lo stato dell'applicazione
                        self.eseguendo_menu = True

class Locale(Menu):
    def gioco(self):
        # multiplayer locale
        # cambio schermata
        self.SCHERMO.blit(self.multiplayer_locale_sfondo, (0,0))
        # mostro il turno
        self.SCHERMO.blit(self.turno_x, (561,0))
        # aggiorno lo schermo
        pygame.display.update()
        # cambio il nome della finestra
        self.NOME = pygame.display.set_caption("Tris - Multiplayer Locale")
        # aggiorno lo stato dell'applicazione
        self.eseguendo_menu = False
        # verifico se l'utente clicca il tasto per tornare indietro
        self.inizializza()
        while not self.eseguendo_menu:
            for event in pygame.event.get():
                # controllo se l'utente clicca il tasto per tornare indietro
                if event.type == pygame.MOUSEBUTTONUP:
                    # definisco le coordinate del cursore
                    posizione_cursore_x, posizione_cursore_y = pygame.mouse.get_pos()
                    #verifico in che zona del menu si trova il click
                    if 8 <= posizione_cursore_x <= 49 and 8 <= posizione_cursore_y <= self.altezza-451:
                        # cambio schermata e aggiorno lo schermo
                        self.disegna_sfondo_e_testi()
                        pygame.display.update()
                        # cambio il nome della finestra
                        self.NOME = pygame.display.set_caption("Tris - Menu Principale")
                        # aggiorno lo stato dell'applicazione
                        self.eseguendo_menu = True
                    # verifico in area si trova il click
                    if 60 <= posizione_cursore_x <= 560 and 0 <= posizione_cursore_y <= 500:
                        # verifico in che colonna si trova il click
                        if ( posizione_cursore_x >= 60 and posizione_cursore_x <= 224 ):
                            # verifico in che riga si trova il click
                            if ( posizione_cursore_y >= 0 and posizione_cursore_y <= 164 ):
                                self.quadrante = "alto a sinistra"
                            elif ( posizione_cursore_y >= 168 and posizione_cursore_y <= 331 ):
                                self.quadrante = "centro a sinistra"
                            elif ( posizione_cursore_y >= 336 and posizione_cursore_y <= 500 ):
                                self.quadrante = "basso a sinistra"
                        elif ( posizione_cursore_x >= 229 and posizione_cursore_x <= 393 ):
                            if ( posizione_cursore_y >= 0 and posizione_cursore_y <= 164 ):
                                self.quadrante = "alto in centro"
                            elif ( posizione_cursore_y >= 168 and posizione_cursore_y <= 331 ):
                                self.quadrante = "centro"
                            elif ( posizione_cursore_y >= 336 and posizione_cursore_y <= 500 ):
                                self.quadrante = "basso in centro"
                        elif ( posizione_cursore_x >= 398 and posizione_cursore_x <= 560 ):
                            if ( posizione_cursore_y >= 0 and posizione_cursore_y <= 164 ):
                                self.quadrante = "alto a destra"
                            elif ( posizione_cursore_y >= 168 and posizione_cursore_y <= 331 ):
                                self.quadrante = "centro a destra"
                            elif ( posizione_cursore_y >= 336 and posizione_cursore_y <= 500 ):
                                self.quadrante = "basso a destra"
                        
                        # definisco le coordinate del quadrante
                        if self.quadrante == "alto a sinistra":
                            self.quadratox = 60
                            self.quadratoy = 0
                        elif self.quadrante == "centro a sinistra":
                            self.quadratox = 60
                            self.quadratoy = 168
                        elif self.quadrante == "basso a sinistra":
                            self.quadratox = 60
                            self.quadratoy = 336
                        elif self.quadrante == "alto in centro":
                            self.quadratox = 229
                            self.quadratoy = 0
                        elif self.quadrante == "centro":
                            self.quadratox = 229
                            self.quadratoy = 168
                        elif self.quadrante == "basso in centro":
                            self.quadratox = 229
                            self.quadratoy = 336
                        elif self.quadrante == "alto a destra":
                            self.quadratox = 398
                            self.quadratoy = 0
                        elif self.quadrante == "centro a destra":
                            self.quadratox = 398
                            self.quadratoy = 168
                        elif self.quadrante == "basso a destra":
                            self.quadratox = 398
                            self.quadratoy = 336
                        
                        # verifica il turno
                        if self.turno == 0:
                            if self.quadrante == "alto a sinistra":
                                self.quadrante1, self.rigaA, self.colonnaA, self.diagonaleA, self.turno = self.disegna_x(self.quadrante, self.quadrante1, self.quadrante2, self.quadrante3, self.quadrante4, self.quadrante5, self.quadrante6, self.quadrante7, self.quadrante8, self.quadrante9, self.quadratox, self.quadratoy, self.rigaA, self.rigaB, self.rigaC, self.colonnaA, self.colonnaB, self.colonnaC, self.diagonaleA, self.diagonaleB, self.turno)
                            elif self.quadrante == "centro a sinistra":
                                self.quadrante4, self.rigaB, self.colonnaA, self.turno = self.disegna_x(self.quadrante, self.quadrante1, self.quadrante2, self.quadrante3, self.quadrante4, self.quadrante5, self.quadrante6, self.quadrante7, self.quadrante8, self.quadrante9, self.quadratox, self.quadratoy, self.rigaA, self.rigaB, self.rigaC, self.colonnaA, self.colonnaB, self.colonnaC, self.diagonaleA, self.diagonaleB, self.turno)
                            elif self.quadrante == "basso a sinistra":
                                self.quadrante7, self.rigaC, self.colonnaA, self.diagonaleB, self.turno = self.disegna_x(self.quadrante, self.quadrante1, self.quadrante2, self.quadrante3, self.quadrante4, self.quadrante5, self.quadrante6, self.quadrante7, self.quadrante8, self.quadrante9, self.quadratox, self.quadratoy, self.rigaA, self.rigaB, self.rigaC, self.colonnaA, self.colonnaB, self.colonnaC, self.diagonaleA, self.diagonaleB, self.turno)
                            elif self.quadrante == "alto in centro":
                                self.quadrante2, self.rigaA, self.colonnaB, self.turno = self.disegna_x(self.quadrante, self.quadrante1, self.quadrante2, self.quadrante3, self.quadrante4, self.quadrante5, self.quadrante6, self.quadrante7, self.quadrante8, self.quadrante9, self.quadratox, self.quadratoy, self.rigaA, self.rigaB, self.rigaC, self.colonnaA, self.colonnaB, self.colonnaC, self.diagonaleA, self.diagonaleB, self.turno)
                            elif self.quadrante == "centro":
                                self.quadrante5, self.rigaB, self.colonnaB, self.diagonaleA, self.diagonaleB, self.turno = self.disegna_x(self.quadrante, self.quadrante1, self.quadrante2, self.quadrante3, self.quadrante4, self.quadrante5, self.quadrante6, self.quadrante7, self.quadrante8, self.quadrante9, self.quadratox, self.quadratoy, self.rigaA, self.rigaB, self.rigaC, self.colonnaA, self.colonnaB, self.colonnaC, self.diagonaleA, self.diagonaleB, self.turno)
                            elif self.quadrante == "basso in centro":
                                self.quadrante8, self.rigaC, self.colonnaB, self.turno = self.disegna_x(self.quadrante, self.quadrante1, self.quadrante2, self.quadrante3, self.quadrante4, self.quadrante5, self.quadrante6, self.quadrante7, self.quadrante8, self.quadrante9, self.quadratox, self.quadratoy, self.rigaA, self.rigaB, self.rigaC, self.colonnaA, self.colonnaB, self.colonnaC, self.diagonaleA, self.diagonaleB, self.turno)
                            elif self.quadrante == "alto a destra":
                                self.quadrante3, self.rigaA, self.colonnaC, self.diagonaleB, self.turno = self.disegna_x(self.quadrante, self.quadrante1, self.quadrante2, self.quadrante3, self.quadrante4, self.quadrante5, self.quadrante6, self.quadrante7, self.quadrante8, self.quadrante9, self.quadratox, self.quadratoy, self.rigaA, self.rigaB, self.rigaC, self.colonnaA, self.colonnaB, self.colonnaC, self.diagonaleA, self.diagonaleB, self.turno)
                            elif self.quadrante == "centro a destra":
                                self.quadrante6, self.rigaB, self.colonnaC, self.turno = self.disegna_x(self.quadrante, self.quadrante1, self.quadrante2, self.quadrante3, self.quadrante4, self.quadrante5, self.quadrante6, self.quadrante7, self.quadrante8, self.quadrante9, self.quadratox, self.quadratoy, self.rigaA, self.rigaB, self.rigaC, self.colonnaA, self.colonnaB, self.colonnaC, self.diagonaleA, self.diagonaleB, self.turno)
                            elif self.quadrante == "basso a destra":
                                self.quadrante9, self.rigaC, self.colonnaC, self.diagonaleA, self.turno = self.disegna_x(self.quadrante, self.quadrante1, self.quadrante2, self.quadrante3, self.quadrante4, self.quadrante5, self.quadrante6, self.quadrante7, self.quadrante8, self.quadrante9, self.quadratox, self.quadratoy, self.rigaA, self.rigaB, self.rigaC, self.colonnaA, self.colonnaB, self.colonnaC, self.diagonaleA, self.diagonaleB, self.turno)
                            
                            # mostro il turno sullo schermo
                            if self.turno == 0:
                                self.SCHERMO.blit(self.turno_x, (561,0))
                            elif self.turno == 1:
                                self.SCHERMO.blit(self.turno_o, (561,0))
                        elif self.turno == 1:
                            if self.quadrante == "alto a sinistra":
                                self.quadrante1, self.rigaA, self.colonnaA, self.diagonaleA, self.turno = self.disegna_o(self.quadrante, self.quadrante1, self.quadrante2, self.quadrante3, self.quadrante4, self.quadrante5, self.quadrante6, self.quadrante7, self.quadrante8, self.quadrante9, self.quadratox, self.quadratoy, self.rigaA, self.rigaB, self.rigaC, self.colonnaA, self.colonnaB, self.colonnaC, self.diagonaleA, self.diagonaleB, self.turno)
                            elif self.quadrante == "centro a sinistra":
                                self.quadrante4, self.rigaB, self.colonnaA, self.turno = self.disegna_o(self.quadrante, self.quadrante1, self.quadrante2, self.quadrante3, self.quadrante4, self.quadrante5, self.quadrante6, self.quadrante7, self.quadrante8, self.quadrante9, self.quadratox, self.quadratoy, self.rigaA, self.rigaB, self.rigaC, self.colonnaA, self.colonnaB, self.colonnaC, self.diagonaleA, self.diagonaleB, self.turno)
                            elif self.quadrante == "basso a sinistra":
                                self.quadrante7, self.rigaC, self.colonnaA, self.diagonaleB, self.turno = self.disegna_o(self.quadrante, self.quadrante1, self.quadrante2, self.quadrante3, self.quadrante4, self.quadrante5, self.quadrante6, self.quadrante7, self.quadrante8, self.quadrante9, self.quadratox, self.quadratoy, self.rigaA, self.rigaB, self.rigaC, self.colonnaA, self.colonnaB, self.colonnaC, self.diagonaleA, self.diagonaleB, self.turno)
                            elif self.quadrante == "alto in centro":
                                self.quadrante2, self.rigaA, self.colonnaB, self.turno = self.disegna_o(self.quadrante, self.quadrante1, self.quadrante2, self.quadrante3, self.quadrante4, self.quadrante5, self.quadrante6, self.quadrante7, self.quadrante8, self.quadrante9, self.quadratox, self.quadratoy, self.rigaA, self.rigaB, self.rigaC, self.colonnaA, self.colonnaB, self.colonnaC, self.diagonaleA, self.diagonaleB, self.turno)
                            elif self.quadrante == "centro":
                                self.quadrante5, self.rigaB, self.colonnaB, self.diagonaleA, self.diagonaleB, self.turno = self.disegna_o(self.quadrante, self.quadrante1, self.quadrante2, self.quadrante3, self.quadrante4, self.quadrante5, self.quadrante6, self.quadrante7, self.quadrante8, self.quadrante9, self.quadratox, self.quadratoy, self.rigaA, self.rigaB, self.rigaC, self.colonnaA, self.colonnaB, self.colonnaC, self.diagonaleA, self.diagonaleB, self.turno)
                            elif self.quadrante == "basso in centro":
                                self.quadrante8, self.rigaC, self.colonnaB, self.turno = self.disegna_o(self.quadrante, self.quadrante1, self.quadrante2, self.quadrante3, self.quadrante4, self.quadrante5, self.quadrante6, self.quadrante7, self.quadrante8, self.quadrante9, self.quadratox, self.quadratoy, self.rigaA, self.rigaB, self.rigaC, self.colonnaA, self.colonnaB, self.colonnaC, self.diagonaleA, self.diagonaleB, self.turno)
                            elif self.quadrante == "alto a destra":
                                self.quadrante3, self.rigaA, self.colonnaC, self.diagonaleB, self.turno = self.disegna_o(self.quadrante, self.quadrante1, self.quadrante2, self.quadrante3, self.quadrante4, self.quadrante5, self.quadrante6, self.quadrante7, self.quadrante8, self.quadrante9, self.quadratox, self.quadratoy, self.rigaA, self.rigaB, self.rigaC, self.colonnaA, self.colonnaB, self.colonnaC, self.diagonaleA, self.diagonaleB, self.turno)
                            elif self.quadrante == "centro a destra":
                                self.quadrante6, self.rigaB, self.colonnaC, self.turno = self.disegna_o(self.quadrante, self.quadrante1, self.quadrante2, self.quadrante3, self.quadrante4, self.quadrante5, self.quadrante6, self.quadrante7, self.quadrante8, self.quadrante9, self.quadratox, self.quadratoy, self.rigaA, self.rigaB, self.rigaC, self.colonnaA, self.colonnaB, self.colonnaC, self.diagonaleA, self.diagonaleB, self.turno)
                            elif self.quadrante == "basso a destra":
                                self.quadrante9, self.rigaC, self.colonnaC, self.diagonaleA, self.turno = self.disegna_o(self.quadrante, self.quadrante1, self.quadrante2, self.quadrante3, self.quadrante4, self.quadrante5, self.quadrante6, self.quadrante7, self.quadrante8, self.quadrante9, self.quadratox, self.quadratoy, self.rigaA, self.rigaB, self.rigaC, self.colonnaA, self.colonnaB, self.colonnaC, self.diagonaleA, self.diagonaleB, self.turno)
                            
                            # mostro il turno sullo schermo
                            if self.turno == 0:
                                self.SCHERMO.blit(self.turno_x, (561,0))
                            elif self.turno == 1:
                                self.SCHERMO.blit(self.turno_o, (561,0))

                        # controllo chi ha perso
                        if self.rigaA == 3 or self.colonnaA == 3 or self.diagonaleA == 3 or self.rigaB == 3 or self.colonnaB == 3 or self.diagonaleB == 3 or self.rigaC == 3 or self.colonnaC == 3:
                            vincente = "x"
                            self.hai_perso(vincente)
                        elif self.rigaA == -3 or self.colonnaA == -3 or self.diagonaleA == -3 or self.rigaB == -3 or self.colonnaB == -3 or self.diagonaleB == -3 or self.rigaC == -3 or self.colonnaC == -3:
                            vincente = "o"
                            self.hai_perso(vincente)
                        
                        # verifico se i quadranti sono tutti pieni
                        if self.quadrante1 == False and self.quadrante2 == False and self.quadrante3 == False and self.quadrante4 == False and self.quadrante5 == False and self.quadrante6 == False and self.quadrante7 == False and self.quadrante8 == False and self.quadrante9 == False:
                            # mostro la schermata di pareggio
                            self.SCHERMO.blit(self.pareggio, (0,0))
                            # aggiorno lo schermo
                            pygame.display.update()
                            ricominciamo = False
                            while not ricominciamo:
                                for event in pygame.event.get():
                                    if ( event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE ):
                                        # riporta lo schermo alla schermata iniziale del multiplayer locale
                                        self.SCHERMO.blit(self.multiplayer_locale_sfondo, (0,0))
                                        self.SCHERMO.blit(self.turno_x, (561,0))
                                        self.inizializza()
                                        ricominciamo = True
                                    if event.type == pygame.QUIT:
                                            pygame.quit()

                        # aggiorno lo schermo
                        pygame.display.update()

            # controllo se l'utente clicca il tasto per uscire
            if event.type == pygame.QUIT:
                pygame.quit()

class Online(Menu):
    def gioco(self):
        # multiplayer online

        ###################################################################################
        global ngioc
        global comando
        global quadranti_selezionati

        self.s.connect(("192.168.2.56", self.PORT))
        # ricevo il numero del giocatore
        ngioc = ""

        while ngioc == "":
            ngioc = self.s.recv(1024).decode("utf-8")
        
        print(ngioc)
        ###################################################################################

        # cambio schermata
        self.SCHERMO.blit(self.multiplayer_online_sfondo, (0,0))
        # mostro il turno
        self.SCHERMO.blit(self.turno_x, (561,0))
        # aggiorno lo schermo
        pygame.display.update()
        # cambio il nome della finestra
        self.NOME = pygame.display.set_caption("Tris - Multiplayer Online")
        # aggiorno lo stato dell'applicazione
        self.eseguendo_menu = False
        # verifico se l'utente clicca il tasto per tornare indietro
        self.inizializza()
        while not self.eseguendo_menu:
            for event in pygame.event.get():
                # controllo se l'utente clicca il tasto per tornare indietro
                if event.type == pygame.MOUSEBUTTONUP:
                    # definisco le coordinate del cursore
                    posizione_cursore_x, posizione_cursore_y = pygame.mouse.get_pos()
                    #verifico in che zona del menu si trova il click
                    if 8 <= posizione_cursore_x <= 49 and 8 <= posizione_cursore_y <= self.altezza-451:
                        # cambio schermata e aggiorno lo schermo
                        self.disegna_sfondo_e_testi()
                        pygame.display.update()
                        # cambio il nome della finestra
                        self.NOME = pygame.display.set_caption("Tris - Menu Principale")
                        # aggiorno lo stato dell'applicazione
                        self.eseguendo_menu = True

                    # verifico in area si trova il click
                    if 60 <= posizione_cursore_x <= 560 and 0 <= posizione_cursore_y <= 500:
                        try:
                            self.s.send(bytes(f"{self.turno}", "utf-8"))
                        except:
                            pass

                        try:
                            comando = self.s.recv(1024).decode("utf-8")
                        except:
                            pass

                        if comando == "disegnax":

                            # verifico in che colonna si trova il click
                            if ( posizione_cursore_x >= 60 and posizione_cursore_x <= 224 ):
                                # verifico in che riga si trova il click
                                if ( posizione_cursore_y >= 0 and posizione_cursore_y <= 164 ):
                                    self.quadrante = "alto a sinistra"
                                elif ( posizione_cursore_y >= 168 and posizione_cursore_y <= 331 ):
                                    self.quadrante = "centro a sinistra"
                                elif ( posizione_cursore_y >= 336 and posizione_cursore_y <= 500 ):
                                    self.quadrante = "basso a sinistra"
                            elif ( posizione_cursore_x >= 229 and posizione_cursore_x <= 393 ):
                                if ( posizione_cursore_y >= 0 and posizione_cursore_y <= 164 ):
                                    self.quadrante = "alto in centro"
                                elif ( posizione_cursore_y >= 168 and posizione_cursore_y <= 331 ):
                                    self.quadrante = "centro"
                                elif ( posizione_cursore_y >= 336 and posizione_cursore_y <= 500 ):
                                    self.quadrante = "basso in centro"
                            elif ( posizione_cursore_x >= 398 and posizione_cursore_x <= 560 ):
                                if ( posizione_cursore_y >= 0 and posizione_cursore_y <= 164 ):
                                    self.quadrante = "alto a destra"
                                elif ( posizione_cursore_y >= 168 and posizione_cursore_y <= 331 ):
                                    self.quadrante = "centro a destra"
                                elif ( posizione_cursore_y >= 336 and posizione_cursore_y <= 500 ):
                                    self.quadrante = "basso a destra"
                            
                            # definisco le coordinate del quadrante
                            if self.quadrante == "alto a sinistra":
                                self.quadratox = 60
                                self.quadratoy = 0
                                self.quadrante1 = "False"
                            elif self.quadrante == "centro a sinistra":
                                self.quadratox = 60
                                self.quadratoy = 168
                                self.quadrante4 = "False"
                            elif self.quadrante == "basso a sinistra":
                                self.quadratox = 60
                                self.quadratoy = 336
                                self.quadrante7 = "False"
                            elif self.quadrante == "alto in centro":
                                self.quadratox = 229
                                self.quadratoy = 0
                                self.quadrante2 = "False"
                            elif self.quadrante == "centro":
                                self.quadratox = 229
                                self.quadratoy = 168
                                self.quadrante5 = "False"
                            elif self.quadrante == "basso in centro":
                                self.quadratox = 229
                                self.quadratoy = 336
                                self.quadrante8 = "False"
                            elif self.quadrante == "alto a destra":
                                self.quadratox = 398
                                self.quadratoy = 0
                                self.quadrante3 = "False"
                            elif self.quadrante == "centro a destra":
                                self.quadratox = 398
                                self.quadratoy = 168
                                self.quadrante6 = "False"
                            elif self.quadrante == "basso a destra":
                                self.quadratox = 398
                                self.quadratoy = 336
                                self.quadrante9 = "False"
                            
                            #try:
                            #    self.s.send(bytes(f"{self.quadratox},{self.quadratoy}", "utf-8"))
                            #except:
                            #    pass

                            self.turno += 1

                            try:
                                self.s.send(bytes(f"{self.quadrante1},{self.quadrante2},{self.quadrante3},{self.quadrante4},{self.quadrante5},{self.quadrante6},{self.quadrante7},{self.quadrante8},{self.quadrante9}", "utf-8"))
                            except:
                                pass

                            self.SCHERMO.blit(self.x, (self.quadratox, self.quadratoy))
                            pygame.display.update()

                        if comando == "disegnao":

                            # verifico in che colonna si trova il click
                            if ( posizione_cursore_x >= 60 and posizione_cursore_x <= 224 ):
                                # verifico in che riga si trova il click
                                if ( posizione_cursore_y >= 0 and posizione_cursore_y <= 164 ):
                                    self.quadrante = "alto a sinistra"
                                elif ( posizione_cursore_y >= 168 and posizione_cursore_y <= 331 ):
                                    self.quadrante = "centro a sinistra"
                                elif ( posizione_cursore_y >= 336 and posizione_cursore_y <= 500 ):
                                    self.quadrante = "basso a sinistra"
                            elif ( posizione_cursore_x >= 229 and posizione_cursore_x <= 393 ):
                                if ( posizione_cursore_y >= 0 and posizione_cursore_y <= 164 ):
                                    self.quadrante = "alto in centro"
                                elif ( posizione_cursore_y >= 168 and posizione_cursore_y <= 331 ):
                                    self.quadrante = "centro"
                                elif ( posizione_cursore_y >= 336 and posizione_cursore_y <= 500 ):
                                    self.quadrante = "basso in centro"
                            elif ( posizione_cursore_x >= 398 and posizione_cursore_x <= 560 ):
                                if ( posizione_cursore_y >= 0 and posizione_cursore_y <= 164 ):
                                    self.quadrante = "alto a destra"
                                elif ( posizione_cursore_y >= 168 and posizione_cursore_y <= 331 ):
                                    self.quadrante = "centro a destra"
                                elif ( posizione_cursore_y >= 336 and posizione_cursore_y <= 500 ):
                                    self.quadrante = "basso a destra"
                            
                            # definisco le coordinate del quadrante
                            if self.quadrante == "alto a sinistra":
                                self.quadratox = 60
                                self.quadratoy = 0
                                self.quadrante1 = "False"
                            elif self.quadrante == "centro a sinistra":
                                self.quadratox = 60
                                self.quadratoy = 168
                                self.quadrante4 = "False"
                            elif self.quadrante == "basso a sinistra":
                                self.quadratox = 60
                                self.quadratoy = 336
                                self.quadrante7 = False
                            elif self.quadrante == "alto in centro":
                                self.quadratox = 229
                                self.quadratoy = 0
                                self.quadrante2 = "False"
                            elif self.quadrante == "centro":
                                self.quadratox = 229
                                self.quadratoy = 168
                                self.quadrante5 = "False"
                            elif self.quadrante == "basso in centro":
                                self.quadratox = 229
                                self.quadratoy = 336
                                self.quadrante8 = "False"
                            elif self.quadrante == "alto a destra":
                                self.quadratox = 398
                                self.quadratoy = 0
                                self.quadrante3 = "False"
                            elif self.quadrante == "centro a destra":
                                self.quadratox = 398
                                self.quadratoy = 168
                                self.quadrante6 = "False"
                            elif self.quadrante == "basso a destra":
                                self.quadratox = 398
                                self.quadratoy = 336
                                self.quadrante9 = "False"
                            
                            #try:
                            #    self.s.send(bytes(f"{self.quadratox},{self.quadratoy}", "utf-8"))
                            #except:
                            #    pass 

                            self.turno -= 1

                            try:
                                self.s.send(bytes(f"{self.quadrante1},{self.quadrante2},{self.quadrante3},{self.quadrante4},{self.quadrante5},{self.quadrante6},{self.quadrante7},{self.quadrante8},{self.quadrante9}", "utf-8"))
                            except:
                                pass

                            self.SCHERMO.blit(self.o, (self.quadratox, self.quadratoy))
                            pygame.display.update()

                        try:
                            quadranti_selezionati = self.s.recv(1024).decode("utf-8")
                            print(quadranti_selezionati)
                        except:
                            pass
                            
                        #try:
                        #    turno = self.s.recv(1024).decode("utf-8")
                        #    self.turno = int(turno)
                        #except:
                        #    pass
                        
                        #for i in range(0, len(quadranti_selezionati))
                        #    if quadranti_selezionati[i]:
                        #        if i+:
                        #            self.SCHERMO.blit(self.x, )

                    # aggiorno lo schermo
                    pygame.display.update()

                # controllo se l'utente clicca il tasto per uscire
                if event.type == pygame.QUIT:
                    pygame.quit()