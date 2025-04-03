def rot_n(text, n):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + n) % 26 + base)
        else:
            result += char
    return result

encrypted_text = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}"
for i in range(1, 26):  # thử tất cả các ROT từ 1 đến 25
    print(f"ROT{i}: {rot_n(encrypted_text, i)}")
