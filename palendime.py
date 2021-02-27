def IsPal(s):
	return s == s[::-1]


s = input("Enter Word: ")
s = s.lower()
ans = IsPal(s)

if ans:
	print("Yes")
	print(s)
else:
	print("No")
	print(s)
