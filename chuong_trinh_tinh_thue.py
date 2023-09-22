while True:
    try:
        print('Nhap vao thu nhập mỗi tháng của cá nhân : ')
        a= int(input())
        while True:
                if(a<=6000000):   
                    print('tiền thuế phải đóng:')
                    print(a*0)
                break
        if(6000000<=a<9000000):
            print('tiền thuế phải đóng:')
            print(a*0.02)
            break
        if(9000000<=a<12000000):
            print('tiền thuế phải đóng:')
            print(a*0.03)
            break
        if(a>12000000):
            print('tiền thuế phải đóng:')
            print(a*0.045)
            break
        break
    except ValueError:
        print('kí tự nhập phải là số')
                   
   