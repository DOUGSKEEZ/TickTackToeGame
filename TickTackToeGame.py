import random
import sys
import os

#Define Grid:
a="1"
b="2"
c="3"
d="4"
e="5"
f="6"
g="7"
h="8"
i="9"
#Other definitions:
player_1 = 'Player_1'
player_2 = 'Player_2'
turn = 1
count = 0
gameStart = 1
gameActive = 0

#PRINT GRID
def showGrid():
    print("\n\n     ||     ||     ")
    print(" ",a," || ",b," || ",c," ")
    print("     ||     ||     ")
    print("=====||=====||=====")
    print("     ||     ||     ")
    print(" ",d," || ",e," || ",f," ")
    print("     ||     ||     ")
    print("=====||=====||=====")
    print("     ||     ||     ")
    print(" ",g," || ",h," || ",i," ")
    print("     ||     ||     ")

# USER INPUT#
def userInput():
    global placeMove
    placeMove = input("Please enter grid space for your move: ")

    if placeMove == a or placeMove == b or placeMove == c or placeMove == d or placeMove == e or placeMove == f or placeMove == g or placeMove == h or placeMove == i:
        return placeMove
    else:
        while placeMove != a or placeMove != b or placeMove != c or placeMove != d or placeMove != e or placeMove != f or placeMove != g or placeMove != h or placeMove != i:
            print ('\nERROR!\nThere is already an X or an O here \n       OR       \nThis is NOT a number on the grid.\n')
            placeMove = input("Please enter a grid number between 1-9...")
            if placeMove == a or placeMove == b or placeMove == c or placeMove == d or placeMove == e or placeMove == f or placeMove == g or placeMove == h or placeMove == i:
                return placeMove
            else:
                continue

# CHECK INPUT and PLACE MOVE #
def checkInput(placeMove):
    global a, b, c, d, e, f, g, h, i
    while placeMove == 'X' or placeMove == 'O':
        print('\nERROR!\n\nThere is already an X or O in that grid location!\n')
        userInput()
    else:
        print('Excellent choice.')
        placeInput()

# SET INPUT (inside Check and Place)#
def placeInput():
    ##Turn 1 is X
    global a, b, c, d, e, f, g, h, i
    if turn == 1:
        if placeMove == a:
            a = 'X'
        elif placeMove == b:
            b = 'X'
        elif placeMove == c:
            c = 'X'
        elif placeMove == d:
            d = 'X'
        elif placeMove == e:
            e = 'X'
        elif placeMove == f:
            f = 'X'
        elif placeMove == g:
            g = 'X'
        elif placeMove == h:
            h = 'X'
        elif placeMove == i:
            i = 'X'
    if turn == 2:
        if placeMove == a:
            a = 'O'
        elif placeMove == b:
            b = 'O'
        elif placeMove == c:
            c = 'O'
        elif placeMove == d:
            d = 'O'
        elif placeMove == e:
            e = 'O'
        elif placeMove == f:
            f = 'O'
        elif placeMove == g:
            g = 'O'
        elif placeMove == h:
            h = 'O'
        elif placeMove == i:
            i = 'O'

# Player 1 Name #
def getPlayer1Name():
    global player_1
    player_1 =  input("Please enter Player 1's name: ")
    if len(player_1)>0 and len(player_1)<30:
        return player_1
    elif len(player_1)==0:
        player_1 = 'Player 1'
        return player_1
    else:
        while len(player_1)>30:
            print ('Name too long...')
            player_1 = input("Please enter a shorter name: ")
            if len(player_1)>30:
                return player_1
            else:
                continue
# Player 2 Name #
def getPlayer2Name():
    global player_2
    player_2 =  input("Please enter Player 2's name: ")
    if len(player_2)>0 and len(player_2)<30:
        return player_2
    elif len(player_2)==0:
        player_2 = 'Player 2'
        return player_2
    else:
        while len(player_2)>30:
            print ('Name too long...')
            player_2 = input("Please enter a shorter name: ")
            if len(player_2)>30:
                return player_2
            else:
                continue

def beginGame():
    global gameStart
    global gameActive
    global a,b,c,d,e,f,g,h,i
    while gameActive == 0:
        startGame = input('Would you like to start a new game? (Y/N) ')
        if startGame.lower() == 'y':
            gameActive=1
            getPlayer1Name()
            getPlayer2Name()
            a="1"
            b="2"
            c="3"
            d="4"
            e="5"
            f="6"
            g="7"
            h="8"
            i="9"
            break
        elif startGame.lower() == 'n':
            print('Shutting down................................')
            gameStart = 0
            break
        else:
            print('Sorry, did not understand input.  Please enter Y or N.')
            continue

### GAME EXECUTION ###
while gameStart == 1:

    #Ask to begin game
    beginGame()
    #Shutdown Opt-Out
    if gameStart == 0:
        break

    #Winning Conditions
    topRow = [a,b,c] #1
    midRow = [d,e,f] #2
    botRow = [g,h,i] #3
    matrix = [topRow,midRow,botRow]
    col_1 = [row[0] for row in matrix] #4
    col_2 = [row[1] for row in matrix] #5
    col_3 = [row[2] for row in matrix] #6
    diagDown = [a,e,i] #7
    diagUp = [g,e,c] #8

    #Ending game criteria
    #if count of X's or O's in Winning conditions is 3 then Game Over
    #Player 1 (X's) Wins
    if  topRow.count('X') ==3 or midRow.count('X') ==3 or botRow.count('X') ==3 or col_1.count('X') ==3 or col_2.count('X') ==3 or col_3.count('X') ==3 or diagDown.count('X') ==3 or diagUp.count('X') ==3:
        print('\n\n\n\n\n\n\n\n',player_1,' WINS!!!\n(Player 1)')
        showGrid()
        print('\n\n------------------\n || Game Over. ||\n------------------\n\n\n')
        gameActive = 0
        count = 0
        continue
    #Player 2 (O's) 2 Wins
    elif topRow.count('O') ==3 or midRow.count('O') ==3 or botRow.count('O') ==3 or col_1.count('O') ==3 or col_2.count('O') ==3 or col_3.count('O') ==3 or diagDown.count('O') ==3 or diagUp.count('O') ==3:
        print('\n\n\n\n\n\n\n\n',player_2,' WINS!!!\n(Player 2)')
        showGrid()
        print('\n\n------------------\n || Game Over. ||\n------------------\n\n\n')
        gameActive = 0
        count = 0
        continue
    #DRAW (Full Board)
    elif count ==9: #
        print('\n\n\n\n\n\n\n\n DRAW !!!\n')
        showGrid()
        print('\n\n------------------\n || Game Over. ||\n------------------\n\n\n')
        gameActive = 0
        count = 0
        continue

    #Player Turns
    showGrid()
    if turn == 1:
        #Turn 1 is X
        print('\n\n',player_1,"'s turn. (Player 1)")
        print("Select a space in the grid to place an 'X'")
        userInput()
        checkInput(placeMove)
        turn=2
        count+=1
    else:
        #Turn 2 is O
        print('\n\n',player_2,"'s turn. (Player 2)")
        print("Select a space in the grid to place an 'O'")
        userInput()
        checkInput(placeMove)
        turn=1
        count+=1






