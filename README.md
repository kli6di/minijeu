import pygame
import sys
import time

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Le Jeu des Portes")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Chargement des images
porte_heureuse = pygame.image.load("porte.jpg")  # Remplace par ton chemin d'image
porte_triste = pygame.image.load("porte.jpg")      # Remplace par ton chemin d'image

# Redimensionnement des images pour qu'elles rentrent dans la fenêtre
porte_heureuse = pygame.transform.scale(porte_heureuse, (300, 500))
porte_triste = pygame.transform.scale(porte_triste, (300, 500))

# Chargement des sons
son_heureux = pygame.mixer.Sound("son.wav")  # Remplace par ton chemin de son
son_triste = pygame.mixer.Sound("son.wav")    # Remplace par ton chemin de son

def afficher_texte(texte, x, y, taille=36, couleur=NOIR):
    police = pygame.font.Font(None, taille)
    surface_texte = police.render(texte, True, couleur)
    fenetre.blit(surface_texte, (x, y))

def afficher_portes():
    fenetre.fill(BLANC)
    afficher_texte("Choisis une porte !", 250, 50)
    fenetre.blit(porte_heureuse, (100, 150))  # Porte heureuse à gauche
    fenetre.blit(porte_triste, (450, 150))   # Porte triste à droite
    pygame.display.flip()

def afficher_salle_heureuse():
    fenetre.fill(BLANC)
    afficher_texte("✨✨✨ Félicitations ! Tu es dans la salle heureuse ! ✨✨✨", 50, 250)
    pygame.display.flip()
    son_heureux.play()
    time.sleep(3)  # Attend 3 secondes pour entendre le son

def afficher_salle_triste():
    fenetre.fill(BLANC)
    afficher_texte("🌧️🌧️🌧️ Oh non... Tu es dans la salle triste... 🌧️🌧️🌧️", 50, 250)
    pygame.display.flip()
    son_triste.play()
    time.sleep(3)  # Attend 3 secondes pour entendre le son

def main():
    running = True
    while running:
        afficher_portes()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                # Si l'utilisateur clique sur la porte heureuse
                if 100 <= x <= 400 and 150 <= y <= 650:
                    afficher_salle_heureuse()

                # Si l'utilisateur clique sur la porte triste
                elif 450 <= x <= 750 and 150 <= y <= 650:
                    afficher_salle_triste()

if __name__ == "__main__":
    main()
