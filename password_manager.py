def checkPw():
    if admin_user == user_1 and admin_password == user_1_password:
        print(ask_data)   
    else:
        print(f"Access denied '{admin_user}'")


def checkData():  
    import csv
    with open('user_data.csv', 'r') as data_file:
        csv_reader = csv.reader(data_file)

        for line in csv_reader:
            if request_input == line[0]:
                print(line[1])
            else:
                print("Sorry no match found")
                break








#----main

admin_user = input("Enter username: ")
admin_password = input("Enter password: ")
user_1 = 'Zar'
user_1_password = ''
request_input = input("What is your request: ")
ask_data = input("What is your request: ")
request_input = ask_data



checkPw()

    





