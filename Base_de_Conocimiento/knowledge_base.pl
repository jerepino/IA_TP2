/*
Se plantean 2 metodologias diferentes para "simular" ya sean acciones de actuador o eventos de un sensor.
1-Uso de predicados dinamicos donde se accede a la KB para modificar los valores nominales de por ej: presion, estados, etc.
2-Creando listas con estados, y seleccionando caso de manera random.

*/

/* RAMA 1 Corresponde a la izquierda del arbol    */

%GroundFact
espesor(tuberias,30).  %mm
espesor(valvulaSeguridad,28).
espesor(juntas,30).

%Predicados

elementos(valvulaSeguridad).
elementos(juntas).
elementos(tuberias).

%Lista de estados
estado([oxidado,deslumbrante,buenEstado]).

%Simulamos la lectura del sensor con random
estado_random(X):-estado(L), random_member(X,L).

%Sirve para consultar el elemento de una lista
componentedeLista(X) :- estado(L), member(X, L).

%Consulto el estado de alguno de los componentes
consultarEstado(X,Y):- elementos(X), estado_random(Y).

%Que se debe hacer una vez consultado el estado  (RESPUESTAS DEL ARBOL)
tuberiasEsta(deslumbrante):- write('Se requiere coordinacion para renderizar y colorear el equipo'),!.
tuberiasEsta(oxidado):-write('Se requiere coordinacion para renderizar y colorear el equipo'),!.
tuberiasEsta(buenEstado):-write('Debe consultar su espesor!'),!.

juntasEsta(deslumbrante):- write('Se requiere coordinacion para renderizar y colorear el equipo'),!.
juntasEsta(oxidado):-write('Se requiere coordinacion para renderizar y colorear el equipo'),!.
juntasEsta(buenEstado):-write('Debe consultar su espesor!'),!.

valvulaSeguridadEsta(deslumbrante):- write('Se requiere coordinacion para renderizar y colorear el equipo'),!.
valvulaSeguridadEsta(oxidado):-write('Se requiere coordinacion para renderizar y colorear el equipo'),!.
valvulaSeguridadEsta(buenEstado):-write('Debe consultar su espesor!'),!.

%Hacemos una lista de espesores. Para luego verficar los GroundFact
lista_espesores([27,28.5,27.6,30,29.5,28,30,29]).

%ConsultarEspesor(X,Y) :- el espesor de elemento X es Y
espesor_random(X) :- lista_espesores(L), random_member(X,L).
verificarProblema(E,X):- espesor(E,Y), X < Y, write('Reporte una inspeccion tecnica de inmediato!'),!.
verificarProblema(E,X):- espesor(E,Y), X==Y, write('La condicion del elemento es adecuada!').

consultarEspesor(E,X) :- elementos(E), espesor_random(X), verificarProblema(E,X).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

/*  RAMA 3  - Corresponde a la derecha del arbol    */

%Lista booleana para el estado Pierde/No pierde
list_bool([si,no]).

bool_random(X):-list_bool(L), random_member(X,L).

%Verificamos perdida

verificarPerdida(X):- X==si, write('Por favor, consulte si la perdida ha sido tratada'),nl,!.
verificarPerdida(X):- X==no, write('La junta de la valvula de seguridad esta libre de perdidas'),nl,!.

%Consulta
consultarPerdidaGas(E,X):- elementos(E), bool_random(X), nl, verificarPerdida(X).

%Verificamos arreglo
resultado(X):- X==si, write('Reporte a la unidad tecnica de inspeccion '),nl,!.
resultado(X):- X==no, write('Enviar un reporte al departamente de arreglo de fallas.'),nl,!.

%Consulta
consultarArregloPerdida(X):- list_bool(L), random_member(X,L), resultado(X).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
/*
RAMA CENTRAL!!!!!!!!!!!!!!!!!


  Ejemplo de predicado dinamico

:- dynamic temperatura/1.
 temperatura(23).

 sensor_temperatura :-
    esperar(10),
    leer_temperatura(NuevaTemperatura),
    rectract(temperatura(_AnteriorTemperatura)),
    assert(temperatura(NuevaTemperatura)),
    !,
    sensor_temperatura.

*/


%GroundFact (de tipo dinámico)
:-dynamic(presion/1).    %Le declaro al compilador que va a ser de tipo dinamico
presion(30).
:-dynamic(estadoValvula/1).
estadoValvula(cerrada).
:-dynamic(estadoSensores/1).
estadoSensores(bloqueados).
:-dynamic(presionGas/1).
presionGas(30). %NOMINAL
:-dynamic(estadoSensoresPresion/1).
estadoSensoresPresion(bloqueados).


verificaEvacuacion(X):- X==si, write('Por favor, consulte si la presion de la linea de gas es la apropiada!'),!.
verificaEvacuacion(X):- X==no, write('Por favor, consulte si funciona la valvula de alivio con un 10% de aumento de la presion regular',!).

consultarEvacuacionContinuaGas(X):- bool_random(X),verificaEvacuacion(X).

%%Respuesta NO  EN RAMA CENTRAL ----------------------------

calculaPresion(Adicional,Z):- presion(Y), Z is Y + Y*(Adicional/100).

adicionaPresion:- write('Cual es el adicional (en %): '),read(Adicional),
                  calculaPresion(Adicional,Z),
                  %Cambio el GroundFact  ("SIMULO" variable global)
                  retract(presion(Anterior)),
                  assert(presion(Z)).

consultarValvulaAlivio():- presion(Z), Z < 35 , write('La funcion de seguridad es la apropiada!'),!.
consultarValvulaAlivio():- presion(Z), Z > 35 , write('Por favor, consulte si la valvula se encuentra cerrada!'),!.

%--------------------------------------------

consultarPosicionValvula(X):- estadoValvula(X), X==cerrada, write('Por favor, abra la valvula de seguridad'),!.
consultarPosicionValvula(X):- estadoValvula(X), X==abierta, write('Por favor, consulte si los sensores de control de la misma estan bloqueados'),!.

%SIMULO ACTUADOR ---> ESTOY CAMBIANDO UN ESTADO
cambiarEstadoValvula:- write('Ingrese nuevo estado de posicon: '),read(Estado),
                       %Cambio el GroundFact
                       retract(estadoValvula(Anterior)),
                       assert(estadoValvula(Estado)).

%--------------------------------------------

consultarSensorControl(X):- estadoSensores(X), X==bloqueados, write('Realice limpieza y solucione de problemas de los tubos de sensado.'),!.
consultarSensorControl(X):- estadoSensores(X), X==no_bloqueados, write('Por favor, consulte por el desempenio y la eficiencia del resorte de la valvula de seguridad!'),!.

cambiarEstadoSensores:- write('Desbloquee los sensores: '),read(Estado),
                       %Cambio el GroundFact
                       retract(estadoSensores(Anterior)),
                       assert(estadoSensores(Estado)).

%---------------------------------------------

consultarResorteValvula(X):- X=='esEficiente', write('Por favor, consulte si existe prevencion adecuada de fugas entre el asiento y el orificio!'),!.
consultarResorteValvula(X):- X=='noesEficiente', write('Solicite de inmediato un "service"'),!.

%---------------------------------------------

prevencion([hay,nohay]).
prevencion_random(X):-prevencion(L), random_member(X,L).


verificaPrevencion(X):- X==hay, write('Por favor, consulte si el Piloto funciona correctamente!'),!.
verificaPrevencion(X):- X==nohay, write('Reemplace el asiento y el orificio y ponga la válvula de seguridad en el circuito'),!.

consultarPrevencionAsiento_Orificio(X):- prevencion_random(X),verificaPrevencion(X).

%-----------------------------------------------

verificaPilot(X):- X==si, write('Coloque la válvula de seguridad de acuerdo con las instrucciones'),!.
verificaPilot(X):- X==no, write('Piloto de servicio completo y reinstalación'),!.

consultarFuncionamientoPilot(X):- bool_random(X),verificaPilot(X).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%Respuesta SI  EN RAMA CENTRAL ----------------------------

gasPresion:- write('Cual es la presion del gas en [30-40](en psi): '),read(PresionGas),
                  %Cambio el GroundFact  ("SIMULO" variable global)
                  retract(presionGas(Anterior)),
                  assert(presionGas(PresionGas)).

consultarPresionGas():- presionGas(Z), Z < 35 , write('La presion del gas es la apropiada.'), nl , write('Por favor, consulta si los sensores de control de la presion estan bloqueados!'),!.
consultarPresionGas():- presionGas(Z), Z > 35 , write('La presion del gas no es la apropiada.') , nl , write('Ajustar el regulador de acuerdo con las instrucciones.'),!.

%---------------------------------------------------------------------


consultarSensorControlPresion(X):- estadoSensoresPresion(X), X==bloqueados, write('Limpiar y reparar las fallas de los mismos'),!.
consultarSensorControlPresion(X):- estadoSensoresPresion(X), X==nobloqueados, write('Los sensores estan desbloqueados'),nl,write('Por favor, consulte si es eficiente el resorte que possen!') ,!.

cambiarEstadoSensoresPresion:- write('Desbloquee los sensores: '),read(Estado),
                       %Cambio el GroundFact
                       retract(estadoSensoresPresion(Anterior)),
                       assert(estadoSensoresPresion(Estado)).

%--------------------------------------------------

consultarResorteSeguridad(X):- X=='esEficiente', write('Por favor, consulte si hay alguna fuga evitable entre el asiento y el orificio!'),!.
consultarResorteSeguridad(X):- X=='noesEficiente', write('Reemplazar el resorte en el proximo "service"'),!.


verificaFuga(X):- X==si, write('Coloque la válvula de seguridad de acuerdo con las instrucciones'),!.
verificaFuga(X):- X==no, write('Reemplace el asiento y el orificio y ponga la válvula de seguridad en el circuito'),!.

consultarFugaEvitable(X):- bool_random(X),verificaFuga(X).
