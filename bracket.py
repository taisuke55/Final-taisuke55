import random
import time
from os import remove


class Match:
    def __init__(self, match_layer, match_num):
        self.type = "Match"
        self.match_layer = match_layer
        self.match_num = match_num
        self.team_one = None
        self.team_one_score = None
        self.team_two = None
        self.team_two_score = None

class Team:
    def __init__(self, team_name):
        self.type = "Team"
        self.team_name = team_name
        self.players = []
        self.next = None

class Tournament:
    def __init__(self, name):
        self.name = name
        self.tournament_head = None
        self.team_head = None

    def create_tournament(self):
        team_list = self.team_list()
        size = len(team_list)
        while size < 2:
            print("You need at least 2 teams in the tournament.")
            self.add_team()

            team_list = self.team_list()
            size = len(team_list)

        while True:
            for team in team_list:
                print(f"-{team}")
            print(f"{size} teams join to the tournament.")
            print("Do you neet to add more team to the team list?")
            answer = input("Enter y/n: ")
            while True:
                if answer == "y" or answer == "n":
                    break
                else:
                    answer = input("Enter y/n: ")
            if answer == "y":
                self.add_team()
            elif answer == "n":
                break

            team_list = self.team_list()
            size = len(team_list)
            print()

        print("Do you want to make a tournament now?")
        answer = input("Enter y/n: ")
        while True:
            if answer == "y" or answer == "n":
                break
            else:
                answer = input("Enter y/n: ")
        if answer == "y":
            random.shuffle(team_list)

            self.tournament_head = Match(1, 1)
            self.create_tournament_recursive(self.tournament_head, team_list)

            time.sleep(0.25)
            print(f"Created {self.name} tournament\n")

        time.sleep(0.25)


    def create_tournament_recursive(self, current_match, team_list):

        if len(team_list) >= 4:

            current_match.team_one = Match(current_match.match_layer + 1, current_match.match_num * 2)
            current_match.team_two = Match(current_match.match_layer + 1, current_match.match_num * 2 + 1)

            num = int(len(team_list) / 2)

            team_list_one = team_list[0:num]
            team_list_two = team_list[num:len(team_list)]

            self.create_tournament_recursive(current_match.team_one, team_list_one)
            self.create_tournament_recursive(current_match.team_two, team_list_two)
        elif len(team_list) == 3:
            current_match.team_one = self.team_finder(team_list[0])
            current_match.team_two = Match(current_match.match_layer + 1, current_match.match_num * 2 + 1)

            self.create_tournament_recursive(current_match.team_two, team_list[1:3])
        else:
            current_match.team_one = self.team_finder(team_list[0])
            current_match.team_two = self.team_finder(team_list[1])

    def add_team(self):
        while True:
            while True:
                team_name = input("What is the team name?: ")
                print(f'Are you sure to add "{team_name}" to the team list?')
                answer = input("Enter y/n: ")
                while True:
                    if answer == "y" or answer == "n":
                        break
                    else:
                        answer = input("Enter y/n: ")
                if answer == "y":
                    break

            new_team = Team(team_name)

            if self.team_head is None:
                self.team_head = new_team
            else:
                self.add_team_recursive(self.team_head, new_team)

            time.sleep(0.25)
            print("Team addition is completed.\n")
            time.sleep(0.25)

            print("Do you neet to add more team to the team list?")
            answer = input("Enter y/n: ")
            while True:
                if answer == "y" or answer == "n":
                    break
                else:
                    answer = input("Enter y/n: ")
            if answer == "n":
                break

            print()

    def add_team_recursive(self, current_team, new_team):
        if current_team.next is None:
            current_team.next = new_team
        else:
            self.add_team_recursive(current_team.next, new_team)

    def remove_team(self):
        while True:
            if self.team_head is None:
                print("There is no team in the tournament.\n")
            else:
                team_lists = self.team_list()
                i = 0
                for l in team_lists:
                    print(f"{i + 1}. {l}")
                    i += 1

                print("Which team do you want to remove?")
                while True:
                    s = input("Select the options with number: ")
                    try:
                        y = int(s) - 1
                    except ValueError:
                        print("Enter a natural number")
                    else:
                        break

                self.team_head = self.remove_team_recursive(self.team_head, team_lists[y])

                time.sleep(0.25)
                print(f'Team "{team_lists[y]}"" removal is completed.\n')
                time.sleep(0.25)

                print("Do you neet to remove more team to the team list?")
                answer = input("Enter y/n: ")
                while True:
                    if answer == "y" or answer == "n":
                        break
                    else:
                        answer = input("Enter y/n: ")
                if answer == "n":
                    break

                print()


    def remove_team_recursive(self, current_team, value):
        if current_team is None:
            return None
        if current_team.team_name == value:
            return current_team.next
        current_team.next = self.remove_team_recursive(current_team.next, value)
        return current_team

    def display_tournament(self):
        print(f"-{self.name}-")
        if self.team_head is None:
            pass
        else:
            match_num, match_team, match_score = self.display_tournament_recursive(self.tournament_head, 2)
            print(f"{' ' * 5}Match {match_num}")
            if match_score[0] is None:
                print(f"{' ' * 5}-{match_team[0]:<20}")
                print(f"{' ' * 5}-{match_team[1]:<20}")
                print("Champion")
                print(f"-Match {match_num} winner")
            else:
                print(f"{' ' * 5}-{match_team[0]:<20} {match_score[0]}")
                print(f"{' ' * 5}-{match_team[1]:<20} {match_score[1]}")
                print("Champion")
                if match_score[0] < match_score[1]:
                    print(f"-{match_team[1]}")
                else:
                    print(f"-{match_team[0]}")

            print()
            while True:
                print("1. Edit the results")
                print("2. Exit")

                while True:
                    s = input("Select the options with number: ")
                    try:
                        x = int(s)
                    except ValueError:
                        print("Enter a natural number.")
                    else:
                        break

                match x:
                    case 1:
                        self.match_detail()
                        break

                    case 2:
                        break
            print()

    def display_tournament_recursive(self, current_match, i):
        if current_match.type == "Team":
            return None, [current_match.team_name], []
        elif current_match.type == "Match":
            match_num_1, match_team_1, match_score_1 = self.display_tournament_recursive(current_match.team_one, i + 1)
            if match_num_1 is None:
                team_name = [match_team_1[0]]
            else:
                print(f"{' ' * 5 * i}Match {match_num_1}")

                if match_score_1[0] is None:
                    print(f"{' ' * 5 * i}-{match_team_1[0]:<20}")
                    print(f"{' ' * 5 * i}-{match_team_1[1]:<20}")
                    n = f"Match {match_num_1} winner"
                    team_name = [n]
                else:
                    print(f"{' ' * 5 * i}-{match_team_1[0]:<20} {match_score_1[0]}")
                    print(f"{' ' * 5 * i}-{match_team_1[1]:<20} {match_score_1[1]}")
                    if match_score_1[0] < match_score_1[1]:
                        team_name = [match_team_1[1]]
                    else:
                        team_name = [match_team_1[0]]

            match_num_2, match_team_2, match_score_2 = self.display_tournament_recursive(current_match.team_two, i + 1)
            if match_num_2 is None:
                team_name.append(match_team_2[0])
            else:
                print(f"{' ' * 5 * i}Match {match_num_2}")
                if match_score_2[0] is None:
                    print(f"{' ' * 5 * i}-{match_team_2[0]:<20}")
                    print(f"{' ' * 5 * i}-{match_team_2[1]:<20}")
                    n = f"Match {match_num_2} winner"
                    team_name.append(n)
                else:
                    print(f"{' ' * 5 * i}-{match_team_2[0]:<20} {match_score_2[0]}")
                    print(f"{' ' * 5 * i}-{match_team_2[1]:<20} {match_score_2[1]}")
                    if match_score_2[0] < match_score_2[1]:
                        team_name.append(match_team_2[1])
                    else:
                        team_name.append(match_team_2[0])

            match_score = [current_match.team_one_score,current_match.team_two_score]

            return current_match.match_num, team_name, match_score

    def match_detail(self):
        while True:
            while True:
                s = input("Which match do you want to edit?: Match ")
                try:
                    match_num = int(s)
                except ValueError:
                    print("Enter a natural number.")
                else:
                    break
            j = match_num
            remain = []
            while j > 1:
                remain.insert(0, j % 2)
                j = int(j / 2)

            self.match_detail_recursive(self.tournament_head, 0, match_num, remain)

            print("Do you continue to edit match details?")
            answer = input("Enter y/n: ")
            while True:
                if answer == "y" or answer == "n":
                    break
                else:
                    answer = input("Enter y/n: ")
            if answer == "n":
                break

    def match_detail_recursive(self, current_match, i, match_num, remain):
        if current_match.match_num == match_num:
            team_one = self.recall_team(current_match.team_one)
            team_two = self.recall_team(current_match.team_two)
            if team_one is None:
                if team_two is None:
                    print(f"Enter the detail Match {match_num * 2} and Match {match_num * 2 + 1} first.")
                else:
                    print(f"Enter the detail Match {match_num * 2} first.")
            elif team_two is None:
                print(f"Enter the detail Match {match_num * 2 + 1} first.")
            else:
                if current_match.team_one_score is None:
                    self.enter_detail(current_match, team_one, team_two)
                else:
                    print("There is already the entered score.")
                    print("Do you want to rewrite the score?")
                    answer = input("Enter y/n: ")
                    while True:
                        if answer == "y" or answer == "n":
                            break
                        else:
                            answer = input("Enter y/n: ")
                    if answer == "y":
                        self.enter_detail(current_match, team_one, team_two)
        else:
            if remain[i] == 0:
                self.match_detail_recursive(current_match.team_one, i + 1, match_num, remain)
            else:
                self.match_detail_recursive(current_match.team_two, i + 1, match_num, remain)

    def enter_detail(self, current_match, team_one, team_two):
        while True:
            s = input(f"Enter the score of {team_one}: ")
            try:
                current_match.team_one_score = int(s)
            except ValueError:
                print("Enter a natural number.")
            else:
                break
        while True:
            s = input(f"Enter the score of {team_two}: ")
            try:
                current_match.team_two_score = int(s)
            except ValueError:
                print("Enter a natural number.")
            else:
                break

        print("Complete editing the match.")

    def team_list(self):
        return self.team_list_recursive(self.team_head)

    def team_list_recursive(self, current_node):
        if current_node is None:
            return []
        return [current_node.team_name] + self.team_list_recursive(current_node.next)

    def recall_team(self,current_match):
        if current_match.type == "Team":
            return current_match.team_name
        elif current_match.type == "Match":
            if current_match.team_one_score is None:
                return None
            elif current_match.team_two_score < current_match.team_one_score:
                return self.recall_team(current_match.team_one)
            else:
                return self.recall_team(current_match.team_two)

    def team_finder(self,value):
        if self.team_head is None:
            return None
        else:
            return self.team_finder_recursive(self.team_head, value)

    def team_finder_recursive(self,current_team, value):
        if current_team.team_name == value:
            return current_team
        else:
            return self.team_finder_recursive(current_team.next, value)

    def team_detail(self):
        print("Team lists")
        team_lists = self.team_list()
        i = 0
        for l in team_lists:
            print(f"{i + 1}. {l}")
            i += 1

        print(f"{i + 1}. Exit")

        print("Which team do you want to check the detail?")
        while True:
            s = input("Select the options with number: ")
            try:
                y = int(s) - 1
            except ValueError:
                print("Enter a natural number")
            else:
                break
        if y == i:
            pass
        else:
            self.team_detail_recursive(self.team_head, team_lists[y])


    def team_detail_recursive(self, current_team, value):
        if current_team is None:
            return None
        if current_team.team_name == value:
            while True:
                print(f"{current_team.team_name}")
                print("-Players")
                i = 0
                players = current_team.players
                for l in players:
                    print(f"-{i + 1}. {l}")
                print()

                print("1. Change the team name")
                print("2. Add new players")
                print("3. Remove players")
                print("4. Exit")
                s = input("Select the options with number: ")
                try:
                    x = int(s)
                except ValueError:
                    print("Enter a natural number")
                else:
                    break

                match x:
                    case 1:
                        team_name = input('Enter new team name: ')
                        while True:
                            print(f'Are you sure to change "{current_team.team_name}" to "{team_name}"?')
                            answer = input("Enter y/n: ")
                            while True:
                                if answer == "y" or answer == "n":
                                    break
                                else:
                                    answer = input("Enter y/n: ")
                            if answer == "y":
                                break

                        current_team.team_name = team_name

                        time.sleep(0.25)
                        print(f'Team name changing is completed.\n')
                        time.sleep(0.25)

                        break

                    case 2:
                        print('Enter new players -if you want to add malti-players, divide with","')
                        while True:
                            new_players = input("Players names: ").split(",")
                            print(f'Are you sure to add players below?')
                            for p in new_players:
                                print(f"-{p}")
                            print()
                            answer = input("Enter y/n: ")
                            while True:
                                if answer == "y" or answer == "n":
                                    break
                                else:
                                    answer = input("Enter y/n: ")
                            if answer == "y":
                                break
                        current_team.players = players + new_players

                        break

                    case 3:
                        j = 0
                        print('Which players do you want to remove?')
                        for p in players:
                            print(f"{j + 1}. {p}")
                        print(f"{j}.Exit")
                        while True:
                            s = input("Select the options with number: ")
                            try:
                                y = int(s) - 1
                            except ValueError:
                                print("Enter a natural number")
                            else:
                                break
                        if y == j:
                            pass
                        else:
                            new_players = players
                            new_players.remove(players[y])
                            current_team.players = new_players

                            time.sleep(0.25)
                            print(f'"{players[y]}"" removal is completed.\n')
                            time.sleep(0.25)

                        break

                    case 4:
                        break

        else:
            self.team_detail_recursive(current_team.next, value)