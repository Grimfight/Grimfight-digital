# Enums not possible??
class Screen():
    SETUP = 1
    INGAME = 2
#End of Screen()

class PlayerBox(object):
    
    def __init__(self, playerNumber):
        self.x = 50 + 200 * playerNumber
        self.y = 200
        self.playerNumber = playerNumber
        self.health = 20
        self.food = 5
        self.water = 5
#End of PlayerBox()
         
# name = the button name
# screen = the screen on which to show the button
# x = x position
# y = y position
# width = the button width
# height = the button height
# onClick = the function executed when the button is clicked
def createButton(name, screen, x, y, width, height, onClick):
    global buttons
    
    buttons[name] = {'screen': screen, 'x': x, 'y': y, 'width': width, 'height': height, 'onClick': onClick}
    return buttons[name]
#End of createButton()

def nextPlayer():
    global currentPlayer
    global currentRound
    global currentPlayerName
    global playerBoxes
    global amountOfPlayers
    
    if currentPlayer < (amountOfPlayers - 1):
        currentPlayer += 1
        
    else:
        currentPlayer = 0
        currentRound += 1
    currentPlayerName = "Player " + str(playerBoxes[currentPlayer].playerNumber + 1)
#End of nextPlayer()

def addHealth():
    if(playerBoxes[currentPlayer].health < 20):
        playerBoxes[currentPlayer].health += 1
#End of addHealth()

def removeHealth():
    if(playerBoxes[currentPlayer].health > 0):
        playerBoxes[currentPlayer].health -= 1
#End of removeHealth()

def addFood():
    if(playerBoxes[currentPlayer].food < 9):
        playerBoxes[currentPlayer].food += 1
#End of addFood()

def removeFood():
    if(playerBoxes[currentPlayer].food > 0):
        playerBoxes[currentPlayer].food -= 1
#End of removeFood()

def addWater():
    if(playerBoxes[currentPlayer].water < 9):
        playerBoxes[currentPlayer].water += 1
#End of addWater()

def removeWater():
    if(playerBoxes[currentPlayer].water > 0):
        playerBoxes[currentPlayer].water -= 1
#End of removeWater()

def rollDice():
    global dice
    
    dice = str(int(random(1, 7) // 1))
    print(dice)
#End of rollDice()

# Global vars

currentScreen = Screen.SETUP
currentRound = 1
currentPlayer = 0
currentPlayerName = ''
amountOfPlayers = 2
playerBoxes = []
buttons = {}
dice = ''

def setup():
    size(1280, 720)
    
    createButton('start', Screen.SETUP, 800, 75, 300, 100, setupIngame)
    
    rollDice()
    setupSetup()
#End of setup()

def setupSetup():
    global playerBoxes
    global currentScreen
    
    playerBoxes = []

    currentScreen = Screen.SETUP
#End of setupSetup()

def setupIngame():
    global playerBoxes
    global currentScreen
    global currentRound
    global currentPlayer
    global currentPlayerName
    
    currentRound = 1
    currentPlayer = 0
    
    for x in range(int(amountOfPlayers)):
        playerBoxes.append(PlayerBox(x))
        
    currentPlayerName = "Player " + str(playerBoxes[currentPlayer].playerNumber + 1)
    createButton('nextPlayer', Screen.INGAME, 410, 365, 200, 50, nextPlayer)
    createButton('dice', Screen.INGAME, 700, 365, 200, 50, rollDice)
    
    createButton('addHealth', Screen.INGAME, 200, 420, 75, 50, addHealth)
    createButton('removeHealth', Screen.INGAME, 300, 420, 75, 50, removeHealth)
    
    createButton('addFood', Screen.INGAME, 200, 480, 75, 50, addFood)
    createButton('removeFood', Screen.INGAME, 300, 480, 75, 50, removeFood)
    
    createButton('addWater', Screen.INGAME, 200, 540, 75, 50, addWater)
    createButton('removeWater', Screen.INGAME, 300, 540, 75, 50, removeWater)

    currentScreen = Screen.INGAME
#End of setupIngame()
    
def drawSetup():
    # text for how many players
    fill(20)
    text('How many players do you want?', 100, 100)
    
    # rectangle behind input
    fill(225)
    rect(100 , 130, 100, 40)
        
    # the input text
    fill(0)
    text(amountOfPlayers, 110, 160)
    
    #start button text
    text("Start game", 870, 135)
#End of drawSetup()
    
def drawIngame():
    global playerBoxes
    
    # Player amount
    
    text('Amount of players: ' + str(amountOfPlayers), 50, 50)
        
    x = 50
    for playerBox in playerBoxes:
        s = 'Player ' + str(playerBox.playerNumber + 1) + '\n'
        s = s + 'health: ' + str(playerBox.health) + '\n'
        s = s + 'food: ' + str(playerBox.food) + '\n'
        s = s + 'water: ' + str(playerBox.water) + '\n'
        
        textSize(22)
        text(s, x, 90)
        x = x + 175
    
    # Info text
        
    textSize(30)
    text("Current Player: " + currentPlayerName, 50, 400)
    text("Dice Roll: " + dice, 700, 450)
    text("Round: " + str(currentRound), 1000, 50)
    text("Health", 100, 450)
    text("Food", 100, 510)
    text("Water", 100, 570)
    
    # Button text
    
    textSize(20)
    text("Next Player", 455, 398)
    text("Roll Dice", 760, 398)
    text("+", 220, 450)
    text("-", 250, 450)
    text("+", 220, 510)
    text("-", 250, 510)
    text("+", 220, 570)
    text("-", 250, 570)
    
    
#End of drawIngame()

def drawButtons():
    stroke(127)
    fill(200)
    for key in buttons:
        button = buttons[key]
        if(button['screen'] == currentScreen):
            rect(button['x'], button['y'], button['width'], button['height'], 7)
#End of drawButtons()

def draw():
    background(255)
    
    # Draws the buttons depending on currentScreen
    drawButtons()
    
    textSize(30)
    fill(0)
    stroke(0)
    
    if currentScreen == Screen.SETUP:
       drawSetup()
       
    elif currentScreen == Screen.INGAME:
       drawIngame()
#End of draw()

def keyPressed():
    global currentScreen
    global amountOfPlayers
    
    if currentScreen == Screen.SETUP:
        if key == '2' or key == '3' or key == '4':
            amountOfPlayers = int(key)
        elif key == '\n':
            setupIngame()
    elif currentScreen == Screen.INGAME:
        if keyCode == 8: #backspace to go back
            setupSetup()
#End of keyPressed()
    
def mouseClicked(event):
    if event.getButton() == 37: # check for left mouse
        for key in buttons:
            button = buttons[key]
            if button['screen'] == currentScreen and \
                event.getX() >= button['x'] and event.getX() <= (button['x'] + button['width']) and \
                event.getY() >= button['y'] and event.getY() <= (button['y'] + button['height']):
                
                button['onClick']()
#End of mouseClicked()
