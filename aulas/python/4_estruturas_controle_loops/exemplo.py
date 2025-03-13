dias_da_semana = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

for dia in dias_da_semana:
    if dia in ["sábado", "domingo"]:
        print(f"{dia.capitalize()}: Dormir até mais tarde!")
    else:
        print(f"{dia.capitalize()}: Alarme programado para 7h")
