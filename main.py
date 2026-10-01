potencia_w = 2000
horas_uso = 5
tarifa_kwh = 0.85
uso_noturno = True

consumo_kwh = (potencia_w / 1000) * horas_uso

if uso_noturno:
    tarifa_kwh = tarifa_kwh * 0.7

custo_total = consumo_kwh * tarifa_kwh

print(f"Consumo: {consumo_kwh} kWh")
print(f"Custo Total: R$ {custo_total:.2f}")