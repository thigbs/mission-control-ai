def avaliar(dados):

    alertas = []

    if dados["temperatura"] > 70:
        alertas.append("Temperatura crítica do sensor.")

    if dados["ndvi"] < 0.5:
        alertas.append("NDVI abaixo do ideal.")

    if dados["armazenamento"] > 85:
        alertas.append("Armazenamento quase cheio.")

    if dados["estabilidade"] < 80:
        alertas.append("Estabilidade orbital baixa.")

    if not alertas:
        alertas.append("Operação normal.")

    return alertas
