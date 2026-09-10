# 사운드 출처 및 라이선스

모든 음원은 **CC0 1.0 (퍼블릭 도메인)** 입니다.
저작자 표시 의무가 없고, 상업적 배포에 자유롭게 쓸 수 있습니다.
그래도 예의상 아래에 출처를 남겨둡니다.

## 배경음악 (BGM)

| 파일 | 원곡 | 만든 사람 | 출처 |
|---|---|---|---|
| `bgm_main.mp3` | Hush Hamlet | Alexandr Zhelanov 외 | [OpenGameArt](https://opengameart.org/content/hush-hamlet) |
| `bgm_game.mp3` | Cozy Puzzle In-Game 1 | — | [OpenGameArt](https://opengameart.org/content/cozy-puzzle-in-game-1) |
| `bgm_night.mp3` | Lonely Night | — | [OpenGameArt](https://opengameart.org/content/lonely-night) |
| `bgm_boss.mp3` | Boss Battle #2 [8 bit] | — | [OpenGameArt](https://opengameart.org/content/boss-battle-2-8-bit) |

## 효과음 (SFX)

출처: **[Kenney.nl](https://kenney.nl/assets/category:Audio)** — 전 팩 CC0

| 파일 | 원본 | 팩 |
|---|---|---|
| `sfx_click.mp3` | click_001 | Interface Sounds |
| `sfx_coin.mp3` | chips-stack-2 | Casino Audio |
| `sfx_purchase.mp3` | confirmation_002 | Interface Sounds |
| `sfx_delivery.mp3` | open_002 | Interface Sounds |
| `sfx_levelup.mp3` | powerUp2 | Digital Audio |
| `sfx_gacha.mp3` | card-shuffle | Casino Audio |
| `sfx_gacha_reveal.mp3` | cards-pack-open-1 | Casino Audio |
| `sfx_game_start.mp3` | phaserUp3 | Digital Audio |
| `sfx_game_clear.mp3` | jingles_PIZZI07 | Music Jingles |
| `sfx_game_fail.mp3` | jingles_PIZZI02 | Music Jingles |

## 가공 내용

- 원본 `.ogg` → `.mp3` 변환 (libmp3lame, VBR q5)
- 볼륨 평준화: BGM은 -20 LUFS, 효과음은 -16 LUFS
  (효과음이 배경음보다 또렷하게 들리도록 4dB 차이를 뒀습니다)

## 음원을 새로 바꾸고 싶다면

파일 이름만 그대로 유지하고 덮어쓰면 코드 수정 없이 바뀝니다.
새 소리를 추가하려면 `src/hooks/useSoundEffects.ts` 의 `SFX` / `BGM` 목록에 한 줄 넣으면 됩니다.
