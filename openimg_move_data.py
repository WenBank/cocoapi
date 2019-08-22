import shutil
'''
移动opengImg的训练数据中特定类别的图片
'''
def move_video(txt_path):
    source_prefix = 'E:/openImage/Bbox/Train/'
    target_dir = "E:/openImage/Bbox/catdog_validation/"
    txt = open(txt_path)
    wrong = open('./record', 'a')
    one_record = txt.readline()
    while len(one_record) > 0:
        name = one_record.split(' ')[0]
        print(name)
        prefix = name[0]
        source_dir = source_prefix + 'train_' + prefix + '/'
        source_path = source_dir + name
        try:
            shutil.copy(source_path, target_dir)
        except:
            wrong.write(name + '\n')
        one_record = txt.readline()
    txt.close()

'''
移动opengImg的测试和验证数据中特定类别的图片
'''
def move_testdata(txt_path):
    source_prefix = '/media/we/work/TrainData/OpenImage/validation/validation/'
    target_dir = '/media/we/work/TrainData/OpenImage/validation/test_catdog(more)/'
    txt = open(txt_path)
    wrong = open('./record', 'a')
    one_record = txt.readline()
    while len(one_record) > 0:
        name = one_record.split(' ')[0]
        print(name)
        source_dir = source_prefix
        source_path = source_dir + name
        try:
            shutil.copy(source_path, target_dir)
        except:
            wrong.write(name + '\n')
        one_record = txt.readline()
    txt.close()

if __name__ == "__main__":
    # txt_path = '/media/we/work/TrainData/OpenImage/validation/validation_bbox(more).txt'
    # move_video(txt_path)
    txt_path = '/media/we/work/TrainData/OpenImage/validation/validation_bbox(more).txt'
    move_testdata(txt_path)