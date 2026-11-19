"""
PRJ.5 - Criptografia por mistura de caracteres com números complexos

1) Cada caractere vira um número (posição na tabela ALFABETO, começando em 1).
2) Dois caracteres seguidos formam um complexo: z = a + bi.
3) Cifrar: c = z * chave      Decifrar: z = c / chave
Multiplicar por um complexo gira e estica o ponto no plano cartesiano.
"""

import matplotlib.pyplot as plt

ALFABETO = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,!?áéíóúâêôãõçÁÉÍÓÚÂÊÔÃÕÇ"
CHAVE = complex(3, 4)   # número complexo diferente de zero


def valor(caractere):
    return ALFABETO.index(caractere) + 1


def caractere(numero):
    return ALFABETO[round(numero) - 1]


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
    plt.savefig("cifra_complexa.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    texto = input("Digite o texto: ") or "Ola, Mundo!"

    originais, cifrados = cifrar(texto, CHAVE)

    print("Original :", originais)
    print("Cifrado  :", cifrados)
    print("Decifrado:", decifrar(cifrados, CHAVE))

    plotar(originais, cifrados)