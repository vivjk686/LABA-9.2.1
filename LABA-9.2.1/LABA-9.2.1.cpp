//////////////////////////////////////////////////////////////////////////////
// LABA-9.2.1.cpp
// Лабораторна робота № 9.2 (Частина 1)
// Тема: Директиви препроцесора та умовна компіляція
// Варіант 32
//
// Розрахунок виразу:
// w = min(x + y, x + z) + z^2,     якщо 1 <= z < 10
// w = max(x^2, 5y) - z,            якщо z < 1 або z >= 10
//////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <cstdio>
#include <cmath>
#include "macros.h"

using namespace std;

// ============================================================================
// ІНСТРУКЦІЯ: ДЕ І ЯК ЗМІНЮВАТИ ДИРЕКТИВУ ПРЕПРОЦЕСОРА (ІНДЕФ):
// ----------------------------------------------------------------------------
// РЯДОК 24:
//   Щоб була активна 1-ША ГІЛКА (1 <= z < 10):
//       #define MODE_1
//
//   Щоб була активна 2-ГА ГІЛКА (z < 1 або z >= 10):
//       Закоментуйте цей рядок:
//       //#define MODE_1
//       (або замініть на #undef MODE_1)
// ============================================================================
#define MODE_1 // <-- ОСЬ ТУТ МІНЯТИ: закоментуйте для активації 2-ї гілки!

#ifndef UNIT_TESTING
int main()
{
    cout << "Laboratorna robota No 9.2 (Chastyna 1, Variant 32)" << endl;
    cout << "Vykorystannya makrosiv ta dyrektyv umovnoyi kompilyatsiyi" << endl << endl;

    double x, y, z, w;

    cout << "Vvedit x: "; cin >> x;
    cout << "Vvedit y: "; cin >> y;
    cout << "Vvedit z: "; cin >> z;
    cout << endl;

#ifdef MODE_1
    // ------------------------------------------------------------------------
    // ГІЛКА 1: компілюється для умови 1 <= z < 10
    // w = min(x + y, x + z) + z^2
    // ------------------------------------------------------------------------
    cout << "[PREPROCESSOR] Kompilyuyetsya HILKA 1 (umova: 1 <= z < 10)" << endl;
    cout << "Formula: w = min(x + y, x + z) + z^2" << endl << endl;

    // Контрольний вивід аргументів через макрос PRINTI
    PRINTI(x);
    PRINTI(y);
    PRINTI(z);

    // Обчислення за формулою з використанням макросів MIN та SQR
    double term1 = x + y;
    double term2 = x + z;
    double min_val = MIN(term1, term2);
    double z_sqr = SQR(z);

    w = min_val + z_sqr;

    // Виведення результату через макрос PRINTR
    PRINTR(w);

#else
    // ------------------------------------------------------------------------
    // ГІЛКА 2: компілюється для умови z < 1 або z >= 10
    // w = max(x^2, 5*y) - z
    // ------------------------------------------------------------------------
    cout << "[PREPROCESSOR] Kompilyuyetsya HILKA 2 (umova: z < 1 abo z >= 10)" << endl;
    cout << "Formula: w = max(x^2, 5*y) - z" << endl << endl;

    // Контрольний вивід аргументів через макрос PRINTI
    PRINTI(x);
    PRINTI(y);
    PRINTI(z);

    // Обчислення за формулою з використанням макросів MAX та SQR
    double x_sqr = SQR(x);
    double five_y = 5.0 * y;
    double max_val = MAX(x_sqr, five_y);

    w = max_val - z;

    // Виведення результату через макрос PRINTR
    PRINTR(w);

#endif // MODE_1

    return 0;
}
#endif
