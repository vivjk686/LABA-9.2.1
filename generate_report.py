# -*- coding: utf-8 -*-
import os
import docx
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = r"C:\Users\User\OneDrive\Документи\лаби\LABA-9.2.1"
IMG_DIR = os.path.join(BASE_DIR, "images")
OUT_DOCX = os.path.join(BASE_DIR, "АП_РІ-13_Шах_ЛР-09.2.1.docx")

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex="F4F6F8"):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._element.get_or_add_tcPr().append(shading_elm)

def set_table_borders(table, color="D3D3D3", sz="4", val="single"):
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>\n'
            f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
            f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
            f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
            f'  <w:insideV w:val="none"/>\n'
            f'  <w:left w:val="none"/>\n'
            f'  <w:right w:val="none"/>\n'
            f'</w:tblBorders>'
        )
        tblPr[0].append(borders)

def add_p(doc, text="", bold=False, italic=False, size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, space_before=0, line_spacing=1.15):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.line_spacing = line_spacing
    if text:
        r = p.add_run(text)
        r.bold = bold
        r.italic = italic
        r.font.name = 'Times New Roman'
        r.font.size = Pt(size)
        r.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_h(doc, text, level=1):
    p = doc.add_paragraph()
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.color.rgb = RGBColor(0, 51, 102)
    
    if level == 1:
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        r.font.size = Pt(14)
    elif level == 2:
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        r.font.size = Pt(12.5)
    return p

def add_code_block(doc, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_shading(cell, "F8F9FA")
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    
    tcPr = cell._element.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:left w:val="single" w:sz="18" w:space="0" w:color="003366"/>\n'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>\n'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>\n'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>\n'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    
    r = p.add_run(code_text)
    r.font.name = 'Consolas'
    r.font.size = Pt(9.5)
    r.font.color.rgb = RGBColor(30, 30, 30)
    
    add_p(doc, "", space_after=4)

def add_image_box(doc, img_path, caption, width_inches=6.0):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(width_inches))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(10)
        r_cap = p_cap.add_run(caption)
        r_cap.font.name = 'Times New Roman'
        r_cap.font.size = Pt(10)
        r_cap.italic = True
        r_cap.font.color.rgb = RGBColor(80, 80, 80)

def generate_report():
    doc = docx.Document()
    
    # Page setup - standard A4, 2 cm margins
    for section in doc.sections:
        section.top_margin = Cm(2)
        section.bottom_margin = Cm(2)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(1.5)
        
    # --- ТИТУЛЬНА СТОРІНКА ---
    add_p(doc, "МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ", bold=True, size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ «ЛЬВІВСЬКА ПОЛІТЕХНІКА»", bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "Кафедра інформаційних систем та мереж", bold=False, italic=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=36)
    
    add_p(doc, "ЗВІТ", bold=True, size=20, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_p(doc, "про виконання лабораторної роботи № 9.2 (Частина 1)", bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "«Директиви препроцесора»", bold=True, size=15, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "з дисципліни", bold=False, italic=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "«Алгоритмізація та програмування»", bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=50)
    
    info_tbl = doc.add_table(rows=2, cols=2)
    info_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_tbl.columns[0].width = Inches(3.2)
    info_tbl.columns[1].width = Inches(3.2)
    
    c0 = info_tbl.cell(0, 1)
    p0 = c0.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r0 = p0.add_run("Виконав:\nстудент групи РІ-13\nШах Владислав Ігорьович\nВаріант № 32")
    r0.font.name = 'Times New Roman'
    r0.font.size = Pt(12)
    
    c1 = info_tbl.cell(1, 1)
    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r1 = p1.add_run("Прийняв:\nГригорович В.Г.")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(12)
    
    add_p(doc, "", space_after=80)
    add_p(doc, "Львів – 2026", bold=False, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)
    doc.add_page_break()
    
    # --- 1. МЕТА ТА ТЕОРЕТИЧНІ ВІДОМОСТІ ---
    add_h(doc, "1. Мета роботи та теоретичні відомості", level=1)
    add_p(doc, "Мета роботи: вивчити особливості використання директив препроцесора мови C++; навчитися розробляти та застосовувати параметризовані макровизначення (#define), організовувати включення власних заголовних файлів (#include) та керувати процесом умовної компіляції програми (#if, #else, #endif).")
    
    add_h(doc, "Теоретичні відомості:", level=2)
    add_p(doc, "1. Препроцесор C++: спеціальна підпрограма, що обробляє початковий текст програми до початку її компіляції. Усі директиви препроцесора починаються із символу # і завершуються кінцем рядка (або символом продовження рядка \\).")
    add_p(doc, "2. Макровизначення (#define): дозволяють задавати іменовані текстові константи або параметризовані шаблони коду (макроси). При виклику макросу відбувається текстова підстановка аргументів. Щоб уникнути помилок пріоритету операцій, усі параметри та весь вираз макросу обов'язково беруться у круглі дужки: #define SQR(x) ((x) * (x)).")
    add_p(doc, "3. Директиви умовної компіляції (#if, #else, #endif): дозволяють вмикати або вимикати компіляцію окремих блоків вихідного коду залежно від значення препроцесорного константного виразу. Згідно з методичними вказівками, значення сталої z, заданої через #define, безпосередньо перевіряється директивою #if (z >= 1 && z < 10). Код неактивної гілки препроцесора повністю ігнорується компілятором і не включається у виконуваний файл програми.")
    
    # --- 2. УМОВА ЗАВДАННЯ ---
    add_h(doc, "2. Умова завдання (Варіант № 32)", level=1)
    add_p(doc, "Спільна частина завдання для Частини 1 (стор. 27):")
    add_p(doc, "Використовуючи директиви умовної компіляції, макровизначення, включення власних заголовних файлів для необхідних оголошень та інші директиви, скласти програму обчислення наведених виразів. Функції max(), min(), визначення модуля (абсолютного значення), виведення результатів, логічних виразів, піднесення до степеня, визначення коренів задати у вигляді макросів. Значення змінних задаються користувачем. Директиви умовної компіляції: препроцесор на основі значення z має визначати, яка із двох зазначених в умові варіанту гілок буде компілюватися.")
    
    add_image_box(doc, os.path.join(IMG_DIR, "task_common.png"), "Рис. 1. Загальна умова до Завдання 9.2 (Частина 1) з методичних вказівок", width_inches=6.0)
    
    add_p(doc, "Індивідуальне завдання для Варіанта № 32 (стор. 31):")
    add_image_box(doc, os.path.join(IMG_DIR, "task_var32.png"), "Рис. 2. Умова Варіанта № 32 з методичних вказівок (стор. 31)", width_inches=6.0)
    
    add_h(doc, "Математичний опис функціональних залежностей:", level=2)
    add_p(doc, "Необхідно обчислити значення w за кусочною формулою:")
    add_p(doc, "Гілка 1 (активна при 1 <= z < 10):")
    add_p(doc, "    w = min^2(x + y, x + z)")
    add_p(doc, "Гілка 2 (активна при z < 1 або z >= 10):")
    add_p(doc, "    w = max(x^2, 5|y - z|)")
    
    # --- 3. СТРУКТУРНА СХЕМА ПРОГРАМИ ТА ІНСТРУКЦІЯ ПЕРЕМИКАННЯ ГІЛОК ---
    add_h(doc, "3. Структурна схема програми та інструкція перемикання гілок", level=1)
    add_image_box(doc, os.path.join(IMG_DIR, "struct.png"), "Рис. 3. Структурна схема програми з директивами препроцесора", width_inches=6.2)
    
    add_h(doc, "Де і як змінювати значення константи z (#define) для зміни активної гілки компіляції:", level=2)
    add_p(doc, "У файлі LABA-9.2.1.cpp на рядку 23 розміщено директиву визначення сталої z:")
    add_p(doc, "• Для активації ГІЛКИ 1 (1 <= z < 10, вираз: w = min^2(x+y, x+z)):\n"
                "  Задати ціле значення z у діапазоні від 1 до 9, наприклад:\n"
                "  #define z 5\n"
                "  При цьому умова #if (z >= 1 && z < 10) обчислюється препроцесором як істинна (1), і компілюється виключно блок першої гілки.")
    add_p(doc, "• Для активації ГІЛКИ 2 (z < 1 або z >= 10, вираз: w = max(x^2, 5|y-z|)):\n"
                "  Задати ціле значення z менше 1 або більше чи рівне 10, наприклад:\n"
                "  #define z 0     (або #define z 12)\n"
                "  У результаті вираз #if (z >= 1 && z < 10) обчислюється як хибний (0), і препроцесор транслює код секції #else (другу гілку).")

    # --- 4. ТЕКСТ ПРОГРАМИ ---
    add_h(doc, "4. Текст програми", level=1)
    
    add_h(doc, "4.1. Власний заголовний файл macros.h (макровизначення)", level=2)
    add_code_block(doc, 
"""#pragma once
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
#define PRINTI(w) puts("control output"); printf(#w " = %d\\n", (int)(w))
#define PRINTR(w) puts("rezult :"); printf(#w " = %f\\n", (double)(w))

// Функції для модульного тестування розрахункових виразів обох гілок
// Гілка 1 (1 <= z < 10): w = min^2(x + y, x + z)
inline double CalcBranch1(double x, double y, double z_val) {
    return SQR(MIN(x + y, x + z_val));
}

// Гілка 2 (z < 1 або z >= 10): w = max(x^2, 5|y - z|)
inline double CalcBranch2(double x, double y, double z_val) {
    return MAX(SQR(x), 5.0 * ABS(y - z_val));
}""")

    add_h(doc, "4.2. Головний файл програми LABA-9.2.1.cpp", level=2)
    add_code_block(doc, 
"""//////////////////////////////////////////////////////////////////////////////
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
// Стала величина z визначає гілку компіляції:
//   Гілка 1 (1 <= z < 10):       #define z 5    (числа від 1 до 9)
//   Гілка 2 (z < 1 або z >= 10): #define z 0    (числа < 1 або >= 10)
// ============================================================================
#define z 5

#ifndef UNIT_TESTING
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

#if (z >= 1 && z < 10)
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
#endif""")

    # --- 5. МОДУЛЬНЕ ТЕСТУВАННЯ ---
    add_h(doc, "5. Модульне тестування (UnitTest9.2.1)", level=1)
    add_p(doc, "Для перевірки коректності функціонування створених макросів MIN, MAX, SQR, ABS та розрахункових виразів для обох гілок розроблено проект автоматизованого тестування UnitTest9.2.1 за допомогою Microsoft Native Unit Test Framework:")
    
    add_code_block(doc, 
"""#include "pch.h"
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
}""")

    add_p(doc, "Результати виконання модульних тестів (усі 6 тестів пройшли успішно):")
    add_image_box(doc, os.path.join(IMG_DIR, "console_test.png"), "Рис. 4. Успішне проходження всіх тестів проекту UnitTest9.2.1", width_inches=6.0)

    # --- 6. РЕЗУЛЬТАТИ ВИКОНАННЯ ПРОГРАМИ ---
    add_h(doc, "6. Результати виконання програми", level=1)
    add_p(doc, "Програму протестовано для обох гілок шляхом зміни значення константи z у директиві препроцесора #define z:")
    add_image_box(doc, os.path.join(IMG_DIR, "console_main.png"), "Рис. 5. Результати виконання програми для Гілки 1 (z=5) та Гілки 2 (z=0)", width_inches=6.0)
    
    add_p(doc, "Зведена таблиця перевірки результатів обчислень:")
    
    tbl = doc.add_table(rows=3, cols=6)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl)
    
    headers = ["Режим / Гілка", "x", "y", "z (стала #define)", "Формула", "Результат w"]
    for i, h_text in enumerate(headers):
        cell = tbl.cell(0, i)
        set_cell_shading(cell, "003366")
        set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h_text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    data = [
        ["Гілка 1 (#define z 5)", "2.0", "3.0", "5 (1 <= z < 10)", "min^2(x+y, x+z)", "25.000000"],
        ["Гілка 2 (#define z 0)", "4.0", "2.0", "0 (z < 1)", "max(x^2, 5|y-z|)", "16.000000"]
    ]
    
    for row_idx, r_data in enumerate(data, start=1):
        bg = "FFFFFF" if row_idx % 2 != 0 else "F4F6F8"
        for col_idx, val in enumerate(r_data):
            cell = tbl.cell(row_idx, col_idx)
            set_cell_shading(cell, bg)
            set_cell_margins(cell, top=60, bottom=60, left=100, right=100)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.name = 'Consolas' if col_idx in [1, 2, 3, 5] else 'Times New Roman'
            r.font.size = Pt(10)

    add_p(doc, "", space_after=6)

    # --- 7. ПОСИЛАННЯ НА GITHUB ---
    add_h(doc, "7. Посилання на GitHub-репозиторій", level=1)
    add_p(doc, "Вихідний програмний код, макроси, юніт-тести, файл рішення Visual Studio та звіт завантажено у репозиторій:")
    add_p(doc, "https://github.com/vivjk686/LABA-9.2.1", bold=True, size=12, align=WD_ALIGN_PARAGRAPH.LEFT)

    # --- 8. ВІДПОВІДІ НА КОНТРОЛЬНІ ПИТАННЯ ---
    add_h(doc, "8. Відповіді на контрольні питання", level=1)
    
    qa = [
        ("1. Поняття та необхідність модулів.",
         "Модуль — це логічно та фізично відокремлена частина програми, яка містить опис інтерфейсу (у .h файлі) та реалізацію (у .cpp файлі). Розбиття на модулі спрощує тестування, дозволяє організувати паралельну розробку та скорочує час повторної компіляції великих проектів."),
        
        ("2. Збирання файлів з текстами програм.",
         "Збирання виконується препроцесором за допомогою директиви #include, яка замінює рядок директиви повним вмістом вказаного файлу. Використовуються форми #include <...> (для системних бібліотек) та #include \"...\" (для власних файлів проекту)."),
        
        ("3. Збирання об'єктних модулів.",
         "Збирання об'єктних модулів (.obj) у виконуваний файл (.exe) або бібліотеку (.lib/.dll) здійснює лінкер (компонувальник). Він зв'язує виклики функцій з їхніми фактичними адресами у відповідних модулях."),
        
        ("4. Директиви препроцесора.",
         "Директиви препроцесора — це спеціальні команди компілятору, що виконуються до початку компіляції. До них належать: #define (макровизначення), #include (включення файлів), #ifdef / #ifndef / #if / #else / #endif (умовна компіляція), #pragma (специфічні вказівки для компілятора)."),
        
        ("5. Відокремлення інтерфейсу від реалізації.",
         "Інтерфейсна частина містить прототипи функцій, оголошення типів даних та extern-змінних і розміщується у .h-файлах. Реалізація (тіла функцій, виділення пам'яті) поміщається у .cpp-файли. Це забезпечує інкапсуляцію та приховування деталей реалізації."),
        
        ("6. Простори імен (namespaces).",
         "Простори імен дозволяють локалізувати імена ідентифікаторів (змінних, функцій, типів), запобігаючи конфліктам однакових імен, які можуть зустрічатися у різних модулях проекту.")
    ]
    
    for q, a in qa:
        add_p(doc, q, bold=True, size=11, space_before=4, space_after=2)
        add_p(doc, a, bold=False, size=11, space_before=0, space_after=6)

    # --- 9. ВИСНОВКИ ---
    add_h(doc, "9. Висновки", level=1)
    add_p(doc, "Під час виконання лабораторної роботи № 9.2 (Частина 1) було здобуто та практично закріплено навички роботи з макровизначеннями та директивами препроцесора мови C++.")
    add_p(doc, "1. Створено власний заголовний файл macros.h, де реалізовано параметризовані макроси MIN(a,b), MAX(a,b), SQR(x), ABS(x), PRINTI(w) та PRINTR(w), що продемонструвало переваги макропідстановок.")
    add_p(doc, "2. Реалізовано умовну компіляцію за допомогою директив #define, #if, #else, #endif. Препроцесор за числовим значенням константи #define z автоматично обирає відповідну розрахункову гілку математичного виразу варіанта 32.")
    add_p(doc, "3. Написано проект автоматизованого модульного тестування UnitTest9.2.1 (6 тестів), що повністю підтвердило правильність роботи макросів та математичну точність обчислень.")

    doc.save(OUT_DOCX)
    print("Report saved successfully:", OUT_DOCX)

if __name__ == "__main__":
    generate_report()
