import matplotlib.pyplot as plt
import math
import numpy


def modelo(tita, tita_v, tita_a, dt, F = 0.0):
    """
    :param tita: angulo del pendulo
    :param tita_v: velocidad angular del pendulo
    :param dt: delta del tiempo
    :param F: Entrada de control. En este caso Fuerza
    :return : [posicion angular , velocidad angular, aceleracion angular] [rad]
    """
    g = 9.81
    M = 2
    m = 0.5
    l = 0.5

    tita_n = tita + tita_v * dt + (tita_a * dt ** 2) / 2
    tita_v_n = tita + tita_a * dt
    tita_a_n = (g * math.sin(tita_n) + math.cos(tita_n) *
                ((-F - m * l * tita_v_n ** 2 * math.sin(tita_n)) / (M + m))) \
               / l * (4 / 3 - (m * math.pow(math.cos(tita_n), 2))
                      / (M + m))
    return [tita_n, tita_v_n, tita_a_n]


if __name__ == '__main__':
    # Datos
    g = 9.81
    M = 2
    m = 0.5
    l = 0.5
    F = 0
    # Vectores para plotear
    vector_tita = []
    vector_tita_v = []
    vector_tita_a = []
    # Estado inicial

    tita_0 = -0.01 #-math.pi/10
    tita_v_0 = 0
    tita_a_0 = (g * math.sin(tita_0) + math.cos(tita_0) *
              ((-F - m * l * tita_v_0 ** 2 * math.sin(tita_0)) / (M + m))) \
             / l * (4/3 - (m * math.pow(math.cos(tita_0), 2))
                    / (M + m))
    # definicion del tiempo
    t = 0 #tiempo inicial
    dt = 0.1 #paso
    #armo el estado inicial
    estado_act = [tita_0, tita_v_0, tita_a_0]
    vector_tita.append(estado_act[0])
    vector_tita_v.append(estado_act[1])
    vector_tita_a.append(estado_act[0])
    while t <= 3.5:
        estado_act = modelo(estado_act[0], estado_act[1], estado_act[2], dt)
        vector_tita.append(estado_act[0])
        vector_tita_v.append(estado_act[1])
        vector_tita_a.append(estado_act[0])
        t += dt

    # Paso tita de radianas a grados
    for i, valor in enumerate(vector_tita):
        vector_tita[i] = math.degrees(valor)

    #Ploteo los resultados
    plt.figure(1)

    axes = plt.subplot(311)

    axes.set_ylabel('tita [°]')

    axes.set_title('Posicion, velocidad y aceleracion  angular pendulo')

    plt.plot([n for n in numpy.arange(0, 3.5 + dt, dt)], vector_tita, 'b' , label="Posicion Angular")

    plt.legend()

    axes_ = plt.subplot(312)

    axes_.set_ylabel('tita_v [radianes/s]')

    plt.plot([n for n in numpy.arange(0, 3.5 + dt, dt)], vector_tita_v, 'g', label="Velocidad Angular")

    plt.legend()

    axes_ = plt.subplot(313)

    axes_.set_xlabel('Tiempo')

    axes_.set_ylabel('tita_a [radianes/s²]')

    plt.plot([n for n in numpy.arange(0, 3.5 + dt, dt)], vector_tita_a, 'r', label="Aceleracion Angular")

    plt.legend()

    plt.show()
