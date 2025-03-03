def afficher_salle_heureuse():
    print("Félicitations ! Tu es dans la salle heureuse !")
    print("C'est un endroit rempli de joie et de lumière. Profite de ton séjour !")

def afficher_salle_triste():
    print("Oh non... Tu es dans la salle triste.")
    print("C'est un endroit sombre et froid. Prends courage, peut-être qu'une autre fois sera meilleure.")

def poser_question():
    question = "Veux-tu entrer dans la salle heureuse ? (oui/non) : "
    reponse = input(question).strip().lower()

    if reponse == "oui":
        afficher_salle_heureuse()
    elif reponse == "non":
        afficher_salle_triste()
    else:
        print("Réponse invalide. Tu dois choisir entre 'oui' ou 'non'.")
        poser_question()  # Redemande la question si la réponse n'est pas valide

def main():
    print("Bienvenue dans le mini-jeu des portes !")
    print("Devant toi se trouvent deux portes. L'une mène à une salle heureuse, l'autre à une salle triste.")
    print("Réponds à la question suivante pour choisir ta porte.")
    
    poser_question()

if __name__ == "__main__":
    main()