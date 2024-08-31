from classes import *


def assignment_1():
    protium = Atom('H', 1, 0)
    deuterium = Atom('H', 1, 1)
    oxygen = Atom('O', 8, 8)
    tritium = Atom('H', 1, 2)
    oxygen.isotope(9)

    assert tritium.neutrons == 2
    assert tritium.mass_number() == 3
    assert protium < deuterium
    assert deuterium <= tritium
    assert tritium >= protium
    #print (oxygen > tritium) # <-- this should raise an Exception


def assignment_2():
    hydrogen = Atom('H', 1, 0)
    carbon = Atom('C', 6, 6)
    oxygen = Atom('O', 8, 8)

    water = Molecule( [ (hydrogen, 2), (oxygen, 1) ] )
    co2 = Molecule( [ (carbon, 1), (oxygen, 2) ])
    print (water) # H2O
    print (co2) # CO2
    print (water + co2) # H2OCO2


def assignment_3():
    hydrogen = Atom('H', 1, 0)
    carbon = Atom('C', 6, 6)
    oxygen = Atom('O', 8, 8)

    water = Molecule( [ (hydrogen, 2), (oxygen, 1) ] )
    co2 = Molecule( [ (carbon, 1), (oxygen, 2) ])
    demo = Chloroplast()
    els = [water, co2]

    while (True):
        print ('\nWhat molecule would you like to add?')
        print ('[1] Water')
        print ('[2] carbondioxyde')
        print ('Please enter your choice: ', end='')
        try:
            choice = int(input())
            res = demo.add_molecule(els[choice-1])
            if (len(res)==0):
                print (demo)
            else:
                print ('\n=== Photosynthesis!')
                print (res)
                print (demo)

        except Exception:
            print ('\n=== That is not a valid choice.')


if __name__ == "__main__":
    assignment_1()
    assignment_2()
    assignment_3()