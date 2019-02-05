OPERATER={1:"+",2:"-",3:"*",4:"/"}
flag=False
def  cal(a,b,action):
	a=float(a)
	b=float(b)
	if action=="+":
		return a+b
	if action=="-":
		return a-b
	if action == '*':
		return a*b
	if  action =='/':
		if b==0:
			return 0
		else:
			return a/b	
			


def calculate(a,b,c,d):
	global OPERATER
	global flag
	for i in range(1,5):
		final1=cal(a,b,OPERATER[i])
		for j in range(1,5):
			final2=cal(final1,c,OPERATER[j])
			final4=cal(c,d,OPERATER[j])
			final7=cal(c,final1,OPERATER[j])
			for k in range(1,5):
				final3=cal(final2,d,OPERATER[k])
				final5=cal(final1,final4,OPERATER[k])
				final6=cal(d,final2,OPERATER[k])
				final8=cal(final7,d,OPERATER[k])
				final9=cal(d,final7,OPERATER[k])				
				if final3==24 and flag==False:
					print "((",a,OPERATER[i],b,")",OPERATER[j],c,")",OPERATER[k],d,"=",final3
					flag=True
					return 0
				if final5==24 and flag==False:
					print "(",a,OPERATER[i],b,")",OPERATER[k],"(",c,OPERATER[j],d,")=",final5
					flag=True
					return 0
				if final6==24 and flag==False:
					print d,OPERATER[k],"((",a,OPERATER[i],b,")",OPERATER[j],c,")=",final6
					flag=True
					return 0
				if final8==24 and flag==False:
					print "(",c,OPERATER[j],"(",a,OPERATER[i],b,"))",OPERATER[k],d,"=",final8
					flag=True
					return 0
				if final9==24 and flag==False:
					print d,OPERATER[k],"(",c,OPERATER[j],"(",a,OPERATER[i],b,"))=",final9
					flag=True
					return 0



def main():
	global flag
	isflag=False
	while isflag==False:
		flag=False
		a,b,c,d=map(int,raw_input("please input four integers:").split(','))
		INTEGER={0:a,1:b,2:c,3:d}
		if a==0 and b==0 and c==0 and d==0:
			isflag=True
		for i in range(1,5):
			calculate(INTEGER[(i+1)%4],INTEGER[(i+2)%4],INTEGER[(i+3)%4],INTEGER[(i+4)%4])
			calculate(INTEGER[(i+1)%4],INTEGER[(i+2)%4],INTEGER[(i+4)%4],INTEGER[(i+3)%4])
			calculate(INTEGER[(i+1)%4],INTEGER[(i+3)%4],INTEGER[(i+2)%4],INTEGER[(i+4)%4])
			calculate(INTEGER[(i+1)%4],INTEGER[(i+3)%4],INTEGER[(i+4)%4],INTEGER[(i+2)%4])
			calculate(INTEGER[(i+1)%4],INTEGER[(i+4)%4],INTEGER[(i+3)%4],INTEGER[(i+2)%4])
			calculate(INTEGER[(i+1)%4],INTEGER[(i+4)%4],INTEGER[(i+2)%4],INTEGER[(i+3)%4])
		if flag==False:
			print "no answer"

                    

if __name__ == '__main__':
	main()

