import matplotlib.pyplot as plt

def cifrar(texto, k):
    # cada caractere -> número complexo (código ASCII + 0i), multiplicado pela chave
    return [complex(ord(ch), 0) * k for ch in texto]

def decifrar(cifrado, k):
    # divide pela chave e volta ao caractere
    return "".join(chr(round((c / k).real)) for c in cifrado)

texto = input("Texto: ")
k = complex(input("Chave (ex: 2+3j): ").replace(" ", ""))

cifrado = cifrar(texto, k)
print("Cifrado:", cifrado)
print("Decifrado:", decifrar(cifrado, k))

# --- gráfico no plano cartesiano ---
original = [complex(ord(ch), 0) for ch in texto]
plt.scatter([z.real for z in original], [z.imag for z in original], label="Original")
plt.scatter([z.real for z in cifrado], [z.imag for z in cifrado], label="Cifrado")
plt.axhline(0, color="k"); plt.axvline(0, color="k")
plt.xlabel("Parte Real"); plt.ylabel("Parte Imaginária")
plt.title("Caracteres no plano complexo")
plt.legend(); plt.grid(True); plt.show()