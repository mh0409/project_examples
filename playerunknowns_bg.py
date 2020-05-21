# Import libraries and files that will be used
from datetime import datetime, timedelta
import csv
# import random
import MotifTools
import SimulTools
import matplotlib.pyplot as plt
import time

# Task 0:  Load data
# Read kills.txt data
kills = MotifTools.get_data('../assignment-final-data/kills.txt')

# Read cheaters.txt data
cheaters = MotifTools.get_data('../assignment-final-data/cheaters.txt')
cheat_dict = {x[0]:MotifTools.get_time(x[1]) for x in cheaters}

# Task 1: Find number of vicitm-cheater motifs
killer_cheaters = MotifTools.find_motifs(kills, cheat_dict)

print("Count of players who became cheaters within 5 days of being killed by\
 a cheater:", killer_cheaters)

# Task 2: Simulating an alternate universe
# Create dictionary of the kill data rows, with match IDs as keys
match_dict = SimulTools.make_custom_dict(kills, cheat_dict, 0, 0,\
                len(kills[0]) - 1)

# From above dict, create new dict containing only matches with cheaters
# at the match time
cheat_matches = SimulTools.find_cheating_matches(match_dict, cheat_dict)

# Create list that will hold the count of victim_-cheater motifs for simulations
simulation_cheaters = []

# Run 10 simulations:
for i in range(1, 11):
    # Create simulated kills data
    simulation = SimulTools.run_simulation(cheat_matches, cheat_dict)

    # Calculate number of cheaters for each simulation
    sim_killer_cheaters = MotifTools.find_motifs(simulation, cheat_dict)

    # Append to list of simulation cheater counts
    simulation_cheaters.append(sim_killer_cheaters)

# Inspect number of cheaters per simulation
print("Cheaters in each simulation: ", simulation_cheaters)

# Task 3: Create plot of real victim-cheater motifs vs. simulations

# Create plot of simulations
x = [x for x in range(1, 11)] # create x - number of simulation
plt.bar(x, simulation_cheaters, align = 'center', alpha=0.5)
x_pos = range(1, 11) # create x-tick labels
plt.xticks(x_pos, x_pos) # assign x-tick labels
plt.yticks([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
plt.ylabel('Number of victim-cheater motifss')
plt.xlabel('Simulation')
plt.title('Number of victim-cheater motifs per PU:BG simulation')
# Add horizontal line showing original victim-cheater motif
plt.axhline(killer_cheaters, color = 'g', linestyle = '--')
plt.text(4, killer_cheaters - 2, 'Motifs in orginal data: 29',
ha = 'left', va = 'center')
plt.show()
