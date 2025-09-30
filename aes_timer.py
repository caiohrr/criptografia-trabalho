import subprocess
import sys
import time
import os

def measure_aes_cipher(input_file, output_file, key):
    start = time.time()
    # Comando OpenSSL AES-256-CBC cifragem
    subprocess.run([
        "openssl", "enc", "-aes-256-cbc",
        "-salt",
        "-in", input_file,
        "-out", output_file,
        "-k", key
    ], check=True)
    end = time.time()
    return end - start

def measure_aes_decipher(input_file, output_file, key):
    start = time.time()
    # Comando OpenSSL AES-256-CBC decifragem
    subprocess.run([
        "openssl", "enc", "-d", "-aes-256-cbc",
        "-in", input_file,
        "-out", output_file,
        "-k", key
    ], check=True)
    end = time.time()
    return end - start

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Uso: python aes_timer.py <arquivo> <chave> <modo:cipher|decipher>")
        sys.exit(1)

    input_file = sys.argv[1]
    key = sys.argv[2]
    mode = sys.argv[3].lower()

    base_name = os.path.splitext(input_file)[0]

    if mode == "cipher":
        output_file = f"{base_name}-aes.enc"
        elapsed = measure_aes_cipher(input_file, output_file, key)
        print(f"Arquivo cifrado salvo em {output_file}")
        print(f"Tempo de cifragem AES: {elapsed:.6f} segundos")
    elif mode == "decipher":
        output_file = f"{base_name}-aes.dec.txt"
        elapsed = measure_aes_decipher(input_file, output_file, key)
        print(f"Arquivo decifrado salvo em {output_file}")
        print(f"Tempo de decifragem AES: {elapsed:.6f} segundos")
    else:
        print("Modo inválido. Use 'cipher' ou 'decipher'.")

