from functions import *

currentScreen = Screen.SETUP
amountOfPlayers = 2

playerBoxes = []

def setup():
    size(1000, 800)
    
    def testClick(): print('test')
    createButton('test', Screen.INGAME, 0,0, 50, 50, testClick)
    print(buttons['test']['x'] + buttons['test']['width'])
    
def drawSetup():
    #draws and shows the input for how many players
    textBox()
# end of drawSetup()
    
def drawIngame():
    global playerBoxes
    
    # draw buttons
    stroke(127)
    fill(100)
    for key in buttons:
        button = buttons[key]
        rect(button['x'], button['y'], button['x'] + button['width'], button['y'] + button['height'], 7)
        
    text('Amount of players: ' + str(amountOfPlayers), 100, 100)
        
    x = 50
    for playerBox in playerBoxes:
        s = 'Player ' + str(playerBox.playerNumber + 1) + '\n'
        s = s + 'health: ' + str(playerBox.health) + '\n'
        s = s + 'food: ' + str(playerBox.food) + '\n'
        s = s + 'water: ' + str(playerBox.water) + '\n'
        
        textSize(25)
        text(s, x, 200)
        x = x + 200
        
# end of drawIngame()

def draw():
    background(255)
    textSize(30)
    fill(0)
    stroke(0)
    
    if currentScreen == Screen.SETUP:
       drawSetup()
       
    elif currentScreen == Screen.INGAME:
       drawIngame()
# end of draw()

def keyPressed():
    global currentScreen
    global amountOfPlayers
    global playerBoxes
    
    if currentScreen == Screen.SETUP:
        if key == '2' or key == '3' or key == '4':
            amountOfPlayers = key
        elif key == '\n':
            for x in range(int(amountOfPlayers)):
                print(x)
                playerBoxes.append(PlayerBox(x))
            #
            currentScreen = Screen.INGAME
    elif currentScreen == Screen.INGAME:
        if keyCode == 8: #backspace to go back
            currentScreen = Screen.SETUP
    
def mouseClicked(event):
    if event.getButton() == 37: # check for left mouse
        for key in buttons:
            button = buttons[key]
            if event.getX() >= button['x'] and event.getX() <= (button['x'] + button['width']) and event.getY() >= button['y'] and event.getY() <= (button['y'] + button['height']):
                print('runs button', key)
                button['onClick']()
    

def textBox():
    # text for how many players
    fill(20)
    text('How many players do you want?', 100, 100)
    
    # rectangle behind input
    fill(225)
    rect(200 , 150, 100, 40)
        
    # the input text
    fill(0)
    text(amountOfPlayers, 200, 180)
    
    
