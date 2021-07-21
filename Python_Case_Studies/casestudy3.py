import re


class CustomerNotAllowedException(Exception):

    def __init__(self, name, message="Customer is blacklisted"):
        self.name = name
        self.message = message
        super().__init__(self.message)


if __name__ == "__main__":

    dictNames = {}
    with open("C:\\Users\\user\\Downloads\\FairDealCustomerData.csv", 'r') as customerdata:
        for record in customerdata:
            regex = re.compile("([a-zA-Z]+.+),\s([a-zA-Z]+).\s([a-zA-Z]+[\/\]\s[a-zA-Z]*\\b)")
            dictNames[regex.findall(record)[0][1] + " " + regex.findall(record)[0][2] +
                      regex.findall(record)[0][0]] = int(record.strip().split(",")[2])

    searchElig = input("Enter the name: ")

    if searchElig in dictNames.keys() and dictNames[searchElig] == 0:
        print("Eligible")
    elif searchElig in dictNames.keys() and dictNames[searchElig] == 1:
        raise CustomerNotAllowedException(searchElig)
    else:
        print("Name not found")