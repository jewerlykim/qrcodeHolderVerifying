import time
import cv2
from matplotlib import pyplot as plt
import sys


usual = cv2.imread('./assets/usual.jpg')
collex = cv2.imread('./assets/collex.jpg')
dogesoundclub = cv2.imread('./assets/dogesoundclub.jpg')
krbc = cv2.imread('./assets/krbc.jpg')
metakongz = cv2.imread('./assets/metakonz.jpg')
toxicape = cv2.imread('./assets/toxicape.jpg')


# b, g, r = cv2.split(usual)
# image2 = cv2.merge([r, g, b])

# plt.imshow(image2)
# time.sleep(5)

# sys.exit(0)


k = 0
walletaddress = "0x0000000000000000000000000000000000000000"
cv2.imshow('image', usual)

while k != 27:
    print("init")

    if k == ord('s') and walletaddress == "0x0000000000000000000000000000000000000000":
        cv2.imshow('image', collex)

        print("dddd")
    elif k == ord('d') and walletaddress == "0x0000000000000000000000000000000000000000":
        cv2.imshow('image', dogesoundclub)

        print("dddd")
    else:
        cv2.imshow('image', usual)

        print("dddd")

    k = cv2.waitKey(5000)

cv2.destroyAllWindows()

# cv2.imshow('image', usual)
# while True:

#     cv2.imshow("Sheep", usual)
#     keycode = cv2.waitKey(0)
#     if keycode == ord('c') or keycode == ord('C'):
#         cv2.imshow("Sheep", collex)
#     elif keycode == 27:
#         break
# elif cv2.waitKey(1) and 0xFF == ord('d'):
#     cv2.imshow("Sheep", dogesoundclub)
# elif cv2.waitKey(1) and 0xFF == ord('k'):
#     cv2.imshow("Sheep", krbc)
# elif cv2.waitKey(1) and 0xFF == ord('m'):
#     cv2.imshow("Sheep", metakongz)
# elif cv2.waitKey(1) and 0xFF == ord('t'):
#     cv2.imshow("Sheep", toxicape)
# else:
#     cv2.imshow("Sheep", usual)
# sys.exit()  # to exit from all the processes


cv2.destroyAllWindows()
