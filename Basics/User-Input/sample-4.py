def adventure_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself at the entrance of a dark forest. Do you enter?")
    choice = input("Enter 'yes' to enter or 'no' to leave: ").lower()

    if choice == 'yes':
        print("You venture into the darkness of the forest.")
        print("After walking for hours, you come across a split path. Do you go 'left' or 'right'?")
        path = input("Choose 'left' or 'right': ").lower()

        if path == 'left':
            print("You take the left path and encounter a wild bear!")
            action = input("Do you 'run' back or 'climb' a tree? ").lower()
            if action == 'run':
                print("You managed to escape safely! However, you find yourself back at the forest entrance. The adventure ends here.")
            elif action == 'climb':
                print("You climbed a tree and waited until the bear left. You then find a hidden path leading out of the forest. You've made it out safely!")
            else:
                print("Invalid choice. Lost in confusion, you wander the forest until you find your way out. The adventure ends, but it could have been different.")

        elif path == 'right':
            print("You take the right path and find a treasure chest!")
            print("Do you open it? 'yes' or 'no'?")
            open_chest = input("Choose 'yes' or 'no': ").lower()
            if open_chest == 'yes':
                print("You found a treasure full of gold and jewels! You return home as a wealthy adventurer.")
            else:
                print("You decide not to open the chest. As you walk away, you wonder what could have been inside. The adventure ends, but the mystery remains.")
        else:
            print("Invalid choice. You wander aimlessly and eventually find your way back home. The adventure ends, but feels incomplete.")

    elif choice == 'no':
        print("You decide not to enter the forest. Perhaps another day you will find out what lies within. The adventure ends before it begins.")
    else:
        print("Invalid choice. Unable to decide, you find yourself returning home, pondering what might have been.")

adventure_game()
