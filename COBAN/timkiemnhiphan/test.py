def tach_chuoi(chuoi):
    ket_qua = []
    do_dai = len(chuoi)
    d=0
    for i in range(1, do_dai + 1):
        for j in range(do_dai - i + 1):
            ket_qua.append(chuoi[j:j+i])
            d+=1

    return (ket_qua,d)
import math
chuoi_input = "12345"
ket_qua = tach_chuoi(chuoi_input)
print(math.factorial(5))
print(ket_qua)
