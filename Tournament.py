#open tournament creation app
import bracket

print("---Tournament Creation App---")
t_name = input("What is the tournament name?: ")
t = bracket.Tournament(t_name)

while True:
    print("1. Tournament bracket")
    print("2. Team")
    print("3. Terminate the App")

    while True:
        s = input("Select the options with number: ")
        try:
            x = int(s)
        except ValueError:
            print("Enter a natural number")
        else:
            break

    print()

    match x:
        case 1:
            while True:
                print("1. Create tournament bracket")
                print("2. Check the detail of tournament")
                print("3. Edit the results")
                print("4. Exit Tournament bracket menu")

                while True:
                    s = input("Select the options with number: ")
                    try:
                        y = int(s)
                    except ValueError:
                        print("Enter a natural number")
                    else:
                        break
                match y:
                    case 1:
                        print()
                        t.create_tournament()
                    case 2:
                        print()
                        t.display_tournament()
                    case 3:
                        print()
                        t.match_detail()
                    case 4:
                        break

        case 2:
            while True:
                print("1. Add new teams")
                print("2. Remove teams")
                print("3. Team details")
                print("4. Exit Team menu")
                while True:
                    s = input("Select the options with number: ")
                    try:
                        y = int(s)
                    except ValueError:
                        print("Enter a natural number")
                    else:
                        break

                match y:
                    case 1:
                        t.add_team()
                    case 2:
                        t.remove_team()
                    case 3:
                        t.team_detail()
                    case 4:
                        break

        case 3:
            break