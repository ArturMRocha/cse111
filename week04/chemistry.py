import re

# Constantes de índice para tornar o código mais legível, conforme a sugestão.
# Para a lista de valores no dicionário da tabela periódica (ex: ["Actinium", 227])
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

class FormulaError(ValueError):
    """Exceção personalizada para fórmulas químicas inválidas."""
    pass

def parse_formula(formula, periodic_table_dict):
    if not isinstance(formula, str) or not formula:
        raise FormulaError("Fórmula inválida: a entrada deve ser uma string não vazia.")

    # Um conjunto de símbolos de elementos válidos para consulta rápida.
    known_symbols = set(periodic_table_dict.keys())

    # Esta regex tokeniza a fórmula em uma lista de tuplas.
    # Cada tupla contém um símbolo/parêntese e sua quantidade subsequente.
    # Exemplo: "Mg(OH)2" -> [('Mg', ''), ('(', ''), ('O', ''), ('H', ''), (')', '2')]
    tokens = re.findall(r"([A-Z][a-z]*|\(|\))(\d*)", formula)
    
    if not tokens:
        raise FormulaError("Formato de fórmula química inválido.")

    # Uma pilha para gerenciar grupos aninhados dentro de parênteses. Cada item na
    # pilha é um dicionário que representa os elementos nesse escopo.
    stack = [{}]

    for symbol, count_str in tokens:
        # A quantidade padrão é 1 se nenhum número seguir o símbolo.
        quantity = int(count_str) if count_str else 1

        if symbol == "(":
            # Inicia um novo dicionário na pilha para o novo grupo.
            stack.append({})
        elif symbol in known_symbols:
            # Adiciona o elemento e sua quantidade ao dicionário do grupo atual.
            current_group = stack[-1]
            current_group[symbol] = current_group.get(symbol, 0) + quantity
        elif symbol == ")":
            if len(stack) < 2:
                raise FormulaError("Parênteses não correspondentes na fórmula.")
            
            # Remove o grupo concluído da pilha.
            top_group = stack.pop()
            
            # Obtém o dicionário do grupo pai.
            parent_group = stack[-1]

            # Multiplica as quantidades no grupo removido pela quantidade
            # que segue o parêntese e, em seguida, mescla-as no grupo pai.
            for element, count in top_group.items():
                parent_group[element] = parent_group.get(element, 0) + count * quantity
        else:
            raise FormulaError(f"Símbolo inválido: {symbol}")

    if len(stack) > 1:
        raise FormulaError("Parênteses não correspondentes na fórmula.")

    # As contagens finais estão no último dicionário restante na pilha.
    final_counts = stack[0]

    # Converte o dicionário para o formato de lista de listas necessário e o ordena.
    symbol_quantity_list = list(map(list, sorted(final_counts.items())))

    return symbol_quantity_list

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
        if symbol in periodic_table_dict:
            element_data = periodic_table_dict[symbol]
            # Utiliza a variável de índice para maior clareza.
            atomic_mass = element_data[ATOMIC_MASS_INDEX]
            total_molar_mass += atomic_mass * quantity
        else:
            # Este erro será pego pela função parse_formula, mas é uma boa prática
            # ter uma verificação aqui também.
            raise FormulaError(f"Elemento químico desconhecido na fórmula: {symbol}")
    return total_molar_mass

def main():
    """
    Função principal que executa o programa.
    """
    try:
        chemical_formula = input("Digite a fórmula química do composto: ")
        sample_mass = float(input("Digite a massa da amostra em gramas: "))

        periodic_table = make_periodic_table()
        # Chama a função parse_formula para obter a lista de símbolos e quantidades
        symbol_quantity_list = parse_formula(chemical_formula, periodic_table)
        
        molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)
        number_of_moles = sample_mass / molar_mass

        print(f"\n{'-'*30}")
        print(f"Massa Molar de {chemical_formula}: {molar_mass:.5f} g/mol")
        print(f"Número de Moles na amostra: {number_of_moles:.5f} moles")
        print(f"{'-'*30}")
    
    except FormulaError as e:
        print(f"\n[ERRO NA FÓRMULA] {e}")
        print("Por favor, verifique a fórmula digitada.")
    except KeyError as e:
        # Este erro é menos provável agora, mas mantido por segurança.
        print(f"\n[ERRO] Elemento químico desconhecido na fórmula: {e}")
        print("Por favor, verifique a fórmula digitada.")
    except ValueError:
        print("\n[ERRO] Valor inválido. A massa da amostra deve ser um número.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()