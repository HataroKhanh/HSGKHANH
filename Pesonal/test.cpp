#include <iostream>
#include <unordered_map>

int main() {
  std::unordered_map<int, int> myMap;

  // Truy cập khóa không tồn tại, sẽ tạo ra khóa với giá trị 0
  std::cout << myMap[10] << std::endl; // In ra 0

  // Thêm hoặc cập nhật phần tử
  myMap[1] = 2;
  myMap[2] = 3;

  // Truy cập và in ra giá trị
  for (const auto &i : myMap) {
    std::cout << "Key: " << i.first << ", Value: " << i.second << std::endl;
  }

  return 0;
}
