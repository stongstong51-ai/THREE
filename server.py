from flask import Flask, request, jsonify
import json, time, os

app = Flask(__name__)
DB_FILE = "used.json"

@app.route('/check', methods=['POST'])
def check():
    # ... โค้ดเดิมของคุณ ...
    data = request.get_json()
    key, hwid = data.get("key"), data.get("hwid")
    # เพิ่มการอ่านไฟล์ให้ปลอดภัยขึ้น
    if not os.path.exists(DB_FILE):
        return jsonify({"status": "error", "message": "Database not found"})
    
    with open(DB_FILE, 'r') as f:
        db = json.load(f)
    
    if key not in db: return jsonify({"status": "invalid"})
    
    # เช็กวันหมดอายุ
    if time.time() > db[key]["expire"]:
        return jsonify({"status": "expired"})
        
    # เช็ก/ผูก HWID
    if db[key]["hwid"] == "":
        db[key]["hwid"] = hwid
        with open(DB_FILE, 'w') as f:
            json.dump(db, f, indent=4)
    elif db[key]["hwid"] != hwid:
        return jsonify({"status": "hwid_error"})
        
    return jsonify({"status": "ok"})

# แก้ไขส่วนนี้สำคัญที่สุดเพื่อให้ Render รันได้
if __name__ == '__main__':
    # ดึงค่าพอร์ตจาก Render (ถ้าไม่มีให้ใช้ 10000)
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)