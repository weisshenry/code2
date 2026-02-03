import sys
import numpy
import pdb
import t7 as TX

MX=9

def getopx(rowx,colx,sqrx):    
   opx= [[0 for j in range(MX)] for i in range(MX)]
   npx= [[0 for j in range(MX)] for i in range(MX)]
   for rw in range(MX):
      for cl in range(MX): 
         for j in range(MX):
            for i in range(MX):
               opx[j][i]=[1,2,3,4,5,6,7,8,9] 
         for item in rowx[rw]:
            if item in opx[cl][rw]:
               opx[cl][rw].remove(item)
         for item in colx[cl]:
            if item in opx[cl][rw]:
               opx[cl][rw].remove(item) 
         if ((cl > -1) and(cl < 3) and (rw > -1))and (rw <3):
            for item in sqrx[0]:
               if item in opx[cl][rw]:      
                  opx[cl][rw].remove(item) 
                  print('   got sqr %d  item %d  (%d,%d)' %(1,item,rw+1,cl+1))
         elif ((cl > 2) and(cl < 6) and (rw > -1))and (rw <3):
            for item in sqrx[1]:
               if item in opx[cl][rw]:      
                  opx[cl][rw].remove(item) 
                  print('   got sqr %d  item %d  (%d,%d)' %(2,item,rw+1,cl+1))
         elif ((cl > 5) and(cl < 9) and (rw > -1))and (rw <3):
            for item in sqrx[2]:
               if item in opx[cl][rw]:      
                  opx[cl][rw].remove(item) 
                  print('   got sqr %d  item %d  (%d,%d)' %(3,item,rw+1,cl+1))
         elif ((cl > -1) and(cl < 3) and (rw > 2))and (rw <6):
            for item in sqrx[3]:
               if item in opx[cl][rw]:      
                  opx[cl][rw].remove(item) 
                  print('   got sqr %d  item %d  (%d,%d)' %(4,item,rw+1,cl+1))
         elif ((cl > 2) and(cl < 6) and (rw > 2))and (rw <6):
            for item in sqrx[4]:
               if item in opx[cl][rw]:      
                  opx[cl][rw].remove(item) 
                  print('   got sqr %d  item %d  (%d,%d)' %(5,item,rw+1,cl+1))
         elif ((cl > 5) and(cl < 9) and (rw > 2))and (rw <6):
            for item in sqrx[5]:
               if item in opx[cl][rw]:      
                  opx[cl][rw].remove(item) 
                  print('   got sqr %d  item %d  (%d,%d)' %(6,item,rw+1,cl+1))
         elif ((cl > -1) and(cl < 3) and (rw > 5))and (rw <9):
            for item in sqrx[6]:
               if item in opx[cl][rw]:      
                  opx[cl][rw].remove(item) 
                  print('   got sqr %d  item %d  (%d,%d)' %(7,item,rw+1,cl+1))
         elif ((cl > 2) and(cl < 6) and (rw > 5))and (rw <9):
            for item in sqrx[7]:
               if item in opx[cl][rw]:      
                  opx[cl][rw].remove(item) 
                  print('   got sqr %d  item %d  (%d,%d)' %(8,item,rw+1,cl+1))
         elif ((cl > 5) and(cl < 9) and (rw > 5))and (rw <9):
            for item in sqrx[8]:
               if item in opx[cl][rw]:      
                  opx[cl][rw].remove(item) 
                  print('   got sqr %d  item %d  (%d,%d)' %(9,item,rw+1,cl+1))
         
         
         npx[cl][rw] = opx[cl][rw]             
   return npx
 
if __name__ == "__main__":
   sel= 0;print('   Startx %d ' %(sel))
   rowx= TX.loadrows(); colx= TX.loadcols(rowx);
   sqrx= TX.loadsqrs(rowx) 
   npx = getopx(rowx,colx,sqrx) 
   print('   Col1 RowC'); print(npx[0][2])  
   print('   Col6 RowB'); print(npx[5][1])  
   #pdb.set_trace()
   print('   End') 
   sys.exit()
   
   
   
   
