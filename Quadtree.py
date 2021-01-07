import arcade
from QuadtreeEntry import QuadEntry

class Quadtree():

    def __init__(self, x, y, width, height, parant=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.max_points = 4
        self.points = []
        self.splited = False
        
        self.no = None
        self.so = None
        self.sw = None
        self.nw = None

        self.parant = parant


    def contains(self, x, y):
        return self.x - self.width/2 <= x < self.x + self.width/2 and self.y - self.height/2 <= y < self.y + self.height/2


    def insert(self, quad_entry):
        
        if not self.contains(quad_entry.x, quad_entry.y):
            return False

        # Damit keine Daten auf die gleichen Koordinaten geleget werden können
        if quad_entry in self.points:
            return False

        if len(self.points) < self.max_points and not self.splited:
            self.points.append(quad_entry)

            return True
        else: 
            if not self.splited:
                self.no = Quadtree(self.x + self.width/4 , self.y + self.height/4 , self.width/2, self.height/2, parant=self)
                self.so = Quadtree(self.x + self.width/4 , self.y - self.height/4 , self.width/2, self.height/2, parant=self)
                self.sw = Quadtree(self.x - self.width/4 , self.y - self.height/4 , self.width/2, self.height/2, parant=self)
                self.nw = Quadtree(self.x - self.width/4 , self.y + self.height/4 , self.width/2, self.height/2, parant=self)
                self.splited = True

                for point in self.points:
                    self.no.insert(point) or self.so.insert(point) or self.sw.insert(point) or self.nw.insert(point)
                self.points = []
                
            return self.no.insert(quad_entry) or self.so.insert(quad_entry) or self.sw.insert(quad_entry) or self.nw.insert(quad_entry)
    

    def delete(self, x, y):

        if self.splited:
            subtrees = {self.no.contains(x, y):self.no,
                        self.so.contains(x, y):self.so,
                        self.sw.contains(x, y):self.sw,
                        self.nw.contains(x, y):self.nw}

            return subtrees[True].delete(x, y)

        for i, quad_entry in enumerate(self.points):
            if quad_entry.x == x and quad_entry.y == y:
                self.points.pop(i)

                parant_points = []
                if len(self.parant.read(parant_points)) <= self.max_points:
                    self.parant.no = None
                    self.parant.so = None
                    self.parant.sw = None
                    self.parant.nw = None
                    self.parant.splited = False
                    
                    for parant_point in parant_points:
                        self.parant.insert(parant_point)

                return True
        
        return False
        
    

    def search(self, value):
        points = []

        for quad_entry in self.read([]):
            if quad_entry.value == value:
                points.append((quad_entry.x, quad_entry.y))
        
        return points


    def get(self, x, y):

        if self.splited:
            subtrees = {self.no.contains(x, y):self.no,
                        self.so.contains(x, y):self.so,
                        self.sw.contains(x, y):self.sw,
                        self.nw.contains(x, y):self.nw}

            return subtrees[True].get(x, y)

        for quad_entry in self.points:
            if quad_entry.x == x and quad_entry.y == y:
                return quad_entry.value


        return None


    def read(self, points):

        for point in self.points:
            points.append(point)

        if self.splited:
            self.no.read(points)
            self.so.read(points)
            self.sw.read(points)
            self.nw.read(points)
        
        return points


    def move(self):
        for point in self.points:
            point.move()

        if self.splited:
            self.no.move()
            self.so.move()
            self.sw.move()
            self.nw.move()


    def draw_tree(self):
        arcade.draw_rectangle_outline(self.x, self.y, self.width, self.height, arcade.color.WHITE)

        if self.splited:
            self.no.draw_tree()
            self.so.draw_tree()    
            self.sw.draw_tree()
            self.nw.draw_tree()  


    def draw_points(self):
        if self.splited:
            self.no.draw_points()
            self.so.draw_points()    
            self.sw.draw_points()
            self.nw.draw_points()   
        else:
            for point in self.points:
                arcade.draw_point(point.x, point.y, point.color, 10)


    def __str__(self):
        return str(self.points) + "; splited: "+ str(self.splited)






