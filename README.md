# 🎥 유튜브 주제 추천 시스템 – GPT 기반 콘텐츠 추천기

**FastAPI + OpenAI GPT API**를 활용하여 유튜브 콘텐츠 제작자를 위한 주제 추천 서비스를 개발한 프로젝트입니다.  
아이디어 입력만으로 콘텐츠 타겟팅에 도움이 되는 주제를 제안하며, **개인화된 콘텐츠 제작 효율성 향상**을 목표로 했습니다.

---

## 📌 프로젝트 개요

- **목표**: 유튜브 영상 아이디어 기반으로 GPT가 주제를 추천해주는 개인화된 콘텐츠 기획 도우미 구축
- **기획 배경**: 생성형 AI(OpenAI GPT)를 활용해 콘텐츠 제작 시간을 줄이고, 초보 유튜버들도 쉽게 주제를 확장할 수 있도록 지원

---

## 🔧 기술 스택

| 구분 | 기술 |
|------|------|
| Backend | Python, FastAPI, Pydantic |
| AI API | OpenAI GPT (text-davinci-003 or gpt-3.5-turbo) |
| 배포 환경 | Docker, Kubernetes |
| CI/CD | GitHub Actions |
| ETC | Uvicorn, Poetry, Jinja2 (템플릿), Gunicorn |

---

## 🗂️ 주요 기능

### ✅ 주제 추천 API (`/recommend`)
- 사용자가 입력한 채널 설명, 키워드, 톤 등을 기반으로 OpenAI API에 요청
- GPT가 3~5개의 콘텐츠 주제 추천
- 응답 결과를 JSON 형태로 반환

### ✅ 서비스 구조
- FastAPI 기반 RESTful 서버 구축
- 입력값 검증을 위한 Pydantic 모델 활용
- API 응답 속도 최적화 및 비동기 처리

### ✅ 배포 및 운영
- Dockerfile 구성 → 이미지 빌드 및 실행
- Kubernetes 배포 YAML 구성
- GitHub Actions를 통해 Push → 자동 빌드 및 테스트 파이프라인 구성

---

## 📁 프로젝트 구조

