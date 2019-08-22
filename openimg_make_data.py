# -*- coding: UTF-8 -*-
# @Time : 19-6-27 下午3:58 
# @Author : Zero 
# @File : make_data.py 
# @Software: PyCharm

#解析表格文件(.xlsx .obs)生成类别字典
import xlrd
# import xlwt
import csv
def generate_dict(xlsx_path='./label.xlsx'):
    workbook = xlrd.open_workbook(xlsx_path)
    worksheet = workbook.sheet_by_index(0)
    keys = worksheet.col_values(0)[1:]
    values = worksheet.col_values(3)[1:]
    label_dict = dict(zip(keys, values))
    print(label_dict)
    return label_dict
def generate_dict_num(xlsx_path='./label.xlsx'):
    workbook = xlrd.open_workbook(xlsx_path)
    worksheet = workbook.sheet_by_index(0)
    keys = worksheet.col_values(0)[1:]
    values = worksheet.col_values(3)[1:]
    label_dict = dict(zip(keys, values))
    print(label_dict)
    return label_dict
def generate_csv(save_path, label_dict, input_path):
    out_data = open(save_path, 'a')
    csv_writer = csv.writer(out_data)

    input_data = open(input_path, 'r')
    op_data = csv.reader(input_data)

    local_class = ''
    index_nowrite = 0
    index = 0

    for one in op_data:
        print(index)
        IsGroupOf = one[10]
        IsDepiction = one[11]
        if (index_nowrite==0):
            csv_writer.writerow(one)
            index_nowrite=1
            continue
        if (one[2] in label_dict) and '0'==IsGroupOf and '0'==IsDepiction:
            csv_writer.writerow(one)
            index = index + 1
    input_data.close()
    out_data.close()


def genrate_annotions(csv_an, save_txt, label_dict):
    csv_files = open(csv_an, 'r')
    txt_files = open(save_txt, 'a')
    catdog = False
    if catdog:
        cat_txt = ''
        dog_txt = ''
        cat_txt_files = open(cat_txt, 'a')
        dog_txt_files = open(dog_txt, 'a')
        cat_num = dog_num = 0
        CatIndex = DogIndex = 0
    csv_reader = csv.reader(csv_files)
    local_imageID = ''
    tmp_str = ''
    temp = True
    for one in csv_reader:
        if temp:
            temp = False
            continue #越过第一行
        image_ID = one[0]
        if image_ID == local_imageID:
            tmp_str = tmp_str+' '+one[4] + ',' + one[6] + ',' + one[5] + ',' + one[7] + ',' + str(label_dict[one[2]])[:-2]
            # tmp_str = tmp_str+' '+one[4] + ',' + one[6] + ',' + one[5] + ',' + one[7] + ',' + "0"
            local_imageID = image_ID
            if catdog:
                if 0 == label_dict[one[2]]:
                    DogIndex = 1
                elif 1 == label_dict[one[2]]:
                    CatIndex = 1
        else:
            txt_files.write(tmp_str + '\n')
            if catdog:
                # 统计
                if 1 == CatIndex:
                    cat_num += 1
                    cat_txt_files.write(tmp_str + '\n')
                if 1 == DogIndex:
                    dog_num += 1
                    dog_txt_files.write(tmp_str + '\n')
            CatIndex = DogIndex = 0
            tmp_str = str(image_ID) + '.jpg ' +one[4] +',' + one[6] + ',' + one[5] + ',' + one[7] + ',' + str(label_dict[one[2]])[:-2]
            # tmp_str = str(image_ID) + '.jpg ' + one[4] + ',' + one[6] + ',' + one[5] + ',' + one[7] + ',' + "0"
            local_imageID = image_ID
            if catdog:
                if 0 == label_dict[one[2]]:
                    DogIndex = 1
                elif 1 == label_dict[one[2]]:
                    CatIndex = 1
    if catdog:
        if 1 == CatIndex:
            cat_num += 1
            cat_txt_files.write(tmp_str + '\n')
        if 1 == DogIndex:
            dog_num += 1
            dog_txt_files.write(tmp_str + '\n')
        dog_txt_files.close()
        cat_txt_files.close()
    txt_files.write(tmp_str)
    txt_files.close()
    csv_files.close()
# def xml_label():

if __name__ == "__main__":
    '''
    抽取csv中的对应类别的数据
    '''
    if False:
        # xlsx_path = '/media/we/Seagate Expansion Drive/狗数据集/OpenImage/label.xlsx'
        # label_dict = generate_dict(xlsx_path)
        # input_path = '/media/we/Seagate Expansion Drive/狗数据集/OpenImage/train-annotations-bbox.csv'
        # # input_path = '/media/we/Seagate Expansion Drive/狗数据集/OpenImage/validation-annotations-bbox.csv'
        # save_path = '/media/we/Seagate Expansion Drive/狗数据集/OpenImage/train_bbox(精细).csv'
        xlsx_path = '/media/we/work/TrainData/OpenImage/validation/label(more).xlsx'
        label_dict = generate_dict(xlsx_path)
        input_path = '/media/we/work/TrainData/OpenImage/validation/validation-annotations-bbox.csv'
        save_path = '/media/we/work/TrainData/OpenImage/validation/validation_bbox(more).csv'
        generate_csv(save_path, label_dict, input_path)

    '''
    将csv保存成txt
    '''
    if False:
        xlsx_path = '/media/we/Seagate Expansion Drive/狗数据集/OpenImage/label.xlsx'
        label_dict = generate_dict_num(xlsx_path)
        # label_dict = []
        # csv_an = '/media/we/Seagate Expansion Drive/狗数据集/OpenImage/train_bbox(catdog).csv'
        # save_txt = '/media/we/Seagate Expansion Drive/狗数据集/OpenImage/train_bbox(catdog).txt'
        csv_an = '/media/we/Seagate Expansion Drive/狗数据集/OpenImage/validation_bbox(catdog).csv'
        save_txt = '/media/we/Seagate Expansion Drive/狗数据集/OpenImage/validation_bbox(catdog).txt'
        cat_txt = '/media/we/Seagate Expansion Drive/狗数据集/OpenImage/validation_bbox(cat).txt'
        dog_txt = '/media/we/Seagate Expansion Drive/狗数据集/OpenImage/validation_bbox(dog).txt'
        genrate_annotions(csv_an, save_txt, cat_txt, dog_txt,  label_dict)

    '''
    多类数据转txt
    '''
    if True:
        xlsx_path = '/media/we/work/TrainData/OpenImage/validation/label(more).xlsx'
        label_dict = generate_dict(xlsx_path)
        # input_path = '/media/we/Seagate Expansion Drive/狗数据集/OpenImage/train-annotations-bbox.csv'
        # save_path = '/media/we/Seagate Expansion Drive/狗数据集/OpenImage/train_bbox(like).csv'
        # generate_csv(save_path, label_dict, input_path)
        # 转换TXT
        csv_an = '/media/we/work/TrainData/OpenImage/validation/validation_bbox(more).csv'
        save_txt = '/media/we/work/TrainData/OpenImage/validation/validation_bbox(more).txt'
        # cat_txt = '/media/we/Seagate Expansion Drive/狗数据集/OpenImage/validation_bbox(cat).txt'
        # dog_txt = '/media/we/Seagate Expansion Drive/狗数据集/OpenImage/validation_bbox(dog).txt'
        genrate_annotions(csv_an, save_txt, label_dict)