#calc1   calc of sudoko posSet after read of values
import sys
import numpy 
import pdb
import aux1 as TX

 
if __name__ == "__main__":
   sel= 0;print('   Startx %d ' %(sel))
   print('   Load rows, calc cols, and sqrs')
   print('   Calc posSet for each box - grades.txt')
   rowx= TX.loadrows(); colx= TX.loadcols(rowx);
   sqrx= TX.loadsqrs(rowx) 
   npx = TX.getopx(rowx,colx,sqrx) 
   #print('   Col1 RowC'); print(npx[0][2])     
   #pdb.set_trace()
   f1 = open('./grades.txt','w')
   for mx in range(9):
      for lx in range(9):
         for gx in npx[mx][lx]:
            f1.write('%s' %(gx))
         f1.write(', ') 
      f1.write('\n')    
   f1.close()   
   print('   End') 
   sys.exit()
   
   
   
   
