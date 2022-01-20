import pyautogui as pg

for i in range(1, 5):
    # Переход к window
    pg.moveTo(265, 40)
    pg.click()
    # Переход к нужному окну
    pg.moveTo(270, 170)
    pg.click()
    # Переход в начало окна.
    pg.moveTo(215, 90)
    pg.click(clicks = 1)
    amountOfSymbols = 1
    if (i > 10): amountOfSymbols += 1
    pg.press('backspace', presses = amountOfSymbols)
    print('Lol')
    pg.typewrite(str(i))
    pg.hotkey('alt', 'ctrl', 'r')
    # Переход в начало отчёта GPSS   1
    pg.moveTo(215, 90)
    pg.doubleClick()
    pg.press('down', presses = 39)
    pg.press('right', presses = 27)
    # Выделяем значение.
    pg.keyDown('shift')
    pg.press('right', presses = 5)
    pg.keyUp('shift')
    # Копируем значение.
    pg.keyDown('ctrl')
    pg.press('c')
    pg.keyUp('ctrl')
    pg.click()
    # Переходим в окно excel'a.
    pg.moveTo(995, 122)
    pg.click(clicks = 4)
    pg.press('down', presses = i - 1)
    # Вставляем значение.
    pg.keyDown('ctrl')
    pg.press('v')
    pg.keyUp('ctrl')

    # Переход в начало отчёта GPSS      2
    pg.moveTo(215, 90)
    pg.click(clicks = 3)
    pg.press('down', presses = 40)
    pg.press('right', presses = 27)
    # Выделяем значение.
    pg.keyDown('shift')
    pg.press('right', presses = 5)
    pg.keyUp('shift')
    # Копируем значение.
    pg.keyDown('ctrl')
    pg.press('c')
    pg.keyUp('ctrl')
    pg.click()
    # Переходим в окно excel'a.
    pg.moveTo(995, 122)
    pg.click(clicks = 1)
    # pg.press('down', presses = i - 1)
    pg.press('right', presses = 1)
    # Вставляем значение.
    pg.keyDown('ctrl')
    pg.press('v')
    pg.keyUp('ctrl')
    # Переход в начало отчёта GPSS     3
    pg.moveTo(215, 90)
    pg.click(clicks = 3)
    pg.press('down', presses = 44)
    pg.press('right', presses = 46)
    # Выделяем значение.
    pg.keyDown('shift')
    pg.press('right', presses = 5)
    pg.keyUp('shift')
    # Копируем значение.
    pg.keyDown('ctrl')
    pg.press('c')
    pg.keyUp('ctrl')
    pg.click()
    # Переходим в окно excel'a.
    pg.moveTo(995, 122)
    pg.click(clicks = 1)
    # pg.press('down', presses = i - 1)
    pg.press('right', presses = 1)
    # Вставляем значение.
    pg.keyDown('ctrl')
    pg.press('v')
    pg.keyUp('ctrl')

    # Переход в начало отчёта GPSS         4
    pg.moveTo(215, 90)
    pg.click(clicks = 3)
    pg.press('down', presses = 45)
    pg.press('right', presses = 46)
    # Выделяем значение.
    pg.keyDown('shift')
    pg.press('right', presses = 5)
    pg.keyUp('shift')
    # Копируем значение.
    pg.keyDown('ctrl')
    pg.press('c')
    pg.keyUp('ctrl')
    pg.click()
    # Переходим в окно excel'a.
    pg.moveTo(995, 122)
    pg.click(clicks = 1)
    # pg.press('down', presses = i - 1)
    pg.press('right', presses = 1)
    # Вставляем значение.
    pg.keyDown('ctrl')
    pg.press('v')
    pg.keyUp('ctrl')
