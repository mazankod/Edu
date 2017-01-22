import math

x = input('input x= ')
figure = input('figure is :')
try:
    x = int(x)
    figure = str(figure)
except:
    print "error "
    exit(1)
if x <= 0:
    print 'error'
    exit(1)
# elif figure!=('squre','circle'):
#     print 'error figure is %s or x is below zero %s' % (figure, x)
#     exit(1)
if figure == 'square':
    S = x * x
elif figure == 'circle':
    S = math.pi * x * x
else:
    print 'error'
    exit(1)
print "The area is %.2f" % S
exit(0)
