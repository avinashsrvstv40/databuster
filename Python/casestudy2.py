def eligible(prof):
    if prof in profEligibility.keys() and profEligibility[prof] == "yes":
        print("You are eligible")
    else:
        print("Sorry")


def profcheck(prof):
    if prof.lower() in profList:
        return eligible(prof)
    else:
        print("Enter valid profession")


if __name__ == "__main__":
    profEligibility = {}
    profList = []
    with open("C:\\Users\\user\\Downloads\\bank-data.csv", 'r') as records:
        next(records)
        for record in records:
            if record.split(",")[1].replace('.', '') not in profList:
                profList.append(record.split(",")[1].replace('.', '').lower())
                profEligibility[record.split(",")[1].replace(".", "")] \
                    = record.split(",")[3].replace("\n", "").lower()


    while(True):
        user_input = input("Please provide your profession: ")
        if user_input.lower()=="end":
            print("Exiting...")
            break
        else:
            profcheck(user_input)