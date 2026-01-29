import sys
import numpy
import pdb
import t3


if __name__ == "__main__":
   print('   Startx') 
   rowa,rowb,rowc,rowd,rowe,rowf,rowg,rowh,rowj= t3.loadrows()
   pdb.set_trace()
   col1,col2,col3,col4,col5,col6,col7,col8,col9= t3.loadcols(rowa,\
       rowb,rowc,rowd,rowe,rowf,rowg,rowh,rowj)
   sqr1,sqr2,sqr3,sqr4,sqr5,sqr6,sqr7,sqr8,sqr9= t3.loadsqrs(rowa,\
       rowb,rowc,rowd,rowe,rowf,rowg,rowh,rowj)                    
   print('   Row A:')
   print(rowa)
   print('   Col 5')   
   print(col5)
   print('   Sqr 1')
   print(sqr1)
   print('   Sqr 8')
   print(sqr8)   
   print('   Stage2: calc all open numbs')  
   rows = 9;  cols = 9
   # Initializes a 3x4 list with all elements set to 0
   opx= [[0 for j in range(cols)] for i in range(rows)]
   print(my_2d_list)
   
   print('   End') 
   sys.exit()
