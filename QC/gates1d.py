from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.quantum_info import Statevector
import math

q = QuantumRegister(1, 'q')
c = ClassicalRegister(1, 'c')
I_qc = QuantumCircuit(q, name='I')

I_qc.id(q)
I_qc.id(q)
print(I_qc)

H_qc = QuantumCircuit(q, name='H')
H_qc.h(q)
print(H_qc)

X_qc = QuantumCircuit(q, name='X')
X_qc.x(q)
print(X_qc)

Y_qc = QuantumCircuit(q, name='Y')
Y_qc.y(q)
print(Y_qc)

Z_qc = QuantumCircuit(q, name='Z')
Z_qc.z(q)
print(Z_qc)

P_qc = QuantumCircuit(q, name='p')
P_qc.p(math.pi/4, q)
print(P_qc)

# state = Statevector(P_qc)
# print(state.data)

S_qc = QuantumCircuit(q, name='S')
S_qc.s(q)
print(S_qc)

T_qc = QuantumCircuit(q, name='T')
T_qc.t(q)
print(T_qc)

Rx_qc = QuantumCircuit(q, name='Rx')
Rx_qc.rx(math.pi/2, q)
print(Rx_qc)

Ry_qc = QuantumCircuit(q, name='Ry')
Ry_qc.ry(math.pi/2, q)
print(Ry_qc)

Rz_qc = QuantumCircuit(q, name='Rz')
Rz_qc.rz(math.pi/2, q)
print(Rz_qc)