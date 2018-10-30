#구구단
sw=False
for i in range(2,10):
    if sw:
        break
    print('##',i,'단##')
    for k in range(1,10):

        if i*k>=50:
            sw=True
            break
        print(i, 'x', k, '=', i * k)
    print('\n')