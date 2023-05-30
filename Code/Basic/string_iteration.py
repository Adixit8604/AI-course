w="welcome to world"
#w=w[-1::-1]
t=len(w)
print(t)

for i in range(t):
    print(w[i])

for i in range(t-1,-1,-1):
    print(w[i])

for i in w:
    print(i)
print("\n")
for i in w[-1::-1]:
    print(i)