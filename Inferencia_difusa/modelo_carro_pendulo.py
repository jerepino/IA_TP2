import matplotlib.pyplot as plt
from math import sin, cos, pow, pi
from control_difuso import control_difuso as control
import os


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
    M = 0.1
    m = 0.01
    l = 0.3

    # Vectores para plotear
    vector_tita = []
    vector_tita_v = []
    vector_tita_a = []
    # Estado inicial

    tita_0 = pi/2    # Segun la posicion inicial que utilizo es para donde mido el angulo (-,sentido orario y mas negatico) (+, sentido antihorario y positivo)
    tita_v_0 = 0
    numerador = g * sin(tita_0) + cos(tita_0) * (- m * l * pow(tita_v_0, 2) * sin(tita_0)) / (M + m)
    denominador = l * (4 / 3 - m * pow(cos(tita_0), 2) / (M + m))
    tita_a_0 = numerador / denominador


    # definicion del tiempo
    t = 0 #tiempo inicial
    dt = 0.01 #paso
    tiempo = []

    #armo el estado inicial
    estado_act = [tita_0, tita_v_0, tita_a_0]

    while t < 5:
        vector_tita.append(estado_act[0])
        vector_tita_v.append(estado_act[1])
        vector_tita_a.append(estado_act[2])

        F = control(estado_act)

        estado_act = modelo(estado_act, dt)

        tiempo.append(t)
        t += dt

    #Ploteo los resultados

    fig, (a1, a2, a3) = plt.subplots(3, 1)

    a1.set_ylabel('tita [rad]')

    a1.set_title('Posicion, velocidad y aceleracion  angular pendulo')

    a1.plot(tiempo, vector_tita, 'b', label="Posicion Angular")

    a1.legend()

    a2.set_ylabel('velocidad [rad/s]')

    a2.plot(tiempo, vector_tita_v, 'g', label="Velocidad Angular")

    a2.legend()

    a3.set_xlabel('Tiempo [ms]')

    a3.set_ylabel('Aceleracion [rad/s²]')

    a3.plot(tiempo, vector_tita_a, 'r', label="Aceleracion Angular")

    a3.legend()

    plt.show()


    t=0
    for point in range(0, len(tiempo), 1):
        plt.figure()
        plt.plot(l * sin(vector_tita[point]), l * cos(vector_tita[point]), 'bo', markersize=20)
        plt.plot([0, l * sin(vector_tita[point])], [0, l * cos(vector_tita[point])])
        plt.xlim(-l-0.5, l+0.5)
        plt.ylim(-l-0.5, l+0.5)
        plt.xlabel('x-direction')
        plt.ylabel('y-direction')
        filenumber = point
        filenumber=format(filenumber, "05")
        filename="image{}.png".format(filenumber)
        plt.savefig(filename)
        plt.close()
        if t > 2:
            break
        t += dt

    os.system("ffmpeg -f image2 -r 25 -i image%05d.png -vcodec mpeg4 -y movie.avi")

