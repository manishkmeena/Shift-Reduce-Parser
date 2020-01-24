pMat={'+':{'+':'<','*':'<','id':'<','$':'>'},
	  '*':{'+':'>','*':'>','id':'<','$':'>'},
	  'id':{'+':'>','*':'>','id':'e1','$':'>'},
	  '$':{'+':'<','*':'<','id':'<','$':'accept'}}

#print(pMat['+'])


E=['E+E','E*E','id']

stack=['$']
inputStr='id+id*id$'

inputBuff=[]
ip=0
for lap in range(ip+1,len(inputStr)):
	if(inputStr[ip:lap]=='id' or inputStr[ip:lap]=='+' or inputStr[ip:lap]=='*'):
		print(inputStr[ip:lap])
		inputBuff.append(inputStr[ip:lap])
		ip=lap
inputBuff.append("$")

print(inputBuff)


stackTop=stack[-1]
for i in inputBuff:
	#print(i)
	if(pMat[stackTop][i]=='<'):
		
	