"""
# count()
t = (10, 20, 10, 30, 10)

print(t.count(10))   # Output: 3
print(t.count(40))   # Output: 0
"""
#index()
t = (10,20,30,40)
print(t.index(30)) # output:2  
 
print(t.index(50)) # valueError 

# tuple does not support these methods
t = (10,20,30)
t.append(40)