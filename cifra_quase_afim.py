import matplotlib.pyplot as plt

# Chave secreta única (número complexo diferente de zero)
CHAVE = 2 + 3j

def criptografar(texto):
    if len(texto) % 2 != 0:
        texto += " "  # Preenche com espaço se for ímpar
    
    originais = []
    cifrados = []
    
    for i in range(0, len(texto), 2):
        # Converte o par de caracteres em um ponto (a + bj)
        M = complex(ord(texto[i]), ord(texto[i+1]))
        C = M * CHAVE  # Mistura apenas por multiplicação
        
        originais.append(M)
        cifrados.append(C)
        
    return originais, cifrados

def descriptografar(cifrados):
    texto_decifrado = ""
    for C in cifrados:
        M = C / CHAVE
        letra1 = chr(round(M.real))
        letra2 = chr(round(M.imag))
        texto_decifrado += letra1 + letra2
    return texto_decifrado

# --- Execução do Programa ---
texto_entrada = input("Digite o texto para criptografar: ")

pontos_originais, pontos_cifrados = criptografar(texto_entrada)
texto_recuperado = descriptografar(pontos_cifrados)

print("\nPontos Originais (Complexos):", pontos_originais)
print("Pontos Cifrados (Complexos):", pontos_cifrados)
print("Texto Decifrado:", texto_recuperado)

# --- Ilustração no Plano Cartesiano (Argand-Gauss) ---
plt.figure(figsize=(8, 6))

# Plota os pontos originais (Azul)
plt.scatter([z.real for z in pontos_originais], [z.imag for z in pontos_originais], 
            color='blue', label='Texto Original (Pares ASCII)', s=80)

# Plota os pontos cifrados (Vermelho)
plt.scatter([z.real for z in pontos_cifrados], [z.imag for z in pontos_cifrados], 
            color='red', label='Texto Cifrado (Multiplicado pela Chave)', s=80)

# Linhas de grade e eixos
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle='--', alpha=0.6)
plt.title(f"Criptografia no Plano Complexo (Chave = {CHAVE})")
plt.xlabel("Parte Real (1º Caractere do par)")
plt.ylabel("Parte Imaginária (2º Caractere do par)")
plt.legend()
plt.show()
