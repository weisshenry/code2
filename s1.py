import sys
import numpy

rowa=[8,0,0,0,0,4,6,3,0]
rowb=[6,0,4,3,0,0,0,1,8]
rowc=[0,0,0,0,6,8,0,4,0]
rowd=[0,0,0,9,4,0,1,0,6]
rowe=[0,0,0,8,3,0,0,5,2]
rowf=[0,0,7,0,0,0,0,0,3]
rowg=[0,0,6,4,0,3,0,0,0]
rowh=[0,5,0,0,8,0,0,6,4]
rowj=[0,4,8,0,7,0,0,0,0]
col1=[rowa[0],rowb[0],rowc[0],rowd[0],rowe[0],rowf[0],rowg[0],rowh[0],rowj[0]]
col2=[rowa[1],rowb[1],rowc[1],rowd[1],rowe[1],rowf[1],rowg[1],rowh[1],rowj[1]]
col3=[rowa[2],rowb[2],rowc[2],rowd[2],rowe[2],rowf[2],rowg[2],rowh[2],rowj[2]]
col4=[rowa[3],rowb[3],rowc[3],rowd[3],rowe[3],rowf[3],rowg[3],rowh[3],rowj[3]]
col5=[rowa[4],rowb[4],rowc[4],rowd[4],rowe[4],rowf[4],rowg[4],rowh[4],rowj[4]]
col6=[rowa[5],rowb[5],rowc[5],rowd[5],rowe[5],rowf[5],rowg[5],rowh[5],rowj[5]]
col7=[rowa[6],rowb[6],rowc[6],rowd[6],rowe[6],rowf[6],rowg[6],rowh[6],rowj[6]]
col8=[rowa[7],rowb[7],rowc[7],rowd[7],rowe[7],rowf[7],rowg[7],rowh[7],rowj[7]]
col9=[rowa[8],rowb[8],rowc[8],rowd[8],rowe[8],rowf[8],rowg[8],rowh[8],rowj[8]]
sqx1=[rowa[0],rowa[1],rowa[2],rowb[0],rowb[1],rowb[2],rowc[0],rowc[1],rowc[2]]


if __name__ == "__main__":
   print('   Start') 
   a = 3.14
   b= a*a
   print('   b %.2f \b' %(b))
   print(rowa)
   print(col5)
   print(sqx1)
   print('   End') 
   sys.exit()
