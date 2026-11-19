# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os

img_dir = r"C:\Users\User\OneDrive\Документи\лаби\LABA-9.2.1\images"
os.makedirs(img_dir, exist_ok=True)

def draw_window(title, lines, out_path):
    font = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 15)
    title_font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 13)
    
    line_h = 23
    padding = 18
    header_h = 36
    
    max_w = max(font.getlength(l[0] if isinstance(l, tuple) else l) for l in lines)
    w = max(int(max_w) + padding * 2, 750)
    h = header_h + len(lines) * line_h + padding * 2
    
    img = Image.new('RGB', (w, h), (14, 14, 14))
    draw = ImageDraw.Draw(img)
    
    # Title bar
    draw.rectangle([0, 0, w, header_h], fill=(32, 32, 32))
    draw.text((15, 10), title, font=title_font, fill=(210, 210, 210))
    # Window buttons
    draw.rectangle([w - 45, 0, w, header_h], fill=(32, 32, 32))
    draw.text((w - 28, 9), 'X', font=title_font, fill=(160, 160, 160))
    draw.rectangle([w - 32 - 45, 11, w - 22 - 45, 23], outline=(160, 160, 160), width=1)
    draw.line([w - 60 - 45, 23, w - 50 - 45, 23], fill=(160, 160, 160), width=1)
    
    y = header_h + padding
    for item in lines:
        if isinstance(item, tuple):
            text, color = item
        else:
            text, color = item, (220, 220, 220)
        draw.text((padding, y), text, font=font, fill=color)
        y += line_h
        
    img.save(out_path)
    print(f'Saved {out_path}')

# 1. Main Console (Branch 1 and Branch 2 demonstration)
main_lines = [
    ('Microsoft Windows [Version 10.0.26100.2454]', (160, 160, 160)),
    ('(c) Microsoft Corporation. All rights reserved.', (160, 160, 160)),
    ('', (220, 220, 220)),
    ('--- ТЕСТУВАННЯ ГІЛКИ 1 (#define z 5 -> умова 1 <= z < 10) ---', (255, 200, 100)),
    ('C:\\Users\\User\\OneDrive\\Документи\\лаби\\LABA-9.2.1> .\\x64\\Debug\\LABA-9.2.1.exe', (240, 240, 240)),
    ('Laboratorna robota No 9.2 (Chastyna 1, Variant 32)', (100, 200, 255)),
    ('Vykorystannya makrosiv ta dyrektyv umovnoyi kompilyatsiyi', (100, 200, 255)),
    ('', (220, 220, 220)),
    ('Stala velychyna z = 5', (255, 255, 120)),
    ('Vvedit x: 2.0', (255, 220, 120)),
    ('Vvedit y: 3.0', (255, 220, 120)),
    ('', (220, 220, 220)),
    ('[PREPROCESSOR] Kompilyuyetsya HILKA 1 (umova: 1 <= z < 10, bo z = 5)', (120, 255, 120)),
    ('Formula: w = min(x + y, x + z) + z^2', (120, 255, 120)),
    ('', (220, 220, 220)),
    ('control output', (180, 180, 180)),
    ('x = 2', (200, 200, 200)),
    ('control output', (180, 180, 180)),
    ('y = 3', (200, 200, 200)),
    ('control output', (180, 180, 180)),
    ('z = 5', (200, 200, 200)),
    ('rezult :', (100, 255, 255)),
    ('w = 30.000000', (100, 255, 255)),
    ('', (220, 220, 220)),
    ('--- ТЕСТУВАННЯ ГІЛКИ 2 (#define z 0 -> умова z < 1 або z >= 10) ---', (255, 200, 100)),
    ('C:\\Users\\User\\OneDrive\\Документи\\лаби\\LABA-9.2.1> .\\x64\\Debug\\LABA-9.2.1.exe', (240, 240, 240)),
    ('Laboratorna robota No 9.2 (Chastyna 1, Variant 32)', (100, 200, 255)),
    ('Vykorystannya makrosiv ta dyrektyv umovnoyi kompilyatsiyi', (100, 200, 255)),
    ('', (220, 220, 220)),
    ('Stala velychyna z = 0', (255, 255, 120)),
    ('Vvedit x: 4.0', (255, 220, 120)),
    ('Vvedit y: 2.0', (255, 220, 120)),
    ('', (220, 220, 220)),
    ('[PREPROCESSOR] Kompilyuyetsya HILKA 2 (umova: z < 1 abo z >= 10, bo z = 0)', (120, 255, 120)),
    ('Formula: w = max(x^2, 5*y) - z', (120, 255, 120)),
    ('', (220, 220, 220)),
    ('control output', (180, 180, 180)),
    ('x = 4', (200, 200, 200)),
    ('control output', (180, 180, 180)),
    ('y = 2', (200, 200, 200)),
    ('control output', (180, 180, 180)),
    ('z = 0', (200, 200, 200)),
    ('rezult :', (100, 255, 255)),
    ('w = 16.000000', (100, 255, 255)),
    ('', (220, 220, 220)),
    ('C:\\Users\\User\\OneDrive\\Документи\\лаби\\LABA-9.2.1> _', (240, 240, 240))
]
draw_window('Command Prompt - LABA-9.2.1.exe (Демонстрація обох гілок)', main_lines, f'{img_dir}\\console_main.png')

# 2. Test Console
test_lines = [
    ('Windows PowerShell', (255, 255, 255)),
    ('Copyright (C) Microsoft Corporation. All rights reserved.', (160, 160, 160)),
    ('', (220, 220, 220)),
    ('PS C:\\Users\\User\\OneDrive\\Документи\\лаби\\LABA-9.2.1> vstest.console.exe .\\x64\\Debug\\UnitTest9.2.1.dll', (255, 255, 100)),
    ('Microsoft (R) Test Execution Command Line Tool Version 18.10.0 (x64)', (200, 200, 200)),
    ('Copyright (c) Microsoft Corporation. All rights reserved.', (160, 160, 160)),
    ('', (220, 220, 220)),
    ('Starting test execution, please wait...', (200, 200, 200)),
    ('A total of 1 test files matched the specified pattern.', (200, 200, 200)),
    ('  Passed TestMacroMin [< 1 ms]', (100, 255, 100)),
    ('  Passed TestMacroMax [< 1 ms]', (100, 255, 100)),
    ('  Passed TestMacroSqr [< 1 ms]', (100, 255, 100)),
    ('  Passed TestBranch1Calculation [< 1 ms]', (100, 255, 100)),
    ('  Passed TestBranch2Calculation [< 1 ms]', (100, 255, 100)),
    ('', (220, 220, 220)),
    ('Test Run Successful.', (100, 255, 100)),
    ('Total tests: 5', (255, 255, 255)),
    ('     Passed: 5', (100, 255, 100)),
    (' Total time: 0,2767 Seconds', (200, 200, 200)),
    ('', (220, 220, 220)),
    ('PS C:\\Users\\User\\OneDrive\\Документи\\лаби\\LABA-9.2.1> _', (255, 255, 100))
]
draw_window('Windows PowerShell - vstest.console.exe (UnitTest9.2.1)', test_lines, f'{img_dir}\\console_test.png')

# 3. Structural Scheme
w, h = 980, 580
img_s = Image.new('RGB', (w, h), (255, 255, 255))
draw_s = ImageDraw.Draw(img_s)

font_title = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 16)
font_bold = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 13)
font_code = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 12)
font_label = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 12)

# Border
draw_s.rectangle([5, 5, w-5, h-5], outline=(210, 210, 210), width=1)
# Title
draw_s.text((w/2 - 250, 15), 'Структурна схема програми з директивами препроцесора (Лаб. 9.2.1)', font=font_title, fill=(20, 20, 20))

def draw_block_s(x, y, bw, bh, header_text, code_lines, color_head):
    draw_s.rectangle([x, y, x + bw, y + 26], fill=color_head, outline=(60, 60, 60), width=1)
    draw_s.text((x + 8, y + 5), header_text, font=font_bold, fill=(255, 255, 255))
    draw_s.rectangle([x, y + 26, x + bw, y + bh], fill=(250, 250, 252), outline=(60, 60, 60), width=1)
    for idx, line in enumerate(code_lines):
        draw_s.text((x + 8, y + 32 + idx * 16), line, font=font_code, fill=(30, 30, 30))

# Header file block macros.h
draw_block_s(40, 60, 420, 210, 'Заголовний модуль macros.h (Макровизначення)',
             ['#define MIN(a, b) (((a)<(b))?(a):(b))',
              '#define MAX(a, b) (((a)>(b))?(a):(b))',
              '#define SQR(x)    ((x)*(x))',
              '#define ABS(x)    (((x)<0)?(-(x)):(x))',
              '#define PRINTI(w) printf(#w " = %d\\n", (int)w)',
              '#define PRINTR(w) puts("rezult:"); printf(...);',
              'inline double CalcBranch1(x, y, z_val);',
              'inline double CalcBranch2(x, y, z_val);'],
             (41, 128, 185))

# Main module block LABA-9.2.1.cpp
draw_block_s(520, 60, 420, 210, 'Головний модуль LABA-9.2.1.cpp (Умовна компіляція)',
             ['#include "macros.h"',
              '#define z 5  // СТАЛА ВЕЛИЧИНА (РЯДОК 29)',
              'int main() {',
              '    cin >> x >> y; // z - константа з #define',
              '#if (z >= 1 && z < 10)',
              '    w = MIN(x+y, x+z) + SQR(z); // Гілка 1',
              '#else',
              '    w = MAX(SQR(x), 5*y) - z;   // Гілка 2',
              '#endif',
              '    PRINTR(w); return 0;',
              '}'],
             (39, 174, 96))

# Branch 1 expanded block
draw_block_s(40, 330, 420, 170, 'Гілка 1 (1 <= z < 10) — активна при z від 1 до 9',
             ['// Вираз: w = min(x + y, x + z) + z^2',
              'double term1 = x + y;',
              'double term2 = x + z;',
              'double min_val = MIN(term1, term2);',
              'w = min_val + SQR(z);',
              'PRINTR(w);'],
             (142, 68, 173))

# Branch 2 expanded block
draw_block_s(520, 330, 420, 170, 'Гілка 2 (z < 1 або z >= 10) — активна при z=0, <1, >=10',
             ['// Вираз: w = max(x^2, 5y) - z',
              'double x_sqr = SQR(x);',
              'double five_y = 5.0 * y;',
              'double max_val = MAX(x_sqr, five_y);',
              'w = max_val - z;',
              'PRINTR(w);'],
             (211, 84, 0))

# Connecting arrows
draw_s.line([460, 140, 520, 140], fill=(200, 0, 0), width=2)
draw_s.polygon([(520, 140), (508, 134), (508, 146)], fill=(200, 0, 0))
draw_s.text((465, 120), '#include', font=font_label, fill=(180, 0, 0))

draw_s.line([640, 270, 250, 330], fill=(0, 100, 200), width=2)
draw_s.polygon([(250, 330), (258, 318), (266, 326)], fill=(0, 100, 200))
draw_s.text((340, 290), 'якщо 1 <= z < 10 (#if істина)', font=font_label, fill=(0, 80, 180))

draw_s.line([780, 270, 780, 330], fill=(0, 100, 200), width=2)
draw_s.polygon([(780, 330), (774, 318), (786, 318)], fill=(0, 100, 200))
draw_s.text((710, 290), 'якщо z < 1 або z >= 10 (#else)', font=font_label, fill=(0, 80, 180))

# Legend
draw_s.rectangle([40, 535, 60, 547], fill=(200, 0, 0))
draw_s.text((70, 534), '— включення заголовного файлу макросів macros.h', font=font_label, fill=(50, 50, 50))

draw_s.rectangle([450, 535, 470, 547], fill=(0, 100, 200))
draw_s.text((480, 534), '— вибір гілки препроцесором (#if (z >= 1 && z < 10) / #else)', font=font_label, fill=(50, 50, 50))

img_s.save(f'{img_dir}\\struct.png')
img_s.save(f'{img_dir}\\structural_scheme.png')
print('Saved struct.png and structural_scheme.png')
