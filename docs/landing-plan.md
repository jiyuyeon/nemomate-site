# NemoMate 랜딩 사이트 리뉴얼 기획서

> **작성일:** 2026-04-08
> **기반:** Astro 6.1.4 + 기존 디자인 시스템 (primitives.css + tokens.css)
> **디자인 레퍼런스:** ctrl.xyz (레이아웃/타이포/여백) + Duolingo (인터랙션/캐릭터 중심)
> **핵심 원칙:** 따뜻한 브라운 톤 유지 + 시원한 여백 + 친근한 인터랙션

---

## 목차

1. [디자인 시스템 확장](#1-디자인-시스템-확장)
2. [섹션별 상세 기획](#2-섹션별-상세-기획)
3. [글로벌 인터랙션/애니메이션](#3-글로벌-인터랙션애니메이션)
4. [현재 대비 변경점 요약](#4-현재-대비-변경점-요약)
5. [구현 우선순위 및 단계](#5-구현-우선순위-및-단계)

---

## 1. 디자인 시스템 확장

### 1-1. tokens.css 추가/변경 토큰

```css
:root {
  /* --- 폰트 크기: ctrl.xyz 스타일 대형 타이포 --- */
  --font-hero: 96px;          /* 현재 48px -> 96px (2배) */
  --font-display: 48px;       /* 현재 36px -> 48px */
  --font-title: 32px;         /* 현재 24px -> 32px */
  --font-button: 20px;        /* 유지 */
  --font-body: 18px;          /* 현재 16px -> 18px */

  /* --- 레이아웃: 시원한 여백 --- */
  --section-gap: 120px;       /* 현재 80px -> 120px (6~8rem) */
  --content-max: 1100px;      /* 현재 1200px -> 1100px (좀 더 집중감) */
  --content-narrow: 720px;    /* 텍스트 중심 섹션용 */

  /* --- Pill 버튼 전용 --- */
  --radius-pill: 40px;        /* 신규: ctrl.xyz 스타일 pill */

  /* --- 눌림 버튼 (Duolingo) --- */
  --shadow-press: 0 4px 0 var(--brown-700);
  --shadow-press-accent: 0 4px 0 var(--pink-600);

  /* --- 통합 이징 (ctrl.xyz) --- */
  --ease-smooth: cubic-bezier(0.165, 0.84, 0.44, 1);
  --dur-smooth: 0.5s;
  --dur-reveal: 0.8s;

  /* --- Stagger 딜레이 --- */
  --stagger-delay: 0.15s;
}

@media (max-width: 767px) {
  :root {
    --font-hero: 44px;        /* 현재 32px -> 44px */
    --font-display: 32px;     /* 현재 28px -> 32px */
    --font-title: 24px;       /* 현재 20px -> 24px */
    --section-gap: 72px;      /* 현재 48px -> 72px */
  }
}

@media (min-width: 768px) and (max-width: 1023px) {
  :root {
    --font-hero: 64px;
    --font-display: 40px;
    --section-gap: 96px;
  }
}
```

### 1-2. 컴포넌트 시스템 추가

```css
/* --- Pill 버튼 (ctrl.xyz) --- */
.btn-pill {
  border-radius: var(--radius-pill);
  position: relative;
  overflow: hidden;
  z-index: 0;
  transition: transform var(--ease-smooth), color 0.3s;
}

.btn-pill::after {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--brown-900);
  border-radius: inherit;
  transform: translateY(100%);
  transition: transform var(--ease-smooth);
  z-index: -1;
}

.btn-pill:hover::after {
  transform: translateY(0);
}

.btn-pill:hover {
  color: var(--text-inverse);
}

/* --- 눌림 버튼 (Duolingo) --- */
.btn-press {
  border-radius: 18px;
  box-shadow: var(--shadow-press);
  transform: translateY(0);
  transition: transform 0.1s, box-shadow 0.1s;
}

.btn-press:active {
  transform: translateY(3px);
  box-shadow: 0 1px 0 var(--brown-700);
}

.btn-press-accent {
  background: var(--accent);
  color: var(--text-inverse);
  box-shadow: var(--shadow-press-accent);
}

.btn-press-accent:active {
  box-shadow: 0 1px 0 var(--pink-600);
}
```

---

## 2. 섹션별 상세 기획

---

### 2-0. Header (네비게이션)

#### 현재 상태
- 고정 상단 바, 좌 로고 + 우 텍스트 링크, 모바일 햄버거

#### 리뉴얼 방향: Pill 네비게이션 (ctrl.xyz)

#### 레이아웃
```
[  중앙 Pill 네비게이션 바  ]
   소개 | 기능 | 미리보기 | 다운로드

좌측: 로고 (고정)
우측: 다운로드 CTA (pill 버튼)
```

#### CSS 스펙
| 속성 | 값 |
|------|-----|
| 높이 | 72px |
| 배경 | `rgba(253, 250, 239, 0.85)` + `backdrop-filter: blur(12px)` |
| pill 컨테이너 배경 | `var(--bg-secondary)` |
| pill border-radius | 40px (var(--radius-pill)) |
| nav-link 패딩 | 10px 20px |
| nav-link 활성 배경 | `var(--bg-elevated)` |
| nav-link 활성 border-radius | 24px |
| border-bottom | 없음 (그림자로 대체: `var(--shadow-xs)`) |
| 우측 CTA | `.btn-pill .btn-sm` "다운로드" |

#### 인터랙션
- **스크롤 Hide/Show:** 아래로 스크롤 시 `translateY(-100%)` 숨김, 위로 스크롤 시 나타남
- **이징:** `transition: transform 0.5s var(--ease-smooth)`
- **활성 링크:** IntersectionObserver로 현재 섹션 감지, 활성 nav-link에 배경 pill 표시
- **모바일:** pill 대신 전체폭 드롭다운 (현재 방식 유지, radius만 pill로 변경)

#### 변경점
- `border-bottom` 제거 -> `box-shadow` 분리선
- 네비 구조: 좌우 분산 -> 중앙 pill + 좌 로고 + 우 CTA
- 스크롤 시 hide/show 추가
- 헤더 높이 64px -> 72px

---

### 2-1. Hero 섹션

#### 현재 상태
- 수직 중앙 배치: 방 배경 + 네모 캐릭터 (작은 크기) + 제목 + 부제 + CTA 버튼
- `min-height: 100vh`, 배경 그라디언트

#### 리뉴얼 방향: Duolingo식 캐릭터 중심 + ctrl.xyz식 대형 타이포

#### 레이아웃 (데스크톱)
```
+--------------------------------------------------+
|                                                    |
|               (상단 여백: 160px)                    |
|                                                    |
|     당신의 바탕화면 위에,          [네모 캐릭터]     |
|     네모난 작은 친구               (200px 크기)     |
|                                    말풍선           |
|     네모와 함께 방을 꾸미고,                        |
|     대화하고, 놀아주세요                            |
|                                                    |
|     [ 무료 다운로드 ]  [ 미리보기 ]                 |
|                                                    |
|               (하단 여백: 120px)                    |
+--------------------------------------------------+
```

#### CSS 스펙
| 속성 | 값 |
|------|-----|
| 컨테이너 | `max-width: var(--content-max)` |
| 레이아웃 | `display: grid; grid-template-columns: 1.2fr 0.8fr; align-items: center` |
| 상단 패딩 | `padding-top: 160px` (header 72px + 여백 88px) |
| 하단 패딩 | `padding-bottom: 120px` |
| min-height | `100vh` 유지 |
| 배경 | `var(--bg-primary)` 단색 (그라디언트 제거 -- 미니멀) |
| 제목 폰트 | `var(--font-hero)` = 96px, `font-weight: 700`, `line-height: 1.05` |
| 제목 색상 | `var(--brown-900)` |
| 부제 폰트 | `var(--font-body)` = 18px, 색상 `var(--text-secondary)` |
| 부제 max-width | 400px |
| 제목-부제 간격 | 24px |
| 부제-CTA 간격 | 40px |
| 캐릭터 크기 | width 200px (현재 120px -> 200px) |
| 캐릭터 영역 | 우측, 수직 중앙, `position: relative` |
| 말풍선 | 캐릭터 위, hover 시 등장 (현재 유지) |

#### CTA 버튼 스펙
| 속성 | Primary (다운로드) | Secondary (미리보기) |
|------|-----|-----|
| 스타일 | `.btn-press-accent` | `.btn-press` |
| 배경 | `var(--accent)` | `var(--bg-elevated)` |
| 색상 | `var(--text-inverse)` | `var(--text-primary)` |
| 보더 | 없음 | `2px solid var(--border)` |
| border-radius | 18px | 18px |
| box-shadow | `0 4px 0 var(--pink-600)` | `0 4px 0 var(--brown-400)` |
| 패딩 | 16px 32px | 16px 32px |
| 폰트 | `var(--font-button)` = 20px, bold |
| active | `translateY(3px)`, shadow 1px | 동일 |
| 간격 (두 버튼) | 16px |

#### 인터랙션
- **타이틀 등장:** 한 줄씩 `translateY(40px)` -> `0`, `opacity: 0` -> `1`, stagger 0.15s
- **캐릭터 등장:** 우측에서 슬라이드 인 (`translateX(60px)` -> `0`), 0.3s 딜레이
- **캐릭터 idle:** `nemo-idle` 애니메이션 유지 (3s, 좌우 흔들림)
- **캐릭터 hover:** `char_idle.png` -> `char_happy.png` + `nemo-jump` 1회 재생
- **말풍선:** hover 시 `opacity: 0` -> `1` + `translateY(8px)` -> `0` (0.3s)
- **CTA 버튼:** Duolingo 눌림 효과 (active 시 3px 하강)

#### 모바일 (max-width: 767px)
```
[네모 캐릭터 (140px)]
     말풍선

당신의 바탕화면 위에,
네모난 작은 친구

부제 텍스트

[ 무료 다운로드 ]
[ 미리보기 ]
```
- `grid-template-columns: 1fr` (단일 열)
- 캐릭터 상단, 텍스트 하단
- 버튼 세로 배치 (`flex-direction: column`)
- 패딩: `padding-top: 100px; padding-bottom: 80px`

#### 변경점
- 레이아웃: 수직 중앙 -> 좌우 2컬럼 그리드
- 배경: 그라디언트 -> 단색
- 방 배경 이미지: 제거 (Hero에서는 캐릭터에 집중)
- 타이포: 48px -> 96px
- 캐릭터: 120px -> 200px
- CTA: 기본 버튼 -> Duolingo 눌림 버튼
- 여백: 크게 확대

---

### 2-2. Features 섹션 (네모메이트는?)

#### 현재 상태
- 4열 그리드, 카드 컴포넌트 (아이콘 + 제목 + 설명)

#### 리뉴얼 방향: 아이콘 중심 미니멀 그리드 + Duolingo 라운드 카드

#### 레이아웃
```
+--------------------------------------------------+
|                                                    |
|            네모메이트는?  (큰 타이틀)               |
|     바탕화면 위에 사는 양모인형, 네모를 키워보세요    |
|                                                    |
|   +----------+  +----------+  +----------+  +----------+
|   |   아이콘  |  |   아이콘  |  |   아이콘  |  |   아이콘  |
|   |  데스크톱  |  | 방 꾸미기 |  |  미니게임  |  |  AI 대화  |
|   |   친구    |  |          |  |          |  |          |
|   +----------+  +----------+  +----------+  +----------+
|                                                    |
+--------------------------------------------------+
```

#### CSS 스펙
| 속성 | 값 |
|------|-----|
| 섹션 배경 | `var(--bg-secondary)` |
| 섹션 패딩 | `var(--section-gap) 0` = 120px 상하 |
| 타이틀 폰트 | `var(--font-display)` = 48px |
| 서브타이틀 | `var(--font-body)` = 18px, `var(--text-secondary)`, margin-bottom: 64px |
| 그리드 | `grid-template-columns: repeat(4, 1fr)`, `gap: 24px` |
| 카드 배경 | `var(--bg-elevated)` |
| 카드 border | `2px solid var(--border)` |
| 카드 border-radius | 18px (Duolingo 라운드) |
| 카드 패딩 | 32px 24px |
| 카드 box-shadow | `var(--shadow-press)` (눌림 스타일, 하단 4px) |
| 아이콘 크기 | 56px x 56px |
| 아이콘-제목 간격 | 16px |
| 제목-설명 간격 | 8px |
| 제목 폰트 | `var(--font-button)` = 20px, bold |
| 설명 폰트 | `var(--font-label)` = 14px, `var(--text-secondary)` |

#### 인터랙션
- **카드 등장:** stagger 애니메이션, 각 카드 0.15s 딜레이
  - `translateY(30px)` -> `0`, `opacity: 0` -> `1`
  - 이징: `var(--ease-smooth)`
- **카드 hover:** `translateY(-4px)` + `box-shadow: var(--shadow-md)` (눌림 그림자 -> 일반 그림자 전환)
- **카드 active/click:** `translateY(2px)` + `box-shadow: 0 1px 0 var(--brown-700)` (Duolingo 눌림)

#### 모바일
- `grid-template-columns: 1fr 1fr` (태블릿)
- `grid-template-columns: 1fr` (모바일, max-width: 360px 컨테이너)

#### 변경점
- 카드 radius: `var(--radius-window)` 16px -> 18px (Duolingo 라운드)
- 카드에 눌림 그림자 추가
- 카드 패딩 축소 (24px -> 32px 24px, 세로 여유)
- stagger 등장 애니메이션 추가

---

### 2-3. Highlights 섹션 (이런 걸 할 수 있어요)

#### 현재 상태
- 4개 교차 배치 (이미지 + 텍스트 좌우 교대), 이미지 placeholder 상태

#### 리뉴얼 방향: ctrl.xyz식 넉넉한 여백 + 대형 텍스트 + 인터랙티브 미디어

#### 레이아웃 (각 항목)
```
+--------------------------------------------------+
|                                                    |
|   네모야, 오늘 어땠어?            [스크린샷/GIF]    |
|                                    (520x325)       |
|   네모는 당신의 말에 귀 기울이는                    |
|   작은 친구예요.                                   |
|                                                    |
|   "힘들었구나~ 내가 옆에 있을게~"                   |
|                                                    |
|-----------------------------------------------------|
|                                                    |
|   [스크린샷/GIF]            네모의 방을 꾸며주세요   |
|   (520x325)                                        |
|                             가챠로 가구를 모으고...  |
|                                                    |
+--------------------------------------------------+
```

#### CSS 스펙
| 속성 | 값 |
|------|-----|
| 섹션 배경 | `var(--bg-primary)` |
| 섹션 패딩 | `var(--section-gap) 0` = 120px |
| 타이틀 | `var(--font-display)` = 48px |
| 항목 간 간격 | 100px (현재 64px -> 100px, 시원한 여백) |
| 그리드 | `grid-template-columns: 1fr 1fr`, `gap: 64px` (현재 40px -> 64px) |
| 항목 제목 | `var(--font-title)` = 32px (현재 24px -> 32px) |
| 항목 본문 | `var(--font-body)` = 18px, `line-height: 1.7` |
| 말풍선 | 기존 `.nemo-bubble` 유지, `margin-top: 16px` |
| 이미지 영역 | `aspect-ratio: 16/10`, `border-radius: 18px` |
| 이미지 보더 | `2px solid var(--border)` |
| 이미지 overflow | `hidden` |
| reverse 방식 | `direction: rtl` -> `order` 속성으로 변경 (더 시맨틱) |

#### 인터랙션
- **항목 등장:** IntersectionObserver, `translateY(40px)` -> `0` + `opacity`
- **이미지 등장:** 텍스트보다 0.2s 늦게 등장 (stagger)
- **이미지 hover:** `scale(1.02)` + `box-shadow: var(--shadow-lg)` 전환
- **이미지 교체:** placeholder -> 실제 스크린샷/GIF (Phase 2에서)
- **말풍선:** 해당 항목이 뷰포트에 들어오면 typing 효과로 한 글자씩 표시 (선택적)

#### 모바일
- `grid-template-columns: 1fr`
- 이미지 항상 위, 텍스트 아래
- 항목 간 간격 64px

#### 변경점
- 항목 간격: 64px -> 100px
- 그리드 gap: 40px -> 64px
- 제목 크기: 24px -> 32px
- reverse 방식: `direction: rtl` -> CSS `order` (접근성 향상)
- placeholder 스타일: dashed border -> 실제 스크린샷 슬롯 준비

---

### 2-4. Gallery 섹션 (미리보기)

#### 현재 상태
- 가로 스크롤 6개 placeholder, `aspect-ratio: 9/16`, 320px 고정폭

#### 리뉴얼 방향: 앱 스크린샷 쇼케이스 (가로 스크롤 유지, 시각적 개선)

#### 레이아웃
```
+--------------------------------------------------+
|                                                    |
|                   미리보기                          |
|           네모와의 일상을 먼저 만나보세요             |
|                                                    |
|  [  스크린샷1  ] [  스크린샷2  ] [  스크린샷3  ] ... |
|     (280x)        (280x)        (280x)       ->    |
|                                                    |
+--------------------------------------------------+
```

#### CSS 스펙
| 속성 | 값 |
|------|-----|
| 섹션 배경 | `var(--bg-secondary)` |
| 타이틀 | `var(--font-display)` = 48px |
| gallery-track gap | 20px (현재 `var(--gap-section)` 16px -> 20px) |
| gallery-item 너비 | 280px (현재 320px -> 280px, 더 많이 보이게) |
| gallery-item aspect-ratio | `9/16` 유지 (앱 스크린샷) |
| gallery-item border-radius | 18px (Duolingo 라운드) |
| gallery-item border | `2px solid var(--border)` |
| gallery-item box-shadow | `var(--shadow-sm)` |
| 스크롤바 | 커스텀 유지, 높이 4px, `var(--brown-300)` thumb |
| 좌우 패딩 | 컨테이너 바깥까지 확장 (full-bleed scroll) |

#### 인터랙션
- **스크롤 인디케이터:** 좌우 화살표 버튼 또는 좌우 fade gradient
- **아이템 hover:** `scale(1.04)` + `box-shadow: var(--shadow-lg)` (현재 1.03 -> 1.04)
- **아이템 등장:** 좌측에서 stagger 슬라이드 인
- **라이트박스 (선택):** 클릭 시 확대 보기 모달

#### 변경점
- 아이템 radius: 0 -> 18px
- box-shadow 추가
- 스크롤 인디케이터 추가
- full-bleed 스크롤 (컨테이너 밖으로 확장)

---

### 2-5. Download 섹션 (네모를 데려가세요)

#### 현재 상태
- 핑크 그라디언트 배경, 캐릭터 + 제목 + 듀얼 버튼 + 베타 안내

#### 리뉴얼 방향: 브랜드 컬러 강조 + Duolingo 눌림 버튼

#### 레이아웃
```
+==================================================+
|  (브랜드 컬러 영역: 핑크 배경)                      |
|                                                    |
|            [네모 캐릭터 120px]                      |
|            "빨리 만나자~!"                          |
|                                                    |
|         네모를 데려가세요                            |
|     지금 바로 베타 버전을 다운로드하세요              |
|                                                    |
|   [ macOS 다운로드 ]    [ Windows 다운로드 ]        |
|                                                    |
|    Beta v0.1.0 / macOS 12+ / Windows 10+           |
|                                                    |
|   +--------------------------------------------+   |
|   | 베타 안내 카드                               |   |
|   +--------------------------------------------+   |
|                                                    |
+==================================================+
```

#### CSS 스펙
| 속성 | 값 |
|------|-----|
| 섹션 배경 | `var(--accent-bg)` (연한 핑크, 그라디언트 제거) |
| 섹션 패딩 | `var(--section-gap) 0` = 120px |
| 타이틀 | `var(--font-display)` = 48px |
| 서브타이틀 | `var(--font-body)` = 18px |
| 캐릭터 크기 | 100px (현재 80px -> 100px) |
| 버튼 스타일 | `.btn-press` (Duolingo 눌림) |
| Primary 버튼 (감지된 OS) | `.btn-press-accent`, 배경 `var(--accent)`, shadow `0 4px 0 var(--pink-600)` |
| Secondary 버튼 | `.btn-press`, 배경 `var(--bg-elevated)`, border `2px solid var(--border)`, shadow `0 4px 0 var(--brown-400)` |
| 버튼 border-radius | 18px |
| 버튼 패딩 | 14px 28px |
| 버튼 간격 | 16px |
| 안내 카드 | `var(--bg-elevated)`, border-radius 18px, `var(--shadow-sm)` |
| 안내 카드 max-width | 520px |

#### 인터랙션
- **버튼:** Duolingo 눌림 (active 시 3px 하강)
- **캐릭터:** 섹션 진입 시 위에서 bounce 등장 (`translateY(-30px)` -> `0`, 이징으로 바운스)
- **OS 감지:** 현재 로직 유지 (감지된 OS 버튼을 primary로)

#### 변경점
- 배경: 그라디언트 -> 단색 `var(--accent-bg)`
- 버튼: ghost/primary -> Duolingo 눌림 스타일
- 캐릭터: 80px -> 100px
- 안내 카드: border -> shadow 기반

---

### 2-6. Comments 섹션 (네모에게 한마디!)

#### 현재 상태
- 가이드 태그 + 말풍선 + Giscus placeholder

#### 리뉴얼 방향: 미니멀 + 태그 pill화

#### CSS 스펙
| 속성 | 값 |
|------|-----|
| 섹션 배경 | `var(--bg-primary)` |
| 타이틀 | `var(--font-display)` = 48px |
| 태그 border-radius | `var(--radius-pill)` = 40px (pill화) |
| 태그 패딩 | 8px 20px |
| giscus 컨테이너 max-width | `var(--content-narrow)` = 720px |
| placeholder border-radius | 18px |

#### 인터랙션
- **태그:** pill 스타일, hover 시 배경 색상 전환
- **기존 구조 유지:** Giscus 연동 전까지 placeholder

#### 변경점
- 태그: 사각형 -> pill
- 전체적으로 radius 18px 통일
- 여백 확대

---

### 2-7. Footer

#### 현재 상태
- `var(--brown-900)` 배경, 캐릭터 + 소셜 링크 + 저작권

#### 리뉴얼 방향: Duolingo식 브랜드 컬러 풀 배경

#### 레이아웃
```
+==================================================+
|  (브랜드 컬러: 핑크 계열 배경)                      |
|                                                    |
|      [네모] "또 놀러 와~!"        NemoMate          |
|                                                    |
|      Instagram  ·  Twitter(X)  ·  GitHub            |
|                                                    |
|      (c) 2026 NemoMate. All rights reserved.       |
|                                                    |
+==================================================+
```

#### CSS 스펙
| 속성 | 값 |
|------|-----|
| 배경 | `var(--accent)` (핑크, 현재 `var(--brown-900)`) |
| 패딩 | 56px 0 40px |
| 텍스트 색상 | `var(--text-inverse)` (흰색) |
| 캐릭터 크기 | 48px (현재 40px -> 48px) |
| 캐릭터 filter | `brightness(1.3)` (밝게) |
| 말풍선 배경 | `rgba(255, 255, 255, 0.2)` |
| 말풍선 색상 | `var(--text-inverse)` |
| 링크 색상 | `rgba(255, 255, 255, 0.8)`, hover `var(--text-inverse)` |
| 저작권 색상 | `rgba(255, 255, 255, 0.6)` |
| GitHub 링크 | 신규 추가 |

#### 인터랙션
- **링크 hover:** underline 등장 (border-bottom 애니메이션)
- **캐릭터:** 가볍게 idle 애니메이션

#### 변경점
- 배경: `var(--brown-900)` 다크 브라운 -> `var(--accent)` 핑크
- GitHub 링크 추가
- 전체 톤: 어두운 -> 밝고 따뜻한 핑크

---

## 3. 글로벌 인터랙션/애니메이션

### 3-1. 통합 Reveal 시스템

현재 `.reveal` 클래스를 리뉴얼합니다.

```css
/* 기본 reveal */
.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity var(--dur-reveal) var(--ease-smooth),
              transform var(--dur-reveal) var(--ease-smooth);
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Stagger children */
.reveal-stagger > .reveal:nth-child(1) { transition-delay: 0s; }
.reveal-stagger > .reveal:nth-child(2) { transition-delay: var(--stagger-delay); }
.reveal-stagger > .reveal:nth-child(3) { transition-delay: calc(var(--stagger-delay) * 2); }
.reveal-stagger > .reveal:nth-child(4) { transition-delay: calc(var(--stagger-delay) * 3); }
.reveal-stagger > .reveal:nth-child(5) { transition-delay: calc(var(--stagger-delay) * 4); }
.reveal-stagger > .reveal:nth-child(6) { transition-delay: calc(var(--stagger-delay) * 5); }

/* 방향별 reveal */
.reveal-left {
  opacity: 0;
  transform: translateX(-40px);
  transition: opacity var(--dur-reveal) var(--ease-smooth),
              transform var(--dur-reveal) var(--ease-smooth);
}

.reveal-right {
  opacity: 0;
  transform: translateX(40px);
  transition: opacity var(--dur-reveal) var(--ease-smooth),
              transform var(--dur-reveal) var(--ease-smooth);
}

.reveal-left.visible,
.reveal-right.visible {
  opacity: 1;
  transform: translateX(0);
}
```

### 3-2. 통합 이징

모든 전환에 ctrl.xyz 이징을 기본으로 사용:

```
cubic-bezier(0.165, 0.84, 0.44, 1)
```

- 빠른 인터랙션 (버튼 active): 0.1s ease
- 일반 전환 (hover): 0.3s var(--ease-smooth)
- reveal 등장: 0.8s var(--ease-smooth)
- 헤더 show/hide: 0.5s var(--ease-smooth)

### 3-3. Reduced Motion 대응

```css
@media (prefers-reduced-motion: reduce) {
  .reveal, .reveal-left, .reveal-right {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

### 3-4. IntersectionObserver 개선

```js
// Layout.astro 스크립트 업그레이드
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target); // 한 번만 실행
    }
  });
}, {
  threshold: 0.15,
  rootMargin: '0px 0px -50px 0px'  // 약간 위로 올라와야 트리거
});

document.querySelectorAll('.reveal, .reveal-left, .reveal-right')
  .forEach(el => observer.observe(el));
```

### 3-5. 헤더 스크롤 Hide/Show

```js
let lastScrollY = 0;
const header = document.querySelector('.header');

window.addEventListener('scroll', () => {
  const currentScrollY = window.scrollY;
  if (currentScrollY > lastScrollY && currentScrollY > 100) {
    header.classList.add('header-hidden');
  } else {
    header.classList.remove('header-hidden');
  }
  lastScrollY = currentScrollY;
}, { passive: true });
```

```css
.header-hidden {
  transform: translateY(-100%);
}
```

---

## 4. 현재 대비 변경점 요약

### 토큰 변경

| 토큰 | 현재 | 리뉴얼 |
|------|------|--------|
| `--font-hero` | 48px / 32px(m) | 96px / 44px(m) |
| `--font-display` | 36px / 28px(m) | 48px / 32px(m) |
| `--font-title` | 24px / 20px(m) | 32px / 24px(m) |
| `--font-body` | 16px | 18px |
| `--section-gap` | 80px / 48px(m) | 120px / 72px(m) |
| `--content-max` | 1200px | 1100px |
| `--header-height` | 64px | 72px |

### 신규 토큰

| 토큰 | 값 | 용도 |
|------|-----|------|
| `--content-narrow` | 720px | 텍스트 중심 섹션 |
| `--radius-pill` | 40px | Pill 버튼/네비 |
| `--shadow-press` | `0 4px 0 var(--brown-700)` | Duolingo 눌림 |
| `--shadow-press-accent` | `0 4px 0 var(--pink-600)` | 눌림 (액센트) |
| `--ease-smooth` | `cubic-bezier(0.165, 0.84, 0.44, 1)` | 전역 이징 |
| `--dur-smooth` | 0.5s | 전환 시간 |
| `--dur-reveal` | 0.8s | Reveal 시간 |
| `--stagger-delay` | 0.15s | 순차 딜레이 |

### 컴포넌트 변경

| 컴포넌트 | 변경 내용 |
|----------|----------|
| Header | 중앙 pill 네비 + 스크롤 hide/show |
| Hero | 2컬럼 그리드, 방 배경 제거, 대형 타이포, 눌림 CTA |
| Features | 카드에 눌림 그림자, stagger 등장 |
| Highlights | 여백 확대 (64px -> 100px gap), reverse 방식 개선 |
| Gallery | radius 18px, shadow 추가, 스크롤 인디케이터 |
| Download | 단색 배경, 눌림 버튼 |
| Comments | 태그 pill화 |
| Footer | 배경 brown-900 -> accent (핑크) |

### 삭제 항목
- Hero 방 배경 이미지 (`room_lv3.png`)
- Hero 배경 그라디언트
- Download 배경 그라디언트
- Header `border-bottom`

---

## 5. 구현 우선순위 및 단계

### Phase 1: 토큰 & 기반 (소요: 1일)
> 모든 후속 작업의 기반. 여기서 시각적 임팩트의 70%가 결정됨.

1. **tokens.css 확장** -- 신규 토큰 추가, 기존 토큰 값 변경
2. **global.css 업데이트** -- reveal 시스템 리뉴얼, 이징 통합
3. **components.css 확장** -- `.btn-pill`, `.btn-press`, `.btn-press-accent` 추가
4. **Layout.astro** -- IntersectionObserver 개선, 방향별 reveal 지원

**완료 기준:** 토큰 변경만으로 전체 사이트의 타이포/여백이 업그레이드됨

### Phase 2: Hero + Header 리뉴얼 (소요: 1일)
> 첫 화면이 곧 첫인상. 가장 큰 체감 변화.

1. **Header.astro** -- pill 네비 구조 변경, 스크롤 hide/show 스크립트
2. **Hero.astro** -- 2컬럼 그리드, 대형 타이포, 방 배경 제거, 눌림 CTA
3. **Hero 등장 애니메이션** -- 타이틀 stagger + 캐릭터 슬라이드

**완료 기준:** 첫 화면(Hero + Header)이 ctrl.xyz + Duolingo 믹스 느낌

### Phase 3: 섹션별 리뉴얼 (소요: 1~2일)
> 나머지 섹션을 Phase 1 토큰 기반으로 업데이트.

1. **Features.astro** -- 카드 눌림 그림자, stagger 등장
2. **Highlights.astro** -- 여백 확대, reverse 방식 개선, 방향별 reveal
3. **Gallery.astro** -- radius/shadow 업그레이드, 스크롤 인디케이터
4. **Download.astro** -- 단색 배경, 눌림 버튼
5. **Comments.astro** -- 태그 pill화
6. **Footer.astro** -- 핑크 배경 전환

**완료 기준:** 전체 페이지 스크롤 시 일관된 리뉴얼 톤

### Phase 4: 콘텐츠 & 폴리시 (소요: 별도)
> 실제 에셋 준비 후 진행.

1. **스크린샷/GIF 촬영** -- Highlights placeholder 교체
2. **Gallery 실제 이미지** -- 6개 스크린샷 촬영 및 삽입
3. **Giscus 연동** -- Comments 섹션 실제 위젯 활성화
4. **OG 이미지** -- 소셜 공유용 이미지 제작
5. **성능 최적화** -- 이미지 lazy loading, font-display: swap 확인

**완료 기준:** placeholder 없는 완성된 랜딩 페이지

---

## 참고: 파일 변경 목록

| 파일 | 변경 유형 |
|------|----------|
| `src/styles/tokens.css` | 토큰 추가/수정 |
| `src/styles/global.css` | reveal 시스템 리뉴얼 |
| `src/styles/components.css` | btn-pill, btn-press 추가 |
| `src/layouts/Layout.astro` | IO 개선, header-height 반영 |
| `src/components/Header.astro` | pill 네비, 스크롤 hide/show |
| `src/components/Hero.astro` | 2컬럼, 대형 타이포, 눌림 CTA |
| `src/components/Features.astro` | stagger, 눌림 그림자 |
| `src/components/Highlights.astro` | 여백, reverse, reveal |
| `src/components/Gallery.astro` | radius, shadow, 인디케이터 |
| `src/components/Download.astro` | 단색 bg, 눌림 버튼 |
| `src/components/Comments.astro` | 태그 pill |
| `src/components/Footer.astro` | 핑크 배경 |
