import cv2

def main():
    print("OpenCV Template Running...")
    img = cv2.imread("assets/image.jpg")
    if img is None:
        print("No sample image found.")
    else:
        gray_sketch, color_sketch = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)

        cv2.imshow("Original", img)
        cv2.imshow("Pencil Sketch (Gray)", gray_sketch)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
