print("Compound Expressions")


#Expressions can includes multiple expressions
print(25+7+2002)
print(30-2+3)

# Operator Precedence
print(7+3*5) # according to BODMAS rule multiplication have high precedence so 
print(3*5,"Step 1")
print(15+7,"Step 2")

print(5.5*6//2+8) 
print(6//2)
print(5.5*3)
print(16.5+8)
print(6//2*5.5+8)
# ?in python it works with BOIDMAS but while its coming to precedence for some operators it has left to right so for line 13 
# according our BODMAS rule we calculate floordivison then multiplication then additon but in python its to L-to-R precedence
# so additon firstly mutliplication then floor divison then only addition
print(2*3//6//1*10**2)



# Using parentheses to change evaluation order
print((7+3)//5)
print(5.5 * ((6//2) + 8))
print((-3) ** 2)