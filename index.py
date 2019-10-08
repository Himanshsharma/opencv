import cv2
# to read a photo 
a=cv2.imread('jj.jpg',1)
b=cv2.imread('jj.jpg',0)
c=cv2.imread('jj.jpg',-1)
# to resize the image
res=cv2.resize(a,(650,500))
cv2.imshow("him",res)
cv2.waitKey(5600)
cv2.destroyAllWindows()