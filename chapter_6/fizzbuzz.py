for i in range(1, 51):
    if i % 3 == 0:
        print ('フィズ')
    elif i % 5 == 0:
        print ('バズ')
    elif i % 15 == 0:
        print ('フィズバズ')
    else:
        print (i)
