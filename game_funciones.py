from graphics import*
win = GraphWin('Tic-Tac-Toe', 500, 500)
squares = 9
count=0
win.items=[]
def GameTittle():
    tittle = Text(Point(250 , 50), 'TicTacToe Game')
    tittle.setTextColor('black')
    tittle.setSize(12)
    tittle.draw(win)
 
def board():
    print(GameTittle())
    vertical = Line(Point(200, 100), Point(200, 400)) 
    vertical.setOutline('black')
    vertical.draw(win)

    vertical2 = Line(Point(300, 100), Point(300, 400)) 
    vertical2.setOutline('black')
    vertical2.draw(win)

    horizontal = Line(Point(100, 200), Point(400, 200)) 
    horizontal.setOutline('black')
    horizontal.draw(win)

    horizontal2 = Line(Point(100, 300), Point(400, 300))
    horizontal2.setOutline('black')
    horizontal2.draw(win)
    print(Buttons())
    
   
def Buttons():
    
    buttonRes = Rectangle(Point(200,450), Point(300,475))
    buttonRes.setFill('black')
    buttonRes.setOutline('white')
    buttonRes.draw(win)

    restart = Text(Point(250,463), 'Restart')
    restart.setTextColor('cyan')
    restart.setStyle('bold')
    restart.setSize(10)
    restart.draw(win)
    Display()

def theSquarelist():
   # squares = 9
    for i in range(squares):
        tile = Text(Point(150+(i%3)*100, 150+(i//3)*100), i+1)
        win.items.append(tile)
        
def Message() :
    beforeStart = Text(Point(250, 422), 'Click one of the squares to start the game')
    beforeStart.setTextColor('black')
    beforeStart.setSize(10)
    beforeStart.draw(win)

def MessageX():
    winner1 = Text(Point(250, 422), "X won the game")
    winner1.setTextColor('black')
    winner1.setSize(10)
    winner1.draw(win)
    AfterThis()

def MessageO():
    winner2 = Text(Point(250, 422),  " O won the game")
    winner2.setTextColor('black')
    winner2.setSize(10)
    winner2.draw(win)
    AfterThis()
    
def Tie_Message():
    tie = Text(Point(250, 422), "Is a tie ! Press restart to try again")
    tie.setTextColor('black')
    tie.setSize(10)
    tie.draw(win)
    AfterThis()


def Display():
    #squares = 9
    for sq in range(squares):
        win.items[sq].setTextColor('red')
        win.items[sq].setStyle('bold')
        win.items[sq].setSize(10)
        win.items[sq].draw(win)

def theIf():

    if (win.items[0].getText()==win.items[1].getText() and win.items[1].getText()==win.items[2].getText()):
        if win.items[0].getText()== 'X' :
            MessegeX()
        elif win.items[0].getText()== 'O' :
            MessegeO()
        return False
    
    elif (win.items[3].getText()==win.items[4].getText() and win.items[4].getText()==win.items[5].getText()):
        if win.items[3].getText()== 'X' :
            MessageX()
        elif win.items[3].getText()== 'O' :
            MessageO()
        return False
    
    elif (win.items[6].getText()==win.items[7].getText() and win.items[7].getText()==win.items[8].getText()):
        if win.items[6].getText()== 'X' :
            MessageX()
        elif win.items[6].getText()== 'O' :
            MessageO()
        return False
    
    elif (win.items[0].getText()==win.items[3].getText() and win.items[3].getText()==win.items[6].getText()):
        if win.items[0].getText()== 'X' :
            MessageX()
        elif win.items[0].getText()== 'O' :
            Message()
        return False
    
    elif (win.items[1].getText()==win.items[4].getText() and win.items[4].getText()==win.items[7].getText()):
        if win.items[1].getText()== 'X' :
            MessageX()
        elif win.items[1].getText()== 'O' :
            MessageO()
        return False
    elif (win.items[2].getText()==win.items[5].getText() and win.items[5].getText()==win.items[8].getText()):
        if win.items[2].getText()== 'X' :
            MessageX()
        elif win.items[2].getText()== 'O' :
            MessageO()
        return False
    elif (win.items[0].getText()==win.items[4].getText() and win.items[4].getText()==win.items[8].getText()):
        if win.items[0].getText()== 'X' :
            MessageX()
        elif win.items[0].getText()== 'O' :
            MessageO()
        return False
    
    elif (win.items[2].getText()==win.items[4].getText() and win.items[4].getText()==win.items[6].getText()):
        if win.items[2].getText()== 'X' :
            MessageX()
        elif win.items[2].getText()== 'O' :
            MessageO()
        return False
    
    else :
        for i in range(squares):
            if win.items[i].getText() not in ['X','O'] :
                return True
        Tie_Message()
        return False

def restart():
   # count=0
    for i in range(squares):
        win.items[i].setText(str(i+1))
    print(clear(win))
    print(Message())
    print(Press())

def ERROR():
    message = Text(Point(250, 422), "ERROR you cannot repeat the option taken...")
    message.setTextColor('red')
    message.setSize(10)
    message.draw(win)
    

def Press():
    while (theIf()):
        p1 = win.getMouse()
        if ( (p1.getX()>100 and p1.getX()<400) and (p1.getY()>100 and p1.getY()<400)):
            X = int((p1.getX()-100)//100)
            Y = int((p1.getY()-100)//100)
            global count
            if not (win.items[Y*3+X].getText()=='X') and not (win.items[Y*3+X].getText()=='O') :
                if count % 2 == 0 :
                    win.items[Y*3+X].setText('X')
                else :
                    win.items[Y*3+X].setText('O')
                count+=1
                clear(win)
            else :
                ERROR()
        elif ((p1.getX()>200 and p1.getX()<300) and (p1.getY()>450 and p1.getY()<475)) :
            restart () 
        
def AfterThis():
    p1 = win.getMouse()
    if ((p1.getX()>100 and p1.getX()<200) and (p1.getY()>450 and p1.getY()<475)) :
            restart ()
    else :
        clear(win)
        message = Text(Point(250, 422),  "Click on 'Restart' to play again")
        message.setTextColor('black')
        message.setSize(10)
        message.draw(win)
        p1 = win.getMouse()
        if ((p1.getX()>200 and p1.getX()<300) and (p1.getY()>450 and p1.getY()<475)) :
            restart ()
        else :
            print(AfterThis())
            
def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()
    print(board())

def main():
    print(theSquarelist())
    print(board())
    #print(ResandEx())
    print(Message())
    print(Press())
    #print(Display())
main()
