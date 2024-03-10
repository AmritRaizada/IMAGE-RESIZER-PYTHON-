import cv2
#configurable parameters
source="1698649366707.jpeg"
destination="Image-resized.jpg"
scale_percent = int(input("Enter Scale Down% : "))

src = cv2.imread('1698649366707.jpg', cv2.IMREAD_UNCHANGED)
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# resize image
output = cv2.resize(src, (width, height))
cv2.imwrite('Image-resized.jpg', output)
cv2.waitKey(0)