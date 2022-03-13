# -*- coding: UTF-8 -*-
# 要求：输出1~20000内的所有素数，按每行5个打印出来，并分析程序中最费时的函数是什么， 如何改进？

def primeNUM(min,max):
    count = 0
    if min==1:
        print('')
        min += 1
    for i in range(min, max+1):
        for j in range(2, i + 1):
            if i % j == 0:          #判断i能不能被整除
                break               #退出for循环
        if j == i:                  #若j等于i，说明i是素数
            print(i,end=" ")
            count += 1
        if(count == 5):
            print("")
            count = 0
       

primeNUM(2,20000)    
