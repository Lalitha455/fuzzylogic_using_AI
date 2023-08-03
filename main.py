import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
# Define fuzzy variables
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')
# Define membership functions
quality.automf(3)
service.automf(3)
tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])
# Define rules
rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])
# Create control system
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
# Create simulation
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)
# Pass inputs to simulation
tipping.input['quality'] = 6.5
tipping.input['service'] = 9.8
# Compute output
tipping.compute()
# Print output
print(tipping.output['tip'])

