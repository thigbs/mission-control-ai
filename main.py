from src.engine import executar_missao, analisar_com_ia

dados, alertas = executar_missao()

print("\n===================================")
print("      AGROSAT - MISSION CONTROL")
print("===================================\n")

print("DADOS DA MISSÃO")
print(f"NDVI: {dados['ndvi']}")
print(f"Temperatura: {dados['temperatura']} °C")
print(f"Armazenamento: {dados['armazenamento']} %")
print(f"Estabilidade: {dados['estabilidade']} %")

print("\nALERTAS")

for alerta in alertas:
    print(f"- {alerta}")

print("\nANÁLISE DA IA\n")

resultado = analisar_com_ia(dados, alertas)

print(resultado)
