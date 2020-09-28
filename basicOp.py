# -*- coding=utf-8 -*-
###########################
# description:
#   common ops including ① rename a specified file ② delete a specified file ③ move a file to a specified directory
# author:
#   liyucui @ 2020-06-03

import os
import shutil

# 对img_path文件夹中的图片进行重命名
def renameImage():
    img_path = ""
    img_list = os.listdir(img_path)
    for i in range(len(img_list)):
        srcFile = os.path.join(img_path, img_list[i])
        dstFile = os.path.join(img_path, img_list[i].replace('old', 'new'))
        os.rename(srcFile, dstFile)
    print('end')
# 删除文件夹中图片名有特定字母的图片
def deleteImg():
    img_path = ""
    for img in os.listdir(img_path):
        if "letter" in img:
            to_delete_img = os.path.join(img_path, img)
            os.rename(to_delete_img)
    print("end")
# 将src_path文件夹中与dst_path内文件名不重复的文件复制到dst_path
def copyImage():
    dst_path = ""
    src_path = ""
    dst_img = os.listdir(dst_path)
    for src_img in os.listdir(src_path):
        if src_img not in dst_img:
            from_path = os.path.join(src_path, src_img)
            to_path = os.path.join(dst_path, src_img)
            shutil.copy(from_path, to_path)
    print("end")

# 将txt中特定行写入新的txt中
def newTxt():
    src_txt = "/home/lucy/softwares/BBox-Label-Tool-master/annotations.txt"
    # dst_txt = open("/home/lucy/softwares/BBox-Label-Tool-master/JPEG.txt", 'w')
    png_txt = open("/home/lucy/softwares/BBox-Label-Tool-master/png.txt", 'w')
    with open(src_txt, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if '.JPEG' in lines[i]:
                continue
            elif '.png' in lines[i]:
                png_txt.write(lines[i])
            else:
                pass
    print("end")

# txt文件中的数据行数
def rowNums():
    txt_path = "/home/lucy/softwares/BBox-Label-Tool-master/annatations.txt"
    with open(txt_path, 'r') as f:
        lines = f.readlines()
        print('文件行数: ', len(lines))

def merge2txt(txt1_path, txt2_path, dst_txt):
    # txt1_path = "1.txt"
    # txt2_path = '2.txt'
    dst_txt = open(dst_txt, 'w')
    with open(txt1_path, 'r') as f:
        line1 = f.readlines()
    with open(txt2_path, 'r') as f:
        line2 = f.readlines()
    for i in range(len(line1)):
        dst_txt.write(line1[i])
    for i in range(len(line2)):
        dst_txt.write(line2[i])
# 合并两个文件夹中的图片到新文件夹
def merge2imageFile(imageFile1, imageFile2):
    image_list1 = os.listdir(imageFile1)
    image_list2 = os.listdir(imageFile2)
    for i in range(len(image_list2)):
        if image_list2[i] not in image_list1:
            shutil.copy(os.path.join(imageFile2, image_list2[i]), os.path.join(imageFile1, image_list2[i]))

def mergeFile():
    src_path = "/home/lucy/PycharmProjects/MTCNN-Tensorflow-master/newData"
    for file in os.listdir(src_path):
        if 'png' in file:
            png_path = os.path.join(src_path, file)
        elif 'jpeg' in file:
            jpeg_path = os.path.join(src_path, file)
        else:
            pass
    dst_path = os.path.join(src_path, '12')
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)
    for png_file in os.listdir(png_path):
        if '.txt' in png_file:
            merge2txt(os.path.join(png_path, png_file), os.path.join(jpeg_path, png_file), os.path.join(dst_path, png_file))
        else:
            # dir_path = os.path.join(dst_path, png_file)
            # if not os.path.exists(dir_path):
            #     os.mkdir(dir_path)
            merge2imageFile(os.path.join(png_path, png_file), os.path.join(jpeg_path, png_file))
    print("end")

def editTxt():
    src_path = "/home/lucy/PycharmProjects/MTCNN-Tensorflow-master/WIDERFACE/12"
    for file in os.listdir(src_path):
        if '.txt' in file:
            new_file = open(os.path.join(src_path, 'new_'+file), 'w')
            with open(os.path.join(src_path, file), 'r') as txt:
                lines = txt.readlines()
                for i in range(len(lines)):
                    new_line = lines[i].replace('/home/lucy/PycharmProjects/MTCNN-Tensorflow-master', '.')
                    new_file.write(new_line)
        else:pass
    print("end")


def imagesNum():
    img_path1 = "/home/lucy/softwares/BBox-Label-Tool-master/Images/001"
    img_path2 = "/home/lucy/softwares/BBox-Label-Tool-master/ImagesNew/001"
    img1 = os.listdir(img_path1)
    img2 = os.listdir(img_path2)
    print(len(img1))
    print(len(img2))
    print(len(img1)+len(img2))


def deleteImg1():
    img_path1 = "/home/lucy/softwares/BBox-Label-Tool-master/Images/001"
    img_path2 = "/home/lucy/softwares/BBox-Label-Tool-master/ImagesNew/001"
    annotation = "/home/lucy/softwares/BBox-Label-Tool-master/AugAnnatations.txt"
    with open(annotation, 'r') as labels:
        lines = labels.readlines()
        for img1 in os.listdir(img_path1):
            if img1 not in lines:
                os.remove(os.path.join(img_path1, img1))
                if img1 not in os.listdir(img_path1):
                    print("delete image1 %s successful"%img1)
        for img2 in os.listdir(img_path2):
            if img2 not in lines:
                os.remove(os.path.join(img_path2, img2))
                if img2 not in os.listdir(img_path2):
                    print("delete image2 %s successful"%img2)


def addImages():
    txt_path = "/home/lucy/softwares/BBox-Label-Tool-master/annatations.txt"
    base_path1 = "/home/lucy/PycharmProjects/PedestData/18_Human detection and tracking using RGB-D camera/RGB"
    base_path2 = "/home/lucy/PycharmProjects/PedestData/WIDERFace/WIDER_train/images"
    paths = os.listdir(base_path2)
    path_num = []
    for path in paths:
        path_num.append(path.split('-')[0])

    with open(txt_path, 'r') as f:
        labels = f.readlines()
        for i in range(600):
            to_path = labels[i].split(' ')[0]
            dir, img_name = os.path.split(to_path)
            from_path = os.path.join(base_path1, img_name)
            shutil.copy(from_path, to_path)
            print("num: %d, from %s"%(i, from_path))
        for i in range(600, 776):
            to_path = labels[i].split(' ')[0]
            dir, img_name = os.path.split(to_path)
            dir_, name_ = img_name.split('_')
            idx = [k for k, x in enumerate(path_num) if x == str(dir_)]
            path_ = paths[int(idx[0])]
            for image in os.listdir(os.path.join(base_path2, path_)):
                if name_.strip('.JPEG') == image.strip('.jpg').split('_')[-1]:
                    from_path = os.path.join(base_path2, path_, image)
                    shutil.copy(from_path, to_path)
            print(i)


def testTxt():
    txt_path = "/home/lucy/PycharmProjects/DSFD-tensorflow-master/train.txt"
    with open(txt_path, 'r') as f:
        lines = f.readlines()
        print('共有%d张图片'%len(lines))
        for i in range(len(lines)):
            if '.jpg' in lines[i].split(' '):
                print(lines[i])
            else:
                continue


def deleteLabelImg():
    label_path = "/home/lucy/softwares/BBox-Label-Tool-master/Labels/001"
    img_path = label_path.replace('Labels', 'Images')
    for label in os.listdir(label_path):
        with open(os.path.join(label_path, label), 'r') as f:
            person_num = f.readline()
            if int(person_num) == 0:
                label_name = os.path.join(label_path, label)
                img_name = label_name.replace('Labels', 'Images')
                img_name = img_name.replace('.txt', '.png')
                os.remove(img_name)
                os.remove(label_name)
                print("%s has been deleted!" %label_name)
                # img_name = os.path.join()


def delImg():
    img_path = "/home/lucy/softwares/BBox-Label-Tool-master/Images/001"
    label_path = img_path.replace('Images', 'Labels')
    # images = os.listdir(img_path)
    for img in os.listdir(img_path):
        label_name = img.replace('png', 'txt')
        if label_name not in os.listdir(label_path):
            os.remove(os.path.join(img_path, img))
            print('%s has been deleted!'%img)


if __name__ == '__main__':
    # copyImage()
    # newTxt()
    # rowNums()
    # addTxt()
    # merge2txt()
    # mergeFile()
    # editTxt()
    # imagesNum()
    # deleteImg1()
    # addImages()
    # testTxt()
    # deleteLabelImg()
    delImg()
