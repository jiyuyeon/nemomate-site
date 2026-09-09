# NemoMate 소개 사이트 — 디자인 가이드

> 작성일: 2026-04-07
> 버전: v1.0

---

## 1. 디자인 원칙

1. **따뜻함:** NemoMate의 양모인형 질감, 브라운 톤을 웹에서도 유지
2. **심플함:** 과한 장식 없이, 네모와 콘텐츠가 주인공
3. **일관성:** 게임 내 디자인 시스템과 동일한 토큰 사용
4. **접근성:** 충분한 명도 대비, 읽기 쉬운 폰트 크기

---

## 2. 컬러 팔레트

게임 디자인 토큰(`poc/src/styles/tokens.css`)을 기반으로 웹에 맞게 확장한다.

### 브랜드 컬러
| 토큰 | 값 | 용도 |
|------|-----|------|
| `--brown-900` | `#3A2518` | 텍스트 강조, 헤더 |
| `--brown-700` | `#5C4033` | 본문 텍스트, 테두리 |
| `--brown-500` | `#A0896E` | 보조 텍스트 |
| `--brown-400` | `#C4B49E` | 스크롤바, 비활성 요소 |
| `--brown-300` | `#E8D5B8` | 카드 배경, 구분선 |
| `--brown-200` | `#EDE4D4` | 섹션 교차 배경 |
| `--brown-100` | `#F5EDE0` | 밝은 섹션 배경 |
| `--brown-50` | `#fdfaef` | 페이지 기본 배경 |

### 액센트 컬러
| 토큰 | 값 | 용도 |
|------|-----|------|
| `--pink-500` | `#D4A0D0` | CTA 버튼, 액센트 |
| `--pink-600` | `#C490C0` | CTA 호버 |
| `--pink-300` | `rgba(212,160,208,0.3)` | 배지, 하이라이트 배경 |

### 시맨틱 컬러 (웹 확장)
| 토큰 | 값 | 용도 |
|------|-----|------|
| `--web-bg-primary` | `#fdfaef` | 페이지 배경 (=brown-50) |
| `--web-bg-alt` | `#F5EDE0` | 교차 섹션 배경 (=brown-100) |
| `--web-bg-card` | `#ffffff` | 카드 배경 |
| `--web-text-heading` | `#3A2518` | 제목 (=brown-900) |
| `--web-text-body` | `#5C4033` | 본문 (=brown-700) |
| `--web-text-caption` | `#A0896E` | 캡션, 부가 정보 (=brown-500) |

### 배경 패턴
- 섹션 간 구분: `--web-bg-primary`와 `--web-bg-alt`를 교차 사용
- Hero 섹션: 그라디언트 `linear-gradient(180deg, #fdfaef 0%, #F5EDE0 100%)`
- 다운로드 섹션: 액센트 배경 `--pink-300` 위에 화이트 카드

---

## 3. 타이포그래피

### 폰트 스택

| 용도 | 폰트 | 비고 |
|------|------|------|
| **제목 (H1~H3)** | Pretendard Bold (700) | 웹 최적화 한글 폰트 |
| **본문** | Pretendard Regular (400) | |
| **네모 대사** | 게임 폰트 또는 손글씨 폰트 | 말풍선 안에서만 사용 |
| **코드/버전** | monospace (시스템) | 버전 번호, 시스템 요구사항 |

> **참고:** 게임 내 Mona12 픽셀 폰트는 작은 크기에 최적화되어 있어, 웹에서는 Pretendard를 메인으로 사용한다. 네모 대사 말풍선에서만 게임 느낌을 살리기 위해 Mona12 또는 유사 폰트를 제한적으로 사용한다.

### 크기 체계 (웹용)

| 레벨 | 크기 | 행간 | 용도 |
|------|------|------|------|
| `--web-text-hero` | 48px | 1.2 | Hero 메인 카피 |
| `--web-text-h1` | 36px | 1.3 | 섹션 제목 |
| `--web-text-h2` | 24px | 1.4 | 기능 제목 |
| `--web-text-h3` | 20px | 1.4 | 카드 제목 |
| `--web-text-body` | 16px | 1.6 | 본문 |
| `--web-text-caption` | 14px | 1.5 | 캡션, 부가 정보 |
| `--web-text-small` | 12px | 1.5 | 버전, 법적 고지 |

### 모바일 크기 조정
| 레벨 | 데스크톱 | 모바일 (≤768px) |
|------|---------|-----------------|
| Hero | 48px | 32px |
| H1 | 36px | 28px |
| H2 | 24px | 20px |
| Body | 16px | 16px (유지) |

---

## 4. 레이아웃

### 그리드 시스템
- **최대 너비:** 1200px (콘텐츠 영역)
- **좌우 패딩:** 데스크톱 40px, 태블릿 24px, 모바일 16px
- **섹션 간격:** 80px (데스크톱), 48px (모바일)
- **카드 그리드:** 4열 (데스크톱) → 2열 (태블릿) → 1열 (모바일)

### 섹션별 레이아웃

```
┌─────────────────────────────────────────────┐
│                  HEADER                      │  고정, 높이 64px
├─────────────────────────────────────────────┤
│                                              │
│          [네모 캐릭터]                        │  Hero: 중앙 정렬
│     메인 카피 (48px, bold)                    │  높이: 100vh
│     서브 카피 (16px)                         │
│     [CTA 버튼]                               │
│                                              │
├─────────────────────────────────────────────┤
│  소개: 4개 카드 가로 배치                     │  bg: --web-bg-alt
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐                │
│  │ 🏠 │ │ 🎮 │ │ 💬 │ │ ❤️ │                │
│  └────┘ └────┘ └────┘ └────┘                │
├─────────────────────────────────────────────┤
│  기능 하이라이트: 좌우 교차                   │  bg: --web-bg-primary
│  [이미지]  [텍스트]                           │
│  [텍스트]  [이미지]                           │
│  [이미지]  [텍스트]                           │
├─────────────────────────────────────────────┤
│  스크린샷: 캐러셀 or 그리드                   │  bg: --web-bg-alt
├─────────────────────────────────────────────┤
│  다운로드: 중앙 정렬                          │  bg: 액센트 그라디언트
│  [macOS 버튼]  [Windows 버튼]                │
├─────────────────────────────────────────────┤
│  응원 보내기: 댓글 위젯                       │  bg: --web-bg-primary
│  [태그: 응원 / 버그 / 아이디어]              │
│  [Giscus 댓글 영역]                          │
├─────────────────────────────────────────────┤
│  FOOTER                                      │  bg: --brown-900
└─────────────────────────────────────────────┘
```

---

## 5. 컴포넌트 스타일

### 버튼

#### CTA 버튼 (다운로드)
```css
.btn-cta {
  background: var(--pink-500);
  color: white;
  padding: 16px 32px;
  border-radius: 12px;
  font-size: 18px;
  font-weight: 700;
  border: 2px solid var(--brown-700);
  box-shadow: 0 4px 0 var(--brown-700);  /* 게임 느낌의 입체 그림자 */
  transition: transform 0.15s, box-shadow 0.15s;
}
.btn-cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 0 var(--brown-700);
}
.btn-cta:active {
  transform: translateY(2px);
  box-shadow: 0 2px 0 var(--brown-700);
}
```

#### OS 다운로드 버튼
```css
.btn-download {
  background: white;
  color: var(--brown-700);
  padding: 14px 28px;
  border-radius: 10px;
  border: 2px solid var(--brown-300);
  display: flex;
  align-items: center;
  gap: 8px;
}
.btn-download.primary {
  background: var(--pink-500);
  color: white;
  border-color: var(--brown-700);
}
```

### 카드
```css
.feature-card {
  background: var(--web-bg-card);
  border: 2px solid var(--brown-300);
  border-radius: 16px;
  padding: 24px;
  text-align: center;
  transition: transform 0.2s;
}
.feature-card:hover {
  transform: translateY(-4px);
}
```

### 네모 말풍선
```css
.nemo-bubble {
  background: white;
  border: 2px solid var(--brown-700);
  border-radius: 16px 16px 16px 4px;
  padding: 8px 16px;
  font-family: "Mona12", sans-serif;
  font-size: 14px;
  color: var(--brown-700);
  position: relative;
  display: inline-block;
}
```

### 헤더
```css
.header {
  position: fixed;
  top: 0;
  width: 100%;
  height: 64px;
  background: rgba(253, 250, 239, 0.9);  /* brown-50 + 투명도 */
  backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--brown-300);
  z-index: 100;
}
```

### 가이드 태그
```css
.guide-tag {
  display: inline-block;
  padding: 6px 14px;
  border-radius: 20px;
  border: 2px solid var(--brown-300);
  background: var(--web-bg-card);
  color: var(--brown-700);
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.15s;
}
.guide-tag:hover,
.guide-tag.active {
  background: var(--pink-500);
  color: white;
  border-color: var(--brown-700);
}
```

### 갤러리 캐러셀
```css
.gallery-track {
  display: flex;
  gap: 16px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  -webkit-overflow-scrolling: touch;
  padding: 8px 0;
}
.gallery-item {
  flex: 0 0 auto;
  width: 320px;
  border-radius: 12px;
  border: 2px solid var(--brown-300);
  overflow: hidden;
  scroll-snap-align: center;
  transition: transform 0.2s;
}
.gallery-item:hover {
  transform: scale(1.03);
}
/* 스크롤바 커스텀 */
.gallery-track::-webkit-scrollbar { height: 6px; }
.gallery-track::-webkit-scrollbar-thumb {
  background: var(--brown-400);
  border-radius: 3px;
}
```

### 햄버거 메뉴 (모바일)
```css
.hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  padding: 8px;
}
.hamburger span {
  width: 24px;
  height: 2px;
  background: var(--brown-700);
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s;
}
.hamburger.open span:nth-child(1) { transform: rotate(45deg) translate(5px, 5px); }
.hamburger.open span:nth-child(2) { opacity: 0; }
.hamburger.open span:nth-child(3) { transform: rotate(-45deg) translate(5px, -5px); }

@media (max-width: 767px) {
  .hamburger { display: flex; }
  .nav-links {
    position: absolute;
    top: 64px;
    left: 0;
    right: 0;
    background: rgba(253, 250, 239, 0.98);
    backdrop-filter: blur(8px);
    flex-direction: column;
    padding: 16px;
    border-bottom: 1px solid var(--brown-300);
    display: none;
  }
  .nav-links.open { display: flex; }
}
```

### 모바일 다운로드 안내
```css
.mobile-notice {
  display: none;
  text-align: center;
  padding: 24px;
  background: var(--web-bg-card);
  border: 2px solid var(--brown-300);
  border-radius: 16px;
  color: var(--brown-700);
  font-size: 16px;
  line-height: 1.6;
}
```

---

## 6. 애니메이션

### 스크롤 등장 (Fade-in Up)
```css
.reveal {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

### 네모 캐릭터 모션
```css
/* idle: 좌우 살짝 흔들림 */
@keyframes nemo-idle {
  0%, 100% { transform: rotate(-2deg); }
  50% { transform: rotate(2deg); }
}
.nemo-character {
  animation: nemo-idle 3s ease-in-out infinite;
}

/* hover: 점프 */
.nemo-character:hover {
  animation: nemo-jump 0.4s ease;
}
@keyframes nemo-jump {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-12px); }
}
```

### CTA 버튼 펄스
```css
@keyframes pulse-glow {
  0%, 100% { box-shadow: 0 4px 0 var(--brown-700), 0 0 0 0 rgba(212, 160, 208, 0.4); }
  50% { box-shadow: 0 4px 0 var(--brown-700), 0 0 0 8px rgba(212, 160, 208, 0); }
}
.btn-cta { animation: pulse-glow 2s ease-in-out infinite; }
```

---

## 7. 반응형 브레이크포인트

| 이름 | 범위 | 레이아웃 변화 |
|------|------|-------------|
| **Desktop** | ≥1024px | 기본 레이아웃 |
| **Tablet** | 768~1023px | 카드 2열, 좌우교차 → 세로 스택 |
| **Mobile** | ≤767px | 카드 1열, Hero 텍스트 축소, 햄버거 메뉴 |

### 모바일 주요 변경사항
- 헤더: 내비게이션 → 햄버거 메뉴
- Hero: 텍스트 위, 네모 캐릭터 아래 (세로 배치)
- 기능 하이라이트: 이미지 상단, 텍스트 하단
- 다운로드 버튼: 세로 스택 (macOS 위, Windows 아래)
- 갤러리: 가로 스크롤 유지

---

## 8. 접근성 (a11y)

- **명도 대비:** WCAG AA 기준 (4.5:1 이상) — brown-700 on brown-50 = 7.2:1 (통과)
- **포커스 표시:** `:focus-visible` 아웃라인 (pink-500 컬러)
- **키보드 내비게이션:** 모든 인터랙티브 요소 탭 이동 가능
- **alt 텍스트:** 모든 이미지에 의미 있는 대체 텍스트
- **모션 감소:** `prefers-reduced-motion` 시 애니메이션 비활성화
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```
