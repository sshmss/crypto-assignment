from ntpath import join
import string
import random

alphanum = string.ascii_lowercase + string.digits
alphanum_list = list(alphanum)

password = input("Enter a password (max: 6) (lowercase letters and numbers only):")
result_password = ""
iteration = 0
while(result_password != password):
    result_password = random.choices(alphanum_list, k=len(password))
    print(iteration,''.join(result_password))
    iteration = iteration + 1

    if(result_password == list(password)):
        print("Result Password:", ''.join(result_password))
        break
