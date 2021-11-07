
from pathlib import Path
from sys import path

path.append(Path(__file__).parent.absolute())

from land import Land
from species import Species
from simulation import Simulation

new_land = Land()
new_land.Set_Default_Dependences()

new_species = Species("Human")
new_species.Set_Default_Dependences()
new_species.change_characteristic("population", 10)

new_simulation = Simulation(1,1)

new_simulation.Add_Species(new_species)
new_simulation.Change_Land(new_land)

new_simulation.Set_Default_Inter_Dependences()

new_simulation.Move_One_Day_All()

print(new_simulation.actual_species[0])
print(new_simulation.map)