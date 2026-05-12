import random
def tim_o_trong(ma_tran):
    for i in range(3):
        for j in range(3):
            if ma_tran[i][j] == 0:
                return i, j
def luat(x, y):
    if x == 0 and y == 0:
        return ["phai", "xuong"]
    elif x == 1 and y == 0:
        return ["len", "phai", "xuong"]
    elif x == 2 and y == 0:
        return ["len", "phai"]
    elif x == 0 and y == 1:
        return ["trai", "phai", "xuong"]
    elif x == 1 and y == 1:
        return ["len", "xuong", "trai", "phai"]
    elif x == 2 and y == 1:
        return ["len", "trai", "phai"]
    elif x == 1 and y == 2:
        return ["len", "trai", "xuong"]
    elif x == 0 and y == 2:
        return ["trai", "xuong"]
    elif x == 2 and y == 2:
        return ["len", "trai"]
def action(ma_tran):
    x, y = tim_o_trong(ma_tran)
    hanh_dong = luat(x, y)
    return random.choice(hanh_dong)

MA_TRAN = [
    [1,2,3],
    [4,5,6],
    [0,7,8]
]
KETQUA = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]
SO_LAN = 0
while ((MA_TRAN != KETQUA) and (SO_LAN < 10)):
    SO_LAN += 1
    (x, y) = tim_o_trong(MA_TRAN)
    HUONG_DI = action(MA_TRAN)
    print("hanh dong lan ", SO_LAN, ": ", HUONG_DI)
    if(HUONG_DI == "len"):
        MA_TRAN[x][y], MA_TRAN[x-1][y] = MA_TRAN[x-1][y], MA_TRAN[x][y]
    elif(HUONG_DI == "xuong"):
        MA_TRAN[x][y], MA_TRAN[x+1][y] = MA_TRAN[x+1][y], MA_TRAN[x][y]
    elif(HUONG_DI == "trai"):     
        MA_TRAN[x][y], MA_TRAN[x][y-1] = MA_TRAN[x][y-1], MA_TRAN[x][y]
    elif(HUONG_DI == "phai"):    
        MA_TRAN[x][y], MA_TRAN[x][y+1] = MA_TRAN[x][y+1], MA_TRAN[x][y]
    print("ma tran sau khi di chuyen: ", MA_TRAN)
    if(SO_LAN == 10):
        print("Da dat toi so lan cho phep, ket thuc chuong trinh")