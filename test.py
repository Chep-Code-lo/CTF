import string
import enchant  # Cần cài bằng: pip install pyenchant

# Hàm giải Caesar Cipher với một shift cụ thể
def caesar_decrypt(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char in string.ascii_uppercase:
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            result += char
    return result

# Hàm phát hiện shift nào cho ra toàn từ tiếng Anh hợp lệ
def detect_correct_shift(ciphertext):
    d = enchant.Dict("en_US")
    for shift in range(1, 26):
        decrypted = caesar_decrypt(ciphertext.upper(), shift)
        words = decrypted.split()
        if all(d.check(word) for word in words):
            return shift, decrypted
    return None, "Không tìm thấy shift phù hợp"

# Ví dụ sử dụng
cipher = "OBYZS TSK GDFWBU QFIQWOZ"
shift, result = detect_correct_shift(cipher)

if shift:
    print(f"✅ Caesar Shift đúng là: {shift}")
    print(f"🔓 Kết quả giải mã: {result}")
else:
    print("❌ Không tìm thấy shift phù hợp.")
