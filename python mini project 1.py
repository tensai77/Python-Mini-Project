def start_game():
    print("\nWelcome to *The Samurai's Legacy*!")
    print("You are Hiro, a young samurai tasked with reclaiming your family's honor.")
    print("Every decision you make will shape your story. Choose wisely.\n")
    chapter_one()

def chapter_one():
    print("\n--- Chapter 1: The Forest of Shadows ---")
    print("You are traveling through the Forest of Shadows, seeking the lost relic of your clan.")
    print("Suddenly, you hear a cry for help. Do you:")
    print("1. Investigate the sound.")
    print("2. Ignore it and continue on your mission.")
    print("3. Prepare an ambush, suspecting a trap.")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        investigate_cry()
    elif choice == "2":
        skip_rescue()
    elif choice == "3":
        ambush_prep()
    else:
        print("Invalid choice. Please choose again.\n")
        chapter_one()

def investigate_cry():
    print("\nYou rush towards the sound and find a wounded traveler surrounded by wolves.")
    print("Do you:")
    print("1. Fight the wolves to save the traveler.")
    print("2. Help from a distance using your bow.")
    print("3. Leave quietly; your mission takes priority.")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        print("\nYou defeat the wolves, earning the traveler's gratitude. He reveals he is a monk and gives you a protective talisman.")
        print("This talisman may help you later.")
        chapter_two()
    elif choice == "2":
        print("\nYou help from a distance, but the traveler dies. Searching his belongings, you find a map of the region.")
        print("The map could guide you to hidden paths.")
        chapter_two()
    elif choice == "3":
        print("\nYou ignore the scene and move on, feeling a pang of guilt.")
        print("Your journey continues, but you sense unseen consequences.")
        chapter_two()
    else:
        print("Invalid choice. Please choose again.\n")
        investigate_cry()

def skip_rescue():
    print("\nYou press on, ignoring the cry for help.")
    print("As you walk further, you are ambushed by bandits.")
    print("Do you:")
    print("1. Fight them head-on.")
    print("2. Try to escape.")
    print("3. Negotiate for safe passage.")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        print("\nYou fight bravely but are injured. You manage to survive but at a great cost to your strength.")
        chapter_two()
    elif choice == "2":
        print("\nYou narrowly escape, leaving behind your provisions. The journey ahead becomes harder.")
        chapter_two()
    elif choice == "3":
        print("\nYou convince the bandits to let you go by offering your coin pouch.")
        print("You are spared but left without money.")
        chapter_two()
    else:
        print("Invalid choice. Please choose again.\n")
        skip_rescue()

def ambush_prep():
    print("\nYou set up an ambush and discover the cry was a trick by bandits.")
    print("Thanks to your preparation, you easily defeat them.")
    print("Among their loot, you find a strange key marked with an ancient symbol.")
    chapter_two()

def chapter_two():
    print("\n--- Chapter 2: The Forgotten Shrine ---")
    print("Following the path, you arrive at a forgotten shrine said to hold your clan's relic.")
    print("The shrine is guarded by a ronin who challenges you to prove your worth.")
    print("Do you:")
    print("1. Accept his challenge to a duel.")
    print("2. Attempt to outsmart him with words.")
    print("3. Offer the key or talisman (if you have one).")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        print("\nThe duel is fierce, but your training prevails. The ronin allows you to enter the shrine.")
        shrine_outcome("duel")
    elif choice == "2":
        print("\nYou convince the ronin that your mission is righteous. He steps aside.")
        shrine_outcome("persuasion")
    elif choice == "3":
        special_item_path()
    else:
        print("Invalid choice. Please choose again.\n")
        chapter_two()

def special_item_path():
    print("\nYou present the talisman or key.")
    print("The ronin recognizes its significance and bows to you, granting access to the shrine.")
    print("Inside, you find the relic and an ancient scroll.")
    win_game("special")

def shrine_outcome(method):
    if method == "duel":
        print("\nInside the shrine, you find the relic of your clan.")
        print("However, your wounds from the duel weigh heavily.")
        win_game("standard")
    elif method == "persuasion":
        print("\nInside the shrine, you find the relic along with additional treasures.")
        win_game("standard")

def win_game(path):
    if path == "special":
        print("\nCongratulations! You have reclaimed your clan's relic and uncovered ancient knowledge.")
        print("Your journey is a story of wisdom and valor, told for generations to come.")
    else:
        print("\nCongratulations! You have reclaimed the relic, restoring honor to your clan.")
        print("Your bravery will be remembered forever.")
    play_again()

def play_again():
    choice = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if choice == "yes":
        start_game()
    elif choice == "no":
        print("\nThank you for playing *The Samurai's Legacy*. Farewell, brave warrior!")
    else:
        print("Invalid choice. Please choose again.")
        play_again()

# Start the game
start_game()
