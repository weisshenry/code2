import sys
import numpy
import pdb
import t4
llst=[1,2,3,4,5,6,7,8,9]

def getopxx(rowx,colx,sqrx):
   opnxx= [[0 for j in range(9)] for i in range(9)]
   for j in range(9):
      for i in range(9):
         opnxx[j][i]=llst
   for j in range(9):
      for i in range(9):
         for item in rowx[i]:
            if item in opnxx[j][i]:
               opnxx[j][i].remove(item)
         for item in colx[j]:
            if item in opnxx[j][i]:
               opnxx[j][i].remove(item)
   return opnxx            
               

if __name__ == "__main__":
   print('   Startx') 
   rowx= t4.loadrows()   
   colx= t4.loadcols(rowx)
   sqrx= t4.loadsqrs(rowx) 
   rowa=rowx[0];rowb=rowx[1];rowc=rowx[2];rowd=rowx[3];rowe=rowx[4];
   rowf=rowx[5];rowg=rowx[6];rowh=rowx[7];rowj=rowx[8]
   col1=colx[0];col2=colx[1];col3=colx[2];col4=colx[3];col5=colx[4];
   col6=colx[5];col7=colx[6];col8=colx[7];col9=colx[8]
   sqr1=sqrx[0];sqr2=sqrx[1];sqr3=sqrx[2];sqr4=sqrx[3];sqr5=sqrx[4];
   sqr6=sqrx[5];sqr7=sqrx[6];sqr8=sqrx[7];sqr9=sqrx[8];
   print('   Row A');   print(rowa)
   print('   Col 5');   print(col5)
   print('   Sqr 1');   print(sqr1)
   print('   Sqr 8');   print(sqr8)   
   print('   Stage2: calc all open numbs')  
   rows = 9;  cols = 9; llst=[1,2,3,4,5,6,7,8,9]
   # Initializes a 3x4 list with all elements set to 0
   opx= [[0 for j in range(cols)] for i in range(rows)]
   for j in range(cols):
      for i in range(rows):
         opx[j][i]=llst
   #print(opx)
   print(rowa);   print(col1);   print(sqr1)
   opnn = t4.getopx(opx,rowa,col1,sqr1)
   print('   open lst')
   print(opnn)
   opnxx = getopxx(rowx,colx,sqrx)
   print('   opnxx 1,1  and 3,3 ')
   print(opnxx[1][1])
   print('   End') 
   sys.exit()
