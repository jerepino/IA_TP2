explota(Tuberia) :- presion(Tuberia, P), presion_maxima(Tuberia, PM), P > PM.
explota(Tuberia) :- presion(Tuberia, P), temperatura(Tuberia, T), P > 50, T > 80.

temperatura(t1, X) :- X is 75.
temperatura(t2, X) :- X is 95.

presion(t1, X) :- X is 60.
presion(t2, X) :- X is 30.

presion_maxima(T, PM) :- tipo(T, supertuberia), PM is 100.
presion_maxima(T, PM) :- tipo(T, tuberia_barata), PM is 50.

tipo(t1, supertuberia).
tipo(t2, tuberia_barata).

prueba(X) :- prueba(X).