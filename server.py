from flask import Flask, request, jsonify
import json, time, os

app = Flask(__name__)
DB_FILE = "used.json"

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    key, hwid = data.get("key"), data.get("hwid")
    db = json.load(open(DB_FILE)) if os.path.exists(DB_FILE) else {}
    
    if key not in db: return jsonify({"status": "invalid"})
    
    # เช็กวันหมดอายุ
    if time.time() > db[key]["expire"]:
        return jsonify({"status": "expired"})
        
    # เช็ก/ผูก HWID
    if db[key]["hwid"] == "":
        db[key]["hwid"] = hwid
        json.dump(db, open(DB_FILE, "w"), indent=4)
    elif db[key]["hwid"] != hwid:
        return jsonify({"status": "hwid_error"})
        
    return jsonify({"status": "ok"})

if __name__ == '__main__': app.run(port=5000)