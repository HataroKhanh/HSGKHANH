#include <GL/glut.h>
#include <cmath>
#include <iostream>
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif
int centerX = 47;  // Tọa độ x của tâm
int centerY = 30;  // Tọa độ y của tâm
int radius = 9;    // Bán kính
int centerX1 = 93; // Tọa độ x của tâm
int centerY1 = 30; // Tọa độ y của tâm
int radius1 = 9;   // Bán kính
void hinhtron() {
  glBegin(GL_LINE_LOOP);
  for (int i = 0; i < 360; i++) {
    float theta = i * 3.14159 / 180; // Chuyển đổi từ độ sang radian
    float x = centerX + radius * cos(theta);
    float y = centerY + radius * sin(theta);
    glVertex2f(x, y);
  }
  glEnd();
}
