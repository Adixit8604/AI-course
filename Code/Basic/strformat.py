#named indexes:
txtl = "Welcome to {fname} {lname}".format(fname = "WsCube", lname = "Tech")
#numbered indexes:

txt2 = "Welcome to {0} {1}".format("WsCube","Tech")
#empty placeholders:

txt3 = "Welcome to {} {}".format("WsCube","Tech") 


print(txtl)
print(txt2)
print(txt3)

 
w="Welcome {} to {} Wscubetech".format("hello",20);
print(w)

w="Welcome {1} to {0} Wscubetech".format("hello", 20);
print(w)

w="Welcome to Wscubetech". format (30,40)
print(w)