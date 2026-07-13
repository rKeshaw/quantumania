from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import qasm2

# first circuit
q = QuantumRegister(1, 'q')
c = ClassicalRegister(1, 'c')
qc = QuantumCircuit(q, c, name='qc1')

q2 = QuantumRegister(1, 'q2')
c2 = ClassicalRegister(1, 'c2')
qc2 = QuantumCircuit(q2, c2, name='qc2')

qc.add_register(c2)
qc.add_register(q2)
qc2.add_register(q)

qc.measure(q,c2)
qc2.h(q)

qc3 = qc.compose(qc2)
print(qc3)