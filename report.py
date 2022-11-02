from expense import get_expenses
import csv

# returns the total amount of expenses for a given user (not including involvement)
def get_expenses_amount_by_user(user):
    expenses = get_expenses()
    expenses_by_user = 0
    for expense in expenses:
        if expense['spender'] == user:
            expenses_by_user += float(expense['amount'])
    return expenses_by_user


# returns the total amount of expenses for all users
def initiate_dictionnary():
    dictionnary = {}
    users = []
    with open('users.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if len(row) > 0:
                users.append(row[0])
    for user in users:
        dictionnary[user] = get_expenses_amount_by_user(user)
    return dictionnary



# Generate a dictionnary for a given user with all the money he owes to each user
def generate_dict_for_user(ower, users):
    dict_for_user = {}
    for user in users:
        if ower == user:
            continue
        dict_for_user[user] = { "amount": 0 }
    return dict_for_user


# return the formalized status report
def formalize_report():
    status_report = {}
    users = []
    with open('users.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if len(row) > 0:
                users.append(row[0])
    
    for user in users:
        status_report[user] = generate_dict_for_user(user, users)

    return status_report


# return the status report
def get_report():
    report = []

    # Get all expenses
    expenses = get_expenses()
    if len(expenses) == 0:
        return "No expenses yet"

    status_report = formalize_report()

    for expense in expenses:
        if expense['involved'] == []:
            continue
        
        share = float(expense['amount']) / (len(expense['involved']) + 1)
        for user in expense['involved']:
            status_report[user][expense['spender']]['amount'] += share

    # Finalize the report
    for ower in status_report:
        owe_to_others = 0
        string = f"{ower} owes "

        user_report = status_report[ower]
        for user in user_report:
            if user_report[user]['amount'] > 0:
                owe_to_others += 1
                if owe_to_others > 1:
                    string += ", "
                string += f"{round(user_report[user]['amount'], 2)} to {user}"

        if owe_to_others == 0:
            print(f"{ower} owes nothing")
        else:
            print(string)

    return status_report



def broke():
    report = []

    # Get all expenses
    expenses = get_expenses()
    if len(expenses) == 0:
        return "No expenses yet"

    status_report = formalize_report()

    for expense in expenses:
        if expense['involved'] == []:
            continue
        
        share = float(expense['amount']) / (len(expense['involved']) + 1)
        for user in expense['involved']:
            status_report[user][expense['spender']]['amount'] += share

    # Finalize the report
    for ower in status_report:
        owe_to_others = 0
        user_report = status_report[ower]
        for user in user_report:
            if user_report[user]['amount'] > 0:
                owe_to_others += user_report[user]['amount']
        
        print(f"{ower} is {owe_to_others} in debt")