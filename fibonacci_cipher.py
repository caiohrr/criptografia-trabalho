import sys

def shiftUnicode(char, shift, modulo=16384):
    new_code = (ord(char) + shift) % modulo 
    return chr(new_code)

def generateFibonacciPermutation(total_chars, k1, k2):
    f1, f2 = k1, k2
    available = list(range(total_chars))
    permutation = []
    for i in range(total_chars):
        index = f1 % len(available)
        permutation.append(available.pop(index))
        f1, f2 = f2, f1 + f2

    return permutation

def fibonacciTranspose(plain_text, total_chars, k1, k2):
    permutation = generateFibonacciPermutation(total_chars, k1, k2)
    transposed_text = [plain_text[i] for i in permutation]

    return "".join(transposed_text)

def fibonacciDetranspose(cipher_text, total_chars, k1, k2):
    permutation = generateFibonacciPermutation(total_chars, k1, k2)

    inverse_permutation = [0] * total_chars
    for i, p in enumerate(permutation):
        inverse_permutation[p] = i

    detransposed_text = [cipher_text[i] for i in inverse_permutation]
    return "".join(detransposed_text)

def fibonacciSubstitute(plain_text, total_chars, k1, k2):
    f1, f2 = k1, k2
    substituted_text = [] 
    for char in plain_text:
        cipher_char = shiftUnicode(char, f1)
        substituted_text.append(cipher_char)
        f1, f2 = f2, f1 + f2

    return "".join(substituted_text)


def fibonacciDesubstitute(cipher_text, total_chars, k1, k2):
    f1, f2 = k1, k2
    desubstituted_text = [] 
    for char in cipher_text:
        plain_char = shiftUnicode(char, -f1)
        desubstituted_text.append(plain_char)
        f1, f2 = f2, f1 + f2

    return "".join(desubstituted_text)



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python fibonacci_cipher.py <arquivo> <chave> [--decrypt]")
        sys.exit(1)

    input_file_name = sys.argv[1]
    key = sys.argv[2]
    decrypt_mode = len(sys.argv) > 3 and sys.argv[3] == "--decrypt"

    with open(input_file_name, 'r', encoding="utf-8") as input_file:
        text = input_file.read()

    total_chars = len(text)

    k1 = sum(ord(k) for k in key[0::2])
    k2 = sum(ord(k) for k in key[1::2])

    if k1 > k2:
        k1, k2 = k2, k1
    
    print(f"k1 = {k1}, k2 = {k2}")

    if decrypt_mode:
        print(f"Decifrando o arquivo {input_file_name} com a chave {key}")
        
        detransposed_text = fibonacciDetranspose(text, total_chars, k1, k2)
        deciphered_text = fibonacciDesubstitute(detransposed_text, total_chars, k1, k2)

        output_file_name = f"{input_file_name.split('.')[0]}-decifrado.txt"
        with open(output_file_name, "w", encoding="utf-8") as output_file:
            output_file.write(deciphered_text)

        print(f"Arquivo decifrado salvo em {output_file_name}")

    else:
        print(f"Cifrando o arquivo {input_file_name} com a chave {key}")

        substituted_text = fibonacciSubstitute(text, total_chars, k1, k2)
        ciphered_text = fibonacciTranspose(substituted_text, total_chars, k1, k2)

        output_file_name = f"{input_file_name.split('.')[0]}-cifrado.txt"
        with open(output_file_name, "w", encoding="utf-8") as output_file:
            output_file.write(ciphered_text)

        print(f"Arquivo cifrado salvo em {output_file_name}")
