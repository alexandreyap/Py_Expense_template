from PyInquirer import prompt
import csv

user_questions = [
{
        "type":"input",
        "name":"spender",
        "message":"New User - Name: ",
        "validate": lambda val: len(val.strip()) > 0 or "Please enter a name",
    },
]

def add_user(*args):
    # This function should create a new user, asking for its name
    user = prompt(user_questions)
    userName = user['spender'].strip()

    # Check if the user already exists
    with open('users.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if userName in row:
                print('User already exists')
                return

    # Add the user to the users.csv file
    with open('users.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([userName])

    print(f"User {userName} Added !")
    return