import cv2
a=0
while True:
    a+=8
    print(a)
    file_name = "porco/{}.png".format(a)
    src = cv2.imread(file_name, 1)
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
    b, g, r = cv2.split(src)
    rgba = [b,g,r, alpha]
    dst = cv2.merge(rgba,4)
    cv2.imwrite("semfundo/{}.png".format(a), dst)
