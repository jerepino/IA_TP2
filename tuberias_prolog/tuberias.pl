alarma(X) :- explota(X).

explota(T) :- tuberia(T), presion(T, P), P> 100.
explota(TU) :- tuberia(TU), presion(TU, P), temperatura(TU, T), P > 50, T > 80, !.

temperatura(t1, X) :- X is 85.
temperatura(t2, X) :- X is 95.

presion(t1, X) :- X is 60.
presion(t2, X) :- X is 130.
presion(v1, X) :- X is 230.

tuberia(t1).
tuberia(t2).

valvula(v1).
