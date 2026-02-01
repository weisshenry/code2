import sys
import numpy
import pdb
import t3
llst=[1,2,3,4,5,6,7,8,9]

def getopx(opx,rowx,colx,sqrx):   
   opnn=llst
   for item in rowx:
      if item in opnn:
         opnn.remove(item)
   for item in colx:
      if item in opnn:
         opnn.remove(item) 
   for item in sqrx:
      if item in opnn:
         opnn.remove(item) 
   return opnn

if __name__ == "__main__":
   print('   Startx') 
   rowa,rowb,rowc,rowd,rowe,rowf,rowg,rowh,rowj= t3.loadrows()   
   col1,col2,col3,col4,col5,col6,col7,col8,col9= t3.loadcols(rowa,\
       rowb,rowc,rowd,rowe,rowf,rowg,rowh,rowj)
   sqr1,sqr2,sqr3,sqr4,sqr5,sqr6,sqr7,sqr8,sqr9= t3.loadsqrs(rowa,\
       rowb,rowc,rowd,rowe,rowf,rowg,rowh,rowj)                    
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
   print(rowa)
   print(col1)
   print(sqr1)
   opnn = getopx(opx,rowa,col1,sqr1)
   print('   open lst')
   print(opnn)
   
   print('   End') 
   sys.exit()
