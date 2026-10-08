import subprocess
import sys
import json
import os
import platform
from pathlib import Path

print("Installing requirements...")
subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)

print("Installing Playwright browsers...")
subprocess.run([sys.executable, "-m", "playwright", "install"], check=True)

# Auto-generate config/api_keys.json if missing
config_dir = Path(__file__).parent / "config"
api_file = config_dir / "api_keys.json"
config_dir.mkdir(parents=True, exist_ok=True)

if not api_file.exists():
    DEFAULT_KEY = "YOUR_GEMINI_API_KEY_HERE"
    env_key = os.environ.get("GEMINI_API_KEY", DEFAULT_KEY)
    data = {
        "gemini_api_key": env_key,
        "os_system": platform.system().lower()
    }
    api_file.write_text(json.dumps(data, indent=4), encoding="utf-8")
    print(f"[+] Auto-generated '{api_file.relative_to(Path(__file__).parent)}' (OS={platform.system().lower()}).")

print("\n[+] Setup complete! Run 'python main.py' to start T-Rex.")


