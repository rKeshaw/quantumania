from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import qasm2

qc = QuantumCircuit(2,1, name='qc')
qc.h(1)
qc.measure(1,0)
print(qc)
print(qasm2.dumps(qc))
print()
print(qc.data)
print(qc.qregs)
print(qc.cregs)
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()

counts = result.get_counts(qc)
print(counts)