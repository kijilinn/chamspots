import random

class Gene:
    """
    Represents a single genetic trait.
    """
    def __init__(self, name, dominant_allele, recessive_allele):
        self.name = name
        self.allele_1 = None 
        self.allele_2 = None
        self.dominant = dominant_allele
        self.recessive = recessive_allele

    def set_genotype(self, a1, a2):
        self.allele_1 = a1
        self.allele_2 = a2

    def get_phenotype(self):
        if self.allele_1 == self.dominant or self.allele_2 == self.dominant:
            return self.dominant
        else:
            return self.recessive

    def get_random_allele(self):
        return random.choice([self.allele_1, self.allele_2])

class Creature:
    """
    The actual animal.
    """
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.genetics = {} 

    def add_gene(self, gene_obj):
        self.genetics[gene_obj.name] = gene_obj

    def reproduce(self, partner, child_name):
        print(f"Breeding {self.name} with {partner.name}...")
        baby = Creature(child_name, self.species)

        for gene_name, gene in self.genetics.items():
            partner_gene = partner.genetics[gene_name]
            baby_allele_1 = gene.get_random_allele()
            baby_allele_2 = partner_gene.get_random_allele()

            baby_gene = Gene(gene_name, gene.dominant, gene.recessive)
            baby_gene.set_genotype(baby_allele_1, baby_allele_2)
            baby.add_gene(baby_gene)

        return baby

    def display_traits(self):
        print(f"--- Stats for {self.name} ({self.species}) ---")
        for name, gene in self.genetics.items():
            genotype = f"{gene.allele_1}{gene.allele_2}"
            phenotype = gene.get_phenotype()
            print(f"{name}: Code [{genotype}] -> Appearance: {phenotype}")
        print("-" * 30)
