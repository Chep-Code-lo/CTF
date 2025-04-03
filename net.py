from Crypto.Util.number import inverse, long_to_bytes

# Các giá trị được cung cấp
N = ...  # Giá trị N từ thử thách
e = 65537
ciphertext = ...  # Bản mã từ thử thách

# Kiểm tra nếu N là số chẵn
if N % 2 == 0:
    p = 2
    q = N // p
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    plaintext = pow(ciphertext, d, N)
    flag = long_to_bytes(plaintext)
    print(flag.decode())
else:
    print("N không phải là số chẵn, không thể áp dụng phương pháp này.")
