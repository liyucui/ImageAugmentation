import os
import cv2

def resizeImg(list):
    new_list = open(list.replace('annatations', 'Annotation'), 'w')
    with open(list, 'r') as f:
        for label in f.readlines():
            img_dir, img_box = label.split(' ')[0], label.split(' ')[1:]
            if '.JPEG' not in img_dir:
                continue
            else:
                img = cv2.imread(img_dir)
                resizeImg = cv2.resize(img, (640, 480))
                cv2.imwrite(img_dir.replace('001', '002'), resizeImg)
                print('start transform')
            print('end')

def getResizedBox(label):
    pass
if __name__ == '__main__':
    annotation = "/home/lucy/softwares/BBox-Label-Tool-master/annatations.txt"
    resizeImg(annotation)
    # getResizedBox(annotation)