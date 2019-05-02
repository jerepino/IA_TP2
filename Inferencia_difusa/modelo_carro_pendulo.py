import matplotlib.pyplot as plt
from math import sin, cos, pow, pi, degrees


def modelo(tita, dt):
    """
    :param tita: [angulo, velocidad, aceleracion] del pendulo
    :param dt: delta del tiempo
    :return tita_n: [posicion angular , velocidad angular, aceleracion angular] [rad]
    """
    tita_n = tita
    numerador = g * sin(tita[0]) + cos(tita[0]) * (- F - m * l * pow(tita[1], 2) * sin(tita[0])) / (M + m)
    denominador = l * (4 / 3 - m * pow(cos(tita[0]), 2) / (M + m))
    tita_n[2] = numerador / denominador
    tita_n[1] = tita[1] + tita[2] * dt
    tita_n[0] = tita[0] + tita[1] * dt + tita[2] * pow(dt, 2) / 2

    return tita_n


if __name__ == '__main__':
    # Datos
    g = 9.81
    M = 2
    m = 0.2
    l = 0.5
    F = 0
    # Vectores para plotear
    vector_tita = []
    vector_tita_v = []
    vector_tita_a = []
    # Estado inicial

    tita_0 = 0.01  # Segun la posicion inicial que utilizo es para donde mido el angulo (-,sentido orario y mas negatico) (+, sentido antihorario y positivo)
    tita_v_0 = 0
    tita_a_0 = 0


    # definicion del tiempo
    t = 0 #tiempo inicial
    dt = 0.001 #paso
    tiempo = []

    #armo el estado inicial
    estado_act = [tita_0, tita_v_0, tita_a_0]

    while t < 2000:
        vector_tita.append(estado_act[0])
        vector_tita_v.append(estado_act[1])
        vector_tita_a.append(estado_act[2])

        estado_act = modelo(estado_act, dt)

        tiempo.append(t)
        t += dt

    #Ploteo los resultados

    fig, (a1, a2, a3) = plt.subplots(3,1)

    a1.set_ylabel('tita [rad]')

    a1.set_title('Posicion, velocidad y aceleracion  angular pendulo')

    a1.plot(tiempo, vector_tita, 'b', label="Posicion Angular")

    a1.legend()

    a2.set_ylabel('velocidad [rad/s]')

    a2.plot(tiempo, vector_tita_v, 'g', label="Velocidad Angular")

    a2.legend()

    a3.set_xlabel('Tiempo')

    a3.set_ylabel('Aceleracion [rad/s²]')

    a3.plot(tiempo, vector_tita_a, 'r', label="Aceleracion Angular")

    a3.legend()

    plt.show()
