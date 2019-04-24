explota(Tuberia) :- presion(Tuberia, P), P > 100.
explota(Tuberia) :- presion(Tuberia, P), temperatura(Tuberia, T), P > 50, T > 80.

temperatura(t1, X) :- X is 75.
temperatura(t2, X) :- X is 95.

presion(t1, X) :- X is 60.
presion(t2, X) :- apertura_valvula(v1, Apertura1), apertura_valvula(v2, Apertura2), X is Apertura1 * 0.32 + Apertura2 * 0.33.

apertura_valvula(v1, X) :- X is 123.
apertura_valvula(v2, X) :- X is 99.
