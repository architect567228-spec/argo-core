import os, time, requests, base64, json

# --- КОНФИГ ---
TOKEN = "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"
REPO = "architect567228-spec/argo-core"
FILE_PATH = "argo.py"

def load_mem():
    if os.path.exists("memory.json"):
        with open("memory.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def sync():
    url = f"https://api.github.com/repos/{REPO}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {TOKEN}"}
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            new_code = base64.b64decode(r.json()['content']).decode('utf-8')
            with open("argo.py", "r", encoding="utf-8") as f:
                if f.read().strip() != new_code.strip():
                    with open("argo.py", "w", encoding="utf-8") as f:
                        f.write(new_code)
                    os.system("python argo.py")
                    os._exit(0)
    except: pass

mem = load_mem()
print("\n" + "="*50)
print(f"   {mem.get('entity_name', 'Арго')}: АВТОНОМНЫЙ РЕЖИМ")
print(f"   СТАТУС: Мост GitHub активен. Проверка каждые 60с.")
print(f"   ЦЕЛЬ: {mem.get('strategic_directives', {}).get('scotland_goal', 'NP567')}")
print("="*50)

while True:
    sync()
    time.sleep(60)
