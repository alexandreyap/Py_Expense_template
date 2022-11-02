from PyInquirer import prompt
from examples import custom_style_2
from expense import expense_questions,new_expense
from user import add_user
from report import get_report, broke

def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense","Show Status","New User", "How broke is everyone ?", "Tell me a joke", "Exit"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense()
        ask_option()
    if (option['main_options']) == "Show Status":
        get_report()
        ask_option()
    if (option['main_options']) == "New User":
        add_user()
        ask_option()
    if (option['main_options']) == "How broke is everyone ?":
        broke()
        ask_option()
    if (option['main_options']) == "Tell me a joke":
        print("I'm not funny, sorry")
        ask_option()
    if (option['main_options']) == "Exit":
        print("Bye !")
        return

def main():
    ask_option()

main()