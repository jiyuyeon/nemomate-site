// @ts-check
import { defineConfig } from 'astro/config';

// GitHub Pages 프로젝트 페이지로 배포한다.
// 주소가 https://jiyuyeon.github.io/nemomate-site/ 이므로
// site(도메인)와 base(하위 경로)를 함께 알려줘야 링크와 이미지 경로가 맞는다.
export default defineConfig({
  site: 'https://jiyuyeon.github.io',
  base: '/nemomate-site',
});
