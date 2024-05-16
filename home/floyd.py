import math


def get_path(P, u, v):
    path = [u]
    while u != v:
        u = P[u][v]
        path.append(u)

    return path

V =[
[0	,14	,math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,],
[14,	0	,13,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,],
[math.inf,	math.inf,13,0,14,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,],
[math.inf,	math.inf,	14	,0	,18	,math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,],
[math.inf,	math.inf,	math.inf,	18,	0,	8	,math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,],
[math.inf,	math.inf,	math.inf,	math.inf,	8,	0	,23	,math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	23,0	,9	,math.inf,	math.inf,	math.inf,	math.inf,	math.inf,],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	9,	0	,4	,math.inf,	math.inf,	math.inf,	math.inf,],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	4	,0	,17	,math.inf,	math.inf,	math.inf,],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	17,	0	,12	,math.inf,	math.inf,],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	12	,0	,12,	math.inf,],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	12	,0	,133,],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	133	,0],
]
additional_stations = [
    "Qo'l", "Orzu", "Chodak", "Kon", "Temiryo'obod", "Qo'shminor", "Pop", "Chust", 
    "To'raqo'rg'on", "Raustan", "Namangan", "Chortoq", "Uychi", "Uchqo'rg'on", "Haqqulabod",
    "Paytug`", "Qordaryo", "Andijon-2", "Yangi Andijon", "Jalaquduq", "Savay", "Karsu-Uzbek",
    "Xonobod", "Andijon-1", "Axtachi", "Asaka", "Quvasoy", "Oxunboboyev", "Marg`ilon", "Oltariq",
    "Furqat", "Kakir", "Qo'qon NP", "Qo'qon MP", "Yaypan", "Rapkan", "Arikbashi", "Suvanobod", "Buvayda"
]


# V = [[0, 2, math.inf, 3, 1, math.inf, math.inf, 10],
#      [2, 0, 4, math.inf, math.inf, math.inf, math.inf, math.inf],
#      [math.inf, 4, 0, math.inf, math.inf, math.inf, math.inf, 3],
#      [3, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 8],
#      [1, math.inf, math.inf, math.inf, 0, 2, math.inf, math.inf],
#      [math.inf, math.inf, math.inf, math.inf, 2, 0, 3, math.inf],
#      [math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, 1],
#      [10, math.inf, 3, 8, math.inf, math.inf, 1, 0],
# ]

N = len(V)                       # число вершин в графе
P = [[v for v in range(N)] for u in range(N)]       # начальный список предыдущих вершин для поиска кратчайших маршрутов

for k in range(N):
    for i in range(N):
        for j in range(N):
            d = V[i][k] + V[k][j]
            if V[i][j] > d:
                V[i][j] = d
                P[i][j] = k     # номер промежуточной вершины при движении от i к j

# нумерацця вершин начинается с нуля
start = 1
end = 4
print( get_path(P, end, start),P)