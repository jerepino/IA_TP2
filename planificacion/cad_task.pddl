(define (problem cad_1_p)
  (:domain cad_1)
  (:objects fr_lat - fr_l
            fr_ce_ex - fr_c_e
            fr_ce_int - fr_c_i
            ag_gr - ag_g
            ag_med - ag_m
            ag_ch - ag_c
            broca1 broca2 broca3 - broca
            herr_f1 herr_f2 herr_f3 - cabezaFresa
            pieza1 - pieza
            taladro1 - taladro
            fresa1 - fresa
            armario1 - armario
            v - vertical
            hor - horizontal
            ch - chico
            med - mediano
            gra - grande
  )
  (:init (En armario1 pieza1)
         (En armario1 broca1)
         (En armario1 broca2)
         (En armario1 broca3)
         (En armario1 herr_f1)
         (En armario1 herr_f2)
         (En armario1 herr_f3)
         (Tamanio_herr herr_f1 ch)
         (Tamanio_herr herr_f2 med)
         (Tamanio_herr herr_f3 gra)
         (Tamanio_herr broca1 ch)
         (Tamanio_herr broca2 med)
         (Tamanio_herr broca3 gra)
         (Posicion_vertical pieza1 v)
         (No_usada fresa1)
         (No_usada taladro1)
  )
  (:goal (and (Aplicado pieza1 fr_lat)
              (Aplicado pieza1 fr_ce_ex)
              (Aplicado pieza1 fr_ce_int)
              (Aplicado pieza1 ag_gr)
              (Aplicado pieza1 ag_med)
              (Aplicado pieza1 ag_ch))
  )
)
