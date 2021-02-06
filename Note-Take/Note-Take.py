import os
user = input("Which file you want to open: ")
user=user.lower()+".txt"
if user in os.listdir():
    print(" A) Read the file \n B) Delete the file and start over \n C) Append the file \n D) Replace a single line")
    pick=input("A,B,C,D: ").upper()
    if pick == "A":
         with open(user, 'r') as file:
             print(file.read())
    elif pick =="B":
        with open(user, 'w') as file:
            file.write(input("Write your text here:\n"))
    elif pick =="C":
        with open(user, 'a') as file:
            file.write("\n"+input("Write your text here:\n"))
    elif pick=="D":
        print("1) The line number they want to update.\n2) The text that should replace that line.")
        with open(user, 'r') as file:
            lines=file.readlines()
            print(lines)
            linenum=int(input("Which line?: "))-1
            word=str(input("White your text: "))
            lines[linenum]= word+"\n"
            with open(user, 'w') as file:
                file.writelines(lines)


else:
    with open(user, 'w') as file:
        file.write(input("Write your text here:\n"))

# os.listdir()
