#so sanh hai so a va b bat ky
while True:
    try:
        print('Nhap vao so a: ')
        a= int(input())

        print('Nhap vao so b: ')
        b= int(input())
        while True:
            # if(a!=b):
            #     print('Hai so khac nhau')
            #     break
            if(a==b):
                print('Hai so bang nhau')
                break
            if(a<b):
                print('So a nho hon so b')
                break
            if(a>b):
                print('so b nho hon so a')
                break
            else:
                print('khong phai hai th nay')
                break
        break
    except ValueError:
        print('Ky tu nhap phai la so')