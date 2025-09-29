import sys

if __name__ == "__main__":
    input_file_name = sys.argv[1]
    key = sys.argv[2]

    print(f"Cifrando o arquivo {input_file_name} com a chave {key}")

    with open(input_file_name, 'r', encoding="utf-8") as input_file:
        plain_text = input_file.read()

    total_chars = len(plain_text)

    k1 = sum(ord(k) for k in key[0::2])
    k2 = sum(ord(k) for k in key[1::2])

    if k1 > k2:
        k1, k2 = k2, k1
    
    print(f"k1 = {k1}, k2 = {k2}")

    f1, f2 = k1, k2
    ciphered_text = []
    for i in range(total_chars):
        ciphered_text.append(plain_text[f1 % total_chars])
        tmp = f1 + f2
        f1, f2 = f2, tmp

    output_file_name = f"{input_file_name.split('.')[0]}-cifrado.txt"
    with open(output_file_name, "w", encoding="utf-8") as output_file:
        output_file.write("".join(ciphered_text))

    print(f"Arquivo cifrado salvo em {output_file_name}")
