class PlayerBox(object):
    
     def __init__(self, playerNumber):
         self.x = 50 + 200 * playerNumber
         self.y = 200
         self.playerNumber = playerNumber
         self.health = 20
         self.food = 5
         self.water = 5
         
# def inGame():
    
