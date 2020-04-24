import numpy

surface = open('primary_surface.sfc', 'w')
surface.write('Tabulated surface for mirror 1 CCAT-prime\n')
### grid limits
surface.write('-3500 -3500 3500 3500\n')
### grid points along axes
# nx, ny = 7001, 7001
nx, ny = 101, 101
surface.write( '%s %s\n' %(nx,ny))

### matrix definition
c = numpy.zeros((7,7))
c[0,2] = -57.74022
c[0,3] =  1.5373825
c[0,4] =  1.154294
c[0,5] = -0.441762
c[0,6] =  0.0906601

c[2,0] = -72.17349
c[2,1] =  1.8691899
c[2,2] =  2.8859421
c[2,3] = -1.026471
c[2,4] =  0.2610568

c[4,0] =  1.8083973
c[4,1] = -0.603195
c[4,2] =  0.2177414

c[6,0] =  0.0394559

R_n    =  3000

index = range(7)
x = numpy.linspace(-3500, 3500, nx)
y = numpy.linspace(-3500, 3500, ny)
xx, yy = numpy.meshgrid(x, y)
zz     = numpy.zeros((nx , ny))
# x_pow = numpy.asarray( ( (x/R_n)**0, (x/R_n)**1, (x/R_n)**2, (x/R_n)**3, (x/R_n)**4, (x/R_n)**5, (x/R_n)**6 ) ) 
# y_pow = numpy.asarray( ( (y/R_n)**0, (y/R_n)**1, (y/R_n)**2, (y/R_n)**3, (y/R_n)**4, (y/R_n)**5, (y/R_n)**6 ) ) 
# xpx, ypy = numpy.meshgrid( x_pow, y_pow )

for xi, xg in enumerate(y.ravel()):
    for yi, yg in enumerate(x.ravel()):
        power_term = 0
        for j in index:
            for i in index:
                power_term += c[i,j] * (xg/R_n)**i * (yg/R_n)**j
         #      print 'xi=%s, yi=%s, i=%s, j=%s' % (xi, yi, i, j)
        zz[xi, yi] = power_term
        surface.write('%f\n' % power_term )
surface.close()
