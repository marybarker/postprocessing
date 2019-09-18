from sympy import sin,cos
from sympy.physics.vector import ReferenceFrame, curl
R = ReferenceFrame('R')

'''
v = sin(R[0])*cos(R[1])*cos(R[2])*R.x + sin(R[0])*sin(R[1])*cos(R[2])*R.y + sin(R[0])*sin(R[1])*sin(R[2])*R.z
print('\ncurl V = ', curl(v, R))
w = curl(v, R)
print('\ncurl curl V = ', curl(w, R), '\n')
'''



#v = sin(R[0])*sin(R[1])*R.x + sin(R[1])*sin(R[2])*R.y + sin(R[0])*sin(R[2])*R.z
v = sin(R[1])*sin(R[2])*R.x + sin(R[0])*sin(R[2])*R.y + sin(R[0])*sin(R[1])*R.z
print('\nV = ', v)
print('\ncurl V = ', curl(v, R))
w = curl(v, R)
print('\ncurl curl V = ', curl(w, R), '\n')
