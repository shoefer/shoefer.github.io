import numpy as np
import matplotlib.pylab as plt
from matplotlib import animation
import numpy.random

t = 10000*np.array([40, 50, 60, 80, 100])
f = lambda t: 0.00013*t + 70

T = 10000*np.array([-1000, 1000])
x = f(T)
# guess line


fig = plt.figure()

def plot_gt():

  #plt.plot(T, x, lw=2.0, ls="--", color="b", alpha=0.5)
  xlim, ylim = plt.xlim(), plt.ylim()
  plt.scatter(t, f(t), s=100, color="b", alpha=0.8, label="training examples")
  plt.xlabel("annual revenue")
  plt.ylabel("stock price")
  
  return xlim, ylim

best_x = None
best_me = 0

def animate(nframe):
  print "Animate %d" % nframe
  #if nframe > 0:
  plt.cla()
      
  xlim, ylim = plot_gt()      
  sl = 0.002*numpy.random.random()-0.001
  bi = 35*numpy.random.random()+50
  print sl
  print bi
  g = lambda t: sl*t + bi
  #g = lambda t: 0.00013*t + 70+nframe

  xx = g(T)
  plt.plot(T, xx, lw=5.0, color="r", alpha=0.5, label="current guess")

  me = np.sum( [ np.abs(g(_t)-f(_t)) for _t in t ] )

  global best_x, best_me
  if best_x is not None:
    plt.plot(T, best_x, lw=2.5, color="g", alpha=0.5,label="best guess")

  if best_x is None or me < best_me:
    best_me = me
    best_x = xx

  print me
  
  plt.text(5e5, 30, "Current error: %.2f" % me, fontsize=15, color='red',)
  plt.text(5e5, 50, "Best error:    %.2f" % best_me, fontsize=15, color='green',)

  plt.text(5e4, 450, "Attempt: %d" % (nframe+1))
    

  plt.xlim([0, 1e6])
  plt.ylim([0, 500])
  
  plt.legend()
  
  if nframe == 5:
    plt.savefig("random_guess_animation.png")

#-----------------------
# initial figure explaining accumulated error
if True:
  plt.cla()

  xlim, ylim = plot_gt()      
  #ff = lambda t: 0.0005*t + 46
  ff = lambda t: 0.00015*t + 58

  plt.plot(T, ff(T), lw=3.0, color="r", alpha=0.5, label="current guess")
  for t_ in t:
    plt.plot([t_, t_], [f(t_), ff(t_)], ls="--", lw=2.0, color='r', alpha=0.5) 
#     print f(t_)
#     print ff(t_)
#     print np.abs(f(t_) - ff(t_))
    plt.text(1.03*t_, 1.01*f(t_), "%d" % np.abs(f(t_) - ff(t_)), fontsize=12)

  me = np.sum( [ np.abs(ff(_t)-f(_t)) for _t in t ] )
  plt.text(6e5, 100, "Summed training error = %d" % me, fontsize=15, color='red',)
  print me

  plt.xlim([3*1e5, 11*1e5])
  plt.ylim([50, 700])
  plt.legend()

  plt.savefig("random_guess_training_error.png")
  plt.show()
  import sys
  sys.exit()

#-----------------------
# animation
anim = animation.FuncAnimation(fig, animate, frames=100)
anim.save('random_guess_animation.gif', writer='imagemagick', fps=10,) #extra_args=['-loop','0'])

#plt.show()