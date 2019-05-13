(define (problem cad_1_p)
  (:domain cad_1)
  (:objects a1 - fresado
            a2 - agujereado
            b1 b2 b3 - broca
            cf1 cf2 cf3 - cabezaFresa
            p1 - pieza
            ta - taladro
            fre - fresa
            ar - armario
  )
  (:init (En ar p1)
         (En ar b1)
         (En ar b2)
         (En ar b3)
         (En ar cf1)
         (En ar cf2)
         (En ar cf3)
  )
  (:goal (and (Aplicado p1 a1) (Aplicado p1 a2)))
)
