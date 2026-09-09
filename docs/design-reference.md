# Landing Design Reference — ctrl.xyz + Duolingo

NemoMate 랜딩 리뉴얼 시 참고할 디자인 레퍼런스 분석.

---

## 1. ctrl.xyz

> 미니멀, 라이트모드, 시원한 여백, 대형 타이포, 정교한 마이크로 인터랙션

### 1-1. Layout

| 항목 | 값 |
|---|---|
| Max container (wide) | 1735px |
| Max container (standard) | 1300px |
| Max container (narrow) | 940px |
| Max container (text) | 790px |
| 좌우 패딩 (mobile) | 2rem (20px) each |
| 섹션 간 간격 (mobile) | 4rem (40px) |
| 섹션 간 간격 (desktop) | 6rem ~ 15.5rem |
| 그리드 | Flex 가변 컬럼 (`--items-by-line`, `--items-gap` CSS 변수) |

### 1-2. Typography

| 항목 | 값 |
|---|---|
| Font | "Tomato Grotesk" (대안: DM Sans, Instrument Sans) |
| Base | `html { font-size: 62.5% }` → 1rem = 10px |
| Hero display | 18rem (180px) desktop / 5.5rem (55px) mobile |
| Section title | 5rem (50px) desktop / 2.4rem (24px) mobile |
| Sub-headline | 3.6rem (36px) desktop / 2.8rem (28px) mobile |
| Body | 2.4rem (24px) desktop / 1.8rem (18px) mobile |
| Caption | 1rem ~ 1.5rem (10~15px) |

### 1-3. Color Palette

```
Background:  #ffffff (main), #f9faf9 (alt section), #ecefec (nav/card)
Text:        #0f0f0f (primary), #5a585a (secondary), #727472 (tertiary)
             #a1a6a2 (muted), #bbbfbb (placeholder)
Accent:      #05c92f (green — CTA, hover, links, scrollbar)
             #e2f2e5 (light green tint)
Others:      #ff5a4d (red), #9dc4f5 (sky), #ffcadc (pink)
             #fbe74e (yellow), #2a5cd3 (blue)
Borders:     #d1d6d2 (grey6)
```

그라디언트 없음 — 전부 플랫 솔리드 컬러.

### 1-4. Cards

| 항목 | 값 |
|---|---|
| Card border-radius | 2rem (20px) |
| Card padding | 4~6rem (desktop), 2rem (mobile) |
| Card shadow | `0 2px 2px rgba(0,0,0,0.16)` (최소한) |
| Card border | 없음 (배경색 대비로 구분) |

### 1-5. Navigation

| 항목 | 값 |
|---|---|
| Nav 높이 | padding 기반: 2.7rem (mobile), 6.8rem (desktop) |
| Nav 배경 | #ecefec (pill 형태) |
| Nav border-radius | 1rem (10px) |
| Nav z-index | 900 |
| 스크롤 시 | fixed, 아래 스크롤 시 `translateY(-100%)` 숨김 |
| 숨김 transition | `1s cubic-bezier(.165, .84, .44, 1)` |

### 1-6. Buttons

```css
/* Primary (dark pill) */
height: 6rem (60px) desktop / 4.5rem (45px) mobile;
padding: 0 4rem (40px) desktop / 0 2.5rem (25px) mobile;
border-radius: 4rem (40px);  /* pill shape */
background: #0f0f0f;
border: 2px solid #0f0f0f;
color: #ffffff;

/* Hover: green(#05c92f) bg가 아래→위로 슬라이드 (::after) */
/* Entry: 0.5s / Exit: 0.3s */
```

### 1-7. Interactions & Animations

| 효과 | 구현 |
|---|---|
| Primary easing | `cubic-bezier(0.165, 0.84, 0.44, 1)` |
| Secondary easing | `cubic-bezier(0.455, 0.03, 0.515, 0.955)` |
| Button hover | Green bg 아래→위 슬라이드 (::after pseudo) |
| Nav hide/show | `translateY(-100%)` 1s transition |
| Image load | opacity 0→1 fade-in |
| Social hover | `scale(1.2)` 0.3s |
| Stagger delay | 0.2s sequential |
| Magnetic buttons | JS 기반 포인터 추적 |

### 1-8. Hero Section

| 항목 | 값 |
|---|---|
| Container | 940px (narrow) |
| Top padding | 15.5rem (155px) desktop |
| Headline | 180px display (데스크톱) |
| Background | 순백 #ffffff — 타이포가 주인공 |
| CTA | Black pill button, green hover |
| 장식 | .StickersEffect (데스크톱 전용, 모바일 숨김) |

### 1-9. Footer

| 항목 | 값 |
|---|---|
| Column gap | 12rem (120px) desktop |
| Social buttons | 4rem (40px) 원형, border 2px |
| Social hover | scale(1.2) 0.3s |
| Link hover color | #05c92f (green) |

---

## 2. Duolingo

> 친근한 라운드 UI, 물리적 촉감의 버튼, 캐릭터 중심 히어로, 단일 브랜드 컬러 지배

### 2-1. Layout

| 항목 | 값 |
|---|---|
| Max container (content) | 988px |
| Max container (footer) | 1065px |
| Hero gap (desktop) | 80px (이미지↔텍스트) |
| Section padding (desktop) | 48px 0 |
| Section padding (tablet) | 16px 40px 48px |
| Feature 간 간격 | 96px (vertical) |
| Feature row gap | 140px (이미지↔텍스트) |

**Breakpoints:**
- Desktop: ≥1080px (side-by-side hero)
- Tablet: 368~1080px (stacked hero)
- Mobile: ≤680px (language bar 숨김)

### 2-2. Typography

| 역할 | Font | Size |
|---|---|---|
| Display / Hero | `feather-bold` (커스텀) | 32px (H1), 48px (feature), 64px (CTA) |
| UI / Buttons | `din-round-bold` | 15px, letter-spacing 0.8px, uppercase |
| Body | `din-round-medium` (500) | 17px, line-height 24px |
| Footer heading | `din-round-bold` | 19px |
| Footer links | `din-round-bold` | 15px, opacity 0.5 |
| Small text | `din-round` | 13px |

### 2-3. Color Palette (동물 테마 변수명!)

```
/* Brand Core */
Feather Green (owl):   #58CC02  — Primary CTA, footer bg, feature headings
Tree-frog (shadow):    #58A700  — Button 하단 그림자
Mask Green:            #89E219  — Secondary green
Macaw (blue):          #1CB0F6  — Secondary CTA, "이미 계정 있음" 텍스트

/* Neutral */
Snow (white):          #FFFFFF  — 배경, 반전 텍스트
Polar:                 #F7F7F7  — Alt 배경
Swan:                  #E5E5E5  — 보더, 디바이더
Wolf (grey):           #777777  — Secondary 텍스트
Eel (dark):            #4B4B4B  — Primary 텍스트

/* Accent */
Cardinal (red):        #FF4B4B  — 에러
Bee (yellow):          #FFC800
Fox (orange):          #FF9600
Beetle (purple):       #CE82FF
```

그라디언트 없음 — 전부 플랫 솔리드.

### 2-4. Buttons (핵심!)

```css
/* === Primary (GET STARTED) === */
/* Wrapper div */
border-radius: 18px;
box-shadow: 0 4px 0px #58A700;  /* 어두운 green 하단 그림자 = 입체감 */

/* Button */
background-color: #58CC02;
color: #ffffff;
border: none;
border-radius: 18px;
height: 50px;
max-width: 330px;
font-size: 15px;
font-weight: 700;
letter-spacing: 0.8px;
text-transform: uppercase;

/* Hover → filter: brightness(1.1) */
/* Active → box-shadow: none; translate: 0 3px; (눌림 효과!) */
transition: box-shadow 0.2s ease, translate 0.2s ease;

/* === Secondary (I ALREADY HAVE AN ACCOUNT) === */
background-color: #ffffff;
border: 2px solid #ebebeb;
color: #1CB0F6;
box-shadow: 0 4px 0px #e5e5e5;  /* 회색 하단 그림자 */
/* Hover → filter: brightness(0.9) */
```

**핵심 패턴:** 버튼 아래 `box-shadow` + `:active` 시 그림자 제거 + `translate: 0 3px` → 물리적 눌림 촉감

### 2-5. Navigation

| 항목 | 값 |
|---|---|
| 높이 | 70px, fixed |
| 배경 | white |
| z-index | 2 |
| Inner max-width | 988px |
| Logo | 161×38px (desktop), 179×42px (tablet) |
| Language strip | 80px 높이, 상하 2px border (#E5E5E5) |
| Language item gap | 20px |
| Language strip | 680px 이하에서 숨김 |

### 2-6. Interactions

| 효과 | 구현 |
|---|---|
| Button press | `translate: 0 3px` + shadow 제거 (0.2s ease) |
| Button hover | `filter: brightness(1.1)` (primary), `brightness(0.9)` (secondary) |
| Language carousel | `transform: translateX()` 0.5s ease-in-out |
| Feature animations | Lottie (bodymovin) SVG/JSON 루프 애니메이션 |
| Scroll animation | 없음 (스크롤 트리거 없음) |

### 2-7. Hero Section

**Desktop (≥1080px)**
```
[ 이미지 464×466px ]  ← 80px gap →  [ 텍스트 + CTA ]
                max-width: 988px, centered
```

**Tablet (≤1080px)**
```
[ 이미지 400×355px ]
[ H1 텍스트 ]
[ CTA 버튼 ]
padding: 16px 40px 48px
```

| 항목 | 값 |
|---|---|
| H1 | 32px, din-round-bold, #4B4B4B |
| H1 max-width | 550px |
| CTA margin-top | 40px |
| CTA gap | 12px |
| Button max-width | 330px |
| 배경 | 순백 — 캐릭터 일러스트가 주인공 |

### 2-8. Footer

| 항목 | 값 |
|---|---|
| 배경 | #58CC02 (brand green) |
| 텍스트 | white, 링크는 opacity 0.5 |
| Link grid max-width | 1065px |
| Column width | ~170px each |
| Column heading | 19px, bold |
| Links | 15px, bold, opacity 0.5, padding 5px 0 |
| Language row | border-top: 2px solid rgba(255,255,255,0.2) |
| Owl icon | 64×64px |

---

## 3. NemoMate 랜딩에 적용할 핵심 패턴

### From ctrl.xyz (시원한 레이아웃 + 인터랙션)
1. **대형 타이포 히어로** — 180px급 display font, 타이포로 임팩트
2. **Pill 버튼** — border-radius 40px, hover 시 green bg 슬라이드업 (::after)
3. **Pill 네비게이션** — 스크롤 시 hide/show, cubic-bezier 이징
4. **여백 중심 디자인** — 섹션 간 6~15rem 간격, 940~1300px 컨테이너
5. **Primary easing** — `cubic-bezier(0.165, 0.84, 0.44, 1)` 전체 통일
6. **Stagger 애니메이션** — 0.2s 순차 딜레이

### From Duolingo (친근함 + 촉감)
1. **눌림 버튼** — `box-shadow: 0 4px 0 darker-shade` + active 시 shadow 제거 + translate 3px
2. **캐릭터 중심 히어로** — 마스코트 일러스트 왼쪽, 텍스트+CTA 오른쪽
3. **단일 브랜드 컬러** — CTA, footer, headings 모두 하나의 메인 컬러
4. **라운드 UI** — border-radius 18px, 동글동글한 인상
5. **Lottie 애니메이션** — feature 섹션에 루핑 SVG 애니메이션
6. **Footer = 브랜드 컬러 배경** — 메인 컬러 풀 배경 + 흰 텍스트

### NemoMate 맞춤 조합 제안
| 요소 | 참고 | 적용 |
|---|---|---|
| 히어로 | ctrl + duo | 대형 타이포 + 네모 캐릭터 일러스트 |
| 버튼 | Duolingo | 브라운 눌림 버튼 (shadow: darker brown) |
| 네비 | ctrl | Pill nav, 스크롤 hide/show |
| 섹션 레이아웃 | ctrl | 넓은 여백, 940~1300px 컨테이너 |
| 인터랙션 | ctrl | cubic-bezier easing, stagger |
| Feature 섹션 | Duolingo | 이미지↔텍스트 교차 배치 + 애니메이션 |
| Footer | Duolingo | 브라운 풀 배경 + 크림색 텍스트 |
| 컬러 | NemoMate | warm brown 계열 토큰 유지 |
