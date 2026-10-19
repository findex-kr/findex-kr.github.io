// 중앙 집중형 멀티 블로그 & 수익화(광고/제휴) 설정 파일
// 구글 애드센스 및 쿠팡 파트너스 실제 수익 코드가 연동된 상태입니다.

export const SITE_CONFIG = {
  title: '핀덱스 (FINDEX) · 금융·세무·AI 계산 포털',
  shortName: 'FINDEX',
  description: '핀덱스(FINDEX)는 2026년 최신 연봉 실수령액, 퇴직금·실업급여, 대출이자·DSR, 해외직구 관부가세, 배당 복리 및 AI 비용 계산기를 제공하는 데이터 포털입니다.',
  url: import.meta.env.PUBLIC_SITE_URL || 'https://findex-kr.github.io',
  lang: 'ko',
  author: 'FINDEX Research Lab',
  contactEmail: 'e.jang.soltec21@gmail.com',

  // 1. 검색엔진 소유권 확인 메타태그 (구글 서치콘솔 & 네이버 서치어드바이저)
  verification: {
    google: import.meta.env.PUBLIC_GOOGLE_SITE_VERIFICATION || 'yqkhsOaN2L947vEwYzeg3zImGM7cowQ4TVskWb8PMKQ',
    naver: import.meta.env.PUBLIC_NAVER_SITE_VERIFICATION || 'a8a5a0f96b98c647edbad5299eef9e282e76169e',
  },

  // 2. 광고 네트워크 설정 (구글 애드센스 실제 게시자 ID 연동 완료)
  ads: {
    googleAdSenseId: import.meta.env.PUBLIC_ADSENSE_ID || 'ca-pub-3663569229526025',
    kakaoAdFitUnitTop: import.meta.env.PUBLIC_ADFIT_TOP || '',
    kakaoAdFitUnitBottom: import.meta.env.PUBLIC_ADFIT_BOTTOM || '',
    showPlaceholderWhenEmpty: false,
  },

  // 3. 제휴 마케팅 (쿠팡 파트너스 실제 수익 링크 연동 완료)
  affiliates: {
    customs: [
      {
        badge: '직구 vs 로켓직구 특가',
        title: '해외직구 대신 쿠팡 로켓직구·국내 정발 최저가 비교하기',
        description: '관부가세와 해외 배송대행비를 합치면 국내 로켓배송·로켓직구가 더 저렴할 수 있습니다. 오늘 기준 실시간 특가와 무료반품 혜택을 확인해 보세요.',
        ctaText: '쿠팡 실시간 특가 & 할인 혜택 보기 →',
        url: 'https://link.coupang.com/a/hZcG58ptNA',
        disclosure: '이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다.'
      }
    ],
    salary: [
      {
        badge: '직장인 스마트 소비',
        title: '월급날 직장인 필수 생활용품 · 가전 · 자기계발 특가전',
        description: '고물가 시대 고정 지출을 줄여주는 로켓와우 초특가 생필품과 업무 생산성을 높이는 데스크테리어 인기 상품을 한눈에 확인하세요.',
        ctaText: '직장인 베스트 특가 상품 확인하기 →',
        url: 'https://link.coupang.com/a/hZcG58ptNA',
        disclosure: '이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다.'
      }
    ],
    dividend: [
      {
        badge: '재테크 · 경제 필독서 & 장비',
        title: '배당주 · ETF 투자자를 위한 베스트셀러 & 스마트 기기 특가',
        description: '성공적인 장기 복리 투자를 돕는 재테크 필독서와 실시간 시세 확인용 태블릿·모니터 특가 혜택을 확인해 보세요.',
        ctaText: '오늘의 특가 및 추천 혜택 보기 →',
        url: 'https://link.coupang.com/a/hZcG58ptNA',
        disclosure: '이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다.'
      }
    ],
    ai: [
      {
        badge: 'AI · IT 생산성 장비',
        title: 'AI 업무 효율 200% 높이는 고성능 노트북 · 모니터 · 키보드 특가',
        description: '클로드·챗GPT 코딩과 멀티태스킹에 최적화된 맥북, 울트라와이드 모니터, 기계식 키보드 실시간 할인율을 확인하세요.',
        ctaText: 'IT · 디지털 실시간 할인 혜택 보기 →',
        url: 'https://link.coupang.com/a/hZcG58ptNA',
        disclosure: '이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다.'
      }
    ]
  },

  // 4. 상단 네비게이션 메뉴
  navLinks: [
    { label: '홈', href: '/' },
    { label: '관부가세', href: '/tools/customs-calculator/' },
    { label: '연봉 실수령', href: '/tools/salary-calculator/' },
    { label: '퇴직금', href: '/tools/severance-calculator/' },
    { label: '대출이자', href: '/tools/loan-calculator/' },
    { label: '배당 복리', href: '/tools/dividend-calculator/' },
    { label: 'AI 구독비교', href: '/tools/ai-cost-calculator/' },
    { label: '가이드(블로그)', href: '/blog/' },
  ]
};
