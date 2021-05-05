import glob
import os

import numpy
import scipy
from pandas import DataFrame
from scipy.io import savemat

def main():
    count_line=0
    total_line=0
    total_file=0

    files = glob.glob('data/*')

    c1 = list()
    c2 = list()
    c3 = list()
    c4 = list()


    for file in files:
        with open(file) as numbers:
            #print("reading file->",file)
            c1_local = list()
            c2_local = list()
            c3_local = list()
            c4_local = list()

            for rec in numbers:
                if count_line >= 125:
                    #column1
                    if rec[17] == '-':
                        sayi = '-0.{}'.format(rec[19:35])
                        c1_local.append(float(sayi))
                        # print('-0.{}'.format(rec[19:35]))
                        #print(float(sayi))
                    else:
                        sayi = rec[17:35]
                        c1_local.append(float(sayi))
                        #print(float(sayi))

                    # column2
                    if rec[36] == '-':
                        sayi = '-0.{}'.format(rec[38:55])
                        #print("sayi->", sayi)
                        c2_local.append(float(sayi))

                    else:
                        sayi = rec[36:55]
                        c2_local.append(float(sayi))
                        #print(float(sayi))

                    # column3
                    if rec[55] == '-':
                        sayi = '-0.{}'.format(rec[57:65])
                        #print("sayi->", sayi)
                        c3_local.append(float(sayi))
                    else:
                        sayi = rec[55:65]
                        #print("sayi->", sayi)
                        c3_local.append(float(sayi))

                    # column4
                    if rec[66] == '-':
                        sayi = '-0.{}'.format(rec[68:76])
                        #print("sayi->", sayi)
                        c4_local.append(float(sayi))
                    else:
                        sayi = rec[66:76]
                        #print("sayi->", sayi)
                        c4_local.append(float(sayi))
                    total_line += 1
                count_line += 1

            c1.append(c1_local.copy())
            c2.append(c2_local.copy())
            c3.append(c3_local.copy())
            c4.append(c4_local.copy())

            c1_local.clear()
            c2_local.clear()
            c3_local.clear()
            c4_local.clear()

            #print("toplam->", total_line)
            #print("closing file->", file)
            numbers.close()
            total_file+=1
            count_line=0

    #print(c1)
    mean_c1 = numpy.mean(c1,axis=0)
    #print(mean_c1)
    #print("average->", (-0.484169309481e-03 + -0.484169285067e-03) / 2)

    mean_c2 = numpy.mean(c2, axis=0)
    mean_c3 = numpy.mean(c3, axis=0)
    mean_c4 = numpy.mean(c4, axis=0)



    #print(mean_c1)

    c_mean = numpy.array([mean_c1,mean_c2,mean_c3,mean_c4])
    #print(c_mean.shape)
    c_mean = c_mean.T
    #print(c_mean.shape)


    c_mean = DataFrame(c_mean,columns=['Mean C1', 'Mean C2', 'Mean C3','Mean C4'])

    print(c_mean)

    #sio.savemat(os.path.join('output', 'meta.mat'), c_mean)


    c_mean.to_csv('output/meta.csv') 







main()
