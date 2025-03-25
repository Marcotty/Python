class Snake:
    def __init__(self, body, direction):
        self.body = body
        self.direction = direction
        
    def take_step(self, position):
        head = self.head()
        move = self.body[1:]
        move.append((head[0] + position[0], head[1] + position[1]))
        return move
    
    def stepOutOfBound(self, width, height):
        move = self.body[1:]
        move.append((width, height))
        return move
    
    def set_direction(self, direction):
        self.direction = direction
    
    def head(self):
        return self.body[-1]