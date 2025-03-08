import cv2
# Load the image
image_path = r"c:\Users\Lenovo\Downloads\moon_img.png"  
image = cv2.imread(image_path)
image = cv2.resize(image, (600, 600))  
# 1. Convert to Sketch
def convert_to_sketch(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(gray)
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    inverted_blur = cv2.bitwise_not(blurred)
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)
    return sketch
# 2. Convert to Cartoon
def convert_to_cartoon(image):
    # Apply bilateral filter
    smooth = cv2.bilateralFilter(image, 9, 75, 75)
    # Convert to gray and edge detection
    gray = cv2.cvtColor(smooth, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
    )
    # Combine edges and smooth color
    color = cv2.bitwise_and(smooth, smooth, mask=edges)
    return color
# 3. Convert to Watercolor
def convert_to_watercolor(image):
    # Apply bilateral filter repeatedly
    for _ in range(3):
        image = cv2.bilateralFilter(image, 9, 75, 75)
    # Apply median blur
    watercolor = cv2.medianBlur(image, 11)
    return watercolor
# Apply effects
sketch = convert_to_sketch(image)
cartoon = convert_to_cartoon(image)
watercolor = convert_to_watercolor(image)
# Display the results
cv2.imshow("Watercolor", watercolor)
cv2.imshow("Cartoon", cartoon)
cv2.imshow("Sketch", sketch)
cv2.imshow("Original", image)
# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
