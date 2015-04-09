__author__ = 'U269074'

print ("Welcome to Klara's calculator!")

x = int(raw_input("Definiraj prvo stevilko"))
y = float(raw_input("Definiraj drugo stevilko"))

z = raw_input("Izberi racunsko operacijo (sestevanje/odstevanje/mnozenje/deljenje/potenciranje")

if z =="sestevanje":
    b = x + y
    print "sestevek je " + str(b)
elif z=="odstevanje":
    print x-y
elif z=="mnozenje":
    print x * y
elif z=="deljenje":
    print x/y
elif z=="potenciranje":
    print x**y
else:
     print("Slabe izbire")