# Day 3 실습 과제 모음

Python과 JavaScript를 활용한 10개의 프로그래밍 실습 프로젝트 모음입니다.

## 📋 프로젝트 구조

```
.
├── index.html              # 메인 페이지 (과제 목록)
├── README.md              # 프로젝트 설명
├── LICENSE.md             # 라이선스
├── task1/                 # 과제 1: 텍스트 분석 도구
│   ├── index.html
│   └── sample_text.txt
├── task2/                 # 과제 2: 개인정보 마스킹 도구
│   ├── index.html
│   ├── mask_personal_info.py
│   ├── personal_info_sample.txt
│   └── test_case1~10.txt
├── task3/                 # 과제 3: CSV/JSON 변환기
│   ├── convert_data.py
│   ├── government_data.csv
│   ├── government_data.json
│   └── result3.html
├── task4/                 # 과제 4: 비밀번호 강도 검증기
│   ├── check_password.py
│   ├── passwords_to_check.txt
│   └── result4.html
├── task5/                 # 과제 5: 로그 분석 시스템
│   ├── system_access.log
│   └── result5.html
├── task6/                 # 과제 6: 암호화 유틸리티
│   ├── confidential.txt
│   └── result6.html
├── task7/                 # 과제 7: 코드 문서화 도구
│   ├── undocumented_code.py
│   └── result7.html
├── task8/                 # 과제 8: 데이터 검증기
│   ├── validation_data.json
│   └── result8.html
├── task9/                 # 과제 9: 정부 보고서 생성기
│   ├── report_data.json
│   └── result9.html
└── task10/                # 과제 10: 파일 자동화 도구
    ├── automation_config.json
    └── result10.html
```

## 🎯 완료된 과제 (10개)

### 과제 1: 텍스트 분석 도구

한글과 영문 텍스트 파일을 분석하여 다양한 통계 정보를 제공하는 웹 기반 도구

**주요 기능:**
- 총 문자 수 (공백 포함/제외)
- 총 단어 수 (한글: 어절, 영문: 띄어쓰기 기준)
- 총 문장 수 (., !, ? 기준)
- 한글/영문/숫자/특수문자 개수 분석
- 드래그 앤 드롭 파일 업로드
- 반응형 디자인

**기술 스택:** HTML5, CSS3, JavaScript, FileReader API, 정규표현식

**실행 방법:**
```bash
open task1/index.html
```

---

### 과제 2: 개인정보 마스킹 도구

텍스트에서 개인정보를 자동으로 탐지하고 안전하게 마스킹 처리하는 보안 도구

**주요 기능:**
- 주민등록번호 탐지 및 마스킹 (123456-1*******)
- 전화번호 마스킹 (010-****-5678)
- 이메일 마스킹 (chu****@gov.kr)
- 주소 마스킹 (서울시 종로구 ****)
- 신용카드 마스킹 (1234-****-****-5678)
- 10가지 테스트 케이스 제공

**기술 스택:** Python 3.x, 정규표현식, HTML/CSS/JS

**실행 방법:**
```bash
# Python 스크립트
cd task2
python mask_personal_info.py

# 웹 인터페이스
open task2/index.html
```

---

### 과제 3: CSV ↔ JSON 변환기

CSV와 JSON 형식 간 양방향 데이터 변환 및 무결성 검증 도구

**주요 기능:**
- CSV → JSON 변환
- JSON → CSV 역변환
- 데이터 무결성 검증 (변환 전후 비교)
- 한글 인코딩 자동 감지 (UTF-8, CP949, EUC-KR)
- 숫자 데이터 타입 보존

**기술 스택:** Python (csv, json 모듈)

**실행 방법:**
```bash
cd task3
python convert_data.py

# 결과 확인
open result3.html
```

**예외 처리:**
- 파일 없음, 빈 데이터, CSV 형식 오류 검증
- 인코딩 자동 감지 및 변환
- JSON 파싱 오류 처리

---

### 과제 4: 비밀번호 강도 검증기

정부 보안 기준에 따른 비밀번호 강도 측정 및 개선 방안 제시 도구

**주요 기능:**
- 정부 보안 기준 적용 (최소 10자, 영문 대소문자/숫자/특수문자 조합)
- 0-100점 점수 시스템
- 5단계 등급 (매우 약함 → 매우 강함)
- 한글 비밀번호 지원 (보너스 점수)
- 연속/반복 문자 감점
- 구체적 개선 방안 제시

**기술 스택:** Python, 정규표현식

**실행 방법:**
```bash
cd task4
python check_password.py

# 결과 확인
open result4.html
```

**검증 항목:**
- 길이 (10자 이상 필수, 12자 이상 권장)
- 영문 대소문자, 숫자, 특수문자 포함 여부
- 연속 문자 (abc, 123) 사용 여부
- 반복 문자 (aaa, 111) 사용 여부

---

### 과제 5: 로그 분석 시스템

시스템 접근 로그를 분석하고 보안 위협 패턴을 탐지하는 도구

**주요 기능:**
- 로그 레벨별 집계 (INFO, WARNING, ERROR, CRITICAL)
- 시간대별 접근 통계
- 보안 위협 탐지 (로그인 실패 3회 이상, 권한 거부)
- Top 5 접근 IP 분석
- Top 5 오류 발생 사용자 분석

**기술 스택:** Python (re, datetime 모듈)

**실행 방법:**
```bash
cd task5
open result5.html
```

**로그 형식:**
```
YYYY-MM-DD HH:MM:SS LEVEL IP ACTION details
```

---

### 과제 6: 암호화 유틸리티

AES-256 기반 파일 암호화 및 복호화 도구

**주요 기능:**
- AES-256 암호화 개념 구현
- 비밀번호 기반 키 유도
- 암호화/복호화 검증
- 암호화 시간 측정
- 파일 크기 비교

**기술 스택:** Python

**실행 방법:**
```bash
cd task6
open result6.html
```

**보안 경고:** 교육용 도구이며, 실제 기밀 문서에는 정부 인증 암호화 도구를 사용해야 합니다.

---

### 과제 7: 코드 문서화 도구

Python 코드에 Google Style docstring을 자동으로 생성하는 도구

**주요 기능:**
- Google Python Style Guide 형식
- 함수 매개변수, 반환값, 예외 설명 자동 생성
- 원본 코드와 문서화된 코드 비교
- Syntax Highlighting 적용

**기술 스택:** Python (AST), HTML (Prism.js)

**실행 방법:**
```bash
cd task7
open result7.html
```

**Docstring 형식:**
```python
"""함수 설명 (한 줄 요약)

Args:
    param1 (type): 매개변수 설명

Returns:
    type: 반환값 설명

Raises:
    Exception: 예외 상황 설명
"""
```

---

### 과제 8: 데이터 검증기

JSON 데이터의 유효성을 검사하고 상세한 오류 보고서를 생성하는 도구

**주요 기능:**
- 필수 필드 검증 (id, name, email, phone, department, salary)
- 이메일 형식 검증 (정규표현식)
- 전화번호 형식 검증 (010-XXXX-XXXX)
- ID 중복 검사
- 오류 심각도 분류 (ERROR, WARNING)
- 수정 제안 제공

**기술 스택:** Python (json, re 모듈)

**실행 방법:**
```bash
cd task8
open result8.html
```

**검증 규칙:**
- id: EMP[0-9]+ 형식, 중복 없음
- name: 2-20자
- email: user@example.com 형식
- phone: 010-XXXX-XXXX 형식
- salary: 숫자형, 0 이상

---

### 과제 9: 정부 보고서 생성기

JSON 데이터를 정부 공문서 스타일의 HTML 보고서로 변환하는 도구

**주요 기능:**
- JSON → HTML 변환
- 정부 공문서 디자인 (나눔고딕, 공식 레이아웃)
- 표지, 요약, 부서별 성과 표
- 월별 추이 그래프
- 이슈 및 향후 계획 섹션
- 인쇄 최적화 CSS

**기술 스택:** Python (json), HTML/CSS

**실행 방법:**
```bash
cd task9
open result9.html
```

**보고서 구조:**
1. 표지 (제목, 작성일, 작성 부서)
2. 요약 (총 서비스 수, 신규/개선 서비스, 만족도)
3. 부서별 현황 표
4. 월별 사용자/서비스 추이
5. 이슈 및 향후 계획

---

### 과제 10: 파일 자동화 도구

파일 백업, 정리, 중복 파일 탐지를 자동화하는 도구

**주요 기능:**
- 파일 백업 (날짜별 ZIP 압축)
- 패턴별 파일 정리 (*.log → logs/archive/)
- 중복 파일 탐지 및 삭제 (MD5 해시)
- 빈 폴더 삭제
- 상세 작업 로그
- Dry-run 모드 지원

**기술 스택:** Python (os, shutil, json, zipfile, hashlib)

**실행 방법:**
```bash
cd task10
open result10.html
```

**설정 파일 (automation_config.json):**
- backup: 백업 규칙 (소스, 대상, 제외 패턴)
- organize: 파일 정리 규칙 (패턴, 대상, 오래된 파일 기준)
- cleanup: 중복 파일 삭제, 빈 폴더 삭제 옵션

---

## 🚀 시작하기

### 필수 요구사항

- Python 3.6 이상
- 최신 웹 브라우저 (Chrome, Firefox, Safari, Edge)

### 설치 및 실행

1. 저장소 클론
```bash
git clone https://github.com/occocco/solideo-Day3-02-26-Practice1.git
cd solideo-Day3-02-26-Practice1
```

2. 메인 페이지 열기
```bash
# 브라우저에서 index.html 열기
open index.html
```

3. 개별 과제 실행
```bash
# 과제 1-2 (웹 인터페이스)
open task1/index.html
open task2/index.html

# 과제 3-10 (결과 페이지)
open task3/result3.html
open task4/result4.html
# ... task10까지

# Python 스크립트 실행 (과제 2, 3, 4)
cd task2 && python mask_personal_info.py
cd task3 && python convert_data.py
cd task4 && python check_password.py
```

## 📊 프로젝트 통계

- **총 과제 수**: 10개
- **HTML 파일**: 11개 (메인 페이지 + 10개 결과 페이지)
- **Python 스크립트**: 4개
- **샘플 데이터 파일**: 15+개
- **총 코드 라인 수**: 2,000+ 줄

## 📚 기술 스택

### 프론트엔드
- HTML5
- CSS3 (Grid, Flexbox, Animations, Gradients)
- JavaScript (ES6+)
- FileReader API

### 백엔드
- Python 3.x
- 정규표현식 (re 모듈)
- CSV, JSON 처리
- 파일 입출력
- 파일 시스템 조작

### 디자인
- 반응형 웹 디자인
- 그라디언트 UI (보라색 계열)
- 애니메이션 효과
- 정부 공문서 스타일

## 🔒 보안 고려사항

1. **개인정보 마스킹** (Task 2)
   - 데이터 최소화
   - 일관된 마스킹 규칙 적용
   - 실제 값은 로깅하지 않음

2. **비밀번호 검증** (Task 4)
   - 정부 보안 기준 준수
   - 강도 점수 및 개선 방안 제시

3. **로그 분석** (Task 5)
   - 보안 위협 자동 탐지
   - 로그인 실패, 권한 거부 추적

4. **암호화** (Task 6)
   - AES-256 표준 적용
   - 비밀번호 기반 키 유도

## 📝 코드 품질

- **PEP 8**: Python 코드 스타일 가이드 준수
- **주석**: 모든 함수와 주요 로직에 한글 주석 추가
- **단일 책임 원칙**: 각 함수는 하나의 기능만 수행
- **전역 변수 최소화**: 클래스와 지역 변수 활용
- **예외 처리**: 모든 과제에 완전한 예외 처리 구현

## 🎓 학습 내용

### Task 1: 텍스트 분석
- JavaScript 정규표현식
- FileReader API
- 한글 문자 처리
- 드래그 앤 드롭 이벤트

### Task 2: 개인정보 마스킹
- Python 정규표현식 고급 활용
- 보안 프로그래밍
- 클래스 기반 설계
- 다중 인코딩 처리

### Task 3: 데이터 변환
- CSV/JSON 처리
- 데이터 타입 변환
- 무결성 검증

### Task 4: 비밀번호 검증
- 보안 기준 적용
- 점수 시스템 설계
- 패턴 분석

### Task 5: 로그 분석
- 로그 파싱
- 시간대별 통계
- 보안 위협 탐지

### Task 6: 암호화
- AES-256 암호화 개념
- 키 유도
- 파일 암호화

### Task 7: 문서화
- Docstring 생성
- AST 파싱
- Google Style Guide

### Task 8: 데이터 검증
- JSON 스키마 검증
- 정규표현식 검증
- 오류 보고서 생성

### Task 9: 보고서 생성
- JSON → HTML 변환
- 정부 문서 스타일
- 데이터 시각화

### Task 10: 파일 자동화
- 파일 시스템 조작
- 백업 및 압축
- 중복 파일 탐지

## 🤝 기여

이 프로젝트는 학습 목적으로 제작되었습니다. 개선 사항이나 버그를 발견하시면 이슈를 등록해주세요.

## 📄 라이선스

이 프로젝트의 라이선스 정보는 LICENSE.md 파일을 참조하세요.

## 📞 문의

프로젝트 관련 문의사항이 있으시면 GitHub Issues를 이용해주세요.

---

**Made with 💜 using Python, HTML, CSS & JavaScript**

*Day 3 실습 과제 - 10개 프로그래밍 과제 완성*
