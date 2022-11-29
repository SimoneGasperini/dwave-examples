from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import BinaryQuadraticModel
import dwave.inspector

projects = ['p1', 'p2', 'p3', 'p4', 'p5']
profits = [20, 18, 22, 26, 21]

sampler = EmbeddingComposite(DWaveSampler())

bqm = BinaryQuadraticModel('BINARY')

# maximize the total profit --> min(-prof*proj)
variables = [(proj, -prof) for proj, prof in zip(projects, profits)]
bqm.add_variables_from(variables)

# pick at most one between p1 and p2 --> p1+p2 <= 1*gamma
bqm.add_interactions_from([('p1', 'p2', 30)])

sampleset = sampler.sample(bqm, num_reads=100)

dwave.inspector.show(sampleset)
print(sampleset)
