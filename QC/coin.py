from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1,1)

qc.h(0)
qc.measure(0,0)

M = AerSimulator().run(qc, shots=1000).result().get_counts()
print("Heads:", M['0'], "Tails:", M['1'])
