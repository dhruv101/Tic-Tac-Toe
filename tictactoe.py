tic_tac_toe=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
winner=0               #For breaking out of while loop         
i=2                    #For running draw statement

def display_board(tic_tac_toe):
    print('\n')
    print('   |   |   ')
    print(f' {tic_tac_toe[0][0]} | {tic_tac_toe[0][1]} | {tic_tac_toe[0][2]} ')
    print('   |   |   ')
    print('--- --- ---')
    print('   |   |   ')
    print(f' {tic_tac_toe[1][0]} | {tic_tac_toe[1][1]} | {tic_tac_toe[1][2]} ')
    print('   |   |   ')
    print('--- --- ---')
    print('   |   |   ')
    print(f' {tic_tac_toe[2][0]} | {tic_tac_toe[2][1]} | {tic_tac_toe[2][2]} ')
    print('   |   |   ')
    print('\n')


def player1(choice):                  #enter into the board from player1
    global tic_tac_toe                #Changes will occur globally to tic_tac_toe
    if choice == 1:
        tic_tac_toe[0][0]='X'
    elif choice == 2:
        tic_tac_toe[0][1]='X'
    elif choice == 3:
        tic_tac_toe[0][2]='X'
    elif choice == 4:
        tic_tac_toe[1][0]='X'
    elif choice == 5:
        tic_tac_toe[1][1]='X'
    elif choice == 6:
        tic_tac_toe[1][2]='X'
    elif choice == 7:
        tic_tac_toe[2][0]='X'
    elif choice == 8:
        tic_tac_toe[2][1]='X'
    else :
        tic_tac_toe[2][2]='X'


def player2(choice):                 #enter into the board from player2
    global tic_tac_toe               #Changes will occur globally to tic_tac_toe
    if choice == 1:
        tic_tac_toe[0][0]='O'
    elif choice == 2:
        tic_tac_toe[0][1]='O'
    elif choice == 3:
        tic_tac_toe[0][2]='O'
    elif choice == 4:
        tic_tac_toe[1][0]='O'
    elif choice == 5:
        tic_tac_toe[1][1]='O'
    elif choice == 6:
       tic_tac_toe[1][2]='O'
    elif choice == 7:
        tic_tac_toe[2][0]='O'
    elif choice == 8:
        tic_tac_toe[2][1]='O'
    else :
        tic_tac_toe[2][2]='O'

    
def check_for_winner(tic_tac_toe):           #Checking for winner
    global winner                            #Changes will occur globally to winner
    for i in range(3):
        for j in range(1):
        
            if  tic_tac_toe[i][j] == tic_tac_toe[i][j+1] == tic_tac_toe[i][j+2] :          #Horiontally
                if tic_tac_toe[i][j] == 'X':
                    winner+=1
                    return print('winner is player1!!!!!')
                elif tic_tac_toe[i][j] == 'O':
                    winner+=1
                    return print('winner is player2!!!!!')
            
            if  tic_tac_toe[j][i] == tic_tac_toe[j+1][i] == tic_tac_toe[j+2][i] :          #Vertically
                if tic_tac_toe[j][i] == 'X':
                    winner+=1
                    return print('winner is player1!!!!!')
                elif tic_tac_toe[j][i] == 'O':
                    winner+=1
                    return print('winner is player2!!!!!')

    if  tic_tac_toe[0][0] == tic_tac_toe[1][1] == tic_tac_toe[2][2] :                      #Major Digonal
                if tic_tac_toe[0][0] == 'X':
                    winner+=1
                    return print('winner is player1!!!!!')
                elif tic_tac_toe[0][0] == 'O':
                    winner+=1
                    return print('winner is player2!!!!!')
    
    if  tic_tac_toe[0][2] == tic_tac_toe[1][1] == tic_tac_toe[2][0] :                      #Minor Digonal
                if tic_tac_toe[0][2] == 'X':
                    winner+=1
                    return print('winner is player1!!!!!')
                elif tic_tac_toe[0][2] == 'O':
                    winner+=1
                    return print('winner is player2!!!!!')

print('\n'*2)
print('\t\t\t  *****  *****  *****    *****    *     *****    *****  *****  *****') 
print('\t\t\t    *      *    *          *            *          *    *   *       ')
print('\t\t\t    *      *    *          *   ******   *          *    *   *  ***  ')
print('\t\t\t    *      *    *          *            *          *    *   *       ')
print('\t\t\t    *    *****  *****      *  *      *  *****      *    *****  *****')

display_board([['1','2','3'],['4','5','6'],['7','8','9']])

while True:
    choice=int(input("player 1 : "))       #Asks the player,where he wants to enter
    player1(choice)                        #Updates the list
    display_board(tic_tac_toe)             #Display the board
    check_for_winner(tic_tac_toe)          #Check for winner
    if winner == 1:
        break

    if i == 10:                            #Works only for draw condition
      print('match is a draw')
      break

    choice=int(input("player 2 : "))
    player2(choice)
    display_board(tic_tac_toe)
    check_for_winner(tic_tac_toe)
    if winner == 1:
        break
    
    i+=2


    

