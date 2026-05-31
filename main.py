import os
import time
import requests
import subprocess
import sys

os.system("color 0A")

# 🔗 !! เปลี่ยน IP เป็นของพี่เมื่อขายจริง !!
SERVER_URL = "http://127.0.0.1:5000/check"

def get_hwid():
    try:
        cmd = "wmic csproduct get uuid"
        uuid = subprocess.check_output(cmd, shell=True).decode().split('\n')[1].strip()
        return uuid
    except:
        return os.environ.get("COMPUTERNAME", "UNKNOWN")

# ---------------- LOGIN ----------------
while True:
    os.system("cls")
    print(r"""
████████╗██╗  ██╗██████╗ ███████╗███████╗
╚══██╔══╝██║  ██║██╔══██╗██╔════╝██╔════╝
   ██║   ███████║██████╔╝█████╗  █████╗  
   ██║   ██╔══██║██╔══██╗██╔══╝  ██╔══╝  
   ██║   ██║  ██║██║  ██║███████╗███████╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
           THREE TWO EIGHT (OFFICIAL)
""")
    key = input("License Key : ").strip()
    if not key: continue

    print("กำลังตรวจสอบสิทธิ์ใช้งาน...")
    try:
        response = requests.post(SERVER_URL, json={"key": key, "hwid": get_hwid()}, timeout=7)
        status = response.json().get("status")

        if status == "invalid":
            print("❌ ไม่พบ License นี้ในระบบ")
            time.sleep(2)
        elif status == "hwid_error":
            print("🔒 คีย์นี้ถูกล็อกใช้งานกับเครื่องอื่นไปแล้ว!")
            time.sleep(2)
        elif status == "expired":
            print("⏳ License ของคุณหมดอายุแล้ว")
            time.sleep(2)
        elif status == "ok":
            print("🟢 ล็อกอินสำเร็จ!")
            time.sleep(1)
            break
        else:
            print("⚠️ สถานะไม่รู้จัก")
            time.sleep(2)
    except Exception as e:
        print(f"💥 ไม่สามารถเชื่อมต่อกับเซิร์ฟเวอร์ได้: {e}")
        time.sleep(2)

# ---------------- MENU ----------------
while True:
    os.system("cls")
    print("\n================================")
    print("       THREE TWO EIGHT MENU     ")
    print("================================\n")
    print("[1] เปิดโปรแกรม ยิงตัวโดนหัว")
    print("[2] ออกจากโปรแกรม")
    
    choice = input("\nเลือกเมนู : ")
    if choice == "1":
        print("กำลังเรียกเปิดโปรแกรม...")
        
        # 💡 ดึงไฟล์ stang.exe ที่ซ่อนไว้ในตัว exe หลัก
        if getattr(sys, 'frozen', False):
            current_dir = sys._MEIPASS
        else:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            
        path = os.path.join(current_dir, "stang.exe")
        
        if os.path.exists(path):
            subprocess.Popen([path], shell=True)
            print("🟢 เปิดโปรแกรมหลักสำเร็จ!")
            time.sleep(2)
        else:
            print("❌ เกิดข้อผิดพลาดภายในระบบ (ไม่พบไฟล์สคริปต์)")
            input("กด Enter เพื่อกลับเมนู...")
            
    elif choice == "2":
        break