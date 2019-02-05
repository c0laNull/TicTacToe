from os import system

wybory = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def rysuj_plansze():
    plansza = f"""
{wybory[0]}|{wybory[1]}|{wybory[2]}
-+-+-"       
{wybory[3]}|{wybory[4]}|{wybory[5]}
-+-+-"       
{wybory[6]}|{wybory[7]}|{wybory[8]}
"""
    print(plansza)

def checkwin():
    if wybory[0] == "X" and wybory[3] == "X" and wybory[6] == "X" or wybory[0] == "X" and wybory[1] == "X" and wybory[2] == "X" or wybory[3] == "X" and wybory[4] == "X" and wybory[5] == "X" or wybory[6] == "X" and wybory[7] == "X" and wybory[8] == "X" or wybory[1] == "X" and wybory[4] == "X" and wybory[7] == "X" or wybory[2] == "X" and wybory[5] == "X" and wybory[8] == "X" or wybory[0] == "X" and wybory[4] == "X" and wybory[8] == "X" or wybory[6] == "X" and wybory[4] == "X" and wybory[2] == "X":
        print("Player X won! Do you want to restart the game? (y/n)")
        a = input()
        if a == "y":
            tic_tac_toe()
        elif a == "n":
            print("zegnaj")
            exit()
        else:
            print("Zly wybor!")
            checkwin()
    elif wybory[0] == "O" and wybory[3] == "O" and wybory[6] == "O" or wybory[0] == "O" and wybory[1] == "O" and wybory[2] == "O" or wybory[3] == "O" and wybory[4] == "O" and wybory[5] == "O" or wybory[6] == "O" and wybory[7] == "O" and wybory[8] == "O" or wybory[1] == "O" and wybory[4] == "O" and wybory[7] == "O" or wybory[2] == "O" and wybory[5] == "O" and wybory[8] == "O" or wybory[0] == "O" and wybory[4] == "O" and wybory[8] == "O" or wybory[6] == "O" and wybory[4] == "O" and wybory[2] == "O":
            print("Player O won! Do you want to restart the game? (y/n)")
            a = input()
            if a == "y":
                tic_tac_toe()
            elif a == "n":
                print("zegnaj")
                exit()
            else:
                print("Zly wybor!")
                checkwin()



wynik = 0, 0
def x_plays():
    czy_gra_x = True
    if czy_gra_x == True:
        ktore_pole = int(input("Wybierz numer pola, graczu X: "))
        if ktore_pole >8:
            print("Zly wybor!")
            x_plays()
        else:
            czy_gra_x = False
            checkwin()
            wybory[ktore_pole] = "X"
def o_plays():
    czy_gra_x = False
    if czy_gra_x == False:
        ktore_pole = int(input("Wybierz numer pola, graczu O: "))
        if ktore_pole >8:
            print("Zly wybor!")
            o_plays()
        else:
            czy_gra_x = True
            checkwin()
            wybory[ktore_pole] = "O"
def tic_tac_toe():
    rysuj_plansze()
    while True:
        x_plays()
        rysuj_plansze()
        checkwin()
        o_plays()
        rysuj_plansze()
        checkwin()
tic_tac_toe()

