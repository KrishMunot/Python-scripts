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
        count=0
        for i in file.readlines():
            count1=0
            s=i.split()
            for j in s:
                if(j!='_'):
                    j=int(j)
                self.maze[count][count1]=j
                count1+=1
            count+=1
        self.formvertices()
        self.formedges() 
    def printmaze(self):
        for i in range(0,9):
            if(i%3==0):
                print"-------------------------"
            for j in range(0,9):
                if(j%3==0):
                    print '|',
                print self.maze[i][j],
            print '|'
        print"-------------------------"
