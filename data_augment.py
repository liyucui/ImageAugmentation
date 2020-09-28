import os
import cv2

import random
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance


def modify_file_path(img_path, middle_name):
    (img_path, tmpFileName) = os.path.split(img_path)
    (fileName, extension) = os.path.splitext(tmpFileName)
    fileName = fileName + '_'+middle_name+extension
    file_path = os.path.join(img_path, fileName)
    return file_path


def saveFlipedBoxes(box):
    width = 640
    box =np.array(box.split(' '), dtype=np.float32).reshape(-1, 4)
    new_boxes = ''
    for i in range(box.shape[0]):
        x1 = int(box[i][0])
        y1 = int(box[i][1])
        x2 = int(box[i][2])
        y2 = int(box[i][3])

        if i == 0:
            loc = '%s %s %s %s'%(str(width-x2), str(y1), str(width-x1), str(y2))
        else:
            loc = ' %s %s %s %s'%(str(width-x2),str(y1), str(width-x1), str(y2))
        new_boxes += loc
    return new_boxes
def horizontalFlip(img_path, box):
    middle_name = 'Hor'
    new_file_path = modify_file_path(img_path, middle_name)
    print(new_file_path)
    img = Image.open(img_path).convert('RGB')
    img.transpose(Image.FLIP_LEFT_RIGHT).save(new_file_path)
    flipedBoxes = saveFlipedBoxes(box)
    new_list_dir.write(new_file_path+' '+flipedBoxes+'\n')


def colorJitterring(img_path, jitterring_type, jitterring_class):
    img = Image.open(img_path).convert('RGB')
    i = 0
    for j_class in jitterring_class:
        middle_name = jitterring_type[i]
        new_file_path = modify_file_path(img_path, middle_name)
        if i < 8:
            img.filter(j_class).save(new_file_path)
        else:
            factor = [np.random.randint(8, 16) / 10, np.random.randint(8, 16) / 10, np.random.randint(5, 15)/10, np.random.randint(8, 12)/10]
            j_class(img).enhance(factor[i-8]).save(new_file_path)
        i += 1

def process_data(img_full_path, box):
    horizontalFlip(img_full_path, box)
    # 高斯模糊, 普通模糊, 边缘增强, 找到边缘, 浮雕, 轮廓, 锐化, 平滑, 细节, 亮度增强, 对比度增强, 颜色增强,
    jitterring_type = ['GaussianBlur', 'BLUR', 'EdgeEnhance', 'FindEdges', 'EMBOSS',
                       'SHARPEN', 'SMOOTH', 'DETAIL', 'BrightnessEnhance', 'ColorEnhance',
                       'ContrastEnhance', 'SharpEnhance']
    jitterring_class = [ImageFilter.GaussianBlur, ImageFilter.BLUR, ImageFilter.EDGE_ENHANCE, ImageFilter.FIND_EDGES,
                        ImageFilter.EMBOSS, ImageFilter.SHARPEN, ImageFilter.SMOOTH,
                        ImageFilter.DETAIL, ImageEnhance.Brightness, ImageEnhance.Color,
                        ImageEnhance.Contrast, ImageEnhance.Sharpness]
    colorJitterring(img_full_path, jitterring_type, jitterring_class)

def process_train_set(list_dir):
    with open(list_dir, 'r+') as flist:
        read_data = flist.read()
        flist.truncate() #清空文件
        img_count = 0
        for eachline in read_data.split('\n'):
            img_count += 1
            img_path = eachline.split(' ')[0]
            label = eachline.split(' ')[1:]
            box = ''
            for i in range(len(label)):
                if i == 0:
                    box = box + '%s'%str(label[i])
                else:
                    box = box + ' %s'%str(label[i])
            img_full_path = os.path.join(img_path)
            print(img_full_path)

            # 如果文件不存在, 直接跳过
            if(os.path.exists(img_full_path) == False):
                continue
            process_data(img_full_path, box)



if __name__ == '__main__':
    list_dir = "/home/lucy/softwares/BBox-Label-Tool-master/annatations.txt"
    new_list_dir = open(list_dir.replace('annatations', 'newAnnatations'), 'w')
    process_train_set(list_dir)