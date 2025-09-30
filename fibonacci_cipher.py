import sys
import time

MODULO = 16384

def shiftUnicode(char, shift, modulo=MODULO):
    new_code = (ord(char) + shift) % modulo 
    return chr(new_code)


def fibonacciTranspose(plain_text, total_chars, k1, k2, block_size=10):
    f1, f2 = k1 % block_size, k2 % block_size
    transposed_text = []

    for i in range(0, len(plain_text), block_size):
        block = plain_text[i : i + block_size]
        shift = f1 % len(block)
        block = block[-shift:] + block[:-shift]
        transposed_text.append(block)
        f1, f2 = f2, (f1 + f2) % block_size

    return "".join(transposed_text)

def fibonacciDetranspose(cipher_text, total_chars, k1, k2, block_size=10):
    f1, f2 = k1 % block_size, k2 % block_size
    detransposed_text = []

    for i in range(0, len(cipher_text), block_size):
        block = cipher_text[i:i+block_size]
        shift = f1 % len(block)
        block = block[shift:] + block[:shift]
        detransposed_text.append(block)
        f1, f2 = f2, (f1 + f2) % block_size

    return "".join(detransposed_text)



def fibonacciSubstitute(plain_text, total_chars, k1, k2, modulo=MODULO):
    f1, f2 = k1 % modulo, k2 % modulo
    substituted_text = [] 
    for char in plain_text:
        cipher_char = shiftUnicode(char, f1, modulo)
        substituted_text.append(cipher_char)
        f1, f2 = f2, (f1 + f2) % modulo

    return "".join(substituted_text)


def fibonacciDesubstitute(cipher_text, total_chars, k1, k2, modulo=MODULO):
    f1, f2 = k1 % modulo, k2 % modulo
    desubstituted_text = [] 
    for char in cipher_text:
        plain_char = shiftUnicode(char, -f1, modulo)
        desubstituted_text.append(plain_char)
        f1, f2 = f2, (f1 + f2) % modulo

    return "".join(desubstituted_text)


def measureFibonacciCipher(plain_text, total_chars, k1, k2):
    start = time.time()
    substituted_text = fibonacciSubstitute(plain_text, total_chars, k1, k2)
    ciphered_text = fibonacciTranspose(substituted_text, total_chars, k1, k2)
    end = time.time()
    return end - start

def measureFibonacciDecipher(cipher_text, total_chars, k1, k2):
    start = time.time()
    detransposed_text = fibonacciDetranspose(cipher_text, total_chars, k1, k2)
    deciphered_text = fibonacciDesubstitute(detransposed_text, total_chars, k1, k2)
    end = time.time()
    return end - start

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python fibonacci_cipher.py <arquivo> <chave> [--decrypt]")
        sys.exit(1)

    input_file_name = sys.argv[1]
    key = sys.argv[2]

    decrypt_mode =  "--decrypt" in sys.argv
    measure_time = "--time" in sys.argv

    with open(input_file_name, 'r', encoding="utf-8") as input_file:
        text = input_file.read()

    total_chars = len(text)

    k1 = sum(ord(k) for k in key[0::2])
    k2 = sum(ord(k) for k in key[1::2])

    if k1 > k2:
        k1, k2 = k2, k1
    
    print(f"k1 = {k1}, k2 = {k2}")

    if measure_time:
        if decrypt_mode:
            elapsed = measureFibonacciDecipher(text, total_chars, k1, k2)
            print(f"Tempo de decifragem: {elapsed:.6f} segundos")
        else:
            elapsed = measureFibonacciCipher(text, total_chars, k1, k2)
            print(f"Tempo de cifragem: {elapsed:.6f} segundos")
    elif decrypt_mode:
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
