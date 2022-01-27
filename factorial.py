n = int(float(input('давай вводи положительное число: ')))
res = 0
st = 1
if n < 0:
    print('тут съёмка видео и ввод минуса запрещена')
else:
    while True:
        a = n//(5**st)
        if a < 1:
            print(res, ' нулёв в конце факториала')
            break
        else:
            res+=a
            st+=1