<!-- ═══════════════════════ HEADER ═══════════════════════ -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0b0b14,50:3b1f6e,100:ff8c00&height=230&section=header&text=THE%20WATCHER&fontSize=60&fontColor=ffffff&animation=twinkling&fontAlignY=38&desc=Dreams%20%26%20Hopes%20Repository&descAlignY=58&descSize=20" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=FF8C00&center=true&vCenter=true&width=650&lines=Code+is+my+brush.;Python+is+my+canvas.;Today+I+am+not+who+I+was+yesterday.;%E4%BB%8A%E6%88%91%E7%95%B0%E6%98%A8%E6%88%91" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Turtle](https://img.shields.io/badge/Turtle_Graphics-FF8C00?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Evolving-3b1f6e?style=for-the-badge)
![Major](https://img.shields.io/badge/Major-Game_Contents-0b0b14?style=for-the-badge)

</div>

<br/>

> ### 🦉 *"부엉이는 밤에 눈을 뜬다. 모두가 잠든 시간에도, 보는 자는 멈추지 않는다."*

<br/>

---

## 🌌 오늘의 다짐

<div align="center">

# 今 我 異 昨 我

### 금 아 이 작 아

**오늘의 나는, 어제의 나와 다르다.**

</div>

> 한 줄의 코드, 한 번의 커밋, 하나의 잔디.
> 그것들이 쌓여 어제와 다른 오늘의 나를 만든다.

---

## 📂 Repository Structure

```
📦 dreams-and-hopes
 ┣ 📜 gugudan.py        ← 입력 기반 구구단 함수
 ┣ 📜 turtle_owl.py     ← 터틀 그래픽 아트: THE WATCHER
 ┣ 🖼️ owl.png           ← 실행 결과 스크린샷
 ┗ 📘 README.md         ← 지금 보고 있는 이 문서
```

| 파일 | 역할 | 핵심 개념 |
|:---:|:---|:---|
| `gugudan.py` | 단을 입력받아 구구단 출력 | `def` · `input` · `for` · `range` |
| `turtle_owl.py` | 터틀로 그린 부엉이 작품 | 레이어 구조 · 그라데이션 · 방사형 패턴 |

---

## 1️⃣ MODULE 01 — 구구단 함수

<details open>
<summary><b>⚙️ 동작 흐름 보기</b></summary>

<br/>

```mermaid
flowchart LR
    A([▶ 시작]) --> B[/몇단을 입력할까요?/]
    B --> C[입력값을 정수로 변환]
    C --> D{i = 1 ~ 9}
    D -->|반복| E[단 x i 출력]
    E --> D
    D -->|끝| F([■ 종료])
```

</details>

### 💻 실행 예시

```
몇단을 입력할까요? 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
```

---

## 2️⃣ MODULE 02 — THE WATCHER 🦉

<div align="center">

<img src="owl.png" width="600"/>

*눈을 감지 않는 자. 시간의 고리 한가운데에서 모든 것을 바라본다.*

</div>

### 🎨 레이어 아키텍처

그림은 **뒤에서 앞으로**, 총 7개의 레이어를 쌓아서 완성된다.

```mermaid
flowchart TB
    L1["🌀 Layer 1 · 황금 나선 만다라"] --> L2["⭕ Layer 2 · 시간의 고리"]
    L2 --> L3["⚡ Layer 3 · 에너지 버스트"]
    L3 --> L4["🪶 Layer 4 · 머리 & 깃털 텍스처"]
    L4 --> L5["🌕 Layer 5 · 얼굴 판"]
    L5 --> L6["🔥 Layer 6 · 불타는 눈"]
    L6 --> L7["✒️ Layer 7 · 부리 & 서명"]
```

### 🔬 Technique Breakdown

| 기법 | 설명 |
|:---|:---|
| 🌀 **Spiral Mandala** | 120°에서 1°를 비튼 119° 회전을 260번 반복해서 회전하는 소용돌이를 만든다 |
| 🎨 **Color Interpolation** | 두 RGB 색을 비율로 섞는 함수로 보라색에서 주황색으로 부드럽게 이어지는 그라데이션을 표현한다 |
| 🪶 **Procedural Feathers** | 무작위 각도와 길이의 짧은 획 1,400개 이상으로 깃털 질감을 생성한다 |
| 👁️ **Iris Mechanics** | 동심원 그라데이션에 방사형 선을 겹쳐서 기계식 조리개 같은 홍채를 만든다 |
| ⚡ **Render Optimization** | `tracer(0)`로 그리는 과정을 숨기고 `update()`로 한 번에 출력해서 속도를 끌어올린다 |

---

## 🚀 How to Run

```bash
# 1. 저장소 복제
git clone https://github.com/아이디/저장소이름.git

# 2. 구구단 실행
python gugudan.py

# 3. 부엉이 소환
python turtle_owl.py
```

> ⚠️ 터틀 그래픽은 창을 띄워야 하기 때문에 Colab 같은 웹 환경이 아니라 **내 컴퓨터의 파이썬**으로 실행해야 한다.

---

## 👤 Author

<div align="center">

| | |
|:---:|:---|
| **이름** | 김성훈 |
| **전공** | 🎮 게임콘텐츠 |
| **좌우명** | 今我異昨我 |

<br/>

*"오늘 심은 잔디 한 칸이 내일의 숲이 된다."* 🌱

</div>

<!-- ═══════════════════════ FOOTER ═══════════════════════ -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff8c00,50:3b1f6e,100:0b0b14&height=120&section=footer" width="100%"/>
