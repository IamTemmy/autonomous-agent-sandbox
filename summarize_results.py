import pandas as pd

LOG_FILE = "data/simulation_log.csv"

data = pd.read_csv(LOG_FILE)

if data.empty:
    print("No simulation data found.")
    exit()

preset = data["preset"].iloc[0] if "preset" in data.columns else "unknown"

start_population = data["population"].iloc[0]
end_population = data["population"].iloc[-1]
max_population = data["population"].max()
min_population = data["population"].min()

final_births = data["births"].iloc[-1]
final_deaths = data["deaths"].iloc[-1]

start_energy = data["average_energy"].iloc[0]
end_energy = data["average_energy"].iloc[-1]
max_energy = data["average_energy"].max()
min_energy = data["average_energy"].min()

start_speed = data["average_speed"].iloc[0]
end_speed = data["average_speed"].iloc[-1]

start_vision = data["average_vision"].iloc[0]
end_vision = data["average_vision"].iloc[-1]

start_energy_loss = data["average_energy_loss"].iloc[0]
end_energy_loss = data["average_energy_loss"].iloc[-1]

start_lineages = data["living_lineages"].iloc[0]
end_lineages = data["living_lineages"].iloc[-1]

duration = data["time_seconds"].iloc[-1]

print("\nAUTONOMOUS AGENT SANDBOX — EXPERIMENT SUMMARY")
print("=" * 55)

print(f"Preset: {preset}")
print(f"Duration: {duration:.1f} seconds")

print("\nPopulation")
print("-" * 55)
print(f"Start Population: {start_population}")
print(f"End Population: {end_population}")
print(f"Max Population: {max_population}")
print(f"Min Population: {min_population}")

print("\nBirths and Deaths")
print("-" * 55)
print(f"Total Births: {final_births}")
print(f"Total Deaths: {final_deaths}")

print("\nEnergy")
print("-" * 55)
print(f"Start Avg Energy: {start_energy:.2f}")
print(f"End Avg Energy: {end_energy:.2f}")
print(f"Max Avg Energy: {max_energy:.2f}")
print(f"Min Avg Energy: {min_energy:.2f}")

print("\nTraits")
print("-" * 55)
print(f"Avg Speed: {start_speed:.2f} → {end_speed:.2f}")
print(f"Avg Vision: {start_vision:.2f} → {end_vision:.2f}")
print(f"Avg Energy Loss: {start_energy_loss:.4f} → {end_energy_loss:.4f}")

print("\nLineages")
print("-" * 55)
print(f"Living Lineages: {start_lineages} → {end_lineages}")

print("\nInterpretation")
print("-" * 55)

if end_population > start_population:
    print("Population increased, suggesting the environment supported reproduction and survival.")
elif end_population < start_population:
    print("Population decreased, suggesting the environment applied strong survival pressure.")
else:
    print("Population stayed stable, suggesting a rough balance between survival and death.")

if end_energy > start_energy:
    print("Average energy increased, suggesting agents were generally successful at finding food.")
elif end_energy < start_energy:
    print("Average energy decreased, suggesting food access or environmental pressure was challenging.")
else:
    print("Average energy remained stable.")

if end_lineages < start_lineages:
    print("Some lineages disappeared, suggesting selection pressure favored certain inherited traits.")
else:
    print("Lineage diversity remained stable during this run.")