# 2210356066 Zeynep Nisa Karataş
import sys
import string
words = string.ascii_uppercase[0:10]
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
with_letters = dict()
place_board = dict()
table_1 = {"C": "-", "B1": "-", "B2": "-", "D": "-", "S": "-", "P1": "-", "P2": "-", "P3": "-", "P4": "-"}
table_2 = {"C": "-", "B1": "-", "B2": "-", "D": "-", "S": "-", "P1": "-", "P2": "-", "P3": "-", "P4": "-"}


def create():
    global b_p1, b_p2  # these dictionaries will have only ships places
    b_p1 = dict()
    b_p2 = dict()
    with_letters["Player1"] = dict()  # this dictionary will have blanks and ships places together
    with_letters["Player2"] = dict()
    place_board["Player1"] = dict()  # this will only have '-' and change during the play
    place_board["Player2"] = dict()
    for word in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
        for number in range(1, 11):
            place_board["Player1"][word + str(number)] = "-"
            place_board["Player2"][word + str(number)] = "-"
    for word in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
        for number in range(1, 11):
            with_letters["Player1"][word + str(number)] = "-"
            with_letters["Player2"][word + str(number)] = "-"
    for lines in player_txt:  # this will add carrier, submarine and destroyer ships places into with_letters[Player1]
        player1 = (lines.strip()).split(";")
        for i in ["C", "S", "D"]:
            if i in player1:
                nindex = player1.index(i)
                for n in range(nindex, nindex + player1.count(i)):
                    if player_txt.count(lines) == 1:
                        with_letters["Player1"][words[n] + str(player_txt.index(lines) + 1)] = i
                    else:
                        with_letters["Player1"][words[n] + str(player_txt.index(lines) + 1)] = i
                        with_letters["Player1"][words[n] + str(player_txt.index(lines,
                                                                                player_txt.index(lines) + 1) + 1)] = i
    for lines in player2_txt:   # this will add carrier, submarine and destroyer ships places into with_letters[Player2]
        player2 = (lines.strip()).split(";")
        for i in ["C", "S", "D"]:
            if i in player2:
                nindex = player2.index(i)
                for n in range(nindex, nindex + player2.count(i)):
                    unknown = with_letters["Player2"][words[n] + str(player2_txt.index(lines) + 1)]
                    if player2_txt.count(lines) == 1 and unknown == "-":
                        with_letters["Player2"][words[n] + str(player2_txt.index(lines) + 1)] = i
                    elif player2_txt.count(lines) > 1 and unknown == "-":
                        with_letters["Player2"][words[n] + str(player2_txt.index(lines) + 1)] = i
                        unknow = with_letters["Player2"][words[n] + str(player2_txt.index(lines,
                                                                        player2_txt.index(lines) + 1) + 1)]
                        if unknow == "-":
                            with_letters["Player2"][words[n] + str(player2_txt.index(lines,
                                                                   player2_txt.index(lines) + 1) + 1)] = i
    key_1 = [key for key, value in with_letters["Player1"].items() if value in ("C", "S", "D")]
    key_2 = [key for key, value in with_letters["Player2"].items() if value in ("C", "S", "D")]
    value_1 = []
    value_2 = []
    for k in key_1:
        value_1.append(with_letters["Player1"].get(k))
    b_p1 = dict(zip(key_1, value_1))
    for k in key_2:
        value_2.append(with_letters["Player2"].get(k))
    b_p2 = dict(zip(key_2, value_2))
    for line in options_1:  # this will add battleship and patrol boat ships places into with_letters[Player1]
        line = (line.strip()).split(",")
        if line[1][2] == "r" and line[0][0] == "B":
            for i in range(words.index(line[1][0]), words.index(line[1][0]) + 4):
                b_p1[words[i] + str(line[0][3:])] = line[0][0:2]
                with_letters["Player1"][words[i] + str(line[0][3:])] = line[0][0]
        elif line[1][2] == "d" and line[0][0] == "B":
            for i in range(int(line[0][3:]), int(line[0][3:]) + 4):
                b_p1[line[1][0] + str(i)] = line[0][0:2]
                with_letters["Player1"][line[1][0] + str(i)] = line[0][0]
        elif line[1][2] == "r" and line[0][0] == "P":
            for i in range(words.index(line[1][0]), words.index(line[1][0]) + 2):
                b_p1[words[i] + str(line[0][3:])] = line[0][0:2]
                with_letters["Player1"][words[i] + str(line[0][3:])] = line[0][0]
        elif line[1][2] == "d" and line[0][0] == "P":
            for i in range(int(line[0][3:]), int(line[0][3:]) + 2):
                b_p1[line[1][0] + str(i)] = line[0][0:2]
                with_letters["Player1"][line[1][0] + str(i)] = line[0][0]
    for line in options_2:  # this will add battleship and patrol boat ships places into with_letters[Player2]
        line = (line.strip()).split(",")
        if line[1][2] == "r" and line[0][0] == "B":
            for i in range(words.index(line[1][0]), words.index(line[1][0]) + 4):
                b_p2[words[i] + str(line[0][3:])] = line[0][0:2]
                with_letters["Player2"][words[i] + str(line[0][3:])] = line[0][0]
        elif line[1][2] == "d" and line[0][0] == "B":
            for i in range(int(line[0][3:]), int(line[0][3:]) + 4):
                b_p2[line[1][0] + str(i)] = line[0][0:2]
                with_letters["Player2"][line[1][0] + str(i)] = line[0][0]
        elif line[1][2] == "r" and line[0][0] == "P":
            for i in range(words.index(line[1][0]), words.index(line[1][0]) + 2):
                b_p2[words[i] + str(line[0][3:])] = line[0][0:2]
                with_letters["Player2"][words[i] + str(line[0][3:])] = line[0][0]
        elif line[1][2] == "d" and line[0][0] == "P":
            for i in range(int(line[0][3:]), int(line[0][3:]) + 2):
                b_p2[line[1][0] + str(i)] = line[0][0:2]
                with_letters["Player2"][line[1][0] + str(i)] = line[0][0]


def outputs(x):
    print(x)
    output_f.write(x)


def tables():  # this function will call outputs function for printing all the tables into output file
    table_str = ""
    table_str += "Player1's Hidden Board\t\tPlayer2's Hidden Board\n  A B C D E F G H I J\t\t  A B C D E F G H I J\n"
    plist = [table_1['P1'], table_1['P2'], table_1['P3'], table_1['P4']]
    plist_2 = [table_2['P1'], table_2['P2'], table_2['P3'], table_2['P4']]
    blist = [table_1['B1'], table_1['B2']]
    blist_2 = [table_2['B1'], table_2['B2']]
    for i in plist, plist_2, blist, blist_2:
        i.sort()
        i.reverse()
    for i in numbers:
        if i < 10:
            table_str += "{} ".format(i)
            for j in range(len(words)):
                table_str += "{} ".format(place_board["Player1"][words[j] + str(i)])
            table_str += "\t\t{}".format(i)
            for w in range(len(words)):
                table_str += "{} ".format(place_board["Player2"][words[w] + str(i)])
            table_str += "\n"
        else:
            table_str += "{}".format(i)
            for m in range(len(words)):
                table_str += "{} ".format(place_board["Player1"][words[m] + str(i)])
            table_str += "\t\t{}".format(i)
            for n in range(len(words)):
                table_str += "{} ".format(place_board["Player2"][words[n] + str(i)])
            table_str += "\n\n"
    table_str += "Carrier \t{}\t\tCarrier \t{}\nBattleship\t{}{}\t\tBattleship\t{}{}\nDestroyer\t{}\t\tDestroyer" \
    "\t{}\n".format(table_1['C'], table_2['C'], blist[0], blist[1], blist_2[0], blist_2[1], table_1['D'], table_2['D'])
    table_str += "Submarine\t{}\t\tSubmarine\t{}\nPatrol Boat\t{}{}{}{}\t\tPatrol Boat\t{}{}{}{}\n\n".format\
    (table_1['S'], table_2['S'], plist[0], plist[1], plist[2], plist[3], plist_2[0], plist_2[1], plist_2[2], plist_2[3])
    outputs(table_str)


def battleship_2(x):
    output_f.write("Player2's Move\n\nRound: {}\t\t\t\t\tGrid Size: 10x10\n\n".format(str(two_in_list.index(x) + 1)))
    print("Player2's Move\n\nRound: {}\t\t\t\t\tGrid Size: 10x10\n\n".format(str(two_in_list.index(x) + 1)))
    tables()
    output_f.write("Enter your move:{}\n\n".format(x[0] + "," + x[1]))
    print("Enter your move:{}\n".format(x[0] + "," + x[1]))
    if with_letters["Player1"][x[1] + str(x[0])] != "-":
        place_board["Player1"][x[1] + str(x[0])] = "X"  # this will change "-" to "X" if the place is full
        b_p1[x[1] + str(x[0])] = "X"
    else:
        place_board["Player1"][x[1] + str(x[0])] = "O"  # this will change "-" to "O" if the place is NOT full
    for i in ["C", "B1", "B2", "D", "S", "P1", "P2", "P3", "P4"]:
        if i not in b_p1.values():
            table_1[i] = "X"
    global set_1, list_1
    set_1 = set(table_1.values())
    list_1 = list(set_1)


def battleship_1(x):
    output_f.write("Player1's Move\n\nRound: {}\t\t\t\t\tGrid Size: 10x10\n\n".format(str((one_in_list.index(x)) + 1)))
    print("Player1's Move\n\nRound: {}\t\t\t\t\tGrid Size: 10x10\n".format(str((one_in_list.index(x)) + 1)))
    tables()
    output_f.write("Enter your move:{}\n\n".format(x[0] + "," + x[1]))
    print("Enter your move:{}\n".format(x[0] + "," + x[1]))
    if with_letters["Player2"][x[1] + str(x[0])] != "-":
        place_board["Player2"][x[1] + str(x[0])] = "X"  # this will change "-" to "X" if the place is full
        b_p2[x[1] + str(x[0])] = "X"
    else:
        place_board["Player2"][x[1] + str(x[0])] = "O"  # this will change "-" to "O" if the place is NOT full
    for i in ["C", "B1", "B2", "D", "S", "P1", "P2", "P3", "P4"]:
        if i not in b_p2.values():
            table_2[i] = "X"
    global set_2, list_2
    set_2 = set(table_2.values())
    list_2 = list(set_2)
    if len(list_2) == 1 and list_2[0] == "X":
        finde = one_in_list.index(x)
        battleship_2(two_in_list[finde])


def errors():
    number = [int(i) for i in range(0, 400)]
    alphabet = string.ascii_uppercase
    same_ones = []
    outputs("Battle of Ships Game\n\n")
    for j in range(len(all_in_list)):
        for i in range(len(all_in_list[j])):  # this two loop will take moves one by one
            try:  # if there is any type of error it will print the error and keep moving for following move
                places = all_in_list[j][i]
                if len(places) < 2 or places[0] == '' or places[1] == '':
                    raise IndexError
                elif len(places) > 2 or int(places[0]) not in number or places[1] not in alphabet:
                    raise ValueError
                elif len(places) == 2:
                    assert 0 < int(places[0]) < 11 and places[1] in alphabet[0:10]
                    if all_in_list[j].count(places) == 2:  # if both of the players made the same move at the same time
                        same_ones.append(places)
                        if len(same_ones) % 2 == 1:  # if it is Player1 move it will call battleship_1
                            battleship_1(places)
                        elif len(same_ones) % 2 == 0:  # if it is Player2 move it will call battleship_1
                            battleship_2(places)
                            if len(list_2) == 1 and list_2[0] == "X" and len(list_1) == 1 and list_1[0] == "X":
                                outputs("It is a Draw!\n\nFinal Information\n\n")
                                tables()
                                break
                            elif len(list_1) == 1 and list_1[0] == "X":
                                outputs("Player2wins\n\nFinal Information\n\n")
                                tables()
                                break
                            elif len(list_2) == 1 and list_2[0] == "X":
                                outputs("Player1 Wins\n\nFinal Information\n\n")
                                tables()
                                break
                    else:
                        if places == all_in_list[j][0]:  # if it is Player1 move it will call battleship_1
                            battleship_1(places)
                        elif places == all_in_list[j][1]:  # if it is Player2 move it will call battleship_2
                            battleship_2(places)
                            if len(list_2) == 1 and list_2[0] == "X" and len(list_1) == 1 and list_1[0] == "X":
                                outputs("It is a Draw!\n\nFinal Information\n\n")
                                tables()
                                break
                            elif len(list_1) == 1 and list_1[0] == "X":
                                outputs("Player2 Wins!\n\nFinal Information\n\n")
                                tables()
                                break
                            elif len(list_2) == 1 and list_2[0] == "X":
                                outputs("Player1 Wins!\n\nFinal Information\n\n")
                                tables()
                                break
            except IndexError:
                outputs("IndexError:The place you entered is not exist.\n")
            except ValueError:
                outputs("ValueError:The place you entered is not valid\n")
            except AssertionError:
                outputs("AssertionError: Invalid Operation\n")
            except Exception:
                pass


optional_1 = open("OptionalPlayer1.txt", "r")
optional_2 = open("OptionalPlayer2.txt", "r")
output_f = open("Battleship.out", "w")
output_f.close()
output_f = open("Battleship.out", "a")
options_1 = optional_1.readlines()
options_2 = optional_2.readlines()
try:  # if there are less than 4 files it will print IndexError
    f = sys.argv[1]
    f2 = sys.argv[2]
    f1_in = sys.argv[3]
    f2_in = sys.argv[4]
    try:
        # if there is a wrong input file is written in terminal, this will consider all the combinations of wrong input
        # file names and will print the wrong files with their names
        file = open(f, "r")
        try:
            file2 = open(f2, "r")
            try:
                file1_in = open(f1_in, "r")
                try:
                    file2_in = open(f2_in, "r")
                except FileNotFoundError:
                    outputs("IOError: input file {} is not reachable.".format(f2_in))
            except FileNotFoundError:
                try:
                    file2_in = open(f2_in, "r")
                    outputs("IOError: input files {} are not reachable".format(f1_in))
                except FileNotFoundError:
                    outputs("IOError: input files {} {} are not reachable".format(f1_in, f2_in))
        except FileNotFoundError:
            try:
                file1_in = open(f1_in, "r")
                try:
                    file2_in = open(f2_in, "r")
                    outputs("IOError: input file {} is not reachable".format(f2))
                except FileNotFoundError:
                    outputs("IOError: input files {} {} are not reachable".format(f2, f2_in))
            except FileNotFoundError:
                try:
                    file2_in = open(f2_in, "r")
                    outputs("IOError: input files {} {} are not reachable".format(f2, f1_in))
                except FileNotFoundError:
                    outputs("IOError: input files {} {} {} are not reachable".format(f2, f1_in, f2_in))
    except FileNotFoundError:
        try:
            file2 = open(f2, "r")
            try:
                file1_in = open(f1_in, "r")
                try:
                    file2_in = open(f2_in, "r")
                    outputs("IOError: input file {} is not reachable.".format(f))
                except FileNotFoundError:
                    outputs("IOError: input files {} {} are not reachable.".format(f, f2_in))
            except FileNotFoundError:
                try:
                    file2_in = open(f2_in, "r")
                    outputs("IOError: input files {} {} are not reachable.".format(f, f1_in))
                except FileNotFoundError:
                    outputs("IOError: input files {} {} {} are not reachable.".format(f, f1_in, f2_in))
        except FileNotFoundError:
            try:
                file1_in = open(f1_in, "r")
                try:
                    file2_in = open(f2_in, "r")
                    outputs("IOError: input files {} {} are not reachable.".format(f, f2))
                except FileNotFoundError:
                    outputs("IOError: input files {} {} {} are not reachable.".format(f, f2, f2_in))
            except FileNotFoundError:
                try:
                    file2_in = open(f2_in, "r")
                    outputs("IOError: input files {} {} {}are not reachable.".format(f, f2, f1_in))
                except FileNotFoundError:
                    outputs("IOError: input files {} {} {} {} are not reachable.".format(f, f2, f1_in, f2_in))
except IndexError:
    outputs("IndexError: number of inputs less than expected")
except Exception:
    outputs("kaBOOM: run for your life.")
else:
    try:
        player_txt = file.readlines()
        player2_txt = file2.readlines()
        player1_in = file1_in.readlines()
        player2_in = file2_in.readlines()
        one_list = (player1_in[0].strip()).split(";")
        two_list = (player2_in[0].strip()).split(";")
        one_in_list = [one_list[i].split(",") for i in range(len(one_list) - 1)]
        two_in_list = [two_list[i].split(",") for i in range(len(two_list) - 1)]
        all_in_list = list(zip(one_in_list, two_in_list))
        create()
        errors()
    except NameError:
        pass
    except Exception:
        outputs("kaBOOM: run for your life.")
