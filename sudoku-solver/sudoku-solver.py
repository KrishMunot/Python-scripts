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
    def insert(self,i,j,data):
        self.maze[i][j]=data
    def formvertices(self):
        for i in range(9):
            b=[]
            for j in range(1,10):
                b+=[[i*9+j,self.maze[i][j-1],'*']]
            self.vertex+=[b]
    def formedges(self):
        abc={1:[11]}
        for i in range(1,82):
            self.edges[i]=[]
            x=(i-1)/9
            y=(i-1)%9
            rem=self.vertex[x][y]
            row=(((i-1)/9)%3)
            r1=(row+1)%3
            r2=(row+2)%3
            r1=r1-row
            r2=r2-row
            c=(y%3)
            c1=(c+1)%3
            c2=(c+2)%3
            c1=c1-c
            c2=c2-c
            for j in range(9):
                self.edges[i]+=[self.vertex[x][j]]
                self.edges[i]+=[self.vertex[j][y]]
            self.edges[i]+=[self.vertex[x+r1][y+c1],self.vertex[x+r1][y+c2],self.vertex[x+r2][y+c1],self.vertex[x+r2][y+c2]]
            self.edges[i].remove(rem)
            self.edges[i].remove(rem)
            self.edges[i].sort()
    def rule1(self):
        for i in range(1,82):
            edge_r=(i-1)/9
            edge_c=(i-1)%9
            possiblities=[]
            for z in self.edges[i]:
                i=z[0]
                row=(i-1)/9
                col=(i-1)%9
                if(self.vertex[row][col][1]!='_'):
                    possiblities+=[self.vertex[row][col][1]]
            remaining=[]
            for j in self.answer:
                if j not in possiblities:
                    remaining+=[j]
            if(len(remaining)==1):
                self.vertex[edge_r][edge_c][1]=remaining[0]
    def callrule1(self):
        a=[]
        for i in range(9):
            b=[]
            for j in range(9):
                b+=[self.vertex[i][j][1]]
            a+=[b]
        self.rule2()
        self.rule1()
        change=0
        for i in range(9):
            for j in range(9):
                if a[i][j]!=self.vertex[i][j][1]:
                    change+=1
        if(change!=0):
            self.callrule1()
    def ispossible(self,ver,num):
        for i in self.edges[ver]:
            z=i[0]
            edge_r=(z-1)/9
            edge_c=(z-1)%9
            if(self.vertex[edge_r][edge_c][1]==num):
                return 0
        return 1
    def rule2(self):
        for i in range(9):
            for ans in self.answer:
                number=0
                index=()
                for j in range(9):
                    if(self.vertex[i][j][1]=='_' and self.ispossible(self.vertex[i][j][0], ans)):
                        number+=1
                        index=(i,j)
                if(number==1):
                    self.vertex[index[0]][index[1]][1]=ans
        for j in range(9):
            for ans in self.answer:
                number=0
                index=()
                for i in range(9):
                    if(self.vertex[i][j][1]=='_' and self.ispossible(self.vertex[i][j][0], ans)):
                        number+=1
                        index=(i,j)
                if(number==1):
                    self.vertex[index[0]][index[1]][1]=ans
        box=[[1,2,3,10,11,12,19,20,21],[4,5,6,13,14,15,22,23,24],[7,8,9,16,17,18,25,26,27],[28,29,30,37,38,39,46,47,48],[31,32,33,40,41,42,49,50,51],[34,35,36,43,44,45,52,53,54],[55,56,57,64,65,66,73,74,75],[58,59,60,67,68,69,76,77,78],[61,62,63,70,71,72,79,80,81]]
        for i in range(1,82):
            curbox=[]
            for k in box:
                if i in k:
                    curbox=k
                    break
            for ans in self.answer:
                number=0
                index=()
                for z in curbox:
                    x=(z-1)/9
                    y=(z-1)%9
                    if(self.vertex[x][y][1]=='_' and self.ispossible(self.vertex[x][y][0], ans)):
                        number+=1
                        index=(x,y)
                if(number==1):
                    self.vertex[index[0]][index[1]][1]=ans
    def rules(self):
        self.callrule1()
        no=0
        print "\nSOLUTION: "
        for i in range(9):
            for j in range(9):
                self.maze[i][j]=self.vertex[i][j][1]
                if(self.maze[i][j]=='_'):
                    no+=1
        if(no==0):
            return
