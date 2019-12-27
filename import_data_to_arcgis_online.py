# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import numpy as np




for year in range(1990,2006):
    f = open("G:\\"+str(year)+".txt","w")
    monthlist = []
    for month in range(1,13):
        speed = []
        name = r"G:\data\气象数据\蒸发_EVP\SURF_CLI_CHN_MUL_DAY-EVP-13240-"+str(year)+str(month).rjust(2,"0")+".txt"
        
        file = np.loadtxt(name).tolist()
        for i in file:
            if i[0] == 53651:
                if i[9] == 0:
                    if i[7] != 32700:
                        speed.append(i[7])
#                else:
#                    index = file.index(i)
#                    value = (file[index-1][9]+file[index+1][9])/2
#                    speed.append(value)
        month_ave = sum(speed)
        monthlist.append(month_ave)
        print(str(year)+" "+str(month)+" "+str(month_ave))
        f.write(str(year)+" "+str(month)+" "+str(month_ave)+"\n")
    year_ave = sum(monthlist)
    print(str(year)+" "+str(year_ave))
    f.write(str(year)+" "+str(year_ave))
    f.close()