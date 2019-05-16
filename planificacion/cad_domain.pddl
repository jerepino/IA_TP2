(define (domain cad_1)

  (:requirements :strips :typing)

  (:types pieza  herramientas - objeto
          broca cabezaFresa - herramientas
          taladro armario fresa - maquinas
          ag_g ag_m ag_c fr_l fr_c_e fr_c_i - caracteristica
          vertical horizontal - orientacion
          grande mediano chico - tamanio
  )

  (:predicates (En ?m - maquinas ?o - objeto)
               (Aplicado ?p - pieza ?ac - caracteristica)
               (Posicion_vertical ?p - pieza ?v - vertical)
               (Posicion_horizontal ?p - pieza ?hor - horizontal)
               (Tamanio_herr ?h - herramientas ?t - tamanio)
               (No_usada ?m - maquinas)
               (Usada ?m - maquinas)
  )

  (:action colocar_herramienta_en_
         :parameters(?h - herramientas ?m - maquinas ?a - armario)
         :precondition (and (En ?a ?h) (No_usada ?m))
         :effect (and (En ?m ?h) (not (En ?a ?h)) (not (No_usada ?m)) (Usada ?m))
  )

  (:action quitar_herramienta_de_
         :parameters (?h - herramientas ?m - maquinas ?a - armario)
         :precondition (and (En ?m ?h) (Usada ?m))
         :effect (and (En ?a ?h) (not (En ?m ?h)) (No_usada ?m) (not (Usada ?m)))
  )

  (:action colocar_pieza_en_
         :parameters(?h - pieza ?m ?a - maquinas)
         :precondition (En ?a ?h)
         :effect (and (En ?m ?h) (not (En ?a ?h)))
  )

  (:action quitar_pieza_de_
         :parameters (?h - pieza ?m ?a - maquinas)
         :precondition (En ?m ?h)
         :effect (and (En ?a ?h) (not (En ?m ?h)))
  )



  (:action parar_pieza
         :parameters (?p - pieza ?a - armario ?v - vertical ?hor - horizontal)
         :precondition (and (En ?a ?p) (Posicion_horizontal ?p ?hor))
         :effect (and (Posicion_vertical ?p ?v) (not (Posicion_horizontal ?p ?hor))  )
  )

  (:action acostar_pieza
         :parameters (?p - pieza ?a - armario ?v - vertical ?hor - horizontal)
         :precondition (and (En ?a ?p) (Posicion_vertical ?p ?v))
         :effect (and (Posicion_horizontal ?p ?hor) (not (Posicion_vertical ?p ?v))  )
  )

  (:action fresar_lateral_pieza
         :parameters (?p - pieza ?m - fresa ?h - cabezaFresa ?ac - fr_l ?v - vertical ?g - grande)
         :precondition (and (En ?m ?h) (En ?m ?p) (Posicion_vertical ?p ?v) (Tamanio_herr ?h ?g) (Usada ?m))
         :effect (Aplicado ?p ?ac)
  )

  (:action fresar_central_exterior_pieza
         :parameters (?p - pieza ?m - fresa ?h - cabezaFresa ?ac - fr_c_e ?v - vertical ?med - mediano)
         :precondition (and (En ?m ?h) (En ?m ?p) (Posicion_vertical ?p ?v) (Tamanio_herr ?h ?med) (Usada ?m))
         :effect (Aplicado ?p ?ac)
  )

  (:action fresar_central_interior_pieza
         :parameters (?p - pieza ?m - fresa ?h - cabezaFresa ?ac - fr_c_i ?v - vertical ?ch - chico)
         :precondition (and (En ?m ?h) (En ?m ?p) (Posicion_vertical ?p ?v) (Tamanio_herr ?h ?ch) (Usada ?m))
         :effect (Aplicado ?p ?ac)
  )

  (:action agujerear_G_pieza
         :parameters (?p - pieza ?t - taladro ?b - broca ?ac - ag_g ?v - vertical ?g - grande)
         :precondition (and (En ?t ?b) (En ?t ?p) (Posicion_vertical ?p ?v) (Tamanio_herr ?b ?g) (Usada ?t))
         :effect (Aplicado ?p ?ac)
  )

  (:action agujerear_M_pieza
         :parameters (?p - pieza ?t - taladro ?b - broca ?ac - ag_m ?h - horizontal ?med - mediano)
         :precondition (and (En ?t ?b) (En ?t ?p) (Posicion_horizontal ?p ?h) (Tamanio_herr ?b ?med) (Usada ?t))
         :effect (Aplicado ?p ?ac)
  )

  (:action agujerear_C_pieza
         :parameters (?p - pieza ?t - taladro ?b - broca ?ac - ag_c ?v - vertical ?ch - chico)
         :precondition (and (En ?t ?b) (En ?t ?p) (Posicion_vertical ?p ?v) (Tamanio_herr ?b ?ch) (Usada ?t))
         :effect (Aplicado ?p ?ac)
  )
)
