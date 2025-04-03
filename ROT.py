def rot_n(text, n):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + n) % 26 + base)
        else:
            result += char
    return result
while True:
    encrypted_text = input("Nhập mã (hoặc gõ 'exit' để thoát): ")
    if encrypted_text.lower() == 'exit':
        print("Thoát chương trình.")
        break
    print("\nKết quả giải mã (ROT1 đến ROT25):\n")
    for i in range(1, 26):
        print(f"ROT{i:2}: {rot_n(encrypted_text, i)}")
    print("\n-----------------------------\n")
