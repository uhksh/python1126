import turtle
import random
import math

# ===== 세팅 =====
screen = turtle.Screen()
screen.setup(900, 900)
screen.colormode(255)
screen.bgcolor(8, 8, 18)
screen.title("THE WATCHER - Owl of Metaphysics")
screen.tracer(0)          # 그리는 과정 숨기고 한 번에 출력 (속도 UP)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
random.seed(7)


# ===== 도구 함수 =====
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

    
def disk(x, y, r, color):
    """(x, y) 중심, 반지름 r 인 꽉 찬 원"""
    move(x, y - r)
    t.setheading(0)
    t.color(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()


def mix(c1, c2, k):
    """두 색을 k(0~1) 비율로 섞기 -> 그라데이션"""
    return (int(c1[0] + (c2[0] - c1[0]) * k),
            int(c1[1] + (c2[1] - c1[1]) * k),
            int(c1[2] + (c2[2] - c1[2]) * k))


def ray(x, y, angle, start, length, color, width):
    """(x, y)에서 angle 방향으로 start 거리부터 length 만큼 선 긋기"""
    rad = math.radians(angle)
    move(x + math.cos(rad) * start, y + math.sin(rad) * start)
    t.pensize(width)
    t.color(color)
    t.goto(x + math.cos(rad) * (start + length),
           y + math.sin(rad) * (start + length))


# ===== 1. 형이상학 배경: 황금 나선 만다라 =====
def mandala():
    t.pensize(1)
    move(0, 0)
    t.setheading(0)
    for i in range(260):
        k = i / 260
        t.color(mix((40, 20, 90), (255, 150, 40), k))
        t.forward(i * 1.6)
        t.left(119)          # 120도에서 살짝 비틀어서 회전하는 소용돌이


def sacred_rings():
    """시간의 고리 - 점선 동심원"""
    for r in range(300, 430, 32):
        for a in range(0, 360, 4):
            if (a // 4) % 2 == 0:
                rad1 = math.radians(a + r)
                rad2 = math.radians(a + r + 3)
                move(math.cos(rad1) * r, math.sin(rad1) * r + 20)
                t.pensize(2)
                t.color(mix((90, 60, 160), (255, 170, 60), (r - 300) / 130))
                t.goto(math.cos(rad2) * r, math.sin(rad2) * r + 20)


def energy_bursts():
    """사방으로 터지는 속도선 - 역동성"""
    for i in range(140):
        ang = random.uniform(0, 360)
        start = random.uniform(330, 380)
        length = random.uniform(20, 90)
        c = mix((255, 120, 0), (255, 230, 150), random.random())
        ray(0, 20, ang, start, length, c, random.choice([1, 1, 2]))


# ===== 2. 머리와 깃털 =====
def ear_tuft(side):
    """귀깃 (side = -1 왼쪽, 1 오른쪽)"""
    for i in range(18):
        x0 = side * (110 + i * 4)
        y0 = 200 + i * 2
        c = mix((30, 22, 18), (120, 90, 60), i / 18)
        t.pensize(5)
        t.color(c)
        move(x0, y0)
        t.goto(side * (210 + i * 3), 330 - i * 3)


def head():
    # 바깥 머리 실루엣 (어두운 갈색 그라데이션)
    for r in range(270, 200, -5):
        disk(0, 10, r, mix((25, 18, 14), (70, 52, 38), (270 - r) / 70))
    # 머리 깃털 결: 중심에서 바깥으로 짧은 획
    for i in range(1400):
        ang = random.uniform(0, 360)
        start = random.uniform(120, 260)
        c = random.choice([(40, 30, 22), (95, 72, 50), (150, 120, 85),
                           (20, 15, 12), (180, 150, 110)])
        ray(0, 10, ang, start, random.uniform(8, 22), c, random.choice([1, 2]))


def face_disc(cx, cy):
    """눈 주변 얼굴 판 - 방사형 깃털"""
    for r in range(130, 60, -6):
        disk(cx, cy, r, mix((110, 90, 70), (215, 200, 175), (130 - r) / 70))
    for i in range(500):
        ang = random.uniform(0, 360)
        start = random.uniform(75, 125)
        c = random.choice([(60, 45, 35), (90, 70, 55), (235, 225, 205)])
        ray(cx, cy, ang, start, random.uniform(6, 18), c, 1)


# ===== 3. 눈: 이 그림의 영혼 =====
def eye(cx, cy):
    # 검은 테두리
    disk(cx, cy, 78, (10, 8, 6))
    # 홍채 그라데이션: 바깥 진한 적갈색 -> 안쪽 불타는 주황
    for r in range(72, 30, -2):
        k = (72 - r) / 42
        disk(cx, cy, r, mix((150, 30, 0), (255, 150, 20), k))
    # 홍채 방사 무늬 (기계식 조리개 느낌)
    for a in range(0, 360, 6):
        ray(cx, cy, a, 34, 36, (255, 190, 80), 1)
    for a in range(3, 360, 12):
        ray(cx, cy, a, 40, 25, (120, 20, 0), 1)
    # 동공
    disk(cx, cy, 32, (0, 0, 0))
    # 하이라이트 (살아있는 눈빛)
    disk(cx - 14, cy + 14, 9, (255, 255, 255))
    disk(cx + 12, cy - 10, 3, (220, 220, 255))


def brows():
    """V자 눈썹 - 노려보는 표정"""
    for i in range(12):
        c = mix((15, 12, 10), (70, 55, 40), i / 12)
        t.pensize(6)
        t.color(c)
        move(-10 - i * 3, 95 - i * 4)
        t.goto(-210, 170 - i * 3)
        move(10 + i * 3, 95 - i * 4)
        t.goto(210, 170 - i * 3)


def beak():
    move(0, 45)
    t.color((40, 50, 60), (95, 115, 130))
    t.pensize(2)
    t.begin_fill()
    t.goto(-22, 0)
    t.goto(-8, -60)
    t.goto(0, -85)
    t.goto(8, -60)
    t.goto(22, 0)
    t.goto(0, 45)
    t.end_fill()
    # 부리 광택
    t.pensize(3)
    t.color((170, 190, 205))
    move(-4, 30)
    t.goto(-6, -40)


def chest():
    """가슴 깃털 줄무늬"""
    for row in range(6):
        y = -200 - row * 22
        for col in range(-8, 9):
            x = col * 28 + random.uniform(-6, 6)
            if x * x / 260 ** 2 + (y + 120) ** 2 / 230 ** 2 < 1:
                t.pensize(3)
                t.color(random.choice([(30, 22, 16), (60, 45, 32)]))
                move(x - 6, y + 6)
                t.goto(x, y - 8)
                t.goto(x + 6, y + 6)


# ===== 4. 서명 =====
def title():
    move(0, -410)
    t.color((255, 170, 60))
    t.write("THE WATCHER  //  눈을 감지 않는 자", align="center",
            font=("Arial", 18, "bold"))


# ===== 실행 =====
mandala()
sacred_rings()
energy_bursts()
ear_tuft(-1)
ear_tuft(1)
head()
face_disc(-105, 50)
face_disc(105, 50)
chest()
brows()
eye(-105, 50)
eye(105, 50)
beak()
title()

screen.update()
turtle.done()