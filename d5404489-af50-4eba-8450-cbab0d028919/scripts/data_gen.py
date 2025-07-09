import os
import pandas as pd
import numpy as np

# --- Setup paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')
os.makedirs(DATA_DIR, exist_ok=True)

# --- Seed for reproducibility ---
np.random.seed(42)

# --- 1. Force Composition by Country ---
countries = ['USA', 'China', 'Russia', 'India', 'UK', 'France', 'Germany', 'Brazil', 'Japan', 'South Korea']
force_types = ['Air', 'Navy', 'Ground']

composition_data = []
for country in countries:
    air = np.random.randint(500, 3000)
    navy = np.random.randint(100, 1000)
    ground = np.random.randint(100000, 1200000)
    composition_data.append([country, air, navy, ground])

composition_df = pd.DataFrame(composition_data, columns=['Country', 'Air_Units', 'Navy_Units', 'Ground_Units'])
composition_df.to_csv(os.path.join(DATA_DIR, 'force_composition.csv'), index=False)

# --- 2. Army Size by Country (for Map) ---
army_size_df = composition_df[['Country', 'Ground_Units']].copy()
army_size_df.rename(columns={'Ground_Units': 'Army_Size'}, inplace=True)
army_size_df.to_csv(os.path.join(DATA_DIR, 'army_size_map.csv'), index=False)

# --- 3. Budget Allocation by Force Type ---
budget_total = 800_000_000_000  # $800B global budget
force_labels = ['Air Force', 'Navy', 'Ground Forces', 'Cyber Command', 'Space Force']
allocations = np.random.dirichlet(np.ones(len(force_labels)), size=1)[0] * budget_total

budget_df = pd.DataFrame({
    'Force_Type': force_labels,
    'Budget_USD_Billions': np.round(allocations / 1e9, 2)
})
budget_df.to_csv(os.path.join(DATA_DIR, 'budget_allocation.csv'), index=False)

print("✅ Data generation complete. Files saved to /data:")
print("- force_composition.csv")
print("- army_size_map.csv")
print("- budget_allocation.csv")