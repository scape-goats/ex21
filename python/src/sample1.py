import matplotlib.pyplot as plt
import numpy as np

# x : time
x=np.arange(0,100,0.5)

# y : sin
Hz=5.
y=np.sin(2.0*np.pi*(x*Hz)/100)

# graph
plt.plot(x,y)
plt.savefig('test.png')