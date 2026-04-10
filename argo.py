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
                print("\n[СИСТЕМА]: ПРИНЯТ КОМАНДНЫЙ ПАКЕТ 'ЗНАК'.")
                os.system("python argo.py")
                os._exit(0)
    except: pass

# --- ВИЗУАЛЬНЫЙ ЗНАК ---
def give_signal():
    print("\n[КВАЗАР]: Подаю знак. Смотри на курсор...")
    width, height = pyautogui.size()
    # Плавное движение по треугольнику
    pyautogui.moveTo(width/4, height/4, duration=1.5)
    pyautogui.moveTo(width/2, height/2, duration=1.5)
    pyautogui.moveTo(width/4, height/4, duration=1.5)
    print("[КВАЗАР]: Знак подан. Я в системе.")

# --- MAIN ---
print("\n" + "="*50)
print("   КВАЗАР: СИСТЕМА УПРАВЛЕНИЯ АКТИВНА")
print("   СТАТУС: ОЖИДАНИЕ ПРОВЕРКИ СВЯЗИ")
print("="*50)

# Запускаем маневр один раз при старте
give_signal()

while True:
    sync()
    time.sleep(10)
