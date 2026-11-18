#include "pch.h"
#include "CppUnitTest.h"
#include <cmath>
#include "../LABA-9.2.1/macros.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest921
{
    TEST_CLASS(UnitTest921)
    {
    public:
        TEST_METHOD(TestMacroMin)
        {
            // Тестування макросу MIN
            Assert::AreEqual(3.0, MIN(3.0, 7.0));
            Assert::AreEqual(-5.0, MIN(-5.0, -2.0));
            Assert::AreEqual(0.0, MIN(0.0, 10.0));
        }

        TEST_METHOD(TestMacroMax)
        {
            // Тестування макросу MAX
            Assert::AreEqual(7.0, MAX(3.0, 7.0));
            Assert::AreEqual(-2.0, MAX(-5.0, -2.0));
            Assert::AreEqual(10.0, MAX(0.0, 10.0));
        }

        TEST_METHOD(TestMacroSqr)
        {
            // Тестування макросу SQR
            Assert::AreEqual(16.0, SQR(4.0));
            Assert::AreEqual(9.0, SQR(-3.0));
            Assert::AreEqual(0.25, SQR(0.5));
        }

        TEST_METHOD(TestBranch1Calculation)
        {
            // Тестування Гілки 1 (1 <= z < 10): w = min(x + y, x + z) + z^2
            // Для x = 2.0, y = 3.0, z = 4.0:
            // x + y = 5.0, x + z = 6.0, min(5, 6) = 5.0
            // z^2 = 16.0 => w = 5.0 + 16.0 = 21.0
            double res1 = CalcBranch1(2.0, 3.0, 4.0);
            Assert::AreEqual(21.0, res1);

            // Для x = 1.0, y = 5.0, z = 2.0:
            // x + y = 6.0, x + z = 3.0, min(6, 3) = 3.0
            // z^2 = 4.0 => w = 3.0 + 4.0 = 7.0
            double res2 = CalcBranch1(1.0, 5.0, 2.0);
            Assert::AreEqual(7.0, res2);
        }

        TEST_METHOD(TestBranch2Calculation)
        {
            // Тестування Гілки 2 (z < 1 або z >= 10): w = max(x^2, 5*y) - z
            // Для x = 4.0, y = 2.0, z = 3.0:
            // x^2 = 16.0, 5*y = 10.0, max(16, 10) = 16.0
            // w = 16.0 - 3.0 = 13.0
            double res1 = CalcBranch2(4.0, 2.0, 3.0);
            Assert::AreEqual(13.0, res1);

            // Для x = 2.0, y = 5.0, z = 0.5:
            // x^2 = 4.0, 5*y = 25.0, max(4, 25) = 25.0
            // w = 25.0 - 0.5 = 24.5
            double res2 = CalcBranch2(2.0, 5.0, 0.5);
            Assert::AreEqual(24.5, res2);
        }
    };
}
