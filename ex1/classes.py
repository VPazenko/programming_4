class Atom:
    """
    This class represents any atom in the periodic table. 
    """
    def __init__(self, symbol, atomic_number, neutrons):
        """
        Symbol, atomic number and the number of neutrons in the core.
        """
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.neutrons = neutrons


    def proton_number(self):
        return self.atomic_number
    

    def mass_number(self):
        return self.atomic_number + self.neutrons
    

    def isotope (self, change_neutrons):
        self.neutrons = change_neutrons
        return self
    

    def __gt__(self, other):
        if self.atomic_number != other.atomic_number:
            raise Exception("Atomic numbers (number of protons) not equal!")
        return self.neutrons > other.neutrons

    def __eq__(self, other):
        if self.atomic_number != other.atomic_number:
            raise Exception("Atomic numbers (number of protons) not equal!")
        return self.neutrons == other.neutrons

    def __lt__(self, other):
        if self.atomic_number != other.atomic_number:
            raise Exception("Atomic numbers (number of protons) not equal!")
        return self.neutrons < other.neutrons

    def __le__(self, other):
        if self.atomic_number != other.atomic_number:
            raise Exception("Atomic numbers (number of protons) not equal!")
        return self.neutrons <= other.neutrons
        
    def __ge__(self, other):
        if self.atomic_number != other.atomic_number:
            raise Exception("Atomic numbers (number of protons) not equal!")
        return self.neutrons >= other.neutrons    


class Molecule:
    """
    This class represents any molecule. 
    Molecules look like: The first Atom, number of atoms, the second Atom, etc
    """
    def __init__(self, list_of_tuples):
        self.format = list_of_tuples
        self.repr = self.text()

    def text(self):
        '''
        Function creates a representation of the molecule.
        '''
        molecule = ''
        for elem in self.format:
            molecule += elem[0].symbol
            if elem[1] > 1:
                molecule += str(elem[1])
        return molecule

    def __str__(self):
        return self.repr
    
    def __repr__(self):
        return self.repr

    def __add__(self, other):
            return Molecule(self.format + other.format)

    def __eq__(self, other):
        if isinstance(other, Molecule):
            return self.repr == other.repr
        return self.repr == other

class Chloroplast:
    """
    This class represents a simplified version of the photosynthesis process
    """
    def __init__(self):
        self.water = 0
        self.co2 = 0

        hydrogen = Atom('H', 1, 0)
        carbon = Atom('C', 6, 6)
        oxygen = Atom('O', 8, 8)
        self.C6H12O6 = Molecule( [ (carbon, 6), (hydrogen, 12), (oxygen, 6) ] )
        self.O2 = Molecule( [(oxygen, 2),  ] )


    def add_H2O(self):
        '''
        Function increases the amount of water elements contained in the chloroplast
        '''
        self.water += 1


    def add_CO2(self):
        '''
        Function increases the amount of CO2 elements contained in the chloroplast
        '''
        self.co2 += 1


    def add_molecule(self, molecule):
        '''
        Function trying to add any molecule in the chloroplast.
        If there are enough molecules to photosynthesise, then makes it.
        '''
        try:
            print(molecule)
            func_name = f'add_{molecule}'
            func = getattr(self, func_name)
            func()

        except AttributeError:
            print("AttributeError: Wrong molecule. Only H2O and CO2 are allowed")
      
        finally:
            molecule_list = []
            if (self.water >= 6) and (self.co2 >= 12):
                self.water -= 6
                self.co2 -= 12
                molecule_list += [(self.C6H12O6, 1), (self.O2, 6)]
        
        return molecule_list


    def __str__(self):
        return f'Chloroplast contain {self.water} water moleculs and {self.co2} CO2 molecules'





if __name__ == "__main__":
    print(__doc__)
else:
    print(f"Module '{__name__}' is imported successfully!\n")