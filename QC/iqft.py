from qiskit import QuantumCircuit
import numpy as np

n = 4
qc = QuantumCircuit(n)

for qubit in range(n//2):
    qc.swap(qubit, n-qubit-1)

for target in range(n):
    qc.h(target)
    for control in range(target):
        r = target - control + 1
        qc.cp(-2*np.pi/2**r, control, target)


print(qc)