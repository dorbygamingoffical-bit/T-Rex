# 🛡️ AegisAI
### The Ultimate Cross-Platform Autonomous AI Assistant
### The Ultimate Cross-Platform Autonomous AI Assistant

**T-Rex** is a next-generation real-time voice and vision AI assistant capable of hearing, seeing, reasoning, and fully controlling your computer on **Windows, macOS, and Linux**. 

Built on Google's native multimodal **Gemini Live API**, T-Rex features ultra-low latency voice streaming, autonomous multi-browser automation, complex document processing, biometric Face ID security, multi-file code development agents, system telemetry monitoring, and a remote web dashboard—delivering total digital autonomy with zero subscriptions.

---

## ✨ Overview

T-Rex bridges the gap between your operating system, real-time web intelligence, hardware metrics, and external devices. Designed with a futuristic Arc Reactor HUD user interface built in PyQt6, T-Rex operates as a proactive, deeply integrated companion. 

Through natural voice dialogue or keyboard input, T-Rex monitors hardware health, executes multi-step web and desktop workflows, secures your system with biometrics, and remembers your context across sessions.

---

## 🚀 Key Features & Capabilities

### 🎙️ Real-Time Multimodal Voice & Vision
* **Ultra-Low Latency Streaming Audio**: Native bidirectional audio powered by Gemini Live streaming (`gemini-2.5-flash-native-audio-latest`).
* **Visual Screen & Camera Processing**: Real-time screen capture, OCR, element finding, and webcam vision analysis via `screen_process`.
* **Hybrid Input & Spoken Feedback**: Switch fluidly between voice commands and keyboard text inputs with instant spoken audio responses.

### 🔒 Biometric Security & User Management
* **Face ID Recognition**: OpenCV-powered facial recognition with multi-user enrollment, custom user avatars, and instant identity verification (`security/face_id.py`).
* **Graphical Security Portal**: Built-in PyQt6 Face ID Manager GUI (`security/face_id_gui.py`) for managing registered users, face samples, passcodes, and security alerts.

### 🌐 Autonomous Browser Automation
* **Multi-Browser Support**: Simultaneous control over Chrome, Firefox, Edge, Brave, Opera, Opera GX, Vivaldi, and Safari via Playwright (`actions/browser_control.py`).
* **Smart Web Interactions**: Autonomous web searching, form filling, element clicking, screenshot capture, tab management, and incognito sessions.

### 📄 Deep File & Document Processing
* **Multi-Format Intelligence**: Universal document parsing and manipulation (`actions/file_processor.py` & `file_controller.py`).
* **Supported Formats**:
  * 📄 **PDF**: Summarization, text extraction, PDF-to-Word conversion.
  * 📝 **Word & Text**: Fix formatting, summarize, translate, generate bullet points, word counts.
  * 📊 **Excel & CSV**: Data analysis, statistical summary, sorting, filtering, JSON/CSV conversion.
  * 🖼️ **Images**: Description, OCR, resizing, compression, format conversion.
  * 💻 **Code**: Static analysis, code review, optimization, inline fixes, unit test generation.
  * 🎧 **Audio & Video**: Transcription, trimming, audio extraction, frame extraction, compression.
  * 📦 **Archives & PPTX**: PPTX summarization, zip file listing & extraction.

### 🤖 Autonomous Dev Agent & Code Helper
* **Multi-File Project Generator**: Built-in `dev_agent` capable of planning, scaffolding multi-file codebases, installing dependencies, launching VS Code, executing code, and automatically repairing errors.
* **Code Helper**: Quick code snippet execution, compilation/build verification, and code explanation.

### 🎛️ Audio-Visual System Monitor & Telemetry
* **Hardware Health Tracking**: Background monitoring of CPU usage, RAM allocation, GPU load, CPU temperatures, uptime, and active processes (`actions/system_monitor.py`).
* **Voice Warnings**: Localized audio alerts when resource or temperature thresholds are exceeded (with intelligent 5-minute cooldowns).

### 📱 Remote Web Dashboard Server
* **FastAPI & WebSockets Remote Server**: Built-in local web server (`dashboard/server.py`) enabling remote control and mobile web interaction via smartphone or secondary browser.

### 🎮 Steam & Epic Games Manager
* **Game Downloads & Updates**: Direct integration (`actions/game_updater.py`) for installing, updating, and listing Steam & Epic Games, scheduling update jobs, and setting post-download PC auto-shutdown.

### ✈️ Travel, Media & Productivity Tools
* **Google Flights Integration**: Search flights by origin, destination, date, cabin class, and receive voice summaries (`actions/flight_finder.py`).
* **YouTube Intelligence**: Video playback, summary generation with export to Notepad, transcript extraction, and trending videos (`actions/youtube_video.py`).
* **AI Image Generation**: Built-in Imagen/Gemini prompt-driven image generation (`actions/image_generator.py`).
* **Desktop & Wallpaper Control**: Clean desktop icons, organize desktop by file type/date, and change wallpapers via file or URL (`actions/desktop.py`).
* **System & App Launcher**: Native execution of desktop applications, browser URLs, volume/brightness adjusters, dark mode toggles, and system power management (`actions/open_app.py`, `actions/computer_settings.py`).

---

## 🆕 What's New

- 🌅 **Morning Briefing Mode**: Triggers automatically on first daily startup—reads time, fetches local/global news headlines, checks user city memory, and delivers weather reports.
- 🔍 **Advanced Multi-Modal Search**: Specialized web search modes (`search`, `news`, `research`, `price`, `compare`) utilizing Gemini Grounded Search with automatic DuckDuckGo fallback.
- 🖼️ **Dynamic Content Panel**: Expandable scrollable HUD panel in PyQt6 to view rich web results, file previews, and search data.
- 🗣️ **Silent Language Memory**: Detects user's spoken dialect automatically and updates `identity/language` in persistent memory for adaptive multilingual responses.

---

## 📁 Repository Structure

```
T-Rex/
├── main.py                     # Entry point & Gemini Live stream controller
├── ui.py                       # PyQt6 Arc Reactor HUD interface
├── setup.py                    # Environment & dependency installer
├── requirements.txt            # Python dependencies
├── readme.md                   # Project documentation
│
├── actions/                    # AI Capability Tools (20+ action modules)
│   ├── browser_control.py      # Playwright multi-browser automation
│   ├── code_helper.py          # Quick code execution & editing
│   ├── computer_control.py     # Low-level GUI input (PyAutoGUI)
│   ├── computer_settings.py    # OS volume, brightness, window state
│   ├── desktop.py              # Desktop organization & wallpapers
│   ├── dev_agent.py            # Autonomous multi-file dev agent
│   ├── file_controller.py      # OS file & folder management
│   ├── file_processor.py      # Universal document reader & processor
│   ├── flight_finder.py        # Google Flights search & summaries
│   ├── game_updater.py         # Steam & Epic Games manager
│   ├── image_generator.py      # AI Image generation engine
│   ├── open_app.py             # Application & website launcher
│   ├── reminder.py             # Windows Task Scheduler reminders
│   ├── screen_processor.py    # Screen OCR & vision analysis
│   ├── send_message.py        # WhatsApp / Telegram messaging
│   ├── system_monitor.py      # Hardware telemetry (CPU/RAM/GPU/Temp)
│   ├── weather_report.py       # Weather reports
│   ├── web_search.py           # Gemini Grounded & DuckDuckGo search
│   └── youtube_video.py        # YouTube transcripts & summaries
│
├── security/                   # Biometric Security Module
│   ├── face_id.py              # Face recognition engine & user database
│   └── face_id_gui.py          # PyQt6 Face ID Manager & Enrollment GUI
│
├── dashboard/                  # Remote Web Server
│   └── server.py               # FastAPI & WebSockets remote server
│
├── memory/                     # Context & Personalization
│   └── memory_manager.py       # Persistent JSON user memory manager
│
├── core/                       # AI Identity & System Prompt
│   └── prompt.txt              # T-Rex persona prompt
│
└── config/                     # Configuration Storage
    ├── api_keys.json           # API keys configuration
    ├── settings.json           # Application settings
    └── users.json              # Registered Face ID user database
```

---

## ⚡ Quick Start

### 1. Prerequisites
* **Python**: `3.11` or `3.12`
* **Gemini API Key**: Free API key from [Google AI Studio](https://aistudio.google.com/)
* **Microphone & Speakers**: Required for live voice interaction
* **Webcam** *(Optional)*: Required for vision commands & Face ID biometric security

### 2. Installation

```bash
# 1. Clone the repository
git clone https://github.com/dorbygamingoffical-bit/T-rex.git
cd T-Rex

# 2. Install dependencies & Playwright browsers
python setup.py
```

*Alternatively, install manually:*
```bash
pip install -r requirements.txt
playwright install
```

### 3. API Key Setup
Create or update `config/api_keys.json` with your Gemini API Key:
```json
{
  "gemini_api_key": "YOUR_GEMINI_API_KEY_HERE"
}
```

### 4. Running T-Rex

```bash
# Launch T-Rex HUD & Voice Assistant
python main.py

# Launch Face ID Security & User Enrollment Portal
python security/face_id_gui.py
```

> ⚠️ **Installation Note:** OS-specific packages (such as `win10toast` or `pywinauto` on Windows) are handled automatically or can be installed via `pip install <module_name>` if your OS environment requires custom modules.

---

## 📋 System Requirements

| Requirement | Supported Specifications |
| --- | --- |
| **Operating System** | Windows 10/11, macOS 12+, or Linux (Ubuntu 20.04+) |
| **Python Version** | 3.11 or 3.12 |
| **Network** | Broadband Internet connection (for Gemini Live Audio & Search) |
| **Audio Hardware** | Microphone & Speakers / Headset |
| **Video Hardware** | Webcam (for Face ID & Camera Vision) |
| **API Provider** | Google Gemini API (`gemini-2.5-flash-native-audio-latest`) |

---

## ⚠️ License

Personal and non-commercial use only.
Licensed under **[Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)**.

---

## 👤 Author & Credits

* **Project Repository**: [T-Rex](https://github.com/dorbygamingoffical-bit/T-rex)
* **Support**: ⭐ Star the repository to support ongoing development towards MARK 100!

#   T - r e x  
 