"""
Viết chương trình nhập: số giờ làm mỗi tuần, thù lao trên mỗi giờ làm tiêu chuẩn,
 từ đó tính ra số tiền thực lĩnh của nhân viên. 
 Biết rằng: số giờ tiêu chuẩn mỗi tuần là 44 giờ, 
và mỗi giờ vượt chuẩn được trả gấp rưỡi so với giờ làm chuẩn."""
t=int(input())
h=int(input())
x=t*h
if h>44:x=x+(h-44)*1.5
print(x)