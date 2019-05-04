from math import pi


def membership(x, x_, x_med=0.0):
    """
    Funcion usada para calcular en grado de pertenencia a un conjunto borroso
    :param x: absisas, cualquier valor del universo del discurso
    :param x_: vector, extremos del soporte
    :param x_med: punto medio (punto para el cual la pertenencia es maxima (1))
    :return y: ordenadas o grado de pertenencia
    """
    y = [0, 1]  # Valor minimo y maximo de pertenencia
    if x_med == 0:
        x_med = (x_[0] + x_[1]) / 2
    if x_[0] <= x <= x_med:  # p_1 = [x_i, 0] , p_2 = [x_med, 1]
        y_ = (y[1]-y[0]) * (x - x_[0]) / (x_med - x_[0]) + y[0]
    elif x_med < x <= x_[1]:  # p_1 = [x_med, 1] , p_2 = [x_f, 0]
        y_ = (y[0] - y[1]) * (x - x_med) / (x_[1] - x_med) + y[1]
    else:
        y_ = 0
    return y_


def support():
    """
    Funcion para generar los soportes de mis conjuntos borrosos
    :return sup_pos + sup_vel: devuelve los soportes para posicion y velocidad
    """

    # Defino soportes para la posicion
    sup_pos = []
    ang = 0.175  # limite para el soporte de Z
    sol = 0.4
    sup_pos.append([-pi-0.1, -pi / 2])                      # pos_sup_MN
    sup_pos.append([-(1 + sol) * pi / 2, -ang * sol])   # pos_sup_N
    sup_pos.append([-ang, ang])                         # pos_sup_Z
    sup_pos.append([sol * ang, (1 + sol) * pi / 2])     # pos_sup_P
    sup_pos.append([pi / 2, pi+0.1])                        # pos_sup_MP

    # ----------------------------------------------------------------

    # Defino soportes para la velocidad
    sup_vel = []
    vel_z = 6  # limite para el soporte de V
    sup_vel.append([-15, -9])                       # vel_sup_MN
    sup_vel.append([-(1 + sol) * 9, -vel_z * sol])  # vel_sup_N
    sup_vel.append([-vel_z, vel_z])                 # vel_sup_Z
    sup_vel.append([vel_z * ang, (1 + sol) * 9])    # vel_sup_P
    sup_vel.append([9, 15])                         # vel_sup_MP

    return sup_pos + sup_vel


def borrosificador(x):
    """
    Convierte los valores de posicion y velocidad de entrada nitida en valores [MN, N, Z, P, MP] borrosos
    :param x: [Posicion, velocidad] ambos son nitidos
    :return pos + vel: valores borrosos para [pos_MN, pos_N, pos_Z, pos_P, pos_MP,
                                                vel_MN, vel_N, vel_Z, vel_P, vel_MP]
    """
    pos = []
    vel = []
    sup = support() # obtengo los soportes de los conjuntos borrosos

    med_pos_N = (sup[1][1] + sup[1][0]) * 0.3 / 2
    med_pos_P = (sup[3][1] + sup[3][0]) * 0.3 / 2

    med_vel_N = (sup[6][1] + sup[6][1]) * 0.7 / 2
    med_vel_P = (sup[8][1] + sup[8][1]) * 0.7 / 2

    # -------------------------------------------------
    # -   VALORES DE LA PARTICION BORROSA POSICION    -
    # -------------------------------------------------

    pos.append(membership(x[0], sup[0]))
    pos.append(membership(x[0], sup[1], med_pos_N))
    pos.append(membership(x[0], sup[2]))
    pos.append(membership(x[0], sup[3], med_pos_P))
    pos.append(membership(x[0], sup[4]))

    # -------------------------------------------------
    # -   VALORES DE LA PARTICION BORROSA VELOCIDAD   -
    # -------------------------------------------------

    vel.append(membership(x[1], sup[5]))
    vel.append(membership(x[1], sup[6], med_vel_N))
    vel.append(membership(x[1], sup[7]))
    vel.append(membership(x[1], sup[8], med_vel_P))
    vel.append(membership(x[1], sup[9]))

    return pos + vel


def motor_inferencia(x):
    """
    En esta funcion se agraga la base de reglas y se infiere el resultado
    :param x: vector con los valores de pertenencia. En este caso [P_MN, P_N, P_Z, P_P, P_MP, V_MN, V_N, V_Z, V_P, VMP]
    :return f: devuelve un unico conjunto borroso de salida. En este caso Fuerza
    """

    # Defino mis operaciones borrosas
    AND = min  # Tambien se llama conjuncion o interseccion
    OR = max    # Tambien se llama disyuncion o union
    # FUERZA = min  # Elijo la conjuncion. Tambien se pueden usar la disyuncion

    # --------------------------------------------------------
    # - CALCULO DEL VALOR DE PERTENENCIA DE LOS ANTECEDENTES -
    # --------------------------------------------------------

    # Guardo los antecedentes en las variables
    A_MN = []
    A_N = []
    A_Z = []
    A_P = []
    A_MP = []

    # Fila 0: P is MN and
    A_MP.append(AND(x[0], x[5]))  # V is MN # then F is MP
    A_MP.append(AND(x[0], x[6]))  # V is N # then F is MP
    A_MP.append(AND(x[0], x[7]))  # V is Z # then F is MP
    A_MP.append(AND(x[0], x[8]))  # V is P # then F is MP
    A_MP.append(AND(x[0], x[9]))  # V is MP # then F is MP

    # Fila 1: P is N and
    A_MN.append(AND(x[1], x[5]))  # V is MN # then F is MN
    A_MN.append(AND(x[1], x[6]))  # V is N # then F is MN
    A_N.append(AND(x[1], x[7]))   # V is Z # then F is N
    A_N.append(AND(x[1], x[8]))   # V is P # then F is N
    A_N.append(AND(x[1], x[9]))   # V is MP # then F is N

    # Fila 2: P is Z and
    A_MN.append(AND(x[2], x[5]))  # V is MN # then F is MN
    A_N.append(AND(x[2], x[6]))   # V is N # then F is N
    A_Z.append(AND(x[2], x[7]))   # V is Z # then F is Z
    A_P.append(AND(x[2], x[8]))   # V is P # then F is P
    A_MP.append(AND(x[2], x[9]))  # V is MP # then F is MP

    # Fila 3: P is P and
    A_P.append(AND(x[3], x[5]))   # V is MN # then F is P
    A_P.append(AND(x[3], x[6]))   # V is N # then F is P
    A_P.append(AND(x[3], x[7]))   # V is Z # then F is P
    A_MP.append(AND(x[3], x[8]))  # V is P # then F is MP
    A_MP.append(AND(x[3], x[9]))  # V is MP # then F is MP

    # Fila 4: P is MP and
    A_MN.append(AND(x[4], x[5]))  # V is MN # then F is MN
    A_MN.append(AND(x[4], x[6]))  # V is N # then F is MN
    A_MN.append(AND(x[4], x[7]))  # V is Z # then F is MN
    A_MN.append(AND(x[4], x[8]))  # V is P # then F is MN
    A_MN.append(AND(x[4], x[9]))  # V is MP # then F is MN

    # ------------------------------------------------------------------------------------------
    # -           COMBINACION DE LOS ANTECEDENTES Y RESOLUCION DE LA IMPLICACION               -
    # ------------------------------------------------------------------------------------------

    #   [  F_MN,     F_N,     F_Z,     F_P,     F_MP  ]
    F = [OR(A_MN), OR(A_N), OR(A_Z), OR(A_P), OR(A_MP)]

    return F


def desborrosificador(f):
    """
    Desborrosificador por media de centros (Weighted Average)
    :param f:
    :return num / den:
    """
    s_f = [3*[-11, -5], 3*[-7, -1], 3*[-3, 3], 3*[1, 7], 3*[5, 11]]

    num = 0
    den = 0
    for i, y in enumerate(f):
        med = (s_f[i][1] + s_f[i][0]) / 2
        num += y * med
        den += y

    return num / den


def control_difuso(x):
    """
    Controlador difuso
    :param x: vector de estado actual (nitido)
    :return c: fuerza de control (nitido)
    """
    a = borrosificador([x[0], x[1]])
    b = motor_inferencia(a)
    c = desborrosificador(b)
    return c


# if __name__ == '__main__':
#     h = support()
#     print(h[0])
#     print(h[0][0], h[0][1])
#     m = borrosificador([pi/2, 0])
#     print("pertenencia de los valores -1, 1")
#     print(m)
#     g = motor_inferencia(m)
#     print('salida del motor de inferencia F')
#     print(g)
#     fin = desborrosificador(g)
#     print("el valor es")
#     print(fin)
