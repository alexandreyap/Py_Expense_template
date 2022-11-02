from PyInquirer import prompt
import csv

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
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

]



def new_expense(*args):
    infos = prompt(expense_questions)

    amount = infos['amount']
    label = infos['label']
    spender = infos['spender']

    # Check if spender exists
    exists = False
    with open('users.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if spender in row:
                exists = True
                break
    
    if not exists:
        print('Spender does not exist, please add it first')
        return

    # Add the expense to the expenses.csv file
    with open('expenses.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([amount, label, spender])


    print("Expense Added !")
    return True


