field=[[' ']*3 for n in range(3)]
def greeting():
    print("Приветствуем вас в игре крестики-нолики")
    print("формат ввода: x y")
    print("x - номер строки")
    print("y - номер столбца")

def output_to_the_screen():
    print("  0 1 2")
    for i in range(3):
        row_info=" ".join(field[i])
        print(f"{i} {row_info}")


def ask_cords():
    while True:
        cords = input("Ваш ход: ").split()
        if len(cords)!=2:
            print("Введите две координаты!")
            continue
        x, y = cords
        if not(x.isdigit()) and not(y.isdigit()):
            print("Введите координаты")
            continue
        x,y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона!")
            continue
        if field[x][y] != ' ':
            print("Клетка занята!")
            continue
        return x,y
    
def win():
    win_cords = (((0, 0),(0, 1),(0, 2)),((1, 0),(1, 1),(1, 2)),((2, 0),(2, 1),(2, 2)),
                ((0, 2),(1, 1),(2, 0)),((0, 0),(1, 1),(2, 2)),((0, 0),(1, 0),(2, 0)),
                ((0, 1),(1, 1),(2, 1)),((0, 2),(1, 2),(2, 2)))
    for i in win_cords:
        symbols=[]
        for b in i:
            symbols.append(field[b[0]][b[1]])
        if symbols == ["X","X","X"]:
            print("Победил крестик!")
            return True
        elif symbols == ["0","0","0"]:
            print("Победил нолик!")
            return True
    return False

greeting()

num = 0
while True:
    num += 1
    output_to_the_screen()
    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print("Холит нолик")
    x,y = ask_cords()
    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if win():
        break
    if num==9:
        print("Ничья!")
        break