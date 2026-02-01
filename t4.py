import sys
import numpy
import pdb
llst=[1,2,3,4,5,6,7,8,9]

def loadrows():
   rowa=[8,0,0,0,0,4,6,3,0]
   rowb=[6,0,4,3,0,0,0,1,8]
   rowc=[0,0,0,0,6,8,0,4,0]
   rowd=[0,0,0,9,4,0,1,0,6]
   rowe=[0,0,0,8,3,0,0,5,2]
   rowf=[0,0,7,0,0,0,0,0,3]
   rowg=[0,0,6,4,0,3,0,0,0]
   rowh=[0,5,0,0,8,0,0,6,4]
   rowj=[0,4,8,0,7,0,0,0,0] 
   rowx=[rowa,rowb,rowc,rowd,rowe,rowf,rowg,rowh,rowj]
   return rowx
   
def loadcols(rowx):
   print('   inside loadcols')
   rowa=rowx[0];rowb=rowx[1];rowc=rowx[2];rowd=rowx[3];rowe=rowx[4];
   rowf=rowx[5];rowg=rowx[6];rowh=rowx[7];rowj=rowx[8]
   #pdb.set_trace()
   col1=[rowa[0],rowb[0],rowc[0],rowd[0],rowe[0],rowf[0],rowg[0],rowh[0],rowj[0]]
   col2=[rowa[1],rowb[1],rowc[1],rowd[1],rowe[1],rowf[1],rowg[1],rowh[1],rowj[1]]
   col3=[rowa[2],rowb[2],rowc[2],rowd[2],rowe[2],rowf[2],rowg[2],rowh[2],rowj[2]]
   col4=[rowa[3],rowb[3],rowc[3],rowd[3],rowe[3],rowf[3],rowg[3],rowh[3],rowj[3]]
   col5=[rowa[4],rowb[4],rowc[4],rowd[4],rowe[4],rowf[4],rowg[4],rowh[4],rowj[4]]
   col6=[rowa[5],rowb[5],rowc[5],rowd[5],rowe[5],rowf[5],rowg[5],rowh[5],rowj[5]]
   col7=[rowa[6],rowb[6],rowc[6],rowd[6],rowe[6],rowf[6],rowg[6],rowh[6],rowj[6]]
   col8=[rowa[7],rowb[7],rowc[7],rowd[7],rowe[7],rowf[7],rowg[7],rowh[7],rowj[7]]
   col9=[rowa[8],rowb[8],rowc[8],rowd[8],rowe[8],rowf[8],rowg[8],rowh[8],rowj[8]] 
   colx=[col1,col2,col3,col4,col5,col6,col7,col8,col9]
   return colx
   
def loadsqrs(rowx): 
   rowa=rowx[0];rowb=rowx[1];rowc=rowx[2];rowd=rowx[3];rowe=rowx[4];
   rowf=rowx[5];rowg=rowx[6];rowh=rowx[7];rowj=rowx[8]
   sqr1=[rowa[0],rowa[1],rowa[2],rowb[0],rowb[1],rowb[2],rowc[0],rowc[1],rowc[2]]
   sqr2=[rowa[3],rowa[4],rowa[5],rowb[3],rowb[4],rowb[5],rowc[3],rowc[4],rowc[5]]
   sqr3=[rowa[6],rowa[7],rowa[8],rowb[6],rowb[7],rowb[8],rowc[6],rowc[7],rowc[8]]
   sqr4=[rowd[0],rowd[1],rowd[2],rowe[0],rowe[1],rowe[2],rowf[0],rowf[1],rowf[2]]
   sqr5=[rowd[3],rowd[4],rowd[5],rowe[3],rowe[4],rowe[5],rowf[3],rowf[4],rowf[5]]
   sqr6=[rowd[6],rowd[7],rowd[8],rowe[6],rowe[7],rowe[8],rowf[6],rowf[7],rowf[8]]
   sqr7=[rowg[0],rowg[1],rowg[2],rowh[0],rowh[1],rowh[2],rowj[0],rowj[1],rowj[2]]
   sqr8=[rowg[3],rowg[4],rowg[5],rowh[3],rowh[4],rowh[5],rowj[3],rowj[4],rowj[5]]
   sqr9=[rowg[6],rowg[7],rowg[8],rowh[6],rowh[7],rowh[8],rowj[6],rowj[7],rowj[8]]
   sqrx=[sqr1,sqr2,sqr3,sqr4,sqr5,sqr6,sqr7,sqr8,sqr9]
   return sqrx
   
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


