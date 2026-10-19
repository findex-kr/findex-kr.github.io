import { defineConfig } from 'astro/config';

export default defineConfig({
  site: process.env.PUBLIC_SITE_URL || 'https://findex-kr.github.io',
  build: {
    format: 'directory'
  }
});
