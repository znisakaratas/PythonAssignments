import string
import sys
seatdict = dict()  # it contains category name, seats, and their situation whether they are filled or not
key1 = dict()  # this dictionary is in seatdict dictionary it helds seats and their situation
category_row = dict()  # it has category names and their rows
category_column = dict()  # it has category names and their columns


def create():
    seat_input = line[15:-1].split(" ")
    if seat_input[0] not in seatdict:
        words = string.ascii_uppercase[0:int(seat_input[1][0:2])]
        numbers = [str(j) for j in range(0, int(seat_input[1][3:]))]
        category_row[seat_input[0]] = seat_input[1][0:2]
        category_column[seat_input[0]] = seat_input[1][3:]
        seatdict[seat_input[0]] = dict()
        for i in range(len(words)):  # these loop will create a nested dictionary which helds category name,seats and X
            for j in range(len(numbers)):
                key1 = words[i] + str(numbers[j])
                seatdict[seat_input[0]][key1] = "X"
        potential = int(seat_input[1][0:2]) * int(seat_input[1][3:])
        if int(seat_input[1][0:2]) <= 26:
            print("The category '{}' having {} seats has been created\n".
                  format(seat_input[0], potential), end='')
            return output_f.write("The category '{}' having {} seats has been created\n".
                                  format(seat_input[0], potential))
        else:
            pass
    elif seat_input[0] in seatdict:
        print("Warning: Cannot create the category for the second time. The stadium has already {}\n".format
              (seat_input[0]), end='')
        return output_f.write("Warning: Cannot create the category for the second time. The stadium has already {}\n"
                              .format(seat_input[0]))


def sell():
    sell_input = line[11:-1].split(" ")
    seats = sell_input[3:]  # it has every seats from each line
    words = string.ascii_uppercase[0:int(category_row[sell_input[2]])]
    if sell_input[2] not in seatdict:
        print("The seats are not available due to absence of {}\n".format(sell_input[2]), end='')
        output_f.write("The seats are not available due to absence of {}\n".format(sell_input[2]))
    else:
        for i in range(len(seats)):
            if len(seats[i]) < 4:  # this will sell only one seat
                if seatdict[sell_input[2]][seats[i]] == "X":  # if it is not sold it will continue selling
                    if int(seats[i][1:]) <= int(category_column[sell_input[2]]) and seats[i][0] in words:
                        if str(sell_input[1][0:2]) == "se":
                            seatdict[sell_input[2]][seats[i]] = "T"  # this is for season tickets
                        elif str(sell_input[1][0:2]) == "st":
                            seatdict[sell_input[2]][seats[i]] = "S"  # this is for students
                        else:
                            seatdict[sell_input[2]][seats[i]] = "F"  # this is for full seat
                        print("Success:{} has bought {} at {}\n".format(sell_input[0], seats[i],
                                                                        sell_input[2]), end='')
                        output_f.write("Success:{} has bought {} at {}\n".format(sell_input[0], seats[i],
                                                                                 sell_input[2]))
                    elif int(seats[i][1:]) <= int(category_column[sell_input[2]]) and seats[i][0] not in words:
                        print("Warning:The category {} has less row than the specified index {}\n".
                              format(sell_input[2], seats[i]), end='')
                        output_f.write("Warning:The category {} has less row than the specified index {}\n".
                                       format(sell_input[2], seats[i]))
                    elif int(seats[i][1:]) > int(category_column[sell_input[2]]) and seats[i][0] in words:
                        print("Warning:The category {} has less column than the specified index {}\n".
                              format(sell_input[2], seats[i]), end='')
                        output_f.write("Warning:The category {} has less column than the specified index {}\n".
                                       format(sell_input[2], seats[i]))
                    else:
                        print("Warning:The category {} has less column and row than the specified "
                              "index {}\n".format(sell_input[2], seats[i]), end='')
                        output_f.write("Warning:The category {} has less column and row than the specified "
                                       "index {}\n".format(sell_input[2], seats[i]))
                else:
                    print("Warning:The seat {} cannot be sold to {} since it was already sold\n".format
                          (seats[i], sell_input[0]), end='')
                    output_f.write("Warning:The seat {} cannot be sold to {} since it was already sold\n".format
                                   (seats[i], sell_input[0]))
            else:
                seatrange = seats[i].split("-")  # this will help us getting the range of seats
                if int(seatrange[1]) > int(category_column[sell_input[2]]) and seats[i][0] in words:
                    print("Warning:The category {} has less column than the specified index {}\n".format
                          (sell_input[2], seats[i]), end='')
                    output_f.write("Warning:The category {} has less column than the specified index {}\n".format
                                   (sell_input[2], seats[i]))
                elif int(seatrange[1]) <= int(category_column[sell_input[2]]) and seats[i][0] not in words:
                    print("Warning:The category {} has less row than the specified index {}\n".format
                          (sell_input[2], seats[i]), end='')
                    output_f.write("Warning:The category {} has less row than the specified index {}\n".format
                                   (sell_input[2], seats[i]))
                elif int(seatrange[1]) > int(category_column[sell_input[2]]) and seats[i][0] not in words:
                    print("Warning:The category {} has less row and column than the specified index {}\n".format
                          (sell_input[2], seats[i]), end='')
                    output_f.write("Warning:The category {} has less row and column than the specified index {}\n"
                                   .format(sell_input[2], seats[i]))
                elif seatdict[sell_input[2]][seats[i][0] + str(seatrange[0][1:])] != "X":
                    print("Warning:The seats {} cannot be sold due to some of them have already been sold\n".format
                          (seats[i]), end='')
                    output_f.write("Warning:The seats {} cannot be sold due to some of them have already been "
                                   "sold\n".format(seats[i]))
                elif seatdict[sell_input[2]][seats[i][0] + str(seatrange[0][1:])] == "X":
                    for j in range(int(seatrange[0][1:]), int(seatrange[1]) + 1):
                        if str(sell_input[1][0:2]) == "se":
                            seatdict[sell_input[2]][seats[i][0] + str(j)] = "T"
                        elif str(sell_input[1][0:2]) == "st":
                            seatdict[sell_input[2]][seats[i][0] + str(j)] = "S"
                        else:
                            seatdict[sell_input[2]][seats[i][0] + str(j)] = "F"
                    print("Success:{} has bought {} at {}\n".format(sell_input[0], seats[i], sell_input[2]), end='')
                    output_f.write("Success:{} has bought {} at {}\n".format(sell_input[0], seats[i], sell_input[2]))


def cancel():
    cancel_input = line[13:-1].split(" ")
    seats = cancel_input[1:]
    words = string.ascii_uppercase[0:int(category_row[cancel_input[0]])]
    for i in range(len(seats)):
        if cancel_input[0] not in seatdict:  # if category is not in the stadium it will put warning
            print(output_f.write("The seats are not available due to absence of {}\n".format(cancel_input[0])), end='')
            output_f.write("The seats are not available due to absence of {}\n".format(cancel_input[0]))
        else:
            if int(seats[i][1:]) <= int(category_column[cancel_input[0]]) and seats[i][0] not in words:
                print("Warning:The category {} has less row than specified index {}\n".format(cancel_input[0],
                                                                                              cancel_input[1]), end='')
                output_f.write("Warning:The category {} has less row than specified index {}\n".format(cancel_input[0],
                               cancel_input[1]))
            elif int(seats[i][1:]) > int(category_column[cancel_input[0]]) and seats[i][0] in words:
                print("Warning:The category {} has less column than specified index {}\n".format(cancel_input[0],
                      cancel_input[1]), end='')
                output_f.write("Warning:The category {} has less column than specified index {}\n".format
                               (cancel_input[0], cancel_input[1]))
            elif int(seats[i][1:]) > int(category_column[cancel_input[0]]) and seats[i][0] not in words:
                print("Warning:The category {} has less column and row than specified index {}\n".format
                      (cancel_input[0], cancel_input[1]), end='')
                output_f.write("Warning:The category {} has less column and row than specified index {}\n".
                               format(cancel_input[0], cancel_input[1]))
            else:
                if seatdict[cancel_input[0]][seats[i]] == "X":  # if they are already empty it will put warning
                    print("Warning:The seat {} at {} has already been free!Nothing to cancel\n".format
                          (seats[i], cancel_input[0]), end='')
                    output_f.write("Warning:The seat {} at {} has already been free!Nothing to cancel\n".format
                                   (seats[i], cancel_input[0]))
                else:  # if seats are not empty it will turn them empty buy putting x to the dictionary
                    seatdict[cancel_input[0]][cancel_input[1]] = "X"
                    print("Success:The seat {} at {} has been canceled and now ready to sell again\n".format(seats[i],
                          cancel_input[0]), end='')
                    output_f.write("Success:The seat {} at {} has been canceled and now ready to sell again\n"
                                   .format(seats[i], cancel_input[0]))


def show_category():
    show_input = line[13:-1]
    words = list(string.ascii_uppercase[0:int(category_row[show_input])])
    words = words[::-1]
    output_f.write("Printing category layout of {}".format(show_input))
    print("Printing category layout of {}".format(show_input))
    for i in words:
        print()
        print(i, end=" ")  # it will put words from last to first
        output_f.write("\n{} ".format(i))
        for j in range(int(category_column[show_input])):
            print(seatdict[show_input][i+str(j)], end="  ")  # this will show the situations of seats as X F T
            output_f.write("{}  ".format(seatdict[show_input][i + str(j)]))
    output_f.write("\n")
    print()
    print("  ", end="")
    for k in range(int(category_column[show_input])):
        if k < 10:
            print(k, end="  ")  # those will write down the columns under the table
            output_f.write("  {}".format(k))
        elif k >= 10:
            output_f.write(" {}".format(k))
            print(k, end=" ")
    output_f.write("\n")
    print()


def balance():
    balance_input = line[8:-1].split(" ")
    if balance_input[0] not in seatdict:
        print("The balance of {} cannot be calculated due to absence of {}\n".format(balance_input[0],
                                                                                     balance_input[0]), end='')
        output_f.write("The balance of {} cannot be calculated due to absence of {}\n".format(balance_input[0],
                                                                                              balance_input[0]))
    else:
        values = seatdict[balance_input[0]].values()
        student = list()
        full = list()
        season = list()
        for j in values:
            if j == "S":  # it will consider for each situation such as student(S),full(F),season ticket(T)
                student.append(j)
            if j == "F":
                full.append(j)
            if j == "T":
                season.append(j)
        revenue = (len(season) * 250) + (len(full) * 20) + (len(student) * 10)
        output_f.write("category report of {}\n".format(balance_input[0]))
        output_f.write("-------------------------------\n")
        output_f.write("Sum of students = {}, Sum of full pay = {}, Sum of season ticket = {}, and Revenues = {} "
                       "Dollars\n".format(len(student), len(full), len(season), revenue))
        print("category report of {}\n".format(balance_input[0]), end='')
        print("-------------------------------\n", end='')
        print("Sum of students = {}, Sum of full pay = {}, Sum of season ticket = {}, and Revenues = {} Dollars\n".
              format(len(student), len(full), len(season), revenue), end='')


f = sys.argv[1]  # this will take the input file that we want to read
stoploop = False
with open(f, "a") as file:
    file.write("\n")
output_f = open("output.txt", "w")
file = open(f, "r")
global line
while not stoploop:
    line = file.readline()
    if "CREATECATEGORY" in line:
        create()
    elif "SELLTICKET" in line:
        sell()
    elif "CANCELTICKET" in line:
        cancel()
    elif "SHOWCATEGORY" in line:
        show_category()
    elif "BALANCE" in line:
        balance()
        pass
    else:
        stoploop = True
