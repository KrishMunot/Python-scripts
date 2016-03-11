class sudoku:
    def __init__(self):
        self.maze=[]
        self.color=[]
        self.maxcolor=1
        self.vertex=[]
        self.answer=[1,2,3,4,5,6,7,8,9]
        self.edges={}
        for i in range(0,9):
            self.maze+=[['_','_','_','_','_','_','_','_','_']]           
        file=open("test.txt")
