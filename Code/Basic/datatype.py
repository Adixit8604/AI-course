#integer
a=5
print(a, "is of type", type(a))
a=2.0 
print(a, "is of type", type(a))
a= 1+2j 
print(a, "is of type", type(a))


 
#string
s= "Hello@123"
print(s, type(s))
s='''
Hello
world
'''

print(s)

 

s='10'
print(s, type(s))

 
#list
l=[10,'ws',5.5]
l[2]=10
print(1, type(l))

#tuple
t=(10,20,'hello')
#t[1]=30
print( type(t))
t=(10)
print(t, type(t))

#dictionary
d={
  'course_name':"Python",
  "course_duration":"2 Month"
 }
print(d['course_name'])
print(d,type(d))


#set
s={10,20,30,10}
print(s, type(s))