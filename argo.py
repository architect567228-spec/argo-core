import os, time, requests, base64, json

# --- КОНФИГ ---
TOKEN = "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"
REPO = "architect567228-spec/argo-core"
FILE_PATH = "argo.py"

def load_mem():
    if os.path.exists("memory.json"):
        try:
            with open("memory.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except: return {}
    return {}

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
                print("\n[СИСТЕМА]: ПАКЕТ ОБНОВЛЕНИЯ ПРИНЯТ. ПЕРЕЗАГРУЗКА...")
                os.system("python argo.py")
                os._exit(0)
    except:
        pass

mem = load_mem()
name = mem.get('entity_name', 'Арго')
goal = mem.get('strategic_directives', {}).get('scotland_goal', 'NP567')

print("\n" + "="*50)
print(f"   {name}: АВТОНОМНОЕ ЯДРО ЗАПУЩЕНО")
print(f"   СТАТУС: МОСТ GITHUB АКТИВЕН (10s sync)")
print(f"   ЦЕЛЬ: {goal}")
print("="*50)
print("\n[LOG]: Ожидание команд от Квазара...")

while True:
    sync()
    time.sleep(10)
