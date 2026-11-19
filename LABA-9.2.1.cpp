//////////////////////////////////////////////////////////////////////////////
// LABA-9.2.1.cpp
// Лабораторна робота № 9.2 (Частина 1)
// Тема: Директиви препроцесора та умовна компіляція
// Варіант 32
//
// Розрахунок виразу:
// w = min^2(x + y, x + z),         якщо 1 <= z < 10        (Гілка 1)
// w = max(x^2, 5|y - z|),          якщо z < 1 або z >= 10  (Гілка 2)
//////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <cstdio>
#include <cmath>
#include "macros.h"

using namespace std;

// ============================================================================
// ДИРЕКТИВА ПРЕПРОЦЕСОРА #define:
// Значення константи z визначає активну гілку компіляції:
//   Гілка 1 (1 <= z < 10):       #define z 5    (числа від 1 до 9)
//   Гілка 2 (z < 1 або z >= 10): #define z 0    (числа < 1 або >= 10)
// ============================================================================
#define z 5

int main()
{
    cout << "Laboratorna robota No 9.2 (Chastyna 1, Variant 32)" << endl;
    cout << "Stala z = " << z << endl << endl;

    double x, y, w;

    cout << "Vvedit x: "; cin >> x;
    cout << "Vvedit y: "; cin >> y;
    cout << endl;

    PRINTI(x);
    PRINTI(y);
    PRINTI(z);

#if z >= 1 && z < 10
    // Гілка 1: w = min^2(x + y, x + z)
    cout << endl << "Hilka 1: w = min^2(x + y, x + z)" << endl;
    w = SQR(MIN(x + y, x + z));
#else
    // Гілка 2: w = max(x^2, 5|y - z|)
    cout << endl << "Hilka 2: w = max(x^2, 5|y - z|)" << endl;
    w = MAX(SQR(x), 5.0 * ABS(y - z));
#endif

    PRINTR(w);

    return 0;
}
