import cv2, os, time
from subprocess import call, STDOUT, check_output

def change_png():
    vidcap = cv2.VideoCapture("./test.mp4")
    temp_folder = "/home/younsle/workspace/CTF/christmasCTF/web/tmp_png"

    count = 0
    while True:
        sucess, image = vidcap.read()
        if not sucess:
            break
        cv2.imwrite(os.path.join(temp_folder, "{:d}.png".format(count)), image)
        count+=1

def check_png():
    for i in range(0, 14315):
        # call(["pngcheck", "{n}.png".format(n=i)], stdout=open(os.devnull, "w"), stderr=STDOUT)
        data = check_output(["pngcheck", "{n}.png".format(n=i)])
        # time.sleep(1)
        print(data)

def main():
    check_png()

if __name__ == "__main__":
    main()



