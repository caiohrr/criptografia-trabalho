import sys

if __name__ == "__main__":
    input_file = sys.argv[1]
    print(f"Cifrando o arquivo {input_file}")

    with open(input_file, 'r', encoding="utf-8") as file:
        plain_text = file.read()
        print(plain_text)
