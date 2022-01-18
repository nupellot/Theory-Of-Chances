import pyautogui as pg

# Переход в начало отчёта GPSS   1
pg.moveTo(215, 90, 0.5)
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
pg.moveTo(1048, 259, 0.5)
pg.click(clicks = 4)
# Вставляем значение.
pg.keyDown('ctrl')
pg.press('v')
pg.keyUp('ctrl')

# Переход в начало отчёта GPSS      2
pg.moveTo(215, 90, 0.5)
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
pg.moveTo(1048, 259, 0.5)
pg.click(clicks = 1)
pg.press('right', presses = 1)
# Вставляем значение.
pg.keyDown('ctrl')
pg.press('v')
pg.keyUp('ctrl')

# Переход в начало отчёта GPSS     3
pg.moveTo(215, 90, 0.5)
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
pg.moveTo(1048, 259, 0.5)
pg.click(clicks = 1)
pg.press('right', presses = 1)
# Вставляем значение.
pg.keyDown('ctrl')
pg.press('v')
pg.keyUp('ctrl')

# Переход в начало отчёта GPSS         4
pg.moveTo(215, 90, 0.5)
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
pg.moveTo(1048, 259, 0.5)
pg.click(clicks = 1)
pg.press('right', presses = 1)
# Вставляем значение.
pg.keyDown('ctrl')
pg.press('v')
pg.keyUp('ctrl')
