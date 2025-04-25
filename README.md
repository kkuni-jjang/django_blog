# django_blog
**django로 blog 만들어서 aws로 배포하기**

간단하고 확장 가능한 개인 블로그 프로젝트.  
게시글 작성, 수정, 댓글 기능, 자유게시판까지 포함된 포트폴리오용 웹입니다.

---
### 시연 영상
https://github.com/user-attachments/assets/5cfb79d7-db15-45eb-8cd4-1dd451bc1a09

---
### 주요 기능

### ✅ 게시글 관리
- 블로그 게시글 작성 / 수정 / 삭제
- 썸네일 이미지 첨부 가능
- 게시글 검색 기능
- 태그/카테고리 분류 (선택사항)

### ✅ 댓글 기능
- 게시글별 댓글 작성 및 삭제
- 댓글 form은 게시글 하단에 함께 표시

### ✅ 자유게시판 (board)
- 별도 게시판으로 커뮤니티 구성 가능
- Bootstrap으로 기본 UI 구성

---

### URL 구성 예시

| URL | 설명 |
|-----|------|
| `/` | 블로그 메인 (홈) |
| `/about/` | 자기소개 페이지 |
| `/blog/<id>/` | 게시글 상세 |
| `/blog/new/` | 게시글 작성 |
| `/board/` | 자유게시판 목록 |
| `/board/new/` | 자유게시판 글 작성 |

---

### 주요 모델 요약

### `Post`
| 필드명 | 설명 |
|--------|------|
| title | 제목 |
| content | 내용 |
| thumbnail | 썸네일 이미지 |
| created_at | 작성일 |
| updated_at | 수정일 |

### `Comment`
| 필드명 | 설명 |
|--------|------|
| post | 연결된 게시글 |
| content | 댓글 내용 |
| created_at | 작성일 |

---

### 사용 기술

- Python 3.12
- Django 4.2
- SQLite3
- HTML + CSS (Bootstrap 일부 적용)
- JavaScript (댓글 작성 등 동적 처리)
