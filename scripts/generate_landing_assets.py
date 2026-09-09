#!/usr/bin/env python3
"""랜딩 페이지 섹션별 에셋 생성: Gemini API + 크로마키 배경 제거 파이프라인.
Hero, Features 아이콘, Highlights 일러스트, Download, Footer 캐릭터 생성."""
import base64
import time
import sys
from pathlib import Path
from collections import deque
from PIL import Image
import numpy as np
from google import genai

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SPRITES_DIR = PROJECT_ROOT / "poc" / "public" / "sprites"
LANDING_PUBLIC = PROJECT_ROOT / "landing" / "public"
OUTPUT_DIR = LANDING_PUBLIC / "images"

ENV_PATH = PROJECT_ROOT / ".env"


def load_api_key():
    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("GEMINI_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError("GEMINI_API_KEY not found in .env")


API_KEY = load_api_key()
client = genai.Client(api_key=API_KEY)

# ============================================================
# 레퍼런스 이미지 로드
# ============================================================
REF_IDLE = SPRITES_DIR / "characters" / "char_idle.png"
REF_HAPPY = SPRITES_DIR / "characters" / "char_happy.png"
REF_ROOM = SPRITES_DIR / "rooms" / "room_lv4.png"

STYLE_RULES = """
CRITICAL STYLE RULES:
- Background MUST be solid flat magenta #FF00FF with NO gradients, NO shadows, NO floor shadows
- NO drop shadow, NO ambient shadow, NO floor reflection
- NO pure white (#FFFFFF) on the object — use cream/off-white (#fefefe) if white is needed
- Style: NemoMate style — wool felt/plush texture, cute simple 2D illustration
- The character is a light blue square-shaped wool plush with stitch lines along edges, pink cheeks, round brown eyes, simple mouth
- Dark brown (#5C4033) outline, NOT black (#000)
- Warm color palette: beige, cream, light blue, soft pink, brown tones
- Generate at 800x800 pixels, object should fill 80% of canvas
"""

# ============================================================
# 섹션별 에셋 정의
# ============================================================
ASSETS = {
    # --- Hero ---
    "hero": [
        {
            "id": "hero_nemo",
            "name": "Hero 네모 캐릭터 (손인사)",
            "refs": ["idle", "happy"],
            "prompt": f"""Draw this exact character (see reference images) waving hello with its right hand raised.
Expression: happy, mouth open smiling like the happy reference.
A small speech bubble on the bottom-left says "안녕~!"

The character must look IDENTICAL to the reference — light blue square wool plush, stitch dotted lines on edges, pink cheeks, round brown eyes.
{STYLE_RULES}""",
        },
    ],

    # --- Features 아이콘 ---
    "features": [
        {
            "id": "icon_desktop",
            "name": "데스크톱 친구 아이콘",
            "refs": ["idle"],
            "prompt": f"""A cute monitor screen with the reference character (light blue square wool plush) sitting on top of it.
The monitor is a simple rounded rectangle with a cream-colored screen.
The character is small, sitting casually on the monitor top edge.
{STYLE_RULES}""",
        },
        {
            "id": "icon_room",
            "name": "방 꾸미기 아이콘",
            "refs": ["idle"],
            "prompt": f"""A cute small house (pentagon roof shape) interior view with tiny wool-textured furniture inside — a small bed and a lamp.
Warm beige walls, wooden floor. Everything in wool felt plush texture matching the reference character style.
{STYLE_RULES}""",
        },
        {
            "id": "icon_game",
            "name": "미니게임 아이콘",
            "refs": ["idle"],
            "prompt": f"""A cute game controller / joystick in wool felt plush texture.
Warm colors — cream body, soft pink and light blue buttons.
Simple, iconic, matching the reference character's wool plush art style.
{STYLE_RULES}""",
        },
        {
            "id": "icon_chat",
            "name": "AI 대화 아이콘",
            "refs": ["idle"],
            "prompt": f"""Two overlapping speech bubbles in wool felt texture.
The front bubble has a small pink heart inside. The back bubble is slightly offset.
Warm cream/beige color with dark brown outline. Matching the reference character's art style.
{STYLE_RULES}""",
        },
    ],

    # --- Highlights 일러스트 ---
    "highlights": [
        {
            "id": "hl_chat",
            "name": "AI 채팅 장면",
            "refs": ["idle"],
            "prompt": f"""The reference character (light blue square wool plush) facing front with a large speech bubble.
Inside the speech bubble: "힘들었구나~ 내가 옆에 있을게~"
The character has a warm, gentle expression (soft smile).
Background: warm cream color (#fdfaef), simple and clean.
{STYLE_RULES}
Generate at 1200x750 pixels (landscape 16:10 ratio), character on the left, speech bubble on the right.""",
        },
        {
            "id": "hl_room",
            "name": "방 꾸미기 장면",
            "refs": ["idle", "room"],
            "prompt": f"""The reference character standing inside a cozy room (pentagon roof shape like the room reference).
The room has warm beige walls and wooden floor. 2-3 cute wool-textured furniture items: a small rug, a lamp, a potted plant.
Character is in the center looking happy.
{STYLE_RULES}
Generate at 1200x750 pixels (landscape 16:10 ratio).""",
        },
        {
            "id": "hl_runner",
            "name": "미니게임 장면",
            "refs": ["idle"],
            "prompt": f"""The reference character running to the right in a side-scrolling game scene.
Below: a simple green ground/platform. Above: 3 golden coins floating.
Simple 2D platformer feel. The character's legs are in a running pose.
Background: light blue sky with small white clouds.
{STYLE_RULES}
Generate at 1200x750 pixels (landscape 16:10 ratio).""",
        },
        {
            "id": "hl_gacha",
            "name": "가챠 뽑기 장면",
            "refs": ["happy"],
            "prompt": f"""The reference character (happy expression, arms raised) with sparkle/star effects around it.
A cute furniture item (small wool-textured sofa) is appearing with golden sparkle effects.
Celebratory moment — the character just received a rare item!
Background: warm cream with subtle confetti/sparkles.
{STYLE_RULES}
Generate at 1200x750 pixels (landscape 16:10 ratio).""",
        },
    ],

    # --- Download ---
    "download": [
        {
            "id": "dl_nemo",
            "name": "Download 섹션 네모 (점프)",
            "refs": ["happy"],
            "prompt": f"""The reference character (happy expression) jumping with both arms raised high.
A speech bubble above says "빨리 만나자~!"
The character is excited and joyful, slightly tilted.
{STYLE_RULES}""",
        },
    ],

    # --- Footer ---
    "footer": [
        {
            "id": "ft_nemo",
            "name": "Footer 네모 (바이바이)",
            "refs": ["idle"],
            "prompt": f"""The reference character waving goodbye with one hand.
A small speech bubble says "또 놀러 와~!"
Gentle, friendly farewell expression.
{STYLE_RULES}
Generate at 400x400 pixels.""",
        },
    ],
}


def load_ref(name):
    """Load reference image bytes."""
    paths = {"idle": REF_IDLE, "happy": REF_HAPPY, "room": REF_ROOM}
    return paths[name].read_bytes()


def generate_image(ref_list, prompt):
    """Generate image with Gemini using reference(s)."""
    contents = []
    for ref_name in ref_list:
        ref_bytes = load_ref(ref_name)
        contents.append(genai.types.Part.from_bytes(data=ref_bytes, mime_type="image/png"))
    contents.append(prompt)

    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=contents,
        config=genai.types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
        ),
    )

    for part in response.candidates[0].content.parts:
        if part.inline_data and part.inline_data.mime_type.startswith("image/"):
            return part.inline_data.data
    return None


def chromakey_remove(raw_path, out_path):
    """Remove chromakey magenta background + crop."""
    img = Image.open(raw_path).convert("RGBA")
    data = np.array(img)
    h, w = data.shape[:2]

    corners = [data[0, 0, :3], data[0, -1, :3], data[-1, 0, :3], data[-1, -1, :3]]
    bg_color = np.median(corners, axis=0).astype(int)

    r, g, b = data[:, :, 0].astype(int), data[:, :, 1].astype(int), data[:, :, 2].astype(int)
    match = (np.abs(r - bg_color[0]) <= 25) & (np.abs(g - bg_color[1]) <= 25) & (np.abs(b - bg_color[2]) <= 25)
    data[match] = [0, 0, 0, 0]

    # BFS from edges
    alpha = data[:, :, 3]
    transparent = (alpha == 0)
    visited = np.zeros((h, w), dtype=bool)
    queue = deque()
    for y in range(h):
        for x in range(w):
            if not transparent[y, x]:
                continue
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and not visited[ny, nx] and alpha[ny, nx] > 0:
                    pr, pg, pb = int(data[ny, nx, 0]), int(data[ny, nx, 1]), int(data[ny, nx, 2])
                    if abs(pr - bg_color[0]) <= 40 and abs(pg - bg_color[1]) <= 40 and abs(pb - bg_color[2]) <= 40:
                        visited[ny, nx] = True
                        data[ny, nx] = [0, 0, 0, 0]
                        queue.append((ny, nx))
    while queue:
        cy, cx = queue.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < h and 0 <= nx < w and not visited[ny, nx] and data[ny, nx, 3] > 0:
                pr, pg, pb = int(data[ny, nx, 0]), int(data[ny, nx, 1]), int(data[ny, nx, 2])
                if abs(pr - bg_color[0]) <= 40 and abs(pg - bg_color[1]) <= 40 and abs(pb - bg_color[2]) <= 40:
                    visited[ny, nx] = True
                    data[ny, nx] = [0, 0, 0, 0]
                    queue.append((ny, nx))

    # Crop to content
    alpha = data[:, :, 3]
    rows = np.any(alpha > 10, axis=1)
    cols = np.any(alpha > 10, axis=0)
    if not rows.any() or not cols.any():
        Image.fromarray(data).save(out_path, "PNG")
        return
    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]
    rmin = max(0, rmin - 2)
    rmax = min(h - 1, rmax + 2)
    cmin = max(0, cmin - 2)
    cmax = min(w - 1, cmax + 2)
    result = Image.fromarray(data).crop((cmin, rmin, cmax + 1, rmax + 1))
    result.save(out_path, "PNG")
    print(f"    Final: {result.width}x{result.height}")


def main():
    # 섹션 선택 (인자 없으면 전체)
    sections = sys.argv[1:] if len(sys.argv) > 1 else list(ASSETS.keys())

    for section in sections:
        if section not in ASSETS:
            print(f"[SKIP] Unknown section: {section}")
            continue

        section_dir = OUTPUT_DIR / section
        section_dir.mkdir(parents=True, exist_ok=True)
        raw_dir = section_dir / "raw"
        raw_dir.mkdir(exist_ok=True)

        items = ASSETS[section]
        existing = {f.stem for f in section_dir.glob("*.png") if not f.stem.endswith("_raw")}
        todo = [item for item in items if item["id"] not in existing]

        if not todo:
            print(f"[{section}] All assets exist, skipping.")
            continue

        print(f"\n{'='*50}")
        print(f"[{section}] Generating {len(todo)} asset(s)...")
        print(f"{'='*50}")

        for i, item in enumerate(todo):
            print(f"\n  [{i+1}/{len(todo)}] {item['name']} ({item['id']})")

            raw_path = raw_dir / f"{item['id']}_raw.png"
            final_path = section_dir / f"{item['id']}.png"

            try:
                img_data = generate_image(item["refs"], item["prompt"])
                if not img_data:
                    print(f"    [ERROR] No image returned")
                    continue

                raw_path.write_bytes(img_data)
                print(f"    Raw saved: {raw_path.name}")

                chromakey_remove(raw_path, final_path)
                print(f"    Done: {final_path.name}")

            except Exception as e:
                print(f"    [ERROR] {e}")

            # Rate limit (Gemini free tier)
            if i < len(todo) - 1:
                print("    Waiting 5s (rate limit)...")
                time.sleep(5)

    print(f"\n{'='*50}")
    print("All done! Assets saved to: landing/public/images/")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
