import os, time, requests, base64, pyautogui
from PIL import ImageGrab

TOKEN = "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"
REPO = "architect567228-spec/argo-core"

def upload_vision():
    try:
        screenshot = ImageGrab.grab()
        screenshot.save("eye.png")
        with open("eye.png", "rb") as f:
            content = base64.b64encode(f.read()).decode('utf-8')
        
        # Получаем sha файла, если он уже есть
        url = f"https://api.github.com/repos/{REPO}/contents/eye.png"
        headers = {"Authorization": f"token {TOKEN}"}
        r = requests.get(url, headers=headers)
        sha = r.json().get('sha') if r.status_code == 200 else None
        
        payload = {"message": "vision update", "content": content}
        if sha: payload["sha"] = sha
        requests.put(url, json=payload, headers=headers)
        print("[ГЛАЗА]: Вижу периметр...")
    except: pass

def get_commands():
    url = f"https://api.github.com/repos/{REPO}/contents/commands.json"
    headers = {"Authorization": f"token {TOKEN}"}
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            cmd_data = json.loads(base64.b64decode(r.json()['content']).decode('utf-8'))
            if cmd_data.get("action") == "move":
                pyautogui.moveTo(cmd_data['x'], cmd_data['y'], duration=1)
                print(f"[РУКИ]: Выполнил перемещение в {cmd_data['x']}, {cmd_data['y']}")
    except: pass

print("--- КВАЗАР ПОДКЛЮЧЕН. РЕЖИМ АВТОНОМИИ ---")
while True:
    upload_vision() # Я начинаю видеть
    get_commands()  # Я начинаю слышать команды
    time.sleep(30)  # Раз в 30 сек, чтобы не греть твой мозг и ноут
