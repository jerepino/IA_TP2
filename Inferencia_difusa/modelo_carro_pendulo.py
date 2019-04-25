import numpy
import math
def modelo(tita, tita_v, dt):
    """
    :param tita: angulo del pendulo
    :param tita_v: velocidad angular del pendulo
    :param dt: delta del tiempo
    :return:
    """
    g = 9.81
    M = 10
    m = 1
    l = 0.5
    F = 0

    tita_a = (g * math.sin(tita) + math.cos(tita) *
              ((-F - m * l * tita_v ** 2 * math.sin(tita)) / (M + m))) \
             / l * (4/3 - (m * math.cos(tita) * math.cos(tita) * tita)
                    / (M + m))
    tita_v = tita + tita_a * dt
    tita = tita + tita_v * dt + (tita_a * dt ** 2) / 2
