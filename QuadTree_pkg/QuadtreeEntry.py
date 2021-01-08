import arcade

class QuadEntry():

    def __init__(self, x, y, value):
        # Position
        self.x = x
        self.y = y
        
        # Data
        self.value = value

        # Display values
        self.radius = 5
        self.color = arcade.color.GREEN


    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

    def __str__(self):
        return "xy: (" + str(self.x) + ", " + str(self.y) +"); radius: " + str(self.radius) + "\n value = " + str(self.value)


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
            