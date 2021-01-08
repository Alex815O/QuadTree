import arcade
import random as rd
from Quadtree import Quadtree
from QuadtreeEntry import QuadEntry

points_anz = 10

class QuadWindow(arcade.Window):

    def __init__(self, w, h):
        super().__init__(w, h, "Quadtree")
        self.height = h
        self.width = w
                    
                    
    def setup(self, w, h):
        self.qaudtree = Quadtree(w/2, h/2, w, h)
        arcade.set_background_color(arcade.color.OCEAN_BOAT_BLUE)

        for i in range(0, points_anz):
            self.qaudtree.insert( QuadEntry( rd.randint(0, w), rd.randint(0, h), i) )
        
        # in app command line
        self.command_text = ""

    def on_draw(self):
        arcade.start_render()
        
        # self.qaudtree.move()
        self.qaudtree.draw_tree()
        self.qaudtree.draw_points()

        # show command line
        arcade.draw_text(self.command_text, 10, self.height-20, arcade.color.WHITE)
       

    def on_mouse_press(self, x, y, button, modifiers):
        print("Mouse pressed on ", x, y, self.qaudtree.insert( QuadEntry(x, y, rd.randint(0, 50))))


    def on_key_press(self, key, modifiers):
        if 65288 == key:
            self.command_text = self.command_text[:-2]
        else:
            self.command_text += chr(key)

        if arcade.key.ENTER == key:
            command = self.command_text[:-1]
            self.command_text = ""

            if command == "len":
                points = []
                self.qaudtree.read(points)
                print(len(points))
            
            elif command[:3] == "get":
                _, cx, cy = command.split(" ")
                cx, cy = int(cx), int(cy)
                value = self.qaudtree.get(cx, cy)
                print(cx, cy, ">>", value)

            elif command[:6] == "search":
                _, value = command.split(" ")
                print(value, ">>", self.qaudtree.search(int(value)))
            
            elif command[:3] == "pop":
                _, cx, cy = command.split(" ")
                cx, cy = int(cx), int(cy)
                print(self.qaudtree.delete(cx, cy))
        

if __name__ == "__main__":
    window = QuadWindow(600, 600)
    window.setup(600, 600)
    arcade.run()