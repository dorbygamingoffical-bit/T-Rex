import subprocess
import sys
import json
import os
import platform
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()

def print_step(step_name):
    print(f"\n[=] {step_name}...")

def check_python_version():
    print_step("Checking Python version")
    if sys.version_info < (3, 8):
        print(f"[!] Warning: Python 3.8+ recommended. Current version: {sys.version.split()[0]}")
    else:
        print(f"[+] Python version: {sys.version.split()[0]} ({platform.system()} {platform.machine()})")

def init_directories():
    print_step("Initializing required directories")
    dirs = [
        BASE_DIR / "config",
        BASE_DIR / "config" / "faces",
        BASE_DIR / "output_images",
        BASE_DIR / "projects",
        BASE_DIR / "memory",
        BASE_DIR / "dashboard",
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        print(f"  - Verified: {d.relative_to(BASE_DIR)}")

def install_requirements():
    print_step("Installing dependencies from requirements.txt")
    req_file = BASE_DIR / "requirements.txt"
    if not req_file.exists():
        print("[!] Error: requirements.txt not found!")
        return False
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=False)
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", str(req_file)], check=True)
        print("[+] Dependencies successfully installed.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[!] Error installing dependencies: {e}")
        return False

def install_playwright():
    print_step("Installing Playwright browser binaries")
    try:
        subprocess.run([sys.executable, "-m", "playwright", "install"], check=True)
        print("[+] Playwright browsers installed successfully.")
    except Exception as e:
        print(f"[!] Note: Playwright browser installation encountered an issue: {e}")
        print("    You can retry manually with: python -m playwright install")

def init_configs():
    print_step("Initializing configuration files")
    config_dir = BASE_DIR / "config"
    config_dir.mkdir(parents=True, exist_ok=True)

    # 1. api_keys.json
    api_file = config_dir / "api_keys.json"
    if not api_file.exists():
        env_key = os.environ.get("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")
        data = {
            "gemini_api_key": env_key,
            "os_system": platform.system().lower()
        }
        api_file.write_text(json.dumps(data, indent=4), encoding="utf-8")
        print(f"[+] Created default '{api_file.relative_to(BASE_DIR)}'")
    else:
        print(f"[+] Found existing '{api_file.relative_to(BASE_DIR)}'")

    # 2. settings.json
    settings_file = config_dir / "settings.json"
    if not settings_file.exists():
        default_settings = {
            "auto_start": False,
            "morning_brief": True,
            "assistant_name": "T-Rex",
            "user_name": "User"
        }
        settings_file.write_text(json.dumps(default_settings, indent=4), encoding="utf-8")
        print(f"[+] Created default '{settings_file.relative_to(BASE_DIR)}'")
    else:
        print(f"[+] Found existing '{settings_file.relative_to(BASE_DIR)}'")

    # 3. memory.json
    memory_file = config_dir / "memory.json"
    if not memory_file.exists():
        default_memory = {
            "notes": [],
            "reminders": [],
            "conversations": []
        }
        memory_file.write_text(json.dumps(default_memory, indent=4), encoding="utf-8")
        print(f"[+] Created default '{memory_file.relative_to(BASE_DIR)}'")
    else:
        print(f"[+] Found existing '{memory_file.relative_to(BASE_DIR)}'")

def main():
    print("=" * 50)
    print("           T-Rex Setup Script")
    print("=" * 50)
    
    check_python_version()
    init_directories()
    install_requirements()
    install_playwright()
    init_configs()

    print("\n" + "=" * 50)
    print("[+] Setup completed successfully!")
    print("    - To launch command line interface: python main.py")
    print("    - To launch GUI interface: python ui.py")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()



