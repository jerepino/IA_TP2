from matplotlib import pyplot as plt
from math import pi
from numpy import arange

def membership(x, x_, x_med=0):
    """
    Funcion usada para calcular en grado de pertenencia a un conjunto borroso
    :param x: absisas, universo del discurso
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
    ang = 2
    sol = 0.2
    x = []
    pos_MN = []
    pos_N = []
    pos_Z = []
    pos_P = []
    pos_MP = []


    sup_pos_MN = [-11, -5]
    sup_pos_N = [-7, -1]
    sup_pos_Z = [-3, 3]
    sup_pos_P = [1, 7]
    sup_pos_MP = [5, 11]
    med_pos_N = (sup_pos_N[1] + sup_pos_N[0]) * 0.7 / 2 #el porsentaje mueve la punta: %>1 ->  %<1 <-
    med_pos_P = (sup_pos_P[1] + sup_pos_P[0]) * 0.7 / 2
    m_ = []
    ma_ = []
    for j in arange(-15, 15, 0.001):
        x.append(j)
        pos_MN.append(membership(j, sup_pos_MN))
        pos_N.append(membership(j, sup_pos_N, med_pos_N))
        pos_Z.append(membership(j, sup_pos_Z))
        pos_P.append(membership(j, sup_pos_P, med_pos_P))
        pos_MP.append(membership(j, sup_pos_MP))
        # m_.append(implicacion(y_pos_MP[-1], y_pos_P[-1]))  # Maximo
        ma_.append(F_P(pos_P[-1], pos_MP[-1]))  # Minimo



    plt.plot(x, pos_MN, x, pos_N, x, pos_Z, x, pos_P, x, pos_MP)
    # plt.plot(x, pos_P, x, pos_MP, x, ma_)
    plt.title("Conjuntos Borrosos Posicion")
    plt.grid()
    plt.show()
