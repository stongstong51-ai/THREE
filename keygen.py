import random, string, json, os, time

def generate_key(days):
    chars = string.ascii_uppercase + string.digits
    key = f"THREE328-{''.join(random.choice(chars) for _ in range(12))}"
    
    # คำนวณวันหมดอายุ (ถ้าเป็น 999 คือ VIP ถาวร)
    expire_timestamp = time.time() + (days * 86400) if days != 999 else 9999999999
    return key, expire_timestamp

if __name__ == "__main__":
    print("เลือกประเภทคีย์: [1] 1วัน, [2] 7วัน, [3] VIP(ถาวร)")
    choice = input("เลือก : ")
    days = 1 if choice == "1" else (7 if choice == "2" else 999)
    
    key, exp = generate_key(days)
    db = json.load(open("used.json")) if os.path.exists("used.json") else {}
    db[key] = {"hwid": "", "expire": exp}
    json.dump(db, open("used.json", "w"), indent=4)
    print(f"\n✅ สร้างคีย์เรียบร้อย: {key} (หมดอายุใน {days} วัน)")ๅ