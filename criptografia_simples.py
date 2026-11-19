"""
PRJ.5 - Criptografia por mistura de caracteres com números complexos (UTF-8)

1) Cada caractere vira um número: o seu código Unicode (0 a 0x10FFFF).
2) Dois caracteres seguidos formam um complexo: z = a + bi.
3) Cifrar: c = z * chave      Decifrar: z = c / chave
"""

import matplotlib.pyplot as plt

CHAVE = complex(3, 4)        

# Converte um caractere no seu código Unicode
def valor(caractere):
    return ord(caractere)

# Arredonda o número e o converte de volta no caractere correspondente
def caractere(numero):
    codigo = round(numero)
    return chr(codigo)


def cifrar(texto, chave):
    if len(texto) % 2 == 1:
        texto += " "                      # completa o último par
    originais = [complex(valor(texto[i]), valor(texto[i + 1]))
                 for i in range(0, len(texto), 2)]
    cifrados = [z * chave for z in originais]
    return originais, cifrados


def decifrar(cifrados, chave):
    texto = ""
    for c in cifrados:
        z = c / chave
        texto += caractere(z.real) + caractere(z.imag)
    return texto


def plotar(originais, cifrados):
    plt.figure(figsize=(8, 8))
    plt.scatter([z.real for z in originais], [z.imag for z in originais],
                color="blue", label="Texto original")
    plt.scatter([c.real for c in cifrados], [c.imag for c in cifrados],
                color="red", label="Texto cifrado")
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.xlabel("Parte Real")
    plt.ylabel("Parte Imaginária")
    plt.title(f"Cifra por número complexo (chave = {CHAVE})")
    plt.grid(True)
    plt.legend()
    plt.show()


texto = input("Digite o texto: ")

originais, cifrados = cifrar(texto, CHAVE)

print("Original :", originais)
print("Cifrado  :", cifrados)
print("Decifrado:", decifrar(cifrados, CHAVE))

plotar(originais, cifrados)