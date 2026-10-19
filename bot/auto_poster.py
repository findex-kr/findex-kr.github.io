#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auto Income Factory - Automated SEO Blog Post Generator & Evergreen Updater
- Runs daily at 06:00 AM KST via GitHub Actions
- Publishes new high-CPC posts from bot/topics_pool.json
- If all preset topics are published, automatically generates programmatic long-tail SEO guides
  (e.g., specific salary brackets, loan amounts, dividend targets) so it NEVER runs out of content!
"""

import argparse
import datetime
import json
import os
import sys
import urllib.request
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
TOPICS_FILE = ROOT_DIR / "bot" / "topics_pool.json"
HISTORY_FILE = ROOT_DIR / "bot" / "history.json"
BLOG_DIR = ROOT_DIR / "src" / "content" / "blog"

TOOL_URLS = {
    "customs": ("해외직구 관부가세 자동 계산기", "/tools/customs-calculator/"),
    "salary": ("2026 연봉 실수령액 자동 계산기", "/tools/salary-calculator/"),
    "severance": ("2026 퇴직금 & 실업급여 통합 계산기", "/tools/severance-calculator/"),
    "loan": ("2026 대출 이자 & 스트레스 DSR 3단계 계산기", "/tools/loan-calculator/"),
    "dividend": ("배당주 & ETF 복리 시뮬레이터", "/tools/dividend-calculator/"),
    "ai": ("2026 AI 구독료 vs API 가성비 비교 계산기", "/tools/ai-cost-calculator/"),
}


def load_json(path: Path, default):
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default


def save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def generate_programmatic_topic(published_slugs: set) -> dict:
    """Generates endless long-tail high-CPC topics when topics_pool.json is exhausted."""
    # 1. 연봉 구간별 실수령액 시리즈 (3200만원 ~ 1억 5000만원)
    for sal in range(3200, 15500, 300):
        slug = f"salary-{sal}-man-won-net-pay-2026-analysis"
        if slug not in published_slugs:
            monthly_gross = round(sal / 12, 1)
            return {
                "slug": slug,
                "title": f"2026 연봉 {sal:,}만원 실수령액 상세 분석 (4대보험 9.72%·비과세 식대 20만원 반영)",
                "description": f"세전 연봉 {sal:,}만 원(월 환산 약 {monthly_gross}만 원) 직장인의 2026년 국민연금(4.75%)·건강보험(3.595%)·소득세 공제 후 실제 통장 입금액과 절세 전략을 계산합니다.",
                "category": "finance",
                "relatedTool": "salary",
                "tags": [f"연봉{sal}만원", "2026실수령액", "4대보험공제", "비과세식대", "월급계산"],
                "keyPoints": [
                    f"연봉 {sal:,}만 원의 세전 월급(약 {monthly_gross}만 원)에서 빠져나가는 2026년 4대 보험 및 소득세 상세 내역",
                    "비과세 식대 월 20만 원 포함 여부에 따라 달라지는 연간 실수령액 차이 비교",
                    "연말정산 연금저축·IRP 세액공제로 13월의 월급 환급액을 극대화하는 방법"
                ]
            }

    # 2. 대출 금액별 원리금 vs 원금균등 비교 시리즈 (1억 ~ 9억)
    for eok in range(1, 10):
        slug = f"mortgage-{eok}00-million-interest-and-dsr-comparison"
        if slug not in published_slugs:
            return {
                "slug": slug,
                "title": f"주택담보대출 {eok}억 원 월 상환액 및 원리금균등 vs 원금균등 총 이자 차이 (2026 DSR 3단계)",
                "description": f"대출 원금 {eok}억 원을 30년 만기로 빌릴 때 금리 구간별(3.5%~5.0%) 매달 내야 하는 원리금과 스트레스 DSR 3단계(+1.5% 가산금리) 한도 기준을 분석합니다.",
                "category": "finance",
                "relatedTool": "loan",
                "tags": [f"대출{eok}억이자", "주택담보대출", "원금균등상환", "스트레스DSR3단계", "월상환액"],
                "keyPoints": [
                    f"대출 {eok}억 원 실행 시 원금균등상환 선택으로 아낄 수 있는 수천만 원의 총 이자 절감액",
                    "2026 스트레스 DSR 3단계(+1.50%) 적용 시 필요한 최소 연봉 기준과 한도 계산",
                    "3년 후 중도상환수수료 면제 시점에 원금 일부 상환 시 월 납입금 감소 효과"
                ]
            }

    # 3. 기본 날짜 기반 트렌드 리포트
    today_tag = datetime.date.today().strftime("%Y%m%d")
    return {
        "slug": f"financial-and-tax-saving-briefing-{today_tag}",
        "title": f"{datetime.date.today().strftime('%Y년 %m월 %d일')} 기준 직장인 필수 절세 · 금융 · 직구 핵심 체크리스트",
        "description": "최신 4대 보험 요율, 비과세 계좌(ISA·IRP) 한도, 해외직구 면세 기준 및 AI 구독 비용 최적화 포인트를 한눈에 점검합니다.",
        "category": "finance",
        "relatedTool": "salary",
        "tags": ["절세체크리스트", "연봉실수령액", "중개형ISA", "해외직구면세"],
        "keyPoints": [
            "내 월급과 투자 수익에서 새어나가는 세금(소득세·배당세·관부가세)을 막는 3단계 점검표",
            "웹 계산기를 활용해 대출 이자와 고정 구독료를 매월 10만 원 이상 줄이는 실전 방법",
            "아낀 고정비를 월배당 ETF에 복리 재투자했을 때 만들어지는 현금흐름 시뮬레이션"
        ]
    }


def generate_with_gemini(topic: dict, api_key: str) -> str:
    """Calls Gemini REST API to write a comprehensive Korean SEO guide."""
    tool_name, tool_url = TOOL_URLS.get(topic["relatedTool"], TOOL_URLS["salary"])
    prompt = f"""당신은 대한민국 최고의 금융·세무·IT 전문 에디터입니다.
다음 주제로 검색엔진(구글, 네이버) 상위 노출에 최적화된 전문 가이드를 마크다운(Markdown) 본문 형식으로 작성하세요.
(YAML frontmatter는 제외하고 본문만 출력하세요.)

- 제목: {topic['title']}
- 설명: {topic['description']}
- 필수 포함 핵심 내용: {', '.join(topic['keyPoints'])}
- 내부 링크 유도: 본문 중간과 결론에 자연스럽게 [{tool_name}]({tool_url}) 링크를 포함하세요.

작성 규칙:
1. H2(##), H3(###) 소제목을 명확히 구분하세요.
2. 반드시 비교 표(Markdown Table)를 1개 이상 포함하세요.
3. 독자가 바로 실행할 수 있는 체크리스트와 구체적인 수치 예시를 포함하세요.
4. 분량은 공백 포함 1,800자 이상으로 깊이 있게 작성하세요.
"""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={api_key}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.65}
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        return result["candidates"][0]["content"]["parts"][0]["text"].strip()


def generate_structured_article(topic: dict) -> str:
    """Generates a rich, structured SEO article without external API dependency."""
    tool_name, tool_url = TOOL_URLS.get(topic["relatedTool"], TOOL_URLS["salary"])
    points = topic.get("keyPoints", [])

    body = f"""{topic['description']}

2026년 최신 개정 세법과 공시 요율을 바탕으로 가장 많이 헷갈려 하시는 핵심 기준과 손해를 보지 않기 위한 실전 계산 방법을 단계별로 정리해 드립니다.

## 1. 핵심 요약 및 반드시 알아야 할 3가지 포인트

바쁜 분들을 위해 가장 중요한 핵심 기준 3가지를 먼저 요약합니다.

1. **{points[0] if len(points) > 0 else '2026 최신 법령 및 요율 기준 확인'}**
2. **{points[1] if len(points) > 1 else '조건별 실전 수치 및 세후 차액 비교'}**
3. **{points[2] if len(points) > 2 else '비용 절감 및 절세 체크리스트 실행'}**

> **실전 팁:** 복잡한 수식을 직접 계산할 필요 없이 핀덱스(FINDEX)의 **[{tool_name}]({tool_url})**를 활용하시면 내 조건에 맞는 정확한 금액을 1초 만에 시뮬레이션할 수 있습니다.

## 2. 조건별 상세 비교표 (한눈에 보는 손익 분석)

선택하는 방식과 비과세·우대 요건 적용 여부에 따라 실제 발생하는 비용과 절감 효과를 비교한 표입니다.

| 구분 | 일반 기준 (기본값 적용 시) | 최적화 절세·우대 전략 적용 시 | 예상 차이 및 효과 |
| :--- | :--- | :--- | :--- |
| **초기 세팅 난이도** | 매우 쉬움 (별도 신청 없음) | 5분 내외 조건 확인 및 설정 | **즉시 적용 가능** |
| **세금 및 수수료 부담** | 기본 세율 및 이자 100% 부담 | 비과세·면세·우대 한도 극대화 | **연간 15% ~ 70% 비용 절감** |
| **장기 복리 효과 (3~5년)** | 고정 지출 누적 | 절감된 금액 재투자 가능 | **수십만 ~ 수백만 원 자산 격차** |

## 3. 단계별 실전 체크리스트

실수 없이 혜택을 챙기기 위해 아래 순서대로 점검해 보세요.

### Step 1: 내 현재 기준 금액 및 비과세·면세 한도 확인하기
가장 먼저 내가 지출하거나 투자하려는 금액이 면세·비과세 또는 우대 구간 내에 있는지 확인해야 합니다. 기준 한도를 단 조금이라도 초과할 경우 전체 금액에 대해 과세되거나 상위 구간 요율이 적용될 수 있습니다.

### Step 2: 웹 계산기로 시나리오별 모의 계산 실행
어림짐작으로 판단하기보다 **[{tool_name}]({tool_url})**에 내 실제 수치를 입력해 A안과 B안의 차이를 비교해 보세요. 눈으로 정확한 원화(₩) 및 달러($) 차액을 확인하면 의사결정이 훨씬 명확해집니다.

### Step 3: 절감한 금액으로 현금흐름 파이프라인 강화
아낀 세금이나 구독료, 대출 이자는 그냥 소비하지 말고 별도의 파킹통장이나 중개형 ISA 월배당 ETF 계좌로 모아두면 또 다른 현금흐름을 만드는 든든한 씨앗이 됩니다.
"""
    return body.strip()


def create_markdown_file(topic: dict, body_content: str) -> Path:
    today_str = datetime.date.today().isoformat()
    tags_json = json.dumps(topic.get("tags", []), ensure_ascii=False)
    tool_name, _ = TOOL_URLS.get(topic["relatedTool"], TOOL_URLS["salary"])

    frontmatter = f"""---
title: "{topic['title']}"
description: "{topic['description']}"
pubDate: {today_str}
updatedDate: {today_str}
category: "{topic['category']}"
tags: {tags_json}
relatedTool: "{topic['relatedTool']}"
faq:
  - q: "가장 빠르고 정확하게 내 조건에 맞는 금액을 계산하려면 어떻게 하나요?"
    a: "본문 상단과 하단에 연결된 '{tool_name}'에 수치를 입력하시면 2026년 최신 기준이 반영된 결과를 별도 회원가입 없이 즉시 확인하실 수 있습니다."
  - q: "입력한 개인 금융·직구 금액 정보가 서버에 저장되나요?"
    a: "아니요, 핀덱스(FINDEX)의 모든 계산기는 사용자의 웹 브라우저 내부에서만 동작하며 어떠한 수치도 외부 서버로 전송하거나 저장하지 않으므로 안심하고 이용하실 수 있습니다."
---

{body_content}
"""
    BLOG_DIR.mkdir(parents=True, exist_ok=True)
    file_path = BLOG_DIR / f"{topic['slug']}.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(frontmatter)
    return file_path


def main():
    parser = argparse.ArgumentParser(description="Auto Income Factory Blog Generator")
    parser.add_argument("--demo", action="store_true", help="Force structured template mode without API call")
    parser.add_argument("--count", type=int, default=1, help="Number of posts to generate in this run")
    args = parser.parse_args()

    topics = load_json(TOPICS_FILE, [])
    history = load_json(HISTORY_FILE, {"published_slugs": []})
    published = set(history.get("published_slugs", []))

    for md_file in BLOG_DIR.glob("*.md"):
        published.add(md_file.stem)

    pending_topics = [t for t in topics if t["slug"] not in published]
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    generated_count = 0

    for _ in range(args.count):
        if pending_topics:
            next_topic = pending_topics.pop(0)
        else:
            next_topic = generate_programmatic_topic(published)

        if api_key and not args.demo:
            try:
                body = generate_with_gemini(next_topic, api_key)
            except Exception:
                body = generate_structured_article(next_topic)
        else:
            body = generate_structured_article(next_topic)

        out_path = create_markdown_file(next_topic, body)
        published.add(next_topic["slug"])
        generated_count += 1
        print(f"[SUCCESS] Generated: {out_path.name}")

    history["published_slugs"] = sorted(list(published))
    history["last_run"] = datetime.datetime.now().isoformat()
    save_json(HISTORY_FILE, history)

    print(f"[DONE] Total newly generated posts: {generated_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
