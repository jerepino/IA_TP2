from matplotlib import pyplot as plt


def membership(x, x_, x_med = 0):
    """

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


if __name__ == '__main__':
    x = []
    y_pos_MN = []
    y_pos_N = []
    y_pos_Z = []
    y_pos_P = []
    y_pos_MP = []
    sup_pos_MN = [-19, -9]
    sup_pos_N = [-12, -2]
    sup_pos_Z = [-5, 5]
    sup_pos_P = [2, 12]
    sup_pos_MP = [9, 19]
    m_ = []
    ma_ = []
    for j in range(-19, 20):
        x.append(j)
        y_pos_MN.append(membership(j, sup_pos_MN))
        y_pos_N.append(membership(j, sup_pos_N))
        y_pos_Z.append(membership(j, sup_pos_Z))
        y_pos_MP.append(membership(j, sup_pos_MP))
        m_.append(min(y_pos_MP[-1], y_pos_P[-1]))  # Minimo
        ma_.append(max(y_pos_MP[-1], y_pos_P[-1])) # Maximo
    # plt.plot(x, y_pos_MN, x, y_pos_N, x, y_pos_Z, x, y_pos_P, x, y_pos_MP)

    print(len(m_))
    plt.plot(x, y_pos_P, x, y_pos_MP, x, ma_)
    plt.title("Conjuntos Borrosos Posicion")
    plt.grid()
    plt.show()
