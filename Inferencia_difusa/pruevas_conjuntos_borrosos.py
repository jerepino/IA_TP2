from matplotlib import pyplot as plt
from math import pi
from numpy import arange

def membership(x, x_, x_med=0, fin=0):
    """
    Funcion usada para calcular en grado de pertenencia a un conjunto borroso
    :param x: absisas, universo del discurso
    :param x_: vector, extremos del soporte
    :param x_med: punto medio (punto para el cual la pertenencia es maxima (1))
    :param fin: variable para saber si queda en 1 o 0 el valor del conjunto borroso
    :return y: ordenadas o grado de pertenencia
    """
    # y = [0, 1]  # Valor minimo y maximo de pertenencia
    if x_med == 0:
        x_med = (x_[0] + x_[1]) / 2
    if x_[0] <= x <= x_med:  # p_1 = [x_i, 0] , p_2 = [x_med, 1]
        return (x - x_[0]) / (x_med - x_[0])
    elif x_med < x <= x_[1]:  # p_1 = [x_med, 1] , p_2 = [x_f, 0]
       return (x[1] - x) / (x_[1] - x_med)
    if (fin == -1 and x < x_med) or (fin == 1 and x > x_med):
        return 1
    return 0


def complemento(u_a):
    """
    Calcula el complemento de un valor borroso
    :param u_a: valor borroso
    :return: complemento del valor borroso
    """
    return 1-u_a


def union(u_a, u_b):
    """
    Realiza la union entre dos valores borrosos es tambien llamada disyuncion o OR logico
    :param u_a: pertenencia de un valor x a el conjunto n
    :param u_b: pertenencia de un valor x a el conjunto m
    :return: maximo entre u_a y u_b (es la union entre los conjuntos)
    """
    return max(u_a, u_b)


def interseccion(u_a, u_b):
    """
    Realiza la interseccion entre dos valores borrosos es tambien llamada conjuncion o AND logico
    :param u_a: pertenencia de un valor x a el conjunto n
    :param u_b: pertenencia de un valor x a el conjunto m
    :return: minimo entre u_a y u_b (es la interseccion entre los conjuntos)
    """
    return min(u_a, u_b)

def implicacion(u_a, u_b):
    """
    Realiza la implicacion material u_a -> u_b
    :param u_a: cuerpo, hipótesis o antecedente
    :param u_b: cabeza, conclusión o consecuente
    :return: Grado de implicacion de u_a -> u_b
    """
    return union(complemento(u_a), u_b)


if __name__ == '__main__':
    # Pongo nombres alternativos a las funciones
    AND = conjuncion = min
    F_MN = F_N = F_Z = F_P = F_MP = max
    OR = union
    disyuncion = union
    #-------------------------------------------
    x = []
    pos_MN = []
    pos_N = []
    pos_Z = []
    pos_P = []
    pos_MP = []

    # Defino soportes para la posicion
    sup_pos = []
    ang = 0.02  # limite para el soporte de Z
    sol = 0.4
    sup_pos.append([-pi - 0.1, -pi / 2])  # pos_sup_MN
    sup_pos.append([-(1 + sol) * pi / 2, -ang * sol])  # pos_sup_N
    sup_pos.append([-ang, ang])  # pos_sup_Z
    sup_pos.append([sol * ang, (1 + sol) * pi / 2])  # pos_sup_P
    sup_pos.append([pi / 2, pi + 0.1])  # pos_sup_MP

    # ----------------------------------------------------------------

    # Defino soportes para la velocidad
    sup_vel = []
    vel_z = 6  # limite para el soporte de V
    sup_vel.append([-15, -9])  # vel_sup_MN
    sup_vel.append([-(1 + sol) * 9, -vel_z * sol])  # vel_sup_N
    sup_vel.append([-vel_z, vel_z])  # vel_sup_Z
    sup_vel.append([vel_z * sol, (1 + sol) * 9])  # vel_sup_P
    sup_vel.append([9, 15])

    med_pos_N = (sup_pos[1][1] + sup_pos[1][0]) * 0.3 / 2
    med_pos_P = (sup_pos[3][1] + sup_pos[3][0]) * 0.3 / 2

    med_vel_N = (sup_vel[1][1] + sup_vel[1][0]) * 0.7 / 2
    med_vel_P = (sup_vel[3][1] + sup_vel[3][0]) * 0.7 / 2




    for j in arange(-pi-0.5, pi+0.5, 0.001):
        x.append(j)
        pos_MN.append(membership(j, sup_pos[0], 0, -1))
        pos_N.append(membership(j, sup_pos[1], med_pos_N))
        pos_Z.append(membership(j, sup_pos[2]))
        pos_P.append(membership(j, sup_pos[3], med_pos_P))
        pos_MP.append(membership(j, sup_pos[4], 0, 1))

    vel_MN = []
    vel_N = []
    vel_Z = []
    vel_P = []
    vel_MP = []
    y = []
    for j in arange(-15-1, 15+1, 0.001):
        y.append(j)
        vel_MN.append(membership(j, sup_vel[0], 0, -1))
        vel_N.append(membership(j, sup_vel[1], med_vel_N))
        vel_Z.append(membership(j, sup_vel[2]))
        vel_P.append(membership(j, sup_vel[3], med_vel_P))
        vel_MP.append(membership(j, sup_vel[4], 0, 1))

    s_f = [[-11, -5], [-7, -1], [-2, 2], [1, 7], [5, 11]]
    F_MN = []
    F_N = []
    F_Z = []
    F_P = []
    F_MP = []
    z = []
    for j in arange(-11, 11, 0.001):
        z.append(j)
        F_MN.append(membership(j, s_f[0], 0, -1))
        F_N.append(membership(j, s_f[1]))
        F_Z.append(membership(j, s_f[2]))
        F_P.append(membership(j, s_f[3]))
        F_MP.append(membership(j, s_f[4], 0, 1))

    plt.figure(1)
    plt.plot(x, pos_MN, x, pos_N, x, pos_Z, x, pos_P, x, pos_MP)
    plt.title("Particion Borrosa para Posicion")
    plt.grid()
    plt.figure(2)
    plt.plot(y, vel_MN, y, vel_N, y, vel_Z, y, vel_P, y, vel_MP)
    plt.title("Particion Borrosa para Velocidad")
    plt.grid()
    plt.figure(3)
    plt.plot(z, F_MN, z, F_N, z, F_Z, z, F_P, z, F_MP)
    plt.title("Particion Borrosa para Fuerza")
    plt.grid()

    plt.show()
