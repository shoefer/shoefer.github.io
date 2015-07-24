import numpy as np
import Image

im = Image.open("shoefer2015.jpg")
imsm = im.resize(((im.size[0]/20,im.size[1]/20)))

print ("Shape: %d,%d" % (imsm.size[0], imsm.size[1]))

imsm.save("shoefer2015small.png")
imsmg = imsm.convert('LA')
imsmg.save("shoefer2015small_gray.png")

A = np.asarray(imsmg.getdata()).reshape(imsmg.size[0], imsmg.size[1], 2)

np.savetxt("shoefer2015small_gray_round.txt", np.round(A[:,:,0]/255.,3).T, fmt="%.3f")
