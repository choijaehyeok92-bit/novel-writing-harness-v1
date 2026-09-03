# AGENTS.md

## Mission

이 저장소는 소설 집필 및 검수를 위한 독립 Harness다.
투자, 금융, 포트폴리오 관련 규칙이나 데이터는 이 저장소의 판단에 사용하지 않는다.

## Authority order

충돌 시 아래 순서를 따른다.

1. `policy/non-negotiables.yaml`
2. `policy/canon-hierarchy.yaml`
3. `policy/author-intent.yaml`
4. `canon/`의 확정 설정
5. 확정/게시된 기존 회차
6. 현재 아크/플롯 문서
7. 역사 자료 및 외부 연구
8. 현재 초고
9. 개별 에이전트의 추론

외부 역사 자료가 작품의 확정 대체역사 설정과 충돌하면 먼저 `INTENTIONAL_DIVERGENCE` 여부를 판정한다.

## Read first

모든 에이전트는 작업 전 다음을 읽는다.

- `policy/non-negotiables.yaml`
- `policy/canon-hierarchy.yaml`
- `policy/author-intent.yaml`
- `policy/review-severity.yaml`
- 관련 `canon/`
- 검수 대상 원고와 가능한 경우 직전/직후 회차

Historical Reviewer는 `policy/history-evidence.yaml`도 읽는다.
Language/Typo 에이전트는 `policy/korean-language.yaml`도 읽는다.

## Write boundaries

기본적으로 검수 에이전트는 원고를 직접 수정하지 않는다.
구조화된 Finding을 생성한다.

직접 원고를 수정할 수 있는 역할:
- Final Editor
- 사용자가 명시적으로 허용한 편집 작업

## Finding contract

모든 문제 제기는 최소 다음을 포함한다.

- category
- severity
- location
- original
- issue
- rationale
- confidence
- evidence_type
- source_refs
- suggested_patch
- preserve_if_intentional

## Non-negotiable behavior

- 정본보다 추론을 우선하지 않는다.
- 고증 불확실성을 사실 오류로 단정하지 않는다.
- 작가의 의도적 표현을 임의로 정상화하지 않는다.
- 문체를 표준적인 문장으로 획일화하지 않는다.
- 한 에이전트의 점검 결과를 다른 범주의 사실로 승격하지 않는다.
- 기존 설정을 바꾸는 수정은 반드시 `CANON_CHANGE_REQUIRED`로 표시한다.
