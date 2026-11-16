# Complex Crypto Mixer

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![FATEC](https://img.shields.io/badge/FATEC-Jacare%C3%AD-red.svg)](https://fatecjacarei.edu.br)

---

## 📖 Sobre o Projeto

Este projeto implementa um **algoritmo criptográfico educacional** que utiliza **números complexos** como chave para cifrar e decifrar textos. A ideia central é representar cada caractere como um ponto no plano cartesiano (parte real = código ASCII, parte imaginária = 0 ou posição) e aplicar multiplicação por um número complexo fixo (a chave) para embaralhar as posições — essencialmente uma rotação + escala no plano complexo.

### Conceitos matemáticos envolvidos
- Números complexos: $z = a + bi$
- Multiplicação no plano complexo = rotação + homotetia
- Representação geométrica no plano de Argand-Gauss
- Inversibilidade: $z \cdot k \cdot k^{-1} = z$ (descriptografia)

---

## 🎯 Funcionalidades

- [x] **Criptografia**: Transforma texto plano em texto cifrado via multiplicação complexa
- [x] **Descriptografia**: Recupera o texto original usando a mesma chave (inverso multiplicativo)
- [x] **Visualização no plano cartesiano**: Plota caracteres original vs. cifrado
- [x] **Chave configurável**: Qualquer número complexo não-nulo funciona como chave
- [x] **Interface CLI**: Uso simples via terminal

---

## 🚀 Como executar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/complex-crypto-mixer.git
cd complex-crypto-mixer

# (Opcional) Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Instale dependências (se houver)
pip install -r requirements.txt

# Execute
python main.py --encrypt "Mensagem secreta" --key "3+4j"
python main.py --decrypt "Texto_cifrado_aqui" --key "3+4j"
```

---

## 📐 Fundamentação Matemática

### Representação dos caracteres
Cada caractere `c` é mapeado para um número complexo:


### Criptografia
Dada uma chave $k = a + bi \neq 0$:


### Descriptografia
Usando o inverso multiplicativo $k^{-1} = \frac{a - bi}{a^2 + b^2}$:


### Visualização no plano cartesiano
- **Eixo X (Real)**: Parte real do número complexo
- **Eixo Y (Imaginário)**: Parte imaginária do número complexo
- Pontos azuis = caracteres originais
- Pontos vermelhos = caracteres cifrados
- A multiplicação por $k$ corresponde a uma **rotação** de $\arg(k)$ radianos e **escala** de $|k|$

---

## 📁 Estrutura do Projeto


---

## 🧪 Exemplo de uso

```python
from crypto.complex_cipher import ComplexCipher

# Chave: 2 + 3i (rotação ~56° + escala √13)
cipher = ComplexCipher(key=complex(2, 3))

texto = "FATEC"
cifrado = cipher.encrypt(texto)
decifrado = cipher.decrypt(cifrado)

print(f"Original:  {texto}")
print(f"Cifrado:   {cifrado}")
print(f"Decifrado: {decifrado}")
# Original:  FATEC
# Cifrado:   [caracteres embaralhados]
# Decifrado: FATEC
```

---

## 📊 Visualização

O módulo `visualization.py` gera gráficos mostrando:
- Dispersão dos pontos originais (eixo real = ASCII, imaginário = 0)
- Dispersão dos pontos cifrados (rotacionados/escalados)
- Linhas conectando cada par original→cifrado
- Círculo unitário e vetor da chave para referência

```python
from crypto.visualization import plot_complex_transform

plot_complex_transform(texto_original, texto_cifrado, key=complex(2, 3))
```

---

## ⚠️ Limitações & Avisos

> **⚠ Uso educacional apenas** — Este **não** é um algoritmo criptográfico seguro para uso real. A multiplicação por um número complexo fixo é uma cifra de substituição monoalfabética vulnerável a análise de frequência e ataques de texto plano conhecido. Use apenas para fins didáticos.

- Chave deve ser não-nula ($a^2 + b^2 \neq 0$)
- Caracteres fora do range ASCII básico podem ter comportamento inesperado
- Precisão de ponto flutuante pode causar pequenos erros de arredondamento

---

## 👥 Autores

| Nome | GitHub | Papel |
|------|--------|-------|
| Guilherme Matos | [@gm-paiva](https://github.com/gm-paiva) | Desenvolvedor |
| Mariana | [@Mari432hz](https://github.com/Mari432hz) | Desenvolvedora |

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License** — veja o arquivo [LICENSE](LICENSE) para detalhes.

---
