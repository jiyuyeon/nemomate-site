# NemoMate 소개 사이트 — 기술 명세서

> 작성일: 2026-04-07
> 버전: v1.0

---

## 1. 기술 스택

### 프레임워크
| 항목 | 선택 | 이유 |
|------|------|------|
| **프레임워크** | Astro | 정적 사이트에 최적화, 빌드 후 순수 HTML/CSS/JS. React 경험 활용 가능 |
| **스타일링** | Vanilla CSS + CSS Variables | NemoMate 디자인 토큰 재활용, 별도 라이브러리 불필요 |
| **애니메이션** | CSS Animations + Intersection Observer | 스크롤 트리거 페이드인, 네모 캐릭터 모션 |
| **아이콘** | Lucide Icons (SVG) | 경량, 트리쉐이킹 지원 |
| **폰트** | Pretendard (한글) + 기존 A2Z 폰트 | 웹 최적화된 한글 폰트 |

### 왜 Astro인가?
- **제로 JS 기본값:** 정적 랜딩 페이지에 프레임워크 JS 번들 불필요
- **컴포넌트 재사용:** `.astro` 컴포넌트 또는 React 컴포넌트 혼용 가능
- **빌드 성능:** 빌드 결과물이 순수 HTML → 로딩 최고 속도
- **기존 경험:** 프로젝트가 React 기반이라 학습 곡선 낮음

### 대안 검토
| 대안 | 미선택 이유 |
|------|-----------|
| Next.js | SSR/ISR 불필요, 오버엔지니어링 |
| Vite + React SPA | 정적 콘텐츠에 SPA 불필요, SEO 불리 |
| 순수 HTML/CSS | 컴포넌트 재사용 어려움, 유지보수 비용 |
| Hugo/Jekyll | 마크다운 블로그 특화, 커스텀 레이아웃 자유도 낮음 |

---

## 2. 프로젝트 구조

```
landing/
├── docs/                    # 기획/설계 문서 (현재 디렉토리)
├── src/
│   ├── layouts/
│   │   └── Layout.astro     # 공통 레이아웃 (head, header, footer)
│   ├── components/
│   │   ├── Header.astro     # 고정 내비게이션
│   │   ├── Hero.astro       # 히어로 섹션
│   │   ├── Features.astro   # 핵심 가치 카드
│   │   ├── Highlights.astro # 기능 하이라이트 (좌우 교차)
│   │   ├── Gallery.astro    # 스크린샷 갤러리
│   │   ├── Download.astro   # 다운로드 섹션
│   │   ├── Comments.astro   # 응원 보내기 (Giscus 댓글)
│   │   └── Footer.astro     # 푸터
│   ├── styles/
│   │   ├── tokens.css       # 디자인 토큰 (poc에서 이식)
│   │   ├── global.css       # 전역 스타일
│   │   └── sections.css     # 섹션별 스타일
│   ├── assets/
│   │   ├── images/          # 최적화된 이미지 에셋
│   │   ├── screenshots/     # 게임 스크린샷
│   │   └── fonts/           # 웹폰트
│   └── pages/
│       └── index.astro      # 메인 (유일한) 페이지
├── public/
│   ├── favicon.ico
│   ├── og-image.png
│   └── downloads/           # (선택) 직접 호스팅 시 베타 파일
├── astro.config.mjs
├── package.json
└── tsconfig.json
```

---

## 3. 다운로드 구현

### 방식: GitHub Releases 연동

베타 파일을 GitHub Releases에 업로드하고, 사이트에서 최신 릴리즈의 다운로드 URL로 리다이렉트한다.

#### 구현 방법

**방법 A: 정적 링크 (추천 — MVP)**
```html
<!-- 릴리즈 URL을 직접 하드코딩 -->
<a href="https://github.com/{owner}/{repo}/releases/download/v0.1.0/NemoMate-0.1.0.dmg"
   class="btn-download btn-mac">
  macOS 다운로드
</a>
<a href="https://github.com/{owner}/{repo}/releases/download/v0.1.0/NemoMate-0.1.0-setup.exe"
   class="btn-download btn-win">
  Windows 다운로드
</a>
```
- 장점: 심플, 외부 API 불필요
- 단점: 새 버전 릴리즈 시 사이트 재배포 필요

**방법 B: GitHub API 자동 감지 (확장)**
```javascript
// 빌드 시 최신 릴리즈 URL을 가져와 정적으로 주입
const res = await fetch('https://api.github.com/repos/{owner}/{repo}/releases/latest');
const release = await res.json();
const macAsset = release.assets.find(a => a.name.endsWith('.dmg'));
const winAsset = release.assets.find(a => a.name.endsWith('.exe'));
```
- 장점: 릴리즈만 올리면 사이트 자동 반영 (빌드 트리거 필요)
- 단점: 초기 구현 비용 약간 높음

### OS 자동 감지
```javascript
// 방문자 OS를 감지하여 적합한 다운로드 버튼 강조
const isMac = navigator.platform.toUpperCase().includes('MAC');
const primaryBtn = isMac ? '.btn-mac' : '.btn-win';
document.querySelector(primaryBtn).classList.add('primary');
```

### 모바일 다운로드 대응
```javascript
// 모바일 방문자에게는 다운로드 버튼 대신 PC 유도 안내 표시
const isMobile = /iPhone|iPad|Android/i.test(navigator.userAgent);
if (isMobile) {
  document.querySelector('.download-buttons').style.display = 'none';
  document.querySelector('.mobile-notice').style.display = 'block';
}
```
모바일 안내 문구: "네모메이트는 데스크톱 앱이에요! PC에서 다시 방문해주세요 :)"

---

## 3-1. 댓글 시스템 (응원 보내기)

### 방식: Giscus (GitHub Discussions 기반)

Giscus는 GitHub Discussions를 백엔드로 사용하는 오픈소스 댓글 위젯이다. 별도 서버 없이 정적 사이트에 즉시 연동 가능하다.

#### 설정
1. GitHub repo에서 Discussions 기능 활성화
2. `giscus.app`에서 repo 연결 및 설정 생성
3. Astro 컴포넌트에 스크립트 삽입

```html
<script src="https://giscus.app/client.js"
  data-repo="{owner}/{repo}"
  data-repo-id="{repo-id}"
  data-category="응원 보내기"
  data-category-id="{category-id}"
  data-mapping="specific"
  data-term="landing-comments"
  data-theme="custom"
  data-theme-url="/giscus-theme.css"
  data-lang="ko"
  crossorigin="anonymous"
  async>
</script>
```

#### 커스텀 테마
- Giscus는 커스텀 CSS 테마를 지원 → NemoMate 브라운 톤에 맞춘 `giscus-theme.css` 제작
- `public/giscus-theme.css`에 배치

#### 커스텀 테마 작성 (구현 시 TODO)
- `public/giscus-theme.css` 파일 작성
- 주요 변수: `--color-canvas-default: #fdfaef`, `--color-border-default: #E8D5B8`, `--color-fg-default: #5C4033` 등 NemoMate 토큰에 맞춰 매핑
- Giscus 테마 변수 목록은 giscus.app 공식 문서 참조

#### 제한사항
- 댓글 작성 시 GitHub 로그인 필요 → 비개발자 접근성 낮음
- 대안: GitHub 로그인 없이 사용 가능한 자체 폼 + Google Sheets 방식을 폴백으로 준비

---

## 4. 호스팅 & 배포

### 추천: GitHub Pages

| 항목 | 설정 |
|------|------|
| **호스팅** | GitHub Pages (무료) |
| **빌드** | GitHub Actions → `astro build` → deploy |
| **도메인** | `{username}.github.io/nemomate` (기본) 또는 커스텀 도메인 |
| **SSL** | GitHub Pages 자동 제공 |
| **CDN** | GitHub Pages 내장 CDN |

### GitHub Actions 워크플로우
```yaml
# .github/workflows/deploy.yml
name: Deploy Landing Site
on:
  push:
    branches: [main]
    paths: ['landing/**']

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - name: Install & Build
        working-directory: landing
        run: |
          npm install
          npm run build
      - uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: landing/dist
```

### 대안
| 대안 | 장단점 |
|------|--------|
| Vercel | 자동 배포 편리, 무료 티어 충분. 단 GitHub Pages보다 설정 한 단계 더 |
| Netlify | Vercel과 유사. 폼 처리 내장 (문의 폼 사용 시 유리) |
| Cloudflare Pages | 속도 최고, 무료. 설정 약간 복잡 |

---

## 5. 성능 최적화

### 이미지
- **형식:** WebP 우선, PNG 폴백 (`<picture>` 태그)
- **크기:** Hero 이미지 max 200KB, 스크린샷 각 100KB 이내
- **로딩:** 스크린샷 갤러리는 `loading="lazy"`
- **스프라이트 변환:** 기존 PNG 에셋 → WebP 변환 (빌드 시 자동)

### 폰트
- **서브셋:** 한글 폰트는 사용 글리프만 서브셋팅
- **로딩:** `font-display: swap` (FOUT 허용, FOIT 방지)
- **프리로드:** Hero에 사용되는 폰트 1종만 preload

### 기타
- **CSS:** 인라인 크리티컬 CSS (Astro 기본 지원)
- **JS:** 최소화 — 스크롤 애니메이션 + OS 감지 정도만
- **목표:** Lighthouse 95+ (Performance, Accessibility, SEO)

---

## 6. SEO

- 시맨틱 HTML (`<header>`, `<main>`, `<section>`, `<footer>`)
- Open Graph + Twitter Card 메타태그
- `robots.txt` + `sitemap.xml` (Astro 내장 플러그인)
- 구조화된 데이터 (SoftwareApplication schema)

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "NemoMate",
  "operatingSystem": ["macOS", "Windows"],
  "applicationCategory": "GameApplication",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "KRW"
  }
}
```

---

## 7. 분석 (Analytics)

- **추천:** Plausible 또는 Umami (프라이버시 친화적, 경량)
- **추적 이벤트:**
  - 페이지 뷰
  - 다운로드 버튼 클릭 (macOS / Windows 구분)
  - 섹션 도달률 (Intersection Observer)
  - 외부 링크 클릭 (SNS 등)
