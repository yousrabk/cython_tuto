import matplotlib.pyplot as plt
import time

# import mandelbrot
import pyximport
pyximport.install()
# import python_workshop as mandelbrot
import mandelbrot

t1 = time.clock()
mdl = mandelbrot.comp_mandelbrot( 1024, 768, 4 )
t2 = time.clock()
print("Temps calcul mandelbrot : {} secondes".format(t2-t1))
imgplot = plt.imshow(mdl)
plt.show()
