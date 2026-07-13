from qiskit import QuantumCircuit, QuantumRegister
import math

q = QuantumRegister(2, 'q')

Cx_qc = QuantumCircuit(q, name='CX')

Cx_qc.h(q[0])
Cx_qc.z(q[0])
Cx_qc.id(q[1])

Cx_qc.cx(q[0], q[1])
print(Cx_qc)

Cz_qc = QuantumCircuit(q, name='CZ')

Cz_qc.h(q[0])
Cz_qc.x(q[1])
Cz_qc.cz(q[0], q[1])
print(Cz_qc)

P_qc = QuantumCircuit(q, name='CP')
P_qc.x(q[0])
P_qc.h(q[1])
P_qc.cp(math.pi/2, q[0], q[1])
print(P_qc)

swap_qc = QuantumCircuit(q, name='SWAP')
swap_qc.x(q[0])
swap_qc.h(q[1])
swap_qc.swap(q[0], q[1])
print(swap_qc)

