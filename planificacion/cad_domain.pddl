(define (domain cad_1)
  (:requirements :strips :typing)
  (:types pieza  herramientas - objeto
          broca cabezaFresa - herramientas
          taladro armario fresa - maquinas
          agujereado fresado - caracteristica
  )

  (:predicates (En ?m - maquinas ?o - objeto)
               (Aplicado ?p - pieza ?ac - caracteristica)
  )

  (:action colocar_en_maquina
         :parameters(?m ?a - maquinas ?h - objeto)
         :precondition (En ?a ?h)
         :effect (and (En ?m ?h) (not (En ?a ?h)) )
  )

  (:action quitar_de_maquina
         :parameters (?m ?a - maquinas ?h - objeto)
         :precondition (En ?m ?h)
         :effect (and (En ?a ?h) (not (En ?m ?h)))
  )

  (:action fresar_pieza
         :parameters (?m - fresa ?h - cabezaFresa ?p - pieza ?ac - fresado)
         :precondition (and (En ?m ?h) (En ?m ?p))
         :effect (Aplicado ?p ?ac)
  )

  (:action agujerear_pieza
         :parameters (?t - taladro ?b - broca ?p - pieza ?ac - agujereado)
         :precondition (and (En ?t ?b) (En ?t ?p))
         :effect (Aplicado ?p ?ac)
  )
)
