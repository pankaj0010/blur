import numpy as np
import matplotlib.pyplot as plt

# Load image from file
imageMatrix = plt.imread('children.jpg')
iLen=imageMatrix.shape[0]
iWid=imageMatrix.shape[1]
blurredImageMatrix = np.zeros((iLen,iWid,3), dtype=np.uint8)

# Blur Function
kernelSize=7	# Increase kernelSize to increase blur effect (keep odd number)
pad=int(kernelSize/2)
imageMatrix=np.pad(imageMatrix,[(pad,),(pad,),(0,)], mode='constant')	# Padding to handle borders
kernel=np.random.rand(kernelSize,kernelSize)
for i in range(0,iLen):
	for j in range(0,iWid):
		for k in range (0,3):
			blurredImageMatrix[i,j,k]=(imageMatrix[i:i+kernelSize,j:j+kernelSize,k]*kernel).sum()/kernel.sum()

# Image plots to show contrast
plt.subplot(1,2,1)
plt.tick_params(
	axis='both',      	 # changes apply to both x and y-axis
	which='both',     	 # both major and minor ticks are affected
	bottom='off',     	 # ticks along the bottom edge are off
	top='off',       	 # ticks along the top edge are off
	left='off',			 # ticks along the left edge are off
	right='off',		 # ticks along the right edge are off
	labelleft='off',	 # labels along the left edge are off
	labelbottom='off')   # labels along the bottom edge are off
plt.imshow(imageMatrix)
plt.title("Original Image")

plt.subplot(1,2,2)
plt.tick_params(
	axis='both',      	 # changes apply to both x and y-axis
	which='both',     	 # both major and minor ticks are affected
	bottom='off',     	 # ticks along the bottom edge are off
	top='off',       	 # ticks along the top edge are off
	left='off',			 # ticks along the left edge are off
	right='off',		 # ticks along the right edge are off
	labelleft='off',	 # labels along the left edge are off
	labelbottom='off')   # labels along the bottom edge are off
plt.imshow(blurredImageMatrix)
plt.title("Blurred Image")

plt.show()
