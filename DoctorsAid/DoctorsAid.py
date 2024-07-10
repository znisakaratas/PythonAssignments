# 2210356066
# ZeynepNisaKARATAŞ
patientlist = []  # this is the multi-dimensional list that will  be filled
def output_txt(command):  # 5 of the functions are in this function so it can call them easily

    def create():
        # this function will take the create command and will put patient_input into patientlist.
        patient_input = line[7:].split(",")
        if patient_input not in patientlist:  # if patient is not in system this will record the patient and write it
            patientlist.append(patient_input)
            return output_file.write("Patient {} is recorded.\n".format(patientlist[-1][0]))
        elif patient_input in patientlist:  # If patient was already there it will write this in output file
            return output_file.write("Patient {} cannot be recorded due to duplication.\n".format(patient_input[0]))

    def remove():
        # this function will take the remove command and delete the patients in those lines.
        patients = str(line[7:-1])  # we get the name from line
        patients = patients.replace(" ", "")
        c = 0
        while c < len(patientlist):  # the loop will remove all the patients who was written beside remove
            if patients in patientlist[c]:
                patientlist.pop(c)  # this will delete the patient informations from system
                return output_file.write("Patient {} is removed.\n".format(patients))
            else:  # if patient isnt in system it will write this into output file
                c += 1
        return output_file.write("Patient {} cannot be removed due to absence.\n".format(patients))

    def probability():
        # this function will calculate the probability of a person to get the cancer.
        patients = str(line[12:-1])  # this takes the patient name

        for j in range(len(patientlist)):  # this loop will calculate each patients probability and write it to file.
            pat = patientlist[j]
            if patients in pat:
                percentage = float(patientlist[j][1])
                people = int(patientlist[j][3][0:3])  # numerator of treatment incidence
                totalpeople = int(patientlist[j][3][-6:])  # denominator of treatment incidence
                probability = people / (people + ((1 - percentage) * totalpeople)) * 100
                probability = (float((str(probability))[0:5]))
                probab = format(probability,"g")  # this will erase the zeros after decimal point
                prob = output_file.write(
                    "Patient {} has a probability of {}{} of having {}.\n".format(patients, probab,"%",
                                                                                  patientlist[j][2]))
                return prob
        return output_file.write("Probability for {} cannot be calculated due to absence.\n".format(patients))
    def recommendation():
    # this function will consider the risk and the probability and decide whether the person should get treatment or not
        patients1 = str(line[15:-1])  # we take patients name
        pati1 = int(len(patientlist))
        for i in range(pati1):  # this loop will compare the risk and probability and write if patient should get
            pat1 = patientlist[i][0]                                                        # treatment or not
            if pat1 == patients1:
                percentage1 = float(patientlist[i][1])
                people1 = int(patientlist[i][3][0:3])
                totalpeople1 = int(patientlist[i][3][-6:])
                probability1 = people1 / (people1 + ((1 - percentage1) * totalpeople1)) * 100
                risk = int(float(patientlist[i][5]) * 100)
                if risk < probability1:  # if risk is lesser it writes for patient to have the treatment in output file.
                    return output_file.write("System suggests {} to have the treatment.\n".format(patients1))
                elif risk > probability1:  # if risk is greater it writes not to have treatment in output file
                    return output_file.write("System suggests {} NOT to have the treatment.\n".format(patients1))
                else:
                    pass
            else:
               pass    # if patient is not in system it cant recommend anything and writes this into output file
        return output_file.write("Recommendation for {} cannot be calculated due to absence.\n".format(patients1))


    def list():  # this function will make a table into output file
        title = "Patient"
        title1 = "Diagnosis"  # for each title there are variables
        title2 = "Disease"
        title3 = "Disease"
        title4 = "Treatment"
        title5 = "Treatment"  # the distance is calculated according to the length of the words
        output_file.write(f"{title:<8}{title1:<14}{title2:<16}{title3:<12}{title4:<17}{title5:<10}\n")
        title6 = "Name"
        title7 = "Accurancy"
        title8 = "Name"
        title9 = "Incidence"
        title10 = "Name"
        title11 = "Risk"
        output_file.write(f"{title6:<8}{title7:<14}{title8:<16}{title9:<12}{title10:<17}{title11:<10}\n")
        x = "-" * 80
        output_file.write(f"{x}\n")

        for i in range(len(patientlist)):
            patient_name = patientlist[i][0]
            diagnosis_acc = (float(patientlist[i][1])) * 100
            diagnosis_accuracy = str(diagnosis_acc) + "%"
            disease_name = patientlist[i][2]
            disease_incidence = patientlist[i][3]
            treatment_name = patientlist[i][4]
            treatrisk = float(patientlist[i][5]) * 100
            treat_risk = format(treatrisk, "g")  # this will erase the zeros after decimal point
            treatment_risk = str(treat_risk) + "%"
            # the loop will take each patient from list and all their infos from list and write them into output file
            output_file.write(f"{patient_name:<8}{diagnosis_accuracy:<13}{disease_name:<16}{disease_incidence:<12}"
                              f"{treatment_name:<18}{treatment_risk}\n")


    if command == "create":  # this is the part of the output function which takes the commands and calls the functions
        return create()
    elif command == "remove":
        return remove()
    elif command == "probability":
        return probability()
    elif command == "recommendation":
        return recommendation()
    elif command == "list":
        return list()
    else:
        pass


def input_txt():  # for each command function calls the output function so it can achieve the target function

    if "create" in line:
        output_txt("create")
    elif "remove" in line:
        output_txt("remove")
    elif "probability" in line:
        output_txt("probability")
    elif "recommendation" in line:
        output_txt("recommendation")
    elif "list" in line:
        output_txt("list")
        pass
    else:
        global should_stop  # this will end the loop
        should_stop = True

with open("doctors_aid_inputs.txt", "a", encoding="utf-8") as file:
    file.write("\n")
output_file = open("doctors_aid_outputs.txt", "w", encoding="utf-8")
f = open("doctors_aid_inputs.txt", "r", encoding="utf-8")
should_stop = False
while not should_stop:  # the loop will call the input file and make input function read the lines
    line = f.readline()
    input_txt()
