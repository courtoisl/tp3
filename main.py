import random

niveau_vie = 20
nombre_denemie_combattus = 0
nombre_defaite = 0
nombre_victoire = 0
numero_comba = 0
while niveau_vie > 0:
    print(f"Votre niveau de vie est {niveau_vie}")
    print("✧･ﾟ: *✧･ﾟ:* 　　 *:･ﾟ✧*:･ﾟ✧")
    force_adversaire = random.randint(1,6)
    print(f"Vous tombez face à face avec un adversaire de difficulté : {force_adversaire} ")
    print(f"vous avez combattus {nombre_denemie_combattus} enemies.")
    print("✧･ﾟ: *✧･ﾟ:* 　　 *:･ﾟ✧*:･ﾟ✧")
    choix_menu = str(input("Que voulez-vous faire? a: Combattre ce monstre, b: Fuire, c: Afficher les regles, d: Quitter "))

    if choix_menu == "c":
        print("༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶")
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  "
              "\nDans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire."
              "\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire."
              "\nDans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire."
              "\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0."
              "\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie."
              "\n༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶")
    
    elif choix_menu == "a":
        combattre = random.randint(1,6)
        print("Vous avez choisis de combattre l'enemie.")
        if combattre <= 4:
            niveau_vie = niveau_vie - force_adversaire
            nombre_denemie_combattus = nombre_denemie_combattus + 1
            nombre_defaite = nombre_defaite + 1
            numero_comba = numero_comba + 1
            print(f"vous avez combattus {numero_comba}, gagne {nombre_victoire} et perdu {nombre_defaite}")
            print("Defaite!")
        elif combattre >= 4:
            niveau_vie = niveau_vie + force_adversaire
            nombre_denemie_combattus = nombre_denemie_combattus + 1
            nombre_victoire = nombre_victoire + 1
            numero_comba = numero_comba + 1
            print(f"vous avez combattus {numero_comba}, gagne {nombre_victoire} et perdu {nombre_defaite}")
            print("victoire!")
    elif choix_menu == "b":
        niveau_vie = niveau_vie - 1
        print("Vous perdez 1 point de vie!")
    elif choix_menu == "d":
        print("Merci et au revoir...")
        niveau_vie = False