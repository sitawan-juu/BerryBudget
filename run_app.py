from cryptography.fernet import Fernet
import os

def start_program():
    # 1. ไขรหัสกุญแจ
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
    fernet = Fernet(key)

    # 2. อ่านโค้ดที่ล็อคอยู่
    with open("main1.py", "rb") as file:
        encrypted_data = file.read()

    # 3. ถอดรหัสและรันในหน่วยความจำ (ไม่สร้างไฟล์ใหม่)
    decrypted_code = fernet.decrypt(encrypted_data).decode('utf-8')
    exec(decrypted_code, globals())

if __name__ == "__main__":
    start_program()