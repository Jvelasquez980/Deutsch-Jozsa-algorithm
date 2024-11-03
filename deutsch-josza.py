import numpy as np
from math import sqrt


def producto_tensorial(matrices): #Realizamos el producto tensorial de una lista de matrices
    producto = matrices[0]
    for matriz in matrices[1:]:
        producto = np.kron(producto, matriz)
    return producto

def U(n, f_map):
    num_qubits = n + 1
    U = np.zeros((2**num_qubits, 2**num_qubits)) # Mapea una matriz cuadrada de 2^n+1 columnas y filas

    for input_state in range(2**num_qubits):
        input_string = input_state >> 1
        output_qubit = (input_state & 1) ^ f_map[input_string]
        output_state = (input_string << 1) + output_qubit
        U[input_state, output_state] = 1

    return U

def measure(n, state): # Agarra las probabilidades del vector resultante 
    measurement = np.zeros(2**n)
    for index, value in enumerate(state):
        measurement[index >> 1] += value * value

    return abs(measurement[0]) > 1e-10  

def Deutsch_Jozsa(n, f_map):
    num_qubits = n + 1
    state_0 = np.array([[1], [0]]) #Construimos un estado 0
    X_gate = np.array([[0, 1], [1, 0]]) #Construimos la compuerta de negacion o X
    H_gate = np.array([[1, 1], [1, -1]]) / sqrt(2) # Construimos hadamard

    ancilla = np.dot(X_gate, state_0) # La ancilla la creamos negando el estado 0

    listStates = [state_0] * n + [ancilla] # Inicia todos los qbit(0) y le añade el qbit(1) 
    listGates_H = [H_gate] * (n + 1) #Crea todas las compuertas hadamar

    psi_0 = producto_tensorial(listStates) #Realiza el producto tesorial de todos lo Qbits |ψ_0> 
    composite_H = producto_tensorial(listGates_H) # Realiza el mismo procedimiento para todas las compuertas hadamard

    psi_1 = np.dot(composite_H, psi_0) #|ψ_1>  Aplicamos producto punto a los vectores resultantes de |ψ_0> con las compuertas hadamar de la lista 
    psi_2 = np.dot(U(n, f_map), psi_1) #|ψ_2> Aplicamos la funcion
    psi_3 = np.dot(composite_H, psi_2) #|ψ_3> Cancelamos en hadamard aplicandolo nuevamente 

    return measure(n, psi_3) #Realizamos la medicion :D

def main(n):
    num_functions = 2**(2**n)
    results = []

    for i in range(num_functions):
        f_map = [(i >> j) & 1 for j in range(2**n)]

        # Validación previa: determinar si es constante o balanceada antes de ejecutar Deutsch-Jozsa
        is_constant = all(x == f_map[0] for x in f_map)
        is_balanced = sum(f_map) == (2**(n-1))

        if not is_constant and not is_balanced:
            result = "indefinida"  # La función no es ni constante ni balanceada
        else:
            dj_result = Deutsch_Jozsa(n, f_map)
            result = "constant" if dj_result else "balanced"

        results.append({
            "function": f_map,
            "is_balanced": is_balanced,
            "is_constant": is_constant,
            "num_bits_in_1": sum(f_map),
            "result": result
        })

    # Escribimos el resultado en el formato que se nos pide ademas de que este se escribe en un txt, Deutsch_Jozsa_results.txt
    with open("Deutsch_Jozsa_results.txt", "w") as file:
        file.write("Función\t\t\tEs balanceada\tEs constante\tNúmero de bits en 1\tResultado\n")
        for res in results:
            func_str = "".join(map(str, res['function']))
            file.write(f"{func_str}\t\t{res['is_balanced']}\t\t{res['is_constant']}\t\t{res['num_bits_in_1']}\t\t{res['result']}\n")


main(4) 
# A la funcion main le pasamos el n

# Para tener una mejor visualizacion de los resultados decidi nombrar los resultados que no son ni constantes ni balanceados como indefinidos
# Ademas ecribí estos dentro de un txt Deutsch_Jozsa_results.txt para poder visualizarlos completamente