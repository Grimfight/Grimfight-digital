buttons = {}

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
    
# def inGame():
    
