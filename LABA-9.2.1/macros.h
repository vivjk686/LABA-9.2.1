#pragma once
#include <cstdio>
#include <iostream>

// ============================================================================
// macros.h
// Заголовний файл макровизначень для Лабораторної роботи № 9.2 (Частина 1)
// Варіант 32
// ============================================================================

// 1. Макроси знаходження мінімуму та максимуму з двох виразів
#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define MAX(a, b) (((a) > (b)) ? (a) : (b))

// 2. Макрос піднесення до квадрата
#define SQR(x) ((x) * (x))

// 3. Макрос знаходження абсолютного значення (модуля)
#define ABS(x) (((x) < 0) ? (-(x)) : (x))

// 4. Макроси виведення значень змінних (контрольний вивід та результат)
#define PRINTI(w) puts("control output"); printf(#w " = %d\n", (int)(w))
#define PRINTR(w) puts("rezult :"); printf(#w " = %f\n", (double)(w))

// Допоміжні функції для модульного тестування формул обох гілок
inline double CalcBranch1(double x, double y, double z) {
    return MIN(x + y, x + z) + SQR(z);
}

inline double CalcBranch2(double x, double y, double z) {
    return MAX(SQR(x), 5.0 * y) - z;
}
