def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

def encoder(password):

    list = []
    string_ver = ""
    for i in range (0,len(password)):
        if int(password[i]) < 7:
            list.append(str(int(password[i])+3))
        elif int(password[i]) >= 7:
            list.append(str((int(password[i])+3)%10))

    for j in range(0, len(list)):
        string_ver += list[j]

    return string_ver


def decoder(password):

    list = []
    string_ver = ""
    for i in range(0, len(password)):
        if int(password[i]) > 2:
            list.append(str(int(password[i]) - 3))
        elif int(password[i]) <= 2:
            list.append(str((int(password[i]) + 7) % 10))

    for j in range(0, len(list)):
        string_ver += list[j]

    return string_ver

if __name__ == "__main__":

    while True:

        print_menu()

        user_input = int(input("Please enter an option: "))

        if user_input == 1:

            password = encoder(input("Please enter your password to encode: "))

            print("Your password has been encoded and stored!")
            print()

        elif user_input == 2:

            print(f"The encoded password is {password}, and the original password is {decoder(password)}")
            print()

        elif user_input == 3:
            break


