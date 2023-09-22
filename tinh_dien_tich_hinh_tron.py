while True:
    try:
        #Bước 1:
        print("Mời bạn nhập vào bán kính cua hinh tròn:" )
        a = int(input())
        # Bước 2:
        while True:
            if (a==0):
                print("Số a bạn nhập là 0, nhập lại đi")
            else:
        
        #Bước 3:
                print('Kết quả là:')
                print(a*a*3.14)
            break                 
        break                         
    except ValueError:
        print("Mời nhập lại số không phải chữ")
    