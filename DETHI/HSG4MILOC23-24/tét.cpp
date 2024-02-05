#include <iostream>
#include <set>

int main() {
    std::set<int> mySet = {1, 2, 3, 4, 5};

    int valueToFind = 3;

    // Sử dụng hàm count để kiểm tra sự xuất hiện của giá trị trong set
    int count = mySet.count(valueToFind);

    if (count > 0) {
        std::cout << "Giá trị " << valueToFind << " xuất hiện trong set." << std::endl;
    } else {
        std::cout << "Giá trị " << valueToFind << " không xuất hiện trong set." << std::endl;
    }

    return 0;
}
