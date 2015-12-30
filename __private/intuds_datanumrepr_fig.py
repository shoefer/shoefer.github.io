import numpy as np

if False:
  import Image

  im = Image.open("shoefer2015.jpg")
  imsm = im.resize(((im.size[0]/20,im.size[1]/20)))

  print ("Shape: %d,%d" % (imsm.size[0], imsm.size[1]))

  imsm.save("shoefer2015small.png")
  imsmg = imsm.convert('LA')
  imsmg.save("shoefer2015small_gray.png")

  #A = np.asarray(imsmg.getdata()).reshape(imsmg.size[0], imsmg.size[1], 2)

if True:
  import matplotlib.pyplot as plt
  import matplotlib.image as mpimg

  def rgb2gray(rgb):
    return np.clip(np.dot(rgb[...,:3], [0.299, 0.587, 0.144]), 0, 1)

  img = mpimg.imread('shoefer2015small.png')
  gray = rgb2gray(img)    
  plt.imshow(gray, cmap = plt.get_cmap('gray'))
  print gray

  np.savetxt("shoefer2015small_gray.txt", gray)
  np.savetxt("shoefer2015small_gray_round.txt", np.round(gray,3), fmt="%.3f")

  plt.show()