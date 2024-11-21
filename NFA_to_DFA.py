def convertir_afnd_a_afd(estados, alfabeto, transiciones, estado_inicial, estados_finales):
    # Conjunto inicial del AFD 
    estado_inicial_afd = frozenset([estado_inicial])
    estados_por_procesar = [estado_inicial_afd]
    estados_visitados = set()
    transiciones_afd = {}
    estados_finales_afd = set()

    # Procesamos cada conjunto de estados
    while estados_por_procesar:
        conjunto_actual = estados_por_procesar.pop(0)
        if conjunto_actual in estados_visitados:
            continue

        estados_visitados.add(conjunto_actual)

        # Verificamos si el conjunto actual contiene algún estado final del AFND
        if any(estado in estados_finales for estado in conjunto_actual):
            estados_finales_afd.add(conjunto_actual)

        # Calculamos las transiciones del conjunto actual
        for simbolo in alfabeto:
            nuevos_estados = set()
            for estado in conjunto_actual:
                if (estado, simbolo) in transiciones:
                    nuevos_estados.update(transiciones[(estado, simbolo)])

            if nuevos_estados:
                nuevo_conjunto = frozenset(nuevos_estados)
                transiciones_afd[(conjunto_actual, simbolo)] = nuevo_conjunto

                # Si es un nuevo conjunto, lo agregamos a la lista de procesamiento
                if nuevo_conjunto not in estados_visitados:
                    estados_por_procesar.append(nuevo_conjunto)

    # Devolvemos el AFD en un diccionario
    return {
            "estados": estados_visitados,
            "alfabeto": alfabeto,
            "transiciones": transiciones_afd,
            "estado_inicial": estado_inicial_afd,
            "estados_finales": estados_finales_afd
        }


# Datos del AFND
estados_afnd = ["s0", "s1", "s2","s3"]
alfabeto = ["a", "b"]
transiciones_afnd = {
    ("s0", "a"): ["s1","s2"],
    ("s1", "a"): ["s2"],
    ("s1", "b"): ["s1"],
    ("s2", "a"): ["s2"],
    ("s2", "b"): ["s3"],
    ("s3", "a"): ["s1"],
    ("s3", "b"): ["s3"]

}
estado_inicial_afnd = "s0"
estados_finales_afnd = ["s3"]

# Convertimos el AFND a AFD
afd = convertir_afnd_a_afd(estados_afnd,alfabeto,transiciones_afnd,estado_inicial_afnd,estados_finales_afnd)

# Datos del AFD obtenido
print("Estados del AFD:")
for estado in afd["estados"]:
    print(set(estado))

print("\nTransiciones del AFD:")

for (estado, simbolo), destino in afd["transiciones"].items():
    print(f"{set(estado)} -- {simbolo} --> {set(destino)}")

print("\nEstado inicial del AFD:")
print(set(afd["estado_inicial"]))

print("\nEstados finales del AFD:")
for estado in afd["estados_finales"]:
    print(set(estado))
