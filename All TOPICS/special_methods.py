class Book:
    def __init__(self,title,author):
        self.author= author
        self.title = title
    def __str__(self):
        return f" '{self.title}' by {self.author}"
book =  Book(1984,"George Munsey")
print(book)

class Playlist:
    def __init__(self,songs):
        self.songs = songs
    def __len__(self):
        return len(self.songs)
    def __add__(self, other):
        return Playlist(self.songs + other.songs)
p1 = Playlist(["Song1","Song2"])
print(len(p1))
p2 = Playlist(["Song3"])
print(len(p1)+len(p2))

class Point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y
    def __str__(self):
        return f" {self.x} , {self.y}"
    def __add__(self, other):
        if not isinstance (other,Point):
            return NotImplemented
        return (self.x) + other.x , (self.y) + other.y

pt1 = Point(2,3)
pt2 = Point(4,6)
print(pt1+pt2)