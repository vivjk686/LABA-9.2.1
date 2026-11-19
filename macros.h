#pragma once
#include <cstdio>
#include <iostream>

// ============================================================================
// macros.h
// Заголовний файл макровизначень для Лабораторної роботи № 9.2 (Частина 1)
// Варіант 32
// ============================================================================

// 1. Макроси визначення мінімуму та максимуму з двох виразів
#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define MAX(a, b) (((a) > (b)) ? (a) : (b))

// 2. Макрос піднесення до квадрата
#define SQR(x) ((x) * (x))

// 3. Макрос знаходження абсолютного значення (модуля)
#define ABS(x) (((x) < 0) ? (-(x)) : (x))

// 4. Макроси виведення значень змінних (за зразком методичних вказівок)
#define PRINTI(w) puts("control output"); printf(#w " = %d\n", (int)(w))
#define PRINTR(w) puts("rezult :"); printf(#w " = %f\n", (double)(w))

// Функції для модульного тестування розрахункових виразів обох гілок
// Гілка 1 (1 <= z < 10): w = min^2(x + y, x + z)
inline double CalcBranch1(double x, double y, double z_val) {
    return SQR(MIN(x + y, x + z_val));
}

// Гілка 2 (z < 1 або z >= 10): w = max(x^2, 5|y - z|)
inline double CalcBranch2(double x, double y, double z_val) {
    return MAX(SQR(x), 5.0 * ABS(y - z_val));
}
