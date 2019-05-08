(define (domain transporte_aereo)
  (:predicates
              (CARGO ?x)
              (PLANE ?x)
              (AIRPORT ?x)
              (AT ?x ?y)
              (IN ?x ?y)
  )
  (:action load
     :parameters (?x ?y ?z)
     :precondition (and (AT ?x ?z) (AT ?y ?z) (CARGO ?x) (PLANE ?y) (AIRPORT ?z) )
     :effect (and (not (AT ?x ?z)) (IN ?x ?y))
  )
  (:action unload
     :parameters (?x ?y ?z)
     :precondition (and (IN ?x ?y) (AT ?y ?z) (CARGO ?x) (PLANE ?y) (AIRPORT ?z) )
     :effect (and (AT ?x ?z) (not (IN ?x ?y)) )
  )
  (:action fly
     :parameters (?p ?from ?to)
     :precondition (and (AT ?p ?from) (PLANE ?p) (AIRPORT ?from) (AIRPORT ?to) )
     :effect (and (not(AT ?p ?from)) (AT ?p ?to) )
  )

)
