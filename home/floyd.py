import math


def get_path(P, u, v):
    path = [u]
    while u != v:
        u = P[u][v]
        path.append(u)

    return path

V =[
[0,	21.3,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[21.3,	0,	22.7,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	22.7,	0,	14.3,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	14.3,	0,	13.2,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	13.2,	0,	14.9,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	14.9,	0,	20.6,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	20.6,	0,	8.3,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	24.7,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	8.3,	0,	23.1,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	23.1,	0,	9.3,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	9.3,	0,	4.9,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	4.9,	0,	17.5,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	17.5,	0,	12.4,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	12.4,	0,	12.1,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	12.1,	0,	25,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	25,	0,	13,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	13,	0,	11,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	11,	0,	7.7,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	7.7,	0,	12,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	12,	0,	17.5,	math.inf,	math.inf,	math.inf,	12.1,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	17.5,	0,	10.5,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	10.5,	0,	9.2,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	18.9,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	9.2,	0,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	14.3,	0,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	5.7,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	12.1,	math.inf,	math.inf,	math.inf,	math.inf,	0,	38,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	38,	0,	7.2,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	7.2,	0,	15.3,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	15.3,	0,	30.8,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	30.8,	0,	3.3,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	3.3,	0,	18.4,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	18.4,	0,	25.4,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	25.4,	0,	14.3,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	14.3,	0,	11,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	11,	0,	1.8,	15.7,	math.inf,	math.inf,	math.inf,	21.8,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	1.8,	0,	13.4,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	15.7,	13.4,	0,	12.4,	math.inf,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	12.4,	0,	10,	math.inf,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	10,	0,	7.7,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	7.7,	0,	math.inf,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	24.7,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	21.8,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	0,	math.inf,	],
[math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	18.9,	math.inf,	5.7,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	math.inf,	0,	],
]
additional_stations = [
    "Qo'l", "Orzu", "Chodak", "Kon", "Temiryo'obod", "Qo'shminor", "Pop", "Chust", 
    "To'raqo'rg'on", "Raustan", "Namangan", "Chortoq", "Uychi", "Uchqo'rg'on", "Haqqulabod",
    "Paytug`", "Qordaryo", "Andijon-2", "Yangi Andijon", "Jalaquduq", "Savay", "Karsu-Uzbek",
    "Xonobod", "Andijon-1", "Axtachi", "Asaka", "Quvasoy", "Oxunboboyev", "Marg`ilon", "Oltariq",
    "Furqat", "Kakir", "Qo'qon NP", "Qo'qon MP", "Yaypan", "Rapkan", "Arikbashi", "Suvanobod", "Buvayda"
]



N = len(V)                       # число вершин в графе
P = [[v for v in range(N)] for u in range(N)]       # начальный список предыдущих вершин для поиска кратчайших маршрутов
# Edit_V = V  #Bu stansiyalargacha bolgan masofani to'liq qiymatini  saqlaydi o'zida
def Edit_V():
    Edit_V = V
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d = V[i][k] + V[k][j]
                d = round(d, 1)
                if V[i][j] > d:
                    Edit_V[i][j] = d
                    # V[i][j] = d
                    # P[i][j] = k   
    return Edit_V



def get_path2(station_start, stations_finish):
    N = len(stations_finish)
    station_dictans = {}
    for i in range(N):
        station_dictans[additional_stations[station_start]] = int(stations_finish[i])
    return station_dictans
    