from PyInquirer import prompt
import csv

def get_users(spender):
    users = []

    with open('users.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if len(row) > 0:
                if row[0] != spender:
                    users.append({"name": row[0]})
                else :
                    users.append({"name": row[0], "checked": True})

    return users


expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": [user[0] for user in csv.reader(open('users.csv', 'r'))]
    },
]

def involved_questions(spender):
    involved_questions = [
        {
            "type": "checkbox",
            "message": "Select involved users",
            "name": "involved",
            "choices": get_users(spender),
        }
    ]
    return involved_questions


def new_expense(*args):
    infos = prompt(expense_questions)

    try:
        amount = float(infos['amount'])
    except ValueError:
        print("Invalid amount")
        return

    label = infos['label']
    spender = infos['spender']
    infosv2 = prompt(involved_questions(spender))

    involved = infosv2['involved']
    while len(involved) == 0:
        print("You must select at least one involved user (or the spender if no one else is involved)")
        involved = prompt(involved_questions)['involved']

    if spender in involved:
        involved.remove(spender)
    # No need to check spender's existence as it is a choice from the list of users

    # Add the expense to the expenses.csv file
    with open('expenses.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',  quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([amount, label, spender] + involved)

    print("Expense Added !")
    return True



def get_expenses():
    expenses = []

    with open('expenses.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            if len(row) > 2:
                if (len(row) > 3):
                    involved = row[3:]
                else:
                    involved = []
                expenses.append({
                    "amount": row[0],
                    "label": row[1],
                    "spender": row[2],
                    "involved": involved,
                })

    return expenses

