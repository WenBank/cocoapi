import xml.etree.ElementTree as ET
import os
import cv2
from os import getcwd

def print_dir_files(file_path):
    file_lst = []
    for file_path, sub_dirs, filenames in os.walk(file_path):
        if filenames:
            # 如果是文件，则加append到list中
            for filename in filenames:
                file_lst.append(os.path.join(file_path, filename))
        for sub_dir in sub_dirs:
            # 如果是目录，则递归调用该函数
            print_dir_files(sub_dir)
    return file_lst

classes = ["raccoon"]
def convert_annotation(image_id, imgname, Anns_txt, laber):
    in_file = open('%s'%(image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()
    filename = root.find('filename').text+'.jpg'
    (Anns_name, extension) = os.path.splitext(imgname)
    filename = Anns_name+'.jpg'
    Anns_txt.write(filename)

    # size_obj = root.iter('size')
    img_w=img_h=0
    for size_obj in root.iter('size'):
        img_w = float(size_obj.find('width').text)
        img_h = float(size_obj.find('height').text)

    for obj in root.iter('object'):
        # difficult = obj.find('difficult').text
        cls = obj.find('name').text
        # if cls not in classes or int(difficult)==1:
        #     continue
        # cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (round(float(xmlbox.find('xmin').text)/img_w,7), round(float(xmlbox.find('ymin').text)/img_h,7),
             round(float(xmlbox.find('xmax').text)/img_w,7), round(float(xmlbox.find('ymax').text)/img_h,7))
        cls_id = laber
        Anns_txt.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))
    Anns_txt.write('\n')

if __name__ == '__main__':
    # file_path = '/media/we/Seagate Expansion Drive/狗数据集/ImageNet/CatDog_data/dog_Annotation'
    # file_path = '/media/we/Seagate Expansion Drive/狗数据集/ImageNet/CatDog_data/cat_Annotation'
    file_path = '/media/we/Seagate Expansion Drive/狗数据集/ImageNet/CatDog_data/likecatdog_Annotation/rabbit_6/'
    file_lst = print_dir_files(file_path)
    savepath = '/media/we/Seagate Expansion Drive/狗数据集/ImageNet/new_catdog/Img/'
    #存储转换后的标注结果
    Anns_txt = open('/media/we/Seagate Expansion Drive/狗数据集/ImageNet/new_catdog/train.txt', 'a')
    for filename in file_lst:
        (filepath, tempfilename) = os.path.split(filename)
        (Anns_name, extension) = os.path.splitext(tempfilename)
        # filepath2 = filepath[:60]+'Image'+filepath[74:]
        filepath2 = filepath[:60]+'likecatdog_Image'+filepath[90:] #确定拼接路径是否正确
        imgpath =''
        if ''==extension:
            imgname = Anns_name+'.jpg'
        else:
            imgname = Anns_name+ '.JPEG'
        imgpath = filepath2 + '/' + imgname
        if(True==os.path.exists(imgpath)):
            image_s = cv2.imread(imgpath)
        else:
            continue
        cv2.imwrite(savepath + Anns_name + '.jpg', image_s)
        laber = 6
        convert_annotation(filename, imgname, Anns_txt, laber)
    Anns_txt.close()