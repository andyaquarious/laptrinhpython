# Giải phương trình bậc nhất 1 ẩn ax + b = 0
# Nhập số a và kiểm tra điều kiện khác 0
# Bước 1:
while True:
    try:
        #Bước 1:
        print("Mời bạn nhập vào số a:" )
        a = int(input())
        # Bước 2: Máy tính kiểm tra số a có phải bằng 0 hay không
        while True:
            if (a==0):
                print("Số a bạn nhập là 0, nhập lại đi")
            else:
                #Bước 3: comment Ctrl + /
                print("Nhập số b")
                b = int(input())
                #Bước 4:
                print(-b/a)
                break
        break    
    except ValueError:
        print("Mời nhập lại số không phải chữ")