import urllib.request
import urllib.parse
import time

# Let's test with different headers and referrer
prompts = [
    "a majestic lion with a golden mane",
    "futuristic city with flying cars at night",
    "cyberpunk street market in neo tokyo",
    "an astronaut riding a cosmic horse through galaxies"
]

for p in prompts:
    enc = urllib.parse.quote(p)
    # Test 1: Referer pollinations.ai
    url = f"https://image.pollinations.ai/prompt/{enc}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "Referer": "https://pollinations.ai/",
        "Origin": "https://pollinations.ai",
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8"
    })
    try:
        with urllib.request.urlopen(req, timeout=12) as r:
            print(f"PASS with Referer: '{p}' -> {r.status} ({len(r.read())} bytes)")
    except Exception as e:
        print(f"FAIL with Referer: '{p}' -> {e}")
    time.sleep(1)
