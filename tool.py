import os
import string
import cryptography
from cryptography.fernet import Fernet
# Khóa mã hóa 
key = "hrVo-EeAc-nezBvX0Hfxn02pDAA9_93-XJhsdv7Vd1Q="

# Lấy danh sách tất cả ổ đĩa (trên Windows)
drives = [f"{d}:\\" for d in string.ascii_uppercase if d != 'C' and os.path.exists(f"{d}:\\")]
print(drives)
for drive in drives:
    for root, dirs, files in os.walk(drive, topdown=True):
        # Lọc các thư mục quan trọng
        dirs[:] = [d for d in dirs if d not in ['System Volume Information', '$Recycle.Bin']]
        for file_name in files:
            try:
                file_path = os.path.join(root, file_name)
                if os.path.isfile(file_path):
                    print(f"Giải mã: {file_path}")
                    with open(file_path, "rb") as file:
                        data = file.read()
                    encrypted_data = Fernet(key).decrypt(data)
                    with open(file_path, "wb") as file:
                        file.write(encrypted_data)
            except Exception as e:
                print(f"Lỗi với {file_path}: {e}")