def push(s,e):
	s.append(e)
def pop(s):
	if len(s):
		return s.pop()
	else:
		print("Stack is empty!!!")
def peek(s):
	return s[-1]
def show(s):
	#for i in range(-1,-len(s)-1,-1):
	#	print(s[i])
	if len(s):
		for i in s[::-1]:
			print(i)
	else:
		print("Stack is empty!!!")
		
s=[]

while True:
	print("1. Push")
	print("2. Pop")
	print("3. Peek")
	print("4. Show")
	print("5. Exit")

	ch=int(input("Enter choice : "))

	if ch==1:
		e=int(input("Enter element : "))
		push(s,e)
	elif ch==2:
		print("popped element : ",pop(s))
	elif ch==3:
		print("element at top is : ",peek(s))
	elif ch==4:
		show(s)
	elif ch==5:
		break
	else:
		print("bawla ho gaya kya")