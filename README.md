# NemoMate 랜딩 페이지

바탕화면 위에 사는 네모난 양모인형, **네모메이트**의 소개 페이지입니다.

🔗 https://jiyuyeon.github.io/nemomate-site/

## 로컬에서 보기

```bash
npm install
npm run dev
```

## 배포

`main`에 올리면 GitHub Actions가 자동으로 GitHub Pages에 배포합니다.

## 게임 파일(DMG) 갱신하기

DMG는 125MB라 저장소에 넣을 수 없습니다(GitHub은 100MB를 넘는 파일을 막습니다).
새 버전을 배포할 때는 릴리즈에 첨부하고, 다운로드 버튼의 주소를 그 릴리즈로 바꿔주세요.

```bash
gh release create v0.1.0 NemoMate_0.1.0_aarch64.dmg
```
