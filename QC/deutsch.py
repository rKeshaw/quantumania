from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import random

def oracle(type):
    qc = QuantumCircuit(2)
    if type == 'constant':
        output = random.choice([0, 1])
        if output == 1:
            qc.x(1)
    elif type == 'balanced':
        qc.cx(0, 1)
    return qc

def deutsch(type='balanced'):
    qc = QuantumCircuit(2,1)
    qc.x(1)
    qc.h(0)
    qc.h(1)

    oracle_qc = oracle(type)
    qc.compose(oracle_qc, inplace=True)

    qc.h(0)
    qc.measure(0,0)
    return qc

type = 'balanced'
qc = deutsch(type)

simulator = AerSimulator()
result = simulator.run(qc).result()
counts = result.get_counts()

print(counts)
