// 중앙 집중형 멀티 블로그 & 수익화(광고/제휴) 설정 파일
// 나중에 광고 승인 번호나 제휴 링크만 이곳에 입력하면 사이트 전체에 자동 반영됩니다.

export const SITE_CONFIG = {
  title: '핀덱스 (FINDEX) · 금융·세무·AI 계산 포털',
  shortName: 'FINDEX',
  description: '핀덱스(FINDEX)는 2026년 최신 연봉 실수령액, 퇴직금·실업급여, 대출이자·DSR, 해외직구 관부가세, 배당 복리 및 AI 비용 계산기를 제공하는 데이터 포털입니다.',
  url: import.meta.env.PUBLIC_SITE_URL || 'https://findex-kr.github.io',
  lang: 'ko',
  author: 'FINDEX Research Lab',
  contactEmail: 'e.jang.soltec21@gmail.com',

  // 1. 검색엔진 소유권 확인 메타태그 (구글 서치콘솔 & 네이버 서치어드바이저 코드만 넣으면 자동 적용)
  verification: {
    google: import.meta.env.PUBLIC_GOOGLE_SITE_VERIFICATION || 'yqkhsOaN2L947vEwYzeg3zImGM7cowQ4TVskWb8PMKQ',
    naver: import.meta.env.PUBLIC_NAVER_SITE_VERIFICATION || 'a8a5a0f96b98c647edbad5299eef9e282e76169e',
  },

  // 2. 광고 네트워크 설정 (승인 후 ID만 넣으면 즉시 실제 광고 송출)
  ads: {
    // 구글 애드센스 게시자 ID (예: 'ca-pub-1234567890123456')
    googleAdSenseId: import.meta.env.PUBLIC_ADSENSE_ID || '',
    // 카카오 애드핏 (애드센스 승인 전 1개월 차 즉시 수익용, 3일 내 승인)
    kakaoAdFitUnitTop: import.meta.env.PUBLIC_ADFIT_TOP || '',
    kakaoAdFitUnitBottom: import.meta.env.PUBLIC_ADFIT_BOTTOM || '',
    // 실제 배포용: 광고 코드가 비어있을 때는 빈 회색 박스를 숨김 처리
    showPlaceholderWhenEmpty: false,
  },

  // 2. 제휴 마케팅 (Day-1 즉시 수익화 모듈: 쿠팡 파트너스 / 알리 / SaaS 추천)
  affiliates: {
    customs: [
      {
        badge: '직구 특가 비교',
        title: '해외직구 대신 로켓직구/국내 정발 최저가 확인하기',
        description: '관부가세와 배송대행비를 합치면 국내 로켓직구가 더 저렴할 수 있습니다. 오늘 기준 실시간 할인율과 무료반품 혜택을 비교해 보세요.',
        ctaText: '실시간 로켓직구 최저가 보기 →',
        url: 'https://www.coupang.com/',
        disclosure: '이 포스팅은 제휴 마케팅 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받을 수 있습니다.'
      }
    ],
    salary: [
      {
        badge: '직장인 필수 금융',
        title: '내 연봉 기준 최저금리 신용대출 & 파킹통장 금리 비교',
        description: '연봉 상승 및 이직 시즌에는 금리인하요구권과 고금리 파킹통장 갈아타기만으로도 연 수십만 원의 이자를 아낄 수 있습니다.',
        ctaText: '1분 금리 비교 & 우대혜택 확인 →',
        url: 'https://finlife.fss.or.kr/',
        disclosure: '제휴 및 금융 소비자 정보 안내 페이지로 연결됩니다.'
      }
    ],
    dividend: [
      {
        badge: '미국주식/ETF 혜택',
        title: '미국 배당주 ETF 매수 수수료 우대 & 환전 95% 우대 이벤트',
        description: 'SCHD, JEPI, QQQ 등 월배당 ETF 장기 투자 시 매매 수수료와 환전 스프레드가 복리 수익률을 결정합니다.',
        ctaText: '증권사별 수수료 혜택 비교하기 →',
        url: 'https://www.kofia.or.kr/',
        disclosure: '투자 판단의 책임은 본인에게 있으며 제휴 링크가 포함될 수 있습니다.'
      }
    ],
    ai: [
      {
        badge: 'AI 생산성 툴',
        title: 'ChatGPT Plus · Claude · 고성능 AI API 크레딧 혜택 안내',
        description: '매월 20달러 고정 구독료가 부담스럽다면 사용량 기반 API 연동이나 올인원 AI 워크스페이스로 비용을 70% 이상 절감하세요.',
        ctaText: 'AI 구독료 절감 가이드 및 툴 보기 →',
        url: '/tools/ai-cost-calculator/',
        disclosure: '이 링크는 파트너스 제휴 추천 링크를 포함할 수 있습니다.'
      }
    ]
  },

  // 3. 상단 네비게이션 메뉴
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
