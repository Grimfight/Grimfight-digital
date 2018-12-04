SETUP = 'setup'
INGAME = 'inGame'

currentScreen = SETUP
amountOfPlayers = 2
inp = ''

playerBoxes = []

from functions import PlayerBox

def setup():
    size(1000, 800)
    
    

def draw():
    global playerBoxes
    
    background(255)
    textSize(30)
    fill(0)
    stroke(0)
    
    if currentScreen == SETUP:
       #draws and shows the input for how many players
       textBox()
       
    elif currentScreen == INGAME:
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
            
            
    
# end of draw()

def keyPressed():
    global currentScreen
    global amountOfPlayers
    global playerBoxes
    
    if currentScreen == SETUP:
        if key == '2' or key == '3' or key == '4':
            amountOfPlayers = key
        elif key == '\n':
            for x in range(int(amountOfPlayers)):
                print(x)
                playerBoxes.append(PlayerBox(x))
                
                
            #
            currentScreen = 'inGame'
    elif currentScreen == INGAME:
        if keyCode == 8: #backspace to go back
            currentScreen = SETUP
    
    
    

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
    
    
