def printProgress(percent,width=100):
    chars=percent*width/100;
    print('[',end='')
    print('N'*int(chars),end='');
    print('-'*(width-int(chars)),end='')
    print(']',end='')
    print(" "+str(percent)+"%",end='')
    print('\r',end='')
