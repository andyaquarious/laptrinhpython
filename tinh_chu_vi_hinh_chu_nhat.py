
while True:
    try:
        #Bước 12344556
        print('hello')
        print("Mời bạn nhập vào chieu dai cua hinh chu nhat:" )
        a = int(input())
        # Bước 2:
        while True:
            if (a==0):
                print("Số a bạn nhập là 0, nhập lại đi")
            else:
        #Bước 3:
                print("Mời ban nhập chieu rộng của hình chữ nhật")
                b = int(input())
            break
        if(b>=a):
                print('chiều rộng ko thể lớn hơn hoặc bằng chiều dài,nhập lại đi')
        else:
        #Bước 4:
            print('Kết quả là:')
            print(2*(a+b))
            break                 
        break                         
    except ValueError:
        print("Mời nhập lại số không phải chữ")
    
    
        
              
                        
   