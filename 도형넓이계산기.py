class Cal():
    def __init__ (self, width, height):
        self.width = width
        self.height = height
    
    def Square_area(self):
        return self.width * self.height
         
    def Triangle_area(self):
        return self.width * self.height / 2

    def Circle_area(self):
        return (self.width/2)**2 * 3
        
area = Cal(14,23)

print(area.Square_area())
print(area.Triangle_area())
print(area.Circle_area())


