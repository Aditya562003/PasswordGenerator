import random
import string

def main():
    global password_size
    password = ""
    letters = list(string.ascii_letters)
    digits = list(string.digits)
    punctuations = list(string.punctuation)
    punctuations.remove("\\")
    main_list = list()
    initial_size = 1
    try:
        password_size = int(input("Enter the size of the password \n"))
    except Exception:
        print("Please enter an integer value")
    finally:
        try:
            if password_size%3 == 0:
                while initial_size <= password_size/3:
                    l1 = random.choice(letters)
                    l2 = random.choice(digits)
                    l3 = random.choice(punctuations)
                    main_list.append(l1)
                    main_list.append(l2)
                    main_list.append(l3)
                    initial_size += 1
            elif password_size%3 != 0:
                while initial_size <= password_size//3:
                    l1 = random.choice(letters)
                    l2 = random.choice(digits)
                    l3 = random.choice(punctuations)
                    main_list.append(l1)
                    main_list.append(l2)
                    main_list.append(l3)
                    initial_size += 1
                remaining = password_size - (3 * (password_size//3))
                for  i in range(1, remaining+1):
                    l1 = random.choice(letters)
                    l2 = random.choice(digits)
                    l3 = random.choice(punctuations)
                    n_list = [l1, l2, l3]
                    ran = random.choice(n_list)
                    main_list.append(ran)

            for i in main_list:
                password += i
            print("Password is : ", password, end="")
        except Exception:
            main()

if __name__ == '__main__':
    main()