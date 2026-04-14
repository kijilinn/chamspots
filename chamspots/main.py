# We need to import the classes from the file we just made
from genetics import Gene, Creature 

# --- THE SIMULATION ---

# 1. Define the trait
fur_gene = Gene("Fur Color", "B", "b")

# 2. Create the Parents
mum = Creature("Luna", "Raccoon")
mum.add_gene(fur_gene)
mum.genetics["Fur Color"].set_genotype("B", "B") 

dad = Creature("Bandit", "Raccoon")
dad.add_gene(fur_gene)
dad.genetics["Fur Color"].set_genotype("B", "b")

# 3. Show the parents
mum.display_traits()
dad.display_traits()

# 4. Make babies!
print(f"--- OFFSPRING REPORT ---")
for i in range(1, 6):
    child_name = f"Kit #{i}"
    child = mum.reproduce(dad, child_name)
    child.display_traits()
