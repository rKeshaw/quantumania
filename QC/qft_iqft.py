from qiskit import QuantumCircuit
import numpy as np
from qiskit_aer import AerSimulator

n = 4

def qft(qc, n):
    for target in range(n-1,-1,-1):
        qc.h(target)
        for control in range(target-1,-1,-1):
            r = target - control + 1
            qc.cp(2*np.pi/2**r, control, target)

    for qubit in range(n//2):
        qc.swap(qubit, n-qubit-1)
    
    return qc

def iqft(qc, n):
    for qubit in range(n//2):
        qc.swap(qubit, n-qubit-1)

    for target in range(n):
        for control in range(target):
            r = target - control + 1
            qc.cp(-2*np.pi/2**r, control, target)
        qc.h(target)

    return qc

qft_qc = qft(QuantumCircuit(n), n)
print(qft_qc)
iqft_qc = iqft(QuantumCircuit(n), n)
print(iqft_qc)

simulator = AerSimulator()

qft_measured = qft_qc.copy()
qft_measured.measure_all()
result = simulator.run(qft_measured).result()
counts = result.get_counts()
print(counts)

iqft_measured = iqft_qc.copy()
iqft_measured.measure_all()
result = simulator.run(iqft_measured).result()
counts = result.get_counts()
print(counts)

combo_qc = qft_qc.compose(iqft_qc)
combo_qc.measure_all()
combo_result = simulator.run(combo_qc).result()
counts = combo_result.get_counts()
print(counts)
