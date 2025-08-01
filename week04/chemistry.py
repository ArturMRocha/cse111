from formula import parse_formula

# Constantes de índice para tornar o código mais legível, conforme a sugestão.
# Para a lista de valores no dicionário da tabela periódica (ex: ["Actinium", 227])
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1


def make_periodic_table():
    periodic_table_dict = {
        "Ac": ["Actinium", 227], "Ag": ["Silver", 107.8682], "Al": ["Aluminum", 26.9815386],
        "Ar": ["Argon", 39.948], "As": ["Arsenic", 74.9216], "At": ["Astatine", 210],
        "Au": ["Gold", 196.966569], "B":  ["Boron", 10.811], "Ba": ["Barium", 137.327],
        "Be": ["Beryllium", 9.012182], "Bi": ["Bismuth", 208.9804], "Br": ["Bromine", 79.904],
        "C":  ["Carbon", 12.0107], "Ca": ["Calcium", 40.078], "Cd": ["Cadmium", 112.411],
        "Ce": ["Cerium", 140.116], "Cl": ["Chlorine", 35.453], "Co": ["Cobalt", 58.933195],
        "Cr": ["Chromium", 51.9961], "Cs": ["Cesium", 132.9054519], "Cu": ["Copper", 63.546],
        "Dy": ["Dysprosium", 162.5], "Er": ["Erbium", 167.259], "Eu": ["Europium", 151.964],
        "F":  ["Fluorine", 18.9984032], "Fe": ["Iron", 55.845], "Fr": ["Francium", 223],
        "Ga": ["Gallium", 69.723], "Gd": ["Gadolinium", 157.25], "Ge": ["Germanium", 72.64],
        "H":  ["Hydrogen", 1.00794], "He": ["Helium", 4.002602], "Hf": ["Hafnium", 178.49],
        "Hg": ["Mercury", 200.59], "Ho": ["Holmium", 164.93032], "I":  ["Iodine", 126.90447],
        "In": ["Indium", 114.818], "Ir": ["Iridium", 192.217], "K":  ["Potassium", 39.0983],
        "Kr": ["Krypton", 83.798], "La": ["Lanthanum", 138.90547], "Li": ["Lithium", 6.941],
        "Lu": ["Lutetium", 174.9668], "Mg": ["Magnesium", 24.305], "Mn": ["Manganese", 54.938045],
        "Mo": ["Molybdenum", 95.96], "N":  ["Nitrogen", 14.0067], "Na": ["Sodium", 22.98976928],
        "Nb": ["Niobium", 92.90638], "Nd": ["Neodymium", 144.242], "Ne": ["Neon", 20.1797],
        "Ni": ["Nickel", 58.6934], "Np": ["Neptunium", 237], "O":  ["Oxygen", 15.9994],
        "Os": ["Osmium", 190.23], "P":  ["Phosphorus", 30.973762], "Pa": ["Protactinium", 231.03588],
        "Pb": ["Lead", 207.2], "Pd": ["Palladium", 106.42], "Pm": ["Promethium", 145],
        "Po": ["Polonium", 209], "Pr": ["Praseodymium", 140.90765], "Pt": ["Platinum", 195.084],
        "Pu": ["Plutonium", 244], "Ra": ["Radium", 226], "Rb": ["Rubidium", 85.4678],
        "Re": ["Rhenium", 186.207], "Rh": ["Rhodium", 102.9055], "Rn": ["Radon", 222],
        "Ru": ["Ruthenium", 101.07], "S":  ["Sulfur", 32.065], "Sb": ["Antimony", 121.76],
        "Sc": ["Scandium", 44.955912], "Se": ["Selenium", 78.96], "Si": ["Silicon", 28.0855],
        "Sm": ["Samarium", 150.36], "Sn": ["Tin", 118.71], "Sr": ["Strontium", 87.62],
        "Ta": ["Tantalum", 180.94788], "Tb": ["Terbium", 158.92535], "Tc": ["Technetium", 98],
        "Te": ["Tellurium", 127.6], "Th": ["Thorium", 232.03806], "Ti": ["Titanium", 47.867],
        "Tl": ["Thallium", 204.3833], "Tm": ["Thulium", 168.93421], "U":  ["Uranium", 238.02891],
        "V":  ["Vanadium", 50.9415], "W":  ["Tungsten", 183.84], "Xe": ["Xenon", 131.293],
        "Y":  ["Yttrium", 88.90585], "Yb": ["Ytterbium", 173.054], "Zn": ["Zinc", 65.38],
        "Zr": ["Zirconium", 91.224]
    }
    return periodic_table_dict


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """
    Calcula e retorna a massa molar total de uma lista de elementos e suas quantidades.
    """
    total_molar_mass = 0.0
    for symbol, quantity in symbol_quantity_list:
        element_data = periodic_table_dict[symbol]
        # Utiliza a variável de índice para maior clareza.
        atomic_mass = element_data[ATOMIC_MASS_INDEX]
        total_molar_mass += atomic_mass * quantity
    return total_molar_mass


def main():
    """
    Função principal que executa o programa.
    """
    try:
        chemical_formula = input("Digite a fórmula química do composto: ")
        sample_mass = float(input("Digite a massa da amostra em gramas: "))

        periodic_table = make_periodic_table()
        symbol_quantity_list = parse_formula(chemical_formula)
        molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)
        number_of_moles = sample_mass / molar_mass

        print(f"\n{'-'*30}")
        print(f"Massa Molar de {chemical_formula}: {molar_mass:.5f} g/mol")
        print(f"Número de Moles na amostra: {number_of_moles:.5f} moles")
        print(f"{'-'*30}")

    except FileNotFoundError:
        print("\n[ERRO] O arquivo 'elements.csv' não foi encontrado.")
        print("Por favor, certifique-se de que ele está na mesma pasta que o programa.")
    except KeyError as e:
        print(f"\n[ERRO] Elemento químico desconhecido na fórmula: {e}")
        print("Por favor, verifique a fórmula digitada.")
    except ValueError:
        print("\n[ERRO] Valor inválido. A massa da amostra deve ser um número.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    main()