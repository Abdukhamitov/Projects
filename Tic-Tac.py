def drawField(field):
    for row in range(5):
        if row%2==0:
            practicalRow=int(row/2)
            for column in range(5):
                if column%2==0:
                    practicalColumn=int(column/2)
                    if column!=4:
                        print(field[practicalColumn][practicalRow],end="")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|",end="")
        else:
            print("-----")
player=1
currentField=[[" "," "," "],[" "," "," "],[" "," "," "]]
while(True):
    print(player," Players move:")
    moveRow=int(input("Please enter the row:(0-2)\n "))
    moveColumn=int(input("Please enter the column:(0-2)\n "))
    if player==1:#make move to first player
        if currentField[moveColumn][moveRow]==" ":
            currentField[moveColumn][moveRow]="X"
            player=2
    else:#make move to second player
        if currentField[moveColumn][moveRow]==" ":
            currentField[moveColumn][moveRow]="O"
            player=1
    drawField(currentField);
    #Checking for winner
    if currentField[0][0]=="X" and currentField[0][1]=="X" and currentField[0][2]=="X":
        print("X win")
        break;
    elif currentField[0][0]=="X" and currentField[1][0]=="X" and currentField[2][0]=="X":
        print("X win")
        break;
    elif currentField[1][0]=="X" and currentField[1][1]=="X" and currentField[2][1]=="X":
        print("X win")
        break;
    elif currentField[0][2]=="X" and currentField[1][2]=="X" and currentField[2][2]=="X":
        print("X win")
        break;
    elif currentField[1][0]=="X" and currentField[1][1]=="X" and currentField[1][2]=="X":
        print("X win")
        break;
    elif currentField[2][0]=="X" and currentField[2][1]=="X" and currentField[2][2]=="X":
        print("X win")
        break;
    elif currentField[2][0]=="X" and currentField[1][1]=="X" and currentField[0][2]=="X":
        print("X win")
        break;
    elif currentField[0][0]=="X" and currentField[1][1]=="X" and currentField[2][2]=="X":
        print("X win")
        break;
    elif currentField[0][0]=="O" and currentField[0][1]=="O" and currentField[0][2]=="O":
        print("O win")
        break;
    elif currentField[0][0]=="O" and currentField[1][0]=="O" and currentField[2][0]=="O":
        print("O win")
        break;
    elif currentField[1][0]=="O" and currentField[1][1]=="O" and currentField[2][1]=="O":
        print("O win")
        break;
    elif currentField[0][2]=="O" and currentField[1][2]=="O" and currentField[2][2]=="O":
        print("O win")
        break;
    elif currentField[1][0]=="O" and currentField[1][1]=="O" and currentField[1][2]=="O":
        print("O win")
        break;
    elif currentField[2][0]=="O" and currentField[2][1]=="O" and currentField[2][2]=="O":
        print("O win")
        break;
    elif currentField[2][0]=="O" and currentField[1][1]=="O" and currentField[0][2]=="O":
        print("O win")
        break;
    elif currentField[0][0]=="O" and currentField[1][1]=="O" and currentField[2][2]=="O":
        print("O win")
        break;
