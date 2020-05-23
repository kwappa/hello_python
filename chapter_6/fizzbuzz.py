for i in range(1, 501):
    if i % 15:
        print ('フィズバズ')
    elif i % 5 == 0:
        print ('バズ')
    elif i % 3 == 0:
        print ('フィズ')
    else:
        print (i)
