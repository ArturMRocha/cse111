import math

# --- Funções de Cálculo ---

def compute_volume(radius, height):
    """Calcula o volume de um cilindro."""
    volume = math.pi * (radius**2) * height
    return volume

def compute_surface_area(radius, height):
    """Calcula a área da superfície de um cilindro."""
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    """Calcula a eficiência de armazenamento (volume / área de superfície)."""
    if surface_area == 0:
        return 0
    return volume / surface_area

def compute_cost_efficiency(volume, cost):
    """Calcula a eficiência de custo (volume / custo)."""
    if cost == 0:
        return 0
    return volume / cost

# --- Função Principal ---

def main():
    """
    Função principal que processa os dados das latas, calcula as eficiências
    e imprime os resultados.
    """
    # Dados das latas armazenados em uma lista de dicionários para fácil acesso
    cans_data = [
        {"name": "#1 Piquenique", "radius": 6.83, "height": 10.16, "cost": 0.28},
        {"name": "#1 Alto", "radius": 7.78, "height": 11.91, "cost": 0.43},
        {"name": "#2", "radius": 8.73, "height": 11.59, "cost": 0.45},
        {"name": "#2.5", "radius": 10.32, "height": 11.91, "cost": 0.61},
        {"name": "#3 Cilindro", "radius": 10.79, "height": 17.78, "cost": 0.86},
        {"name": "#5", "radius": 13.02, "height": 14.29, "cost": 0.83},
        {"name": "#6Z", "radius": 5.40, "height": 8.89, "cost": 0.22},
        {"name": "#8Z curto", "radius": 6.83, "height": 7.62, "cost": 0.26},
        {"name": "#10", "radius": 15.72, "height": 17.78, "cost": 1.53},
        {"name": "#211", "radius": 6.83, "height": 12.38, "cost": 0.34},
        {"name": "#300", "radius": 7.62, "height": 11.27, "cost": 0.38},
        {"name": "#303", "radius": 8.10, "height": 11.11, "cost": 0.42}
    ]

    # Variáveis para rastrear a melhor lata para cada eficiência
    best_storage_can = None
    max_storage_efficiency = -1
    best_cost_can = None
    max_cost_efficiency = -1

    print("--- Análise de Eficiência de Latas de Aço ---")

    # Loop para processar cada lata na lista
    for can in cans_data:
        # Extrai os dados da lata atual
        name = can["name"]
        radius = can["radius"]
        height = can["height"]
        cost = can["cost"]

        # Calcula o volume e a área da superfície
        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        
        # Calcula as eficiências
        storage_eff = compute_storage_efficiency(volume, surface_area)
        cost_eff = compute_cost_efficiency(volume, cost)
        
        # Imprime os resultados para a lata atual
        print(f"\nLata: {name}")
        print(f"  Eficiência de Armazenamento: {storage_eff:.4f}")
        print(f"  Eficiência de Custo: {cost_eff:.2f} cm³/dólar")

        # Verifica e atualiza a melhor eficiência de armazenamento
        if storage_eff > max_storage_efficiency:
            max_storage_efficiency = storage_eff
            best_storage_can = name

        # Verifica e atualiza a melhor eficiência de custo
        if cost_eff > max_cost_efficiency:
            max_cost_efficiency = cost_eff
            best_cost_can = name
    
    # Imprime os resultados finais
    print("\n" + "="*50)
    print("                 RESULTADOS FINAIS")
    print("="*50)
    print(f"Melhor Eficiência de Armazenamento:")
    print(f"  Lata: {best_storage_can}")
    print(f"  Eficiência: {max_storage_efficiency:.4f}")
    print("\nMelhor Eficiência de Custo:")
    print(f"  Lata: {best_cost_can}")
    print(f"  Eficiência: {max_cost_efficiency:.2f} cm³/dólar")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()