(define (problem transporte_aereo_problem)
(:domain transporte_aereo)
(:objects C1 C2
          airplane1 airplane2
          SFO JFK)
(:init (CARGO C1) (CARGO C2)
       (PLANE airplane1) (PLANE airplane2)
       (AIRPORT SFO) (AIRPORT JFK)
       (AT C1 SFO) (AT C2 JFK) (AT airplane1 SFO) (AT airplane2 JFK))
(:goal (and (AT C1 JFK) (AT C2 SFO)))
)
