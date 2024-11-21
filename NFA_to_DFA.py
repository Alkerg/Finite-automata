def convertir_afnd_a_afd(estados, alfabeto, transiciones, estado_inicial, estados_finales):
    # Conjunto inicial del AFD (contiene solo el conjunto del estado inicial del AFN)
    estado_inicial_afd = frozenset([estado_inicial])
    estados_por_procesar = [estado_inicial_afd]
    estados_visitados = set()
    transiciones_afd = {}
    estados_finales_afd = set()

    # Procesar cada conjunto de estados
    while estados_por_procesar:
        conjunto_actual = estados_por_procesar.pop(0)
        if conjunto_actual in estados_visitados:
            continue

        estados_visitados.add(conjunto_actual)

        # Verificar si el conjunto actual contiene algún estado final del AFN
        if any(estado in estados_finales for estado in conjunto_actual):
            estados_finales_afd.add(conjunto_actual)

        # Calcular transiciones del conjunto actual
        for simbolo in alfabeto:
            nuevos_estados = set()
            for estado in conjunto_actual:
                if (estado, simbolo) in transiciones:
                    nuevos_estados.update(transiciones[(estado, simbolo)])

            if nuevos_estados:
                nuevo_conjunto = frozenset(nuevos_estados)
                transiciones_afd[(conjunto_actual, simbolo)] = nuevo_conjunto

                # Si es un nuevo conjunto, agregarlo a la lista de procesamiento
                if nuevo_conjunto not in estados_visitados:
                    estados_por_procesar.append(nuevo_conjunto)

    # Devolver el AFD en un diccionario
    return {
            "estados": estados_visitados,
            "alfabeto": alfabeto,
            "transiciones": transiciones_afd,
            "estado_inicial": estado_inicial_afd,
            "estados_finales": estados_finales_afd
        }


if __name__ == "__main__":
    # Definición del AFN
    estados_afn = ["s0", "s1", "s2","s3"]
    alfabeto = ["a", "b"]
    transiciones_afn = {
        ("s0", "a"): ["s1","s2"],
        ("s1", "a"): ["s2"],
        ("s1", "b"): ["s1"],
        ("s2", "a"): ["s2"],
        ("s2", "b"): ["s3"],
        ("s3", "a"): ["s1"],
        ("s3", "b"): ["s3"]

    }
    estado_inicial_afn = "s0"
    estados_finales_afn = ["s3"]

# Convertir el AFN a AFD
afd = convertir_afnd_a_afd(estados_afn,alfabeto,transiciones_afn,estado_inicial_afn,estados_finales_afn)
# Mostrar el AFD resultante
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
