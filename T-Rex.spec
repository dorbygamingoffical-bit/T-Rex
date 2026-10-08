# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files

datas = [
    ('core', 'core'),
    ('config', 'config'),
] + collect_data_files('cv2')

hiddenimports = [
    'encodings',
    'encodings.utf_8',
    'encodings.ascii',
    'encodings.cp1252',
    'encodings.latin_1',
    'encodings.aliases',
    'asyncio',
    'google.genai',
    'google.generativeai',
    'uvicorn',
    'uvicorn.logging',
    'uvicorn.loops',
    'uvicorn.loops.auto',
    'uvicorn.protocols',
    'uvicorn.protocols.http',
    'uvicorn.protocols.http.auto',
    'uvicorn.protocols.websockets',
    'uvicorn.protocols.websockets.auto',
    'fastapi',
    'starlette',
    'comtypes',
    'pycaw',
    'win10toast',
    'pywinauto',
    'sounddevice',
    'soundfile',
    'miniaudio',
    'pdfplumber',
    'docx',
    'pptx',
    'cv2',
    'PIL',
]

excludes = [
    'torch',
    'torchvision',
    'torchaudio',
    'scipy',
    'matplotlib',
    'pytest',
    'tensorboard',
    'sympy',
    'IPython',
    'notebook',
    'tkinter',
]

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=excludes,
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='T-Rex',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
