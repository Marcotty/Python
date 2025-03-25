import Snake


#Directions

RIGHT = (0, 1)
LEFT = (0, -1)
DOWN = (1, 0)
UP = (-1, 0)

class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.Snake = Snake.Snake([(width/2+2, height/2), (width/2+1, height/2), (width/2, height/2)], UP)
        
    def board_matrix(self):
        return [[None for i in range(self.width)] for j in range(self.height)]
    
    def isSnakeBodyPosition(self, pos):
        body = self.Snake.body
        if(pos in body):
            return True
        return False
    
    def isSnakeHeadPosition(self, pos):
        if(pos == self.Snake.head()):
            return True
        return False
    
    def render(self):
        #print("Height : ", self.height)
        #print("Width : ", self.width)
        matrix = self.board_matrix()
        print("  ", "#"*self.width*2)
        i = 0
        j = 0
        for row in matrix:
            print("|  ", end = " ")
            j = 0
            for element in row:
                if(self.isSnakeHeadPosition((i,j))):
                    print("X", end = " ")
                elif(self.isSnakeBodyPosition((i,j))):
                    print("O", end = " ")
                else:
                    print(" ", end = " ")
                j += 1
            print("  |")
            i += 1
        print("  ", "#"*self.width*2)
        
    def isSnakeOutOfBound(self):
        if(game.Snake.head()[0] == 0):
            game.Snake.body = game.Snake.stepOutOfBound(game.width, game.Snake.head()[1])
            return True
        elif(game.Snake.head()[0] == game.width):
            game.Snake.body = game.Snake.stepOutOfBound(0, game.Snake.head()[1])
            return True
        elif(game.Snake.head()[1] == 0):
            game.Snake.body = game.Snake.stepOutOfBound(game.Snake.head()[0], game.height)
            return True
        elif(game.Snake.head()[1] == game.height):
            game.Snake.body = game.Snake.stepOutOfBound(game.Snake.head()[0], 0)
            return True
        return False
                
game = Game(8, 10)
game.render()

while(True):
    command = input()
    if(command == "z"):
        if(game.isSnakeOutOfBound() == True):
            pass
        else:
            game.Snake.body = game.Snake.take_step(UP)
    if(command == "s"):
        game.Snake.body = game.Snake.take_step(DOWN)
    if(command == "d"):
        game.Snake.body = game.Snake.take_step(RIGHT)
    if(command == "q"):
        game.Snake.body = game.Snake.take_step(LEFT)
        
    game.isSnakeOutOfBound()
    
    game.render()