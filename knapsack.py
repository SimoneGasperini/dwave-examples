# Copyright 2022 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dimod import ConstrainedQuadraticModel, Binary, quicksum
from dwave.system import LeapHybridCQMSampler

values = [34, 25, 78, 21, 64]
weights = [3, 5, 9, 4, 2]
W = 10
n = len(values)

# Create the binary variables
x = [Binary(i) for i in range(n)]

# Construct the CQM
cqm = ConstrainedQuadraticModel()

# Add the objective
cqm.set_objective(quicksum(-values[i]*x[i] for i in range(n)))

# Add the two constraints
cqm.add_constraint(quicksum(weights[i]*x[i]
                   for i in range(n)) <= W, label='max weight')
cqm.add_constraint(quicksum(x[i] for i in range(n)) <= 2, label='max items')

# Submit to the CQM sampler
sampler = LeapHybridCQMSampler()
sampleset = sampler.sample_cqm(cqm)

feasible_sampleset = sampleset.filter(lambda row: row.is_feasible).aggregate()
print("\nFeasible sample set:")
print(feasible_sampleset)
