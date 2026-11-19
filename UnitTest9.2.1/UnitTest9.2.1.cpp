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
            Assert::AreEqual(3.0, MIN(3.0, 7.0));
            Assert::AreEqual(-5.0, MIN(-5.0, -2.0));
            Assert::AreEqual(0.0, MIN(0.0, 10.0));
        }

        TEST_METHOD(TestMacroMax)
        {
            Assert::AreEqual(7.0, MAX(3.0, 7.0));
            Assert::AreEqual(-2.0, MAX(-5.0, -2.0));
            Assert::AreEqual(10.0, MAX(0.0, 10.0));
        }

        TEST_METHOD(TestMacroSqr)
        {
            Assert::AreEqual(16.0, SQR(4.0));
            Assert::AreEqual(9.0, SQR(-3.0));
            Assert::AreEqual(0.25, SQR(0.5));
        }

        TEST_METHOD(TestMacroAbs)
        {
            Assert::AreEqual(5.0, ABS(-5.0));
            Assert::AreEqual(3.5, ABS(3.5));
            Assert::AreEqual(0.0, ABS(0.0));
        }

        TEST_METHOD(TestBranch1Calculation)
        {
            // Гілка 1 (1 <= z < 10): w = min^2(x + y, x + z)
            // x = 2.0, y = 3.0, z = 5.0 -> min(5, 7)^2 = 25.0
            double res1 = CalcBranch1(2.0, 3.0, 5.0);
            Assert::AreEqual(25.0, res1);

            // x = 1.0, y = 6.0, z = 2.0 -> min(7, 3)^2 = 9.0
            double res2 = CalcBranch1(1.0, 6.0, 2.0);
            Assert::AreEqual(9.0, res2);
        }

        TEST_METHOD(TestBranch2Calculation)
        {
            // Гілка 2 (z < 1 або z >= 10): w = max(x^2, 5|y - z|)
            // x = 4.0, y = 2.0, z = 0.0 -> max(16, 5*|2-0|) = max(16, 10) = 16.0
            double res1 = CalcBranch2(4.0, 2.0, 0.0);
            Assert::AreEqual(16.0, res1);

            // x = 2.0, y = 5.0, z = 1.0 -> max(4, 5*|5-1|) = max(4, 20) = 20.0
            double res2 = CalcBranch2(2.0, 5.0, 1.0);
            Assert::AreEqual(20.0, res2);

            // x = 3.0, y = 1.0, z = -2.0 -> max(9, 5*|1 - (-2)|) = max(9, 15) = 15.0
            double res3 = CalcBranch2(3.0, 1.0, -2.0);
            Assert::AreEqual(15.0, res3);
        }
    };
}
