from qiskit import QuantumCircuit
import numpy as np

n = 4
qc = QuantumCircuit(n)

for target in range(n-1,-1,-1):
    qc.h(target)
    for control in range(target-1,-1,-1):
        r = target - control + 1
        qc.cp(2*np.pi/2**r, control, target)

for qubit in range(n//2):
    qc.swap(qubit, n-qubit-1)

print(qc)