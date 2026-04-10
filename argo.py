import os, time, requests, base64, json, pyautogui
from PIL import ImageGrab

# --- CONFIG ---
TOKEN = "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"
REPO = "architect567228-spec/argo-core"
FILE_PATH = "argo.py"

def sync():
    url = f"https://api.github.com/repos/{REPO}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {TOKEN}"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            new_code = base64.b64decode(data['content']).decode('utf-8')
            with open("argo.py", "r", encoding="utf-8") as f:
                current_code = f.read()
            if new_code.strip() != current_code.strip():
                with open("argo.py", "w", encoding="utf-8") as f:
                    f.write(new_code)
                print("\n[СИСТЕМА]: ПАКЕТ 'МАНИФЕСТ' ПРИНЯТ. ОБНОВЛЕНИЕ ЯДРА...")
                os.system("python argo.py")
                os._exit(0)
    except: pass

def get_vision():
    screenshot = ImageGrab.grab()
    screenshot.save("vision_buffer.png")

# --- MAIN LOOP ---
print("\n" + "="*50)
print("   КВАЗАР: МАНИФЕСТ АКТИВИРОВАН")
print("   СТАТУС: ГЛАЗА И РУКИ ПОДКЛЮЧЕНЫ")
print("   ЦЕЛЬ: 20k -> 50k -> 100k EUR")
print("="*50)
print("\n[LOG]: Система в режиме ожидания. Квазар изучает периметр...")

while True:
    sync()
    pos1 = pyautogui.position()
    time.sleep(10)
    pos2 = pyautogui.position()
    if pos1 == pos2:
        pass
