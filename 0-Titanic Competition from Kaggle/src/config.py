#########################################################
#讀取檔案
#########################################################

#csv file

import csv
import os
import sys

a = os.path.abspath(__file__)
a = a.split("/")
str_line = '/'
a = str_line.join(a[0:-2])



testset_path = r"{}/data/raw/test.csv".format(a)
trainset_path = r"{}/data/raw/train.csv".format(a)



if __name__ == "__main__":
    print(testset_path)
    # # 開啟 CSV 檔案
    # f =  open("%stest.csv"%abs_file_path,'r')


    # # 以迴圈輸出每一列
    # for row in csv.reader(f):
    #     print(row)
    # f.close();


"""
filelocation = "D:\\1-Project\\2018\\1-HLC\\3-Data\\DATA\\0828\\Student_Info_Dist.csv"
ecod= 'big5'
"""
#########################################################
#Random Forest parameter
#########################################################

"""
RF_testsize = 0.2

n_estimators = 200 # 幾棵樹

min_samples_split = 40

max_depth = 15

min_samples_leaf = 10

"""
