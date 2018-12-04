buttons = {}

class Screen():
    SETUP = 1
    INGAME = 2

class PlayerBox(object):
    
     def __init__(self, playerNumber):
         self.x = 50 + 200 * playerNumber
         self.y = 200
         self.playerNumber = playerNumber
         self.health = 20
         self.food = 5
         self.water = 5
         
# name = the button name, screen = current screen, x = x position, y = y position, width = the button width, height = the button height, onClick = the function executed when the button is clicked
def createButton(name, screen, x, y, width, height, onClick):
    global buttons
    
    buttons[name] = {'x': x, 'y': y, 'width': width, 'height': height, 'onClick': onClick}
    return buttons[name]
    
    
    
# def inGame():
    
