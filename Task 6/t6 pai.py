import cv2
import numpy as np

image = cv2.imread('C:/Users/Sami/Desktop/Task 6/Sunflower_from_Silesia2.jpg') 

mask = np.zeros(image.shape[:2], np.uint8)

rect = (10, 10, image.shape[1]-10, image.shape[0]-10)  

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

result = image * mask2[:, :, np.newaxis]

cv2.imshow('Background Removed', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('output_removed_bg.jpg', result)
print("Image saved as output_removed_bg.jpg")
