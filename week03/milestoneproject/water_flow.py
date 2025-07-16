# water_flow.py

# Definição das constantes físicas para evitar repetição
WATER_DENSITY = 998.2
GRAVITY_ACCELERATION = 9.80665
WATER_DYNAMIC_VISCOSITY = 0.0010016

# Definição das constantes de engenharia
PVC_SCHED80_INNER_DIAMETER = 0.28687
PVC_SCHED80_FRICTION_FACTOR = 0.013
SUPPLY_VELOCITY = 1.65

HDPE_SDR11_INNER_DIAMETER = 0.048692
HDPE_SDR11_FRICTION_FACTOR = 0.018
HOUSEHOLD_VELOCITY = 1.75

def water_column_height(tower_height, tank_height):
    """Calcula a altura da coluna de água."""
    return tower_height + (3 * tank_height) / 4

def pressure_gain_from_water_height(height):
    """Calcula o ganho de pressão a partir da altura da coluna de água."""
    return (WATER_DENSITY * GRAVITY_ACCELERATION * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calcula a perda de pressão devido ao atrito no cano."""
    numerator = -friction_factor * pipe_length * WATER_DENSITY * (fluid_velocity ** 2)
    denominator = 2000 * pipe_diameter
    return numerator / denominator

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calcula a perda de pressão devido às conexões no cano."""
    numerator = -0.04 * WATER_DENSITY * (fluid_velocity ** 2) * quantity_fittings
    denominator = 2000
    return numerator / denominator

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calcula o número de Reynolds."""
    numerator = WATER_DENSITY * hydraulic_diameter * fluid_velocity
    denominator = WATER_DYNAMIC_VISCOSITY
    return numerator / denominator

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Calcula a perda de pressão devido à redução do diâmetro do cano."""
    
    # Adiciona uma verificação para evitar divisão por zero.
    if reynolds_number == 0:
        return 0

    k_numerator = (larger_diameter / smaller_diameter) ** 4 - 1
    k = (0.1 + 50 / reynolds_number) * k_numerator
    
    p_numerator = -k * WATER_DENSITY * (fluid_velocity ** 2)
    p_denominator = 2000
    return p_numerator / p_denominator

def main():
    """Função principal que executa o programa interativo."""
    tower_height = float(input("Altura da torre de água (metros): "))
    tank_height = float(input("Altura das paredes do tanque de água (metros): "))
    length1 = float(input("Comprimento do cano de abastecimento (metros): "))
    quantity_angles = int(input("Número de 90° angulos no cano: "))
    length2 = float(input("Comprimento do cano da rua para a casa (metros): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    # Perdas de pressão no primeiro segmento de cano
    reynolds1 = reynolds_number(PVC_SCHED80_INNER_DIAMETER, SUPPLY_VELOCITY)
    loss = pressure_loss_from_pipe(PVC_SCHED80_INNER_DIAMETER, length1, PVC_SCHED80_FRICTION_FACTOR, SUPPLY_VELOCITY) # CORRIGIDO
    pressure += loss
    loss = pressure_loss_from_fittings(SUPPLY_VELOCITY, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(PVC_SCHED80_INNER_DIAMETER, SUPPLY_VELOCITY, reynolds1, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    # Perdas de pressão no segundo segmento de cano
    loss = pressure_loss_from_pipe(HDPE_SDR11_INNER_DIAMETER, length2, HDPE_SDR11_FRICTION_FACTOR, HOUSEHOLD_VELOCITY)
    pressure += loss

    print(f"\nPressão na casa: {pressure:.1f} kilopascals")

if __name__ == "__main__":
    main()