import sys

def fibonacciDetranspose(transposed_text, total_chars, k1, k2):
    f1, f2 = k1, k2
    detransposed_text = []
    for i in range(total_chars):
        detransposed_text.append(plain_text[f1 % total_chars])
        f1, f2 = f2, f1 + f2

    return "".join(transposed_text)


if __name__ == "__main__":

    input_file_name = sys.argv[1]
    key = sys.argv[2]
    print(f"Deifrando o arquivo {input_file_name} com a chave {key}")

    with open(input_file_name, 'r', encoding="utf-8") as input_file:
        ciphered_text = input_file.read()

    total_chars = len(ciphered_text)

    k1 = sum(ord(k) for k in key[0::2])
    k2 = sum(ord(k) for k in key[1::2])

    if k1 > k2:
        k1, k2 = k2, k1
    
    print(f"k1 = {k1}, k2 = {k2}")


