#test_lcd.py

def lcd(a,b):
    if a%b == 0:
        return b
    else:
        return lcd(b,a%b)


print(lcd(2*2*3*3*5*7*7,2*3*3*3*7*11))
print(2*3*3*7)
