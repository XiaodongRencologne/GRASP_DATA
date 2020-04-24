import numpy

surface = open('secondary_surface.sfc', 'w')
surface.write('Tabulated surface for mirror 1 CCAT-prime\n')
### grid limits
surface.write('-3500 -3500 3500 3500\n')
### grid points along axes
# nx, ny = 7001, 7001
nx, ny = 101, 101
surface.write( '%s %s\n' %(nx,ny))

### matrix definition
c = numpy.zeros((8,8))
c[0,2] =  103.90461
c[0,3] =  6.6513025
c[0,4] =  2.8405781
c[0,5] = -0.7819705
c[0,6] = -0.0400483
c[0,7] =  0.0896645

c[2,0] =  115.44758
c[2,1] =  7.3024355
c[2,2] =  5.7640389
c[2,3] = -1.578144
c[2,4] = -0.0354326
c[2,5] =  0.2781226

c[4,0] =  2.9130983
c[4,1] = -0.8104051
c[4,2] = -0.0185283
c[4,3] =  0.2626023

c[6,0] = -0.0250794
c[6,1] =  0.0709672

R_n    =  3000

index = range(8)
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
            #    print 'xi=%s, yi=%s, i=%s, j=%s' % (xi, yi, i, j)
        zz[xi, yi] = power_term
        surface.write('%f\n' % power_term )
surface.close()
