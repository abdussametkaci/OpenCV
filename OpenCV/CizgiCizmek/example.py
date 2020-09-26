import cv2
import numpy as np

def main():
    resim = np.zeros((600, 600, 3), dtype="uint8")
    resim.fill(255)

    cv2.circle(resim, (300, 300), 100, (0, 255, 0), 2)
    cv2.rectangle(resim, (200, 400), (400, 200), (255, 0, 0), 2)
    cv2.line(resim, (200, 200), (400, 400), (0, 0, 255), 2)
    cv2.line(resim, (200, 400), (400, 200), (0, 0, 255), 2)
    cv2.line(resim, (200, 300), (400, 300), (0, 0, 255), 2)
    cv2.putText(resim, "Hello World!", (200, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

    cv2.imshow("Resim", resim)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()