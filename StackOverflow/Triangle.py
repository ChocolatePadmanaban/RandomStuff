class Triangle():
    def __init__(self, a, b, c):
        """
        Constructor for Vec4
        Expects points as arrays in the form of [x, y].
        All coordinates are given as cartesian coordinates.
        """
        self.a = a
        self.b = b
        self.c = c


    def __str__(self):
        """
        Returns a string representation of the triangle. The string is formatted as follows:

        Point A: 0.00 0.00
        Point B: 0.00 0.00
        Point C: 0.00 0.00

        """
        A1,A2,B1,B2,C1,C2=str(self.a[0]),str(self.a[1]),str(self.b[0]),str(self.b[1]),str(self.c[0]),str(self.c[1])
        astring= "Point A: "+ A1+" "+ A2 +"\nPoint B: "+B1+" "+B2+"\nPoint C: "+C1+" "+C2 
        return astring


atriangle=Triangle([0,1],[1,0],[1,1])
print(str(atriangle))