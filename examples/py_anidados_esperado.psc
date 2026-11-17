Algoritmo ProgramaTraducido
    Definir i, ta_indice1, ta_limite1, j, ta_indice2, ta_limite2 Como Entero
    ta_indice1 <- 0
    ta_limite1 <- 2
    Mientras ta_indice1 < ta_limite1 Hacer
        i <- ta_indice1
        ta_indice2 <- 0
        ta_limite2 <- 2
        Mientras ta_indice2 < ta_limite2 Hacer
            j <- ta_indice2
            Si (i = j) Entonces
                Escribir i, " ", j
            FinSi
            ta_indice2 <- ta_indice2 + (1)
        FinMientras
        ta_indice1 <- ta_indice1 + (1)
    FinMientras
FinAlgoritmo
