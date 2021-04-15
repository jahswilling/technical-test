def sign_up():
    username = input("Enter Username: ")
    password1 = input("Enter Password: ")

    password2 = input("Confirm Password: ")

    if password1 ==password2 :
        file1 = open(f"{username}details.txt","a")
        file1.write(f'{username}\n')
        file1.write(password1)
        file1.close()
        print("user details have been stored")
    else:
        print('passwords do not match')


sign_up()
