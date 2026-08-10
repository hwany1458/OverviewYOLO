# OverviewYOLO 저장소 반영 및 공개 전환 안내

이 문서는 준비된 파일 묶음을 기존 private 저장소 `hwany1458/OverviewYOLO`에 안전하게 반영하는 절차입니다.

## 1. 기존 저장소 백업 및 작업 브랜치 생성

기존 자료를 삭제하거나 덮어쓰기 전에 로컬 clone과 별도 브랜치를 만듭니다.

```bash
git clone https://github.com/hwany1458/OverviewYOLO.git
cd OverviewYOLO
git switch -c public-release-preparation
```

기존 README, 그림, 표, 코드가 있다면 새 묶음과 먼저 비교합니다. 특히 기존 `data/`, `scripts/`, `figures/`, `supplementary/` 폴더는 자동으로 삭제하거나 교체하지 않습니다.

## 2. 파일 병합 원칙

- 새 `README.md`를 저장소 첫 화면의 기준 문서로 사용합니다.
- 기존 정량 CSV가 있다면 `benchmark_results_template.csv`를 덮어쓰지 말고, 새 스키마에 맞춘 별도 결과 파일로 변환합니다.
- 논문 Figure 18–20이나 Table 5–10 생성 코드가 이미 있다면 `scripts/` 또는 `experiments/scripts/` 아래에 배치하고 입력 데이터와 연결합니다.
- 기존 그림 원본은 `figures/source/`, 최종 렌더는 `figures/rendered/`처럼 구분하는 것이 좋습니다.
- 공식 YOLO 저장소 전체와 model weights는 현재 저장소에 복사하지 않습니다.

## 3. 공개 전 가장 먼저 수정할 부분

1. `LICENSE_GUIDANCE.md`를 바탕으로 실제 라이선스를 선택합니다.
2. `docs/CITATION_SETUP.md`의 placeholder를 실제 저자 정보로 바꿔 `CITATION.cff`를 만듭니다.
3. 각 공식 저장소의 tag 또는 commit SHA를 `source_ledger.csv`에 추가합니다.
4. 원고의 각 정량 표 셀을 result/source ID에 연결합니다.
5. Figure-generation scripts와 입력 CSV를 실제로 추가합니다.
6. 실행하지 않은 실험은 `AR`로 표시하지 않습니다.
7. 기존 Table 9의 교차 논문 누적 ablation과 Table 10의 근거 없는 오류 비율을 공개 데이터로 만들지 않습니다.

## 4. 로컬 검증

저장소 루트에서 다음을 실행합니다.

```bash
python scripts/validate_repository.py
```

이 검증은 다음을 확인합니다.

- 14개 핵심 버전의 누락·중복
- 필수 CSV 열
- evidence/comparability label
- `P`·`NC` 비교의 금지된 delta
- `AR` 결과의 run manifest/raw output 존재 필드
- BibTeX key 중복
- 로컬 Markdown 링크

외부 웹 링크의 최신 상태와 논문의 과학적 정확성은 별도로 확인해야 합니다.

## 5. 변경 내용 검토 및 commit

```bash
git status
git diff -- README.md
git diff -- data/source_ledger.csv
git add README.md CHANGELOG.md CONTRIBUTING.md LICENSE_GUIDANCE.md configs data docs experiments references scripts .github .gitignore
git commit -m "Prepare evidence-tracked public companion repository"
git push -u origin public-release-preparation
```

GitHub에서 pull request를 생성하고 Actions의 검증이 통과하는지 확인합니다. 기존 private 저장소의 관련 없는 파일은 이 작업에서 삭제하지 않는 것이 안전합니다.

## 6. public 전환 직전 비밀정보 점검

- API key, token, 비밀번호, private download URL
- reviewer 신원이나 심사 문서
- Word/PDF의 숨은 주석·개인정보
- 로컬 절대경로와 사용자명
- 데이터 사용계약상 공개할 수 없는 파일
- Git 현재 파일뿐 아니라 과거 commit에 포함된 secret

민감정보가 Git history에 있었으면 현재 파일만 삭제해서는 충분하지 않습니다. 공개 전 기관 또는 GitHub의 secret-removal 절차를 적용해야 합니다.

## 7. GitHub에서 public 전환

저장소의 `Settings → General → Danger Zone → Change repository visibility`에서 public으로 변경합니다. 전환 직후 로그아웃 상태 또는 시크릿 창에서 다음을 확인합니다.

- 저장소 첫 화면 접근
- README의 모든 상대 링크
- CSV 및 BibTeX 다운로드
- Actions 결과
- Release와 tag 접근
- 원고 Data Availability의 URL

## 8. 원고와 Response Letter 갱신

- Data Availability의 accessed date를 실제 공개 확인일로 수정합니다.
- 공개한 파일만 명시하고 계획 중인 자료는 제외합니다.
- 가능하면 resubmission용 tag/release를 만들고 해당 release URL을 답변서에 기록합니다.
- Reviewer 답변에는 수정 원고 위치와 함께 repository file 및 record ID를 제시합니다.

권장 release 예시는 `v1.0.0-revision`입니다. 최종 출판 후에는 논문 DOI와 저장소 DOI를 추가한 별도 안정 release를 만드는 것이 좋습니다.
