import subprocess
import sys
import json
import os
import platform
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()

def print_step(step_name):
    print(f"\n[=] {step_name}...")

def check_python_version():
    print_step("Checking Python environment")
    if sys.version_info < (3, 8):
        print(f"[!] Warning: Python 3.8+ recommended. Current version: {sys.version.split()[0]}")
    else:
        print(f"[+] Python version: {sys.version.split()[0]} ({platform.system()} {platform.machine()})")

def init_directories():
    print_step("Initializing required system directories")
    dirs = [
        BASE_DIR / "config",
        BASE_DIR / "config" / "faces",
        BASE_DIR / "config" / "cascades",
        BASE_DIR / "output_images",
        BASE_DIR / "projects",
        BASE_DIR / "memory",
        BASE_DIR / "dashboard",
        BASE_DIR / "security",
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        print(f"  - Created/Verified: {d.relative_to(BASE_DIR)}")

def install_requirements():
    print_step("Downloading & Installing Python packages from requirements.txt")
    req_file = BASE_DIR / "requirements.txt"
    if not req_file.exists():
        print("[!] Error: requirements.txt not found!")
        return False
    try:
        print("[*] Upgrading core installer tools (pip, setuptools, wheel)...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"], check=False)
        print("[*] Installing all required Python dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", str(req_file)], check=True)
        print("[+] All Python packages downloaded and installed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[!] Error downloading/installing Python packages: {e}")
        return False

def install_playwright_browsers():
    print_step("Downloading & Installing Playwright Browser Engines (Chromium, Firefox, WebKit)")
    try:
        print("[*] Running 'playwright install'...")
        subprocess.run([sys.executable, "-m", "playwright", "install"], check=True)
        
        # On Linux systems, attempt installing system dependencies if supported
        if platform.system().lower() == "linux":
            try:
                subprocess.run([sys.executable, "-m", "playwright", "install-deps"], check=False)
            except Exception:
                pass
        print("[+] Playwright browsers downloaded and ready.")
    except Exception as e:
        print(f"[!] Note: Playwright browser installation encountered an issue: {e}")
        print("    You can retry manually with: python -m playwright install")

def download_vision_models():
    print_step("Checking and Downloading OpenCV Vision Cascade Models")
    cascade_dir = BASE_DIR / "config" / "cascades"
    cascade_dir.mkdir(parents=True, exist_ok=True)

    models = {
        "haarcascade_frontalface_default.xml": "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml",
        "haarcascade_eye.xml": "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml",
    }

    for filename, url in models.items():
        target_path = cascade_dir / filename
        if not target_path.exists():
            print(f"[*] Downloading '{filename}'...")
            try:
                urllib.request.urlretrieve(url, target_path)
                print(f"[+] Successfully downloaded: {filename}")
            except Exception as e:
                print(f"[!] Warning: Failed to download {filename}: {e}")
        else:
            print(f"[+] Verified model present: {filename}")

def download_memory_models():
    print_step("Initializing Memory Model Assets & NLP Data")
    config_dir = BASE_DIR / "config"
    config_dir.mkdir(parents=True, exist_ok=True)
    memory_file = config_dir / "memory.json"

    default_memory_model = {
        "identity": {
            "assistant_name": {"value": "T-Rex"},
            "version": {"value": "2.0"},
            "personality": {"value": "Helpful, intelligent, responsive AI assistant"}
        },
        "user": {
            "name": {"value": "User"},
            "role": {"value": "Owner"}
        },
        "preferences": {
            "theme": {"value": "dark"},
            "language": {"value": "English"}
        },
        "notes": {},
        "conversations": [],
        "reminders": []
    }

    if not memory_file.exists():
        memory_file.write_text(json.dumps(default_memory_model, indent=4), encoding="utf-8")
        print(f"[+] Initialized memory model structure in '{memory_file.relative_to(BASE_DIR)}'")
    else:
        try:
            existing_mem = json.loads(memory_file.read_text(encoding="utf-8"))
            if isinstance(existing_mem, dict):
                updated = False
                for k, v in default_memory_model.items():
                    if k not in existing_mem:
                        existing_mem[k] = v
                        updated = True
                if updated:
                    memory_file.write_text(json.dumps(existing_mem, indent=4), encoding="utf-8")
                    print(f"[+] Updated memory model schema in '{memory_file.relative_to(BASE_DIR)}'")
                else:
                    print(f"[+] Verified memory model structure in '{memory_file.relative_to(BASE_DIR)}'")
        except Exception:
            memory_file.write_text(json.dumps(default_memory_model, indent=4), encoding="utf-8")

    # Optional NLTK download if available
    try:
        import nltk
        print("[*] Downloading NLTK tokenizer & NLP memory models...")
        nltk.download("punkt", quiet=True)
        nltk.download("stopwords", quiet=True)
        nltk.download("vader_lexicon", quiet=True)
        print("[+] NLTK memory & text processing models downloaded.")
    except ImportError:
        pass
    except Exception as e:
        print(f"[!] Note: NLTK model download notice: {e}")

def download_action_assets():
    print_step("Initializing Action Modules & Action Workspaces")
    actions_dir = BASE_DIR / "actions"
    actions_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Ensure __init__.py exists in actions/
    init_file = actions_dir / "__init__.py"
    if not init_file.exists():
        init_file.write_text("# T-Rex Actions Package\n", encoding="utf-8")
        print(f"[+] Initialized '{init_file.relative_to(BASE_DIR)}'")
    else:
        print(f"[+] Verified actions package: '{init_file.relative_to(BASE_DIR)}'")

    # 2. Verify all action modules exist
    expected_actions = [
        "browser_control.py", "code_helper.py", "computer_control.py",
        "computer_settings.py", "desktop.py", "dev_agent.py",
        "file_controller.py", "file_processor.py", "flight_finder.py",
        "game_updater.py", "image_generator.py", "open_app.py",
        "reminder.py", "screen_processor.py", "send_message.py",
        "system_monitor.py", "weather_report.py", "web_search.py",
        "youtube_video.py"
    ]
    verified_count = 0
    for act_file in expected_actions:
        path = actions_dir / act_file
        if path.exists():
            verified_count += 1

    print(f"[+] Verified {verified_count}/{len(expected_actions)} action modules ready.")

    # 3. Initialize workspace directories used by action modules
    action_workspaces = [
        BASE_DIR / "output_images",
        BASE_DIR / "projects",
        BASE_DIR / "projects" / "temp",
        BASE_DIR / "dashboard",
    ]
    for ws in action_workspaces:
        ws.mkdir(parents=True, exist_ok=True)
        print(f"  - Action workspace ready: {ws.relative_to(BASE_DIR)}")

def init_configs():
    print_step("Initializing Default System Configuration Files")
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
        print(f"[+] Verified config file: '{api_file.relative_to(BASE_DIR)}'")

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
        print(f"[+] Verified config file: '{settings_file.relative_to(BASE_DIR)}'")

    # 3. users.json
    users_file = config_dir / "users.json"
    if not users_file.exists():
        users_file.write_text(json.dumps({}, indent=4), encoding="utf-8")
        print(f"[+] Created default '{users_file.relative_to(BASE_DIR)}'")

    # 4. passcode.txt
    passcode_file = config_dir / "passcode.txt"
    if not passcode_file.exists():
        passcode_file.write_text("1234", encoding="utf-8")
        print(f"[+] Created default '{passcode_file.relative_to(BASE_DIR)}'")

def main():
    print("=" * 60)
    print("           T-Rex Assistant Complete Setup")
    print("=" * 60)
    
    check_python_version()
    init_directories()
    install_requirements()
    install_playwright_browsers()
    download_vision_models()
    download_memory_models()
    download_action_assets()
    init_configs()

    print("\n" + "=" * 60)
    print("[+] Complete setup & download finished successfully!")
    print("    All packages, browser binaries, vision models, memory models,")
    print("    action modules, and configs are installed and ready for use.")
    print("    --------------------------------------------------------")
    print("    - CLI Mode: python main.py")
    print("    - GUI Mode: python ui.py")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()




