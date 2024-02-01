import cv2

source= "dmsyll.jpg"
destination= "newdmchotasyll.jpg"
scale_percent= 10

src= cv2.imread(source, cv2.IMREAD_UNCHANGED )

new_width= int(src.shape[1] * scale_percent/100)
new_height= int(src.shape[0]* scale_percent/100)

output= cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
cv2.waitKey(0)


'''

cv2 is the module name for OpenCV (Open Source Computer Vision Library) in Python. It provides a vast 
collection of functions and algorithms for real-time computer vision tasks

Read, write, and display images and videos (e.g., cv2.imread(), cv2.imshow(), cv2.VideoCapture())
Resize, crop, rotate, and transform images (e.g., cv2.resize(), cv2.warpAffine())
Apply filters and effects (e.g., blurring, sharpening, edge detection, color transformations)
Convert between different image formats (e.g., RGB, grayscale, HSV)


cv2.imread_unchanged is a method in OpenCV that reads an image file while preserving its original color channels and transparency information (alpha channel). It's specifically useful for working with images that have transparency, such as PNG or TIFF files with alpha channels.


Alpha channels are like magic cloaks for pixels in digital images. They control the visibility of those pixels, allowing you to make them completely transparent, partially transparent, or fully opaque. This ability to adjust transparency comes in handy for a variety of purposes in graphics and design.

'''