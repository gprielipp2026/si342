class Pos:

    def __init__(self,row,col):
        self.row = row
        self.col = col

    def len(self):
        return self.row + self.col

    def __add__(self, other):
        self.row += other.row
        self.col += other.col
        return self

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def step(self, direction: str):
        vectors = {
                    'N': Pos(-1, 0),
                    'E': Pos( 0, 1), 
                    'S': Pos( 1, 0),
                    'W': Pos( 0,-1)
                  }
        if direction not in vectors.keys():
            raise Exception("Invalid direction")

        self = self + vectors[direction]
        

    def __repr__(self):
        return str(self)

    def __str__(self):
        return Pos.disp(self.row,self.col)

    # Static attributes and methods
    sep = ":"

    def disp(v1,v2):
        return f"({v1}{Pos.sep}{v2})";


class LabPos(Pos): # means LabPos extends Pos

    def __init__(self,row,col,lab):
        Pos.__init__(self,row,col)  # calls the constructor from Pos 
        self.lab = lab

    def getLabel(self):
        return self.lab

    def __str__(self):  # override the __str__(self) from class Pos 
        return Pos.__str__(self) + ":" + self.lab

    # static attributes and methods
    def labMerge(points: list):
        return ''.join([x.getLabel() for x in points])

    def dist(p1: Pos, p2: Pos):
        return abs(p1.row - p2.row) + abs(p1.col - p2.col)
