# %matplotlib inline
from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
#################################################
import cv2
# import pandas as pd
def showNimages(imgIds, annFile, imageFile, resultFile):
    """
    :param imageidFile: 要查看的图片imageid，存储一列在csv文件里 （目前设计的imageid需要为6位数，如果少于6位数，可以在前面加多个0）
    :param annFile:使用的标注文件
    :param imageFile:要读取的image所在文件夹
    :param resultFile:画了标注之后的image存储文件夹
    :return:
    """
    # data = pd.read_csv(imageidFile)
    # list = data.values.tolist()
    # str_image_id = []  # 存储的是要提取图片id
    # for i in range(len(imgIds)):
    #     str_tmp =''
    #     for j in range(6-len(str(imgIds[i]))):
    #         str_tmp +='0'
    #     str_tmp += str(imgIds[i])
    #     str_image_id.append(str_tmp)
    # print(str_image_id)
    # print(len(str_image_id))
    coco = COCO(annFile)
    # Anns_txt = open(resultFile+'AnnsCat.txt', 'a')
    Anns_txt = open(resultFile + 'testSheep.txt', 'a')
    dogId = coco.getCatIds(['dog'])
    catId = coco.getCatIds(['cat'])
    sheepId = coco.getCatIds(['sheep'])

    for i in range(len(imgIds)):
        str_image_id = ''
        for j in range(6-len(str(imgIds[i]))):
            str_image_id +='0'
        str_image_id += str(imgIds[i])
        img_tmp_str = '000000' + str_image_id + '.jpg'
        image_s = cv2.imread(imageFile + '000000' + str_image_id + '.jpg')
        image = image_s
        shape = image.shape
        (imgH,imgW,imgC) = shape
        img_anns_tmp = {}
        annIds = coco.getAnnIds(imgIds=imgIds[i], catIds=dogId)
        class_id = 0
        dog_anns = coco.loadAnns(annIds)
        img_anns_tmp[class_id]=dog_anns
        annIds = coco.getAnnIds(imgIds=imgIds[i], catIds=catId)
        class_id = 1
        cat_anns = coco.loadAnns(annIds)
        img_anns_tmp[class_id] = cat_anns
        annIds = coco.getAnnIds(imgIds=imgIds[i], catIds=sheepId)
        class_id = 7
        sheep_anns = coco.loadAnns(annIds)
        img_anns_tmp[class_id] = sheep_anns

        # for n in range(len(anns)):
        #     x, y, w, h = anns[n]['bbox']
        #     x, y, w, h = int(x), int(y), int(w), int(h)
        #     # print(x, y, w, h)
        #     # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255))
        #     x_min = round(float(x)/imgW,7); y_min= round(float(y)/imgH,7)
        #     x_max = round(float(x + w)/imgW,7); y_max = round(float(y + h)/imgH,7)
        #     img_tmp_str += ' ' + str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max) + ',' + str(class_id)
        # annIds = coco.getAnnIds(imgIds=imgIds[i], catIds=catId)
        for key in img_anns_tmp.keys():
            class_id = key
            anns = img_anns_tmp[key]
            for n in range(len(anns)):
                x, y, w, h = anns[n]['bbox']
                x, y, w, h = int(x), int(y), int(w), int(h)
                # print(x, y, w, h)
                # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0))
                #分数
                # x_min = round(float(x) / imgW, 7)
                # y_min = round(float(y) / imgH, 7)
                # x_max = round(float(x + w) / imgW, 7)
                # y_max = round(float(y + h) / imgH, 7)
                #整数
                x_min = x; y_min = y; x_max = x + w; y_max = y + h
                img_tmp_str += ' ' + str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max) + ',' + str(
                    class_id)
        Anns_txt.write(img_tmp_str + '\n')
        # class_id = 1
        # anns = coco.loadAnns(annIds)
        # for n in range(len(anns)):
        #     x, y, w, h = anns[n]['bbox']
        #     x, y, w, h = int(x), int(y), int(w), int(h)
        #     # print(x, y, w, h)
        #     # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0))
        #     x_min = round(float(x)/imgW,7); y_min= round(float(y)/imgH,7)
        #     x_max = round(float(x + w)/imgW,7); y_max = round(float(y + h)/imgH,7)
        #     img_tmp_str += ' ' + str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max) + ',' + str(class_id)
        #
        # Anns_txt.write(img_tmp_str + '\n')
        img_tmp_str = ''
        # cv2.imwrite(resultFile + 'CatImg/000000' + str_image_id + '.jpg', image)
        cv2.imwrite(resultFile + 'testSheep/000000' + str_image_id + '.jpg', image)
    Anns_txt.close()
    print("生成图片存在{}".format(resultFile))
######################################################

pylab.rcParams['figure.figsize'] = (8.0, 10.0)
dataDir='/media/we/work/TrainData/coco'
dataType='train2017'
dataType='val2017'
annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)

imageidFile = '/Desktop/myimage_id.csv'
imageFile = dataDir+'/'+dataType+'/'
resultFile = '/media/we/Seagate Expansion Drive/狗数据集/CoCo/'

# initialize COCO api for instance annotations
coco=COCO(annFile)

total_imgIds = coco.getImgIds()
# 获取'狗'的标签ID
catIds = coco.getCatIds(['sheep'])

# 在所有图像里面找到狗的图像的ID号
imgIds = coco.getImgIds(total_imgIds, catIds)
# imgIds22 = coco.getImgIds(total_imgIds, coco.getCatIds(['dog','cat']))
# imgIds = imgIds -imgIds22
imgAnnIds = coco.getAnnIds(imgIds, catIds)
# 根据找到的ID号找到图像信息
img = coco.loadImgs(imgIds)
Anns = coco.loadAnns(imgAnnIds)
# 根据图像信息加载一张图像
I = io.imread('%s/%s/%s' % (dataDir, dataType, img[1]['file_name']))

for Ann in Anns:
    if Ann['image_id']==img[1]['id']:
        bbox = Ann['bbox']
# 用scikit-image显示出来
plt.axis('off')
plt.imshow(I)
plt.show()

showNimages(imgIds, annFile, imageFile, resultFile)
#
#
#
# # display COCO categories and supercategories
# cats = coco.loadCats(coco.getCatIds(['dog']))
# Anns = coco.loadAnns(coco.getAnnIds())
# nms=[cat['name'] for cat in cats]
# category_id=set([Ann['category_id'] for Ann in Anns])
# print('COCO categories: \n{}\n'.format(' '.join(nms)))
#
# # nms = set([cat['supercategory'] for cat in cats])
# # print('COCO supercategories: \n{}'.format(' '.join(nms)))
# # get all images containing given categories, select one at random
# catIds = coco.getCatIds(catNms=['person','dog','skateboard']);
# imgIds = coco.getImgIds(catIds=catIds );
# imgIds = coco.getImgIds(imgIds = [324158])
# img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]
# # load and display image
# I = io.imread('%s/images/%s/%s'%(dataDir,dataType,img['file_name']))
# # use url to load image
# # I = io.imread(img['coco_url'])
# plt.axis('off')
# plt.imshow(I)
# plt.show()
# # load and display instance annotations
# plt.imshow(I); plt.axis('off')
# annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
# anns = coco.loadAnns(annIds)
# coco.showAnns(anns)