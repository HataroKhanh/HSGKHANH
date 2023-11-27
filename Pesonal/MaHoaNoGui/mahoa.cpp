#include <bits/stdc++.h>
/* #include <filesystem> */
#include <fstream>
#include <ostream>
#include <string>
// namespace fs = std::filesystem;
using namespace std;
/* void findfile() {
  std::string path = "."; // Thư mục hiện tại
  for (const auto &entry : filesystem::directory_iterator(path))
    std::cout << entry.path().filename() << std::endl;
} */
void printLineWithBorder(const std::string &line, int width,
                         const std::string &color) {
  std::cout << color << "| " << line;
  for (size_t i = line.length(); i < width; ++i) {
    std::cout << " ";
  }
  std::cout << " |"
            << "\033[0m" << std::endl;
}
float tiendo(float a) { return 100 / a; }
char replacechar(char &c, int &numpush) { return c - numpush; }
char undochar(char &c, int &numpush) { return c + numpush; }
void coutnamefile(string s) {
  ifstream input(s);
  string line;
  if (!input) {
    cout << "Khong The Mo " << s << '\n';
    return;
  }
  while (getline(input, line)) {
    cout << line << '\n';
  }
  cout << '\n';
}
int revertkey(string &s) {
  string key;
  int num = 2;
  for (char &i : s) {
    key += i + static_cast<char>(num);
  }
  int keyf = key[0] + key[1];
  return keyf;
}
void encript(string s, int a) {
  ifstream input(s);
  string line;
  vector<string> strings;
  if (!input) {
    cout << "Khong The Mo " << s << '\n';
    return;
  }

  while (getline(input, line)) {
    for (char &i : line) {
      i = replacechar(i, a);
    }
    strings.push_back(line);
  }
  ofstream output(s);
  int percent = 0, Tiendo = tiendo(strings.size());
  for (int i = 0; i < strings.size(); i++) {
    output << strings[i] << '\n';
    percent += Tiendo;
    cout << "Dang Ma Hoa " << percent << "%";
    cout.flush();
  }
  cout << '\n';
  cout << "Ma Hoa Thanh Cong!";
}
void decomplile(string &s, int a) {
  ifstream input(s);
  string line;
  vector<string> strings;
  if (!input) {
    cout << "Khong The Mo " << s << '\n';
    return;
  }

  while (getline(input, line)) {
    for (char &i : line) {
      i = undochar(i, a);
    }
    strings.push_back(line);
  }

  ofstream output(s);
  int percent = 0, Tiendo = tiendo(strings.size());
  for (int i = 0; i < strings.size(); i++) {
    output << strings[i] << '\n';
    cout << "Tien Do: " << percent;
    percent += Tiendo;
    cout.flush();
  }
  cout << '\n';
  cout << "Dich Nguoc Thanh Cong!";
}
using namespace std;
int main(int argc, char *argv[]) {
  char chon;
  char yesno = 'N';
  string namefile;
  while (1) {

#ifdef _WIN32
    system("cls");
#elif __linux__
    system("clear");
#endif
    int width = 40;
    std::vector<std::string> lines = {"Phan Mem Ma Hoa By Bui Khanh    ",
                                      "Chuc Nang:",
                                      "1. Doc File",
                                      "2. Ma Hoa",
                                      "3. Dich Nguoc Ma Hoa",
                                      "4. Thoat",
                                      "Chon (1, 2, 3, 4): "};

    // Mã ANSI cho các màu khác nhau
    std::vector<std::string> colors = {
        "\033[31m", // Màu đỏ
        "\033[32m", // Màu xanh lá
        "\033[33m", // Màu vàng
        "\033[34m", // Màu xanh dương
        "\033[35m", // Màu tím
        "\033[36m", // Màu xanh lục
        "\033[37m"  // Màu trắng
    };

    for (size_t i = 0; i < lines.size(); ++i) {
      printLineWithBorder(lines[i], width, colors[i % colors.size()]);
    }
    cin >> chon;

    switch (chon) {
    case '1':
      cout << "Cac Tep Trong Thu Muc\n";
      // findfile();
      cout << '\n';
      cout << "Nhap Ten File: ";
      cin >> namefile;
      coutnamefile(namefile);
      cout << "Continue(y/n): ";
      cin >> yesno;
      if (!(yesno == 'Y' || yesno == 'y'))
        break;
    case '2': {
      cout << "Cac Tep Trong Thu Muc\n";
      // findfile();
      cout << '\n';
      string key;
      cout << "Nhap Ten File: ";
      cin >> namefile;
      cout << "Nhap Key Ma Hoa(Nho Key De Khong Mat Du Lieu): ";
      cin >> key;
      encript(namefile, revertkey(key));
      cin.get();
      break;
    }
    case '3': {
      cout << "Cac Tep Trong Thu Muc\n";
      // findfile();
      string key;
      cout << '\n';
      cout << "Nhap Ten File: ";
      cin >> namefile;
      cout << "Nhap Key: ";
      cin >> key;
      decomplile(namefile, revertkey(key));
      cin.get();
      break;
    }
    case '4':
      return 1;
    }
  }
  return 0;
}
