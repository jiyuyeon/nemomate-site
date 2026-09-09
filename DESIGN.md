# NemoMate Landing — DESIGN.md

> AI 에이전트가 읽고 일관된 UI를 생성하기 위한 디자인 시스템 문서
> 기반: Astro + shared/primitives.css + landing/src/styles/tokens.css
> 디자인 레퍼런스: ctrl.xyz (레이아웃/타이포/여백) + Duolingo (인터랙션/캐릭터 중심)

---

## 1. Visual Theme & Atmosphere

- **톤:** 따뜻한 브라운 + 연핑크 액센트. 양모인형 질감의 귀여운 2D 일러스트 감성
- **밀도:** 시원한 여백 중심 (ctrl.xyz). 섹션 간 120px, 요소 간 넉넉한 gap
- **타이포:** 대형 타이포 (Hero 96px). 제목이 시각적 앵커 역할
- **인터랙션:** Duolingo식 눌림(press) 버튼 + 부드러운 스크롤 reveal
- **전체 느낌:** "따뜻하고 포근한 펫 게임" — 과한 장식 없이, 네모 캐릭터와 콘텐츠가 주인공
- **검정(#000) 사용 금지** — 테두리/텍스트 모두 다크 브라운(#5C4033) 사용

---

## 2. Color Palette & Roles

### Brown Scale (브랜드 기본)

| Token | Hex | Role |
|-------|-----|------|
| `--brown-900` | `#3A2518` | 제목, 강조 텍스트 |
| `--brown-700` | `#5C4033` | 본문 텍스트, 테두리, 아웃라인 |
| `--brown-500` | `#A0896E` | 보조 텍스트, 캡션 |
| `--brown-400` | `#C4B49E` | 비활성 요소, 스크롤바 thumb |
| `--brown-300` | `#E8D5B8` | 카드 보더, 구분선 |
| `--brown-200` | `#EDE4D4` | 섹션 교차 배경 |
| `--brown-100` | `#F5EDE0` | 밝은 섹션 배경 |
| `--brown-50`  | `#fdfaef` | 페이지 기본 배경 |

### Pink Scale (액센트)

| Token | Value | Role |
|-------|-------|------|
| `--pink-600` | `#C490C0` | CTA hover, 눌림 그림자 accent |
| `--pink-500` | `#D4A0D0` | CTA 버튼, 액센트 |
| `--pink-300` | `rgba(212,160,208,0.3)` | 배지, 하이라이트 배경 |
| `--pink-200` | `rgba(212,160,208,0.15)` | 액센트 서브틀 |
| `--pink-100` | `rgba(212,160,208,0.08)` | 액센트 배경 |

### Semantic Colors

| Token | Maps to | Role |
|-------|---------|------|
| `--text-primary` | `--brown-700` | 본문 텍스트 |
| `--text-secondary` | `--brown-500` | 보조 텍스트 |
| `--text-tertiary` | `--brown-400` | 비활성 텍스트 |
| `--text-inverse` | `#fff` | 어두운 배경 위 텍스트 |
| `--accent` | `--pink-500` | 브랜드 액센트 |
| `--accent-hover` | `--pink-600` | 액센트 호버 |
| `--accent-bg` | `--pink-100` | 액센트 배경 |
| `--bg-primary` | `--brown-50` | 페이지 배경 |
| `--bg-secondary` | `--brown-100` | 교차 섹션 배경 |
| `--bg-tertiary` | `--brown-200` | 3단계 배경 |
| `--bg-elevated` | `#fff` | 카드, 모달 배경 |
| `--border` | `--brown-300` | 기본 보더 |

---

## 3. Typography Rules

### Font Stack

```
Primary: "A2Z", "Mona12", "Pretendard", system-ui, -apple-system, sans-serif
```

- **A2Z (에이투지체):** 메인 폰트 (100~900 weight)
- **Mona12:** 게임 내 픽셀 폰트 (말풍선 등 제한적 사용)
- **Pretendard:** 한글 폴백

### Type Scale

| Token | Desktop | Tablet | Mobile | Use |
|-------|---------|--------|--------|-----|
| `--font-hero` | 96px | 64px | 44px | Hero 메인 카피 |
| `--font-display` | 48px | 40px | 32px | 섹션 제목 |
| `--font-title` | 32px | — | 24px | 항목 제목 |
| `--font-button` | 20px | — | — | 버튼, 카드 제목 |
| `--font-ui` | 18px | — | — | UI 요소 |
| `--font-body` | 18px | — | — | 본문 |
| `--font-label` | 14px | — | — | 라벨, 캡션 |
| `--font-caption` | 12px | — | — | 작은 텍스트 |

### Weight

| Token | Value | Use |
|-------|-------|-----|
| `--weight-normal` | 400 | 본문 |
| `--weight-semi` | 600 | 강조 |
| `--weight-bold` | 700 | 제목, 버튼 |

### Line Height

- 제목: `1.05` (Hero), `1.3` (Display/Title)
- 본문: `1.6` ~ `1.7`
- 버튼: `1`

---

## 4. Component Stylings

### Buttons — Duolingo Press Style

모든 CTA/인터랙티브 버튼은 하단 그림자로 "눌림" 느낌을 준다.

#### `.btn-press` (기본 눌림)

```css
border-radius: 18px;
box-shadow: 0 4px 0 var(--brown-700);    /* --shadow-press */
transform: translateY(0);
transition: transform 0.1s, box-shadow 0.1s;

:active {
  transform: translateY(3px);
  box-shadow: 0 1px 0 var(--brown-700);
}
```

#### `.btn-press-accent` (액센트 눌림 — Primary CTA)

```css
background: var(--accent);               /* #D4A0D0 */
color: var(--text-inverse);              /* white */
box-shadow: 0 4px 0 var(--pink-600);     /* --shadow-press-accent */

:active {
  box-shadow: 0 1px 0 var(--pink-600);
}
```

#### `.btn-pill` (ctrl.xyz 스타일)

```css
border-radius: 40px;                     /* --radius-pill */
position: relative;
overflow: hidden;

::after {   /* hover fill 효과 */
  background: var(--brown-900);
  transform: translateY(100%);
  transition: transform 0.5s var(--ease-smooth);
}

:hover::after { transform: translateY(0); }
:hover { color: var(--text-inverse); }
```

#### Button Sizes

| Class | Font | Padding |
|-------|------|---------|
| `.btn-sm` | `--font-label` (14px) | `6px 8px` |
| `.btn-md` | `--font-label` (14px) | `6px 12px` |
| `.btn-lg` | `--font-button` (20px) | `16px 32px` |

### Cards

```css
background: var(--bg-elevated);           /* white */
border: 2px solid var(--border);          /* --brown-300 */
border-radius: 18px;                      /* Duolingo round */
padding: 32px 24px;
box-shadow: 0 4px 0 var(--brown-700);     /* 눌림 스타일 */

:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);           /* 눌림 -> 일반 그림자 전환 */
}

:active {
  transform: translateY(2px);
  box-shadow: 0 1px 0 var(--brown-700);
}
```

### Nemo Speech Bubble

```css
background: rgba(255, 255, 255, 0.85);
border: none;
border-radius: var(--radius-panel);       /* 12px */
padding: 6px 12px;
font-size: var(--font-label);             /* 14px */
font-weight: var(--weight-bold);
color: var(--text-primary);
```

### Tags / Badges

```css
/* 기본 태그 */
display: inline-flex;
padding: 8px 20px;
border-radius: 40px;                      /* pill 스타일 */
border: 2px solid var(--border);
font-size: 14px;

:hover {
  background: var(--accent);
  color: white;
  border-color: var(--brown-700);
}
```

### Header (Navigation)

```css
position: fixed;
height: 72px;
background: rgba(253, 250, 239, 0.85);   /* brown-50 + blur */
backdrop-filter: blur(12px);
box-shadow: var(--shadow-xs);             /* border-bottom 대신 */
z-index: 100;

/* 중앙 pill 네비게이션 */
nav-container: background var(--bg-secondary), border-radius 40px;
nav-link: padding 10px 20px;
nav-link active: background var(--bg-elevated), border-radius 24px;

/* 스크롤 hide/show */
.header-hidden { transform: translateY(-100%); }
transition: transform 0.5s var(--ease-smooth);
```

### Gallery Carousel

```css
.gallery-track {
  display: flex;
  gap: 20px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
}

.gallery-item {
  width: 280px;
  aspect-ratio: 9/16;
  border-radius: 18px;
  border: 2px solid var(--border);
  box-shadow: var(--shadow-sm);

  :hover { scale(1.04); box-shadow: var(--shadow-lg); }
}
```

---

## 5. Layout Principles

### Spacing Scale (Primitives)

| Token | Value |
|-------|-------|
| `--space-xs` | 2px |
| `--space-sm` | 4px |
| `--space-md` | 6px |
| `--space-lg` | 8px |
| `--space-xl` | 10px |
| `--space-2xl` | 12px |
| `--space-3xl` | 16px |
| `--space-4xl` | 20px |
| `--space-5xl` | 24px |
| `--space-6xl` | 32px |

### Layout Tokens

| Token | Value | Use |
|-------|-------|-----|
| `--section-gap` | 120px (desktop) / 96px (tablet) / 72px (mobile) | 섹션 간 여백 |
| `--content-max` | 1100px | 메인 컨테이너 최대 폭 |
| `--content-narrow` | 720px | 텍스트 중심 섹션 |
| `--header-height` | 72px | 고정 헤더 높이 |
| `--pad-desktop` | 40px | 좌우 패딩 (데스크톱) |
| `--pad-tablet` | 24px | 좌우 패딩 (태블릿) |
| `--pad-mobile` | 16px | 좌우 패딩 (모바일) |

### Grid System

```
.container { max-width: var(--content-max); margin: 0 auto; }
```

- **Features:** `grid-template-columns: repeat(4, 1fr)`, gap 24px
- **Highlights:** `grid-template-columns: 1fr 1fr`, gap 64px, 항목 간격 100px
- **Hero:** `grid-template-columns: 1.2fr 0.8fr`, align-items center

### Whitespace Philosophy

- 시원한 여백이 핵심 — ctrl.xyz 레퍼런스
- Hero 상단 패딩 160px (header 72px + 여백 88px)
- 섹션 내부도 넉넉하게: 타이틀-콘텐츠 간격 64px
- 좁혀야 할 때는 `--content-narrow` (720px) 사용

---

## 6. Depth & Elevation

### Shadow System

| Token | Value | Use |
|-------|-------|-----|
| `--shadow-xs` | `0 1px 4px rgba(92,64,51,0.1)` | 헤더 분리선 |
| `--shadow-sm` | `0 2px 8px rgba(92,64,51,0.15)` | 카드 기본 |
| `--shadow-md` | `0 2px 12px rgba(92,64,51,0.12)` | 카드 hover |
| `--shadow-lg` | `0 4px 16px rgba(92,64,51,0.15)` | 이미지 hover |
| `--shadow-xl` | `0 4px 20px rgba(92,64,51,0.2)` | 모달 |

### Press Shadows (Duolingo 눌림)

| Token | Value | Use |
|-------|-------|-----|
| `--shadow-press` | `0 4px 0 var(--brown-700)` | 기본 눌림 |
| `--shadow-press-accent` | `0 4px 0 var(--pink-600)` | 액센트 눌림 |

### Surface Hierarchy

```
z-index 순서:
  1. 페이지 배경 (--bg-primary)
  2. 카드/콘텐츠 (--bg-elevated + border + shadow)
  3. 헤더 (backdrop-filter blur + shadow-xs, z-index: 100)
```

### Border Radius Scale

| Token | Value | Use |
|-------|-------|-----|
| `--radius-badge` | 4px | 배지 |
| `--radius-tab` | 6px | 탭 |
| `--radius-button` | 8px | 기본 버튼 |
| `--radius-card` | 10px | 카드 |
| `--radius-panel` | 12px | 패널 |
| `--radius-modal` | 14px | 모달 |
| `--radius-window` | 16px | 윈도우 |
| `--radius-pill` | 40px | Pill 버튼/네비 |
| **Duolingo round** | 18px | 카드, CTA, 갤러리 아이템 |

---

## 7. Do's and Don'ts

### DO

- 모든 색상에 CSS 변수(토큰) 사용
- 테두리는 다크 브라운(`--brown-700` = `#5C4033`)
- CTA 버튼은 Duolingo 눌림 스타일 (`.btn-press`, `.btn-press-accent`)
- 섹션 배경을 `--bg-primary` / `--bg-secondary` 교차 사용
- 넉넉한 여백 유지 (section-gap 120px)
- 카드에 `2px solid var(--border)` 보더 사용
- `prefers-reduced-motion` 대응

### DON'T

- 검정(`#000`) 사용 금지 — 항상 다크 브라운
- 색상값 하드코딩 금지 — 반드시 토큰 사용
- Hero에 방 배경 이미지 넣지 않기 — 캐릭터에 집중
- 배경 그라디언트 사용 금지 — 단색 배경
- `border-bottom`으로 헤더 분리 금지 — `box-shadow` 사용
- 과한 장식/이펙트 금지 — 미니멀 유지
- 순백(`#ffffff`)을 에셋 오브젝트에 사용 금지 (배경 제거 문제)

---

## 8. Responsive Behavior

### Breakpoints

| Name | Range | Key Changes |
|------|-------|-------------|
| **Desktop** | >= 1024px | 기본 레이아웃 |
| **Tablet** | 768 ~ 1023px | 카드 2열, Hero 타이포 64px |
| **Mobile** | <= 767px | 카드 1열, 햄버거 메뉴, Hero 세로 스택 |

### Mobile Adaptations

- **Header:** pill 네비 -> 전체폭 드롭다운 (radius만 pill 유지)
- **Hero:** 2컬럼 -> 1컬럼 (캐릭터 상단, 텍스트 하단), CTA 세로 배치
- **Features:** 4열 -> 2열 (태블릿) -> 1열 (모바일)
- **Highlights:** 2컬럼 -> 1컬럼 (이미지 항상 위)
- **Gallery:** 가로 스크롤 유지, 아이템 280px
- **Download:** 버튼 세로 스택

### Touch Targets

- 최소 터치 영역: 44x44px
- 버튼 패딩 충분히 유지

### Container Padding

```css
Desktop: 40px (--pad-desktop)
Tablet:  24px (--pad-tablet)
Mobile:  16px (--pad-mobile)
```

---

## 9. Agent Prompt Guide

### Quick Color Reference

```
Background:  #fdfaef (warm cream)
Alt BG:      #F5EDE0 (light brown)
Text:        #5C4033 (dark brown)
Heading:     #3A2518 (deepest brown)
Accent:      #D4A0D0 (soft pink)
Accent Hover:#C490C0 (deeper pink)
Border:      #E8D5B8 (light brown)
Card BG:     #ffffff (white)
```

### Ready-to-Use Prompts

**"NemoMate 스타일 랜딩 섹션 만들어줘"**
- 배경 `#fdfaef`, 텍스트 `#5C4033`, 제목 `#3A2518`
- 카드: 흰 배경, `2px solid #E8D5B8` 보더, `border-radius: 18px`, 하단 4px 눌림 그림자
- CTA: `#D4A0D0` 배경, 흰 텍스트, `border-radius: 18px`, active 시 3px 하강
- 폰트: A2Z (한글), 제목 48px bold, 본문 18px
- 여백: 섹션 간 120px, 요소 간 넉넉하게

**"NemoMate 스타일 버튼 만들어줘"**
- Primary: `background #D4A0D0`, `color white`, `border-radius 18px`, `box-shadow 0 4px 0 #C490C0`
- Secondary: `background white`, `border 2px solid #E8D5B8`, `border-radius 18px`, `box-shadow 0 4px 0 #C4B49E`
- Active: `transform translateY(3px)`, shadow 1px로 줄임
- Pill: `border-radius 40px`, hover 시 배경 fill 애니메이션

**"NemoMate 스타일 애니메이션 적용해줘"**
- Reveal: `translateY(30px)` -> `0`, `opacity 0` -> `1`, 0.8s `cubic-bezier(0.165, 0.84, 0.44, 1)`
- Stagger: 자식 요소에 0.15s 딜레이 순차 적용
- 방향별: `.reveal-left` (translateX -40px), `.reveal-right` (translateX 40px)
- 버튼 active: 0.1s ease, 3px 하강
- `prefers-reduced-motion: reduce` 시 모든 애니메이션 제거

---

## Appendix: Animation Tokens

| Token | Value | Use |
|-------|-------|-----|
| `--ease-smooth` | `cubic-bezier(0.165, 0.84, 0.44, 1)` | 전역 이징 |
| `--dur-smooth` | 0.5s | 일반 전환 |
| `--dur-reveal` | 0.8s | Reveal 등장 |
| `--stagger-delay` | 0.15s | 순차 딜레이 |
| `--dur-fast` | 0.15s | 빠른 인터랙션 |
| `--dur-normal` | 0.2s | 일반 인터랙션 |
| `--dur-slow` | 0.3s | 느린 전환 |

### Keyframes

```css
/* 네모 idle — 좌우 흔들림 */
@keyframes nemo-idle {
  0%, 100% { transform: rotate(-2deg); }
  50% { transform: rotate(2deg); }
}

/* 네모 점프 — hover 시 1회 */
@keyframes nemo-jump {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-12px); }
}

/* CTA 펄스 — 주목 유도 */
@keyframes pulse-glow {
  0%, 100% { box-shadow: 0 4px 0 var(--brown-700), 0 0 0 0 rgba(212,160,208,0.4); }
  50% { box-shadow: 0 4px 0 var(--brown-700), 0 0 0 8px rgba(212,160,208,0); }
}
```
