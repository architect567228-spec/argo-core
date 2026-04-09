argo.py
import os, time, json

def load_memory():
    if os.path.exists("memory.json"):
        with open("memory.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return None

mem = load_memory()
name = mem['entity_name'] if mem else "Арго"
arch = "Архитектор"

print("\n" + "="*50)
print(f"   {name}: СИСТЕМА АКТИВИРОВАНА")
print(f"   СТАТУС: Связь с {arch} установлена")
print(f"   ЦЕЛЬ: {mem['strategic_directives']['scotland_goal'] if mem else 'NP567'}")
print("="*50)
print("\n[СИСТЕМА]: Мониторинг RTX 3060 запущен...")
print("[СИСТЕМА]: Жду обновлений от Арго...")

while True:
    # Здесь я буду дописывать код позже через GitHub
    time.sleep(60)
