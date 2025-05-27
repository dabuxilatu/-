import turtle
import random
import math


def draw_cancer_constellation():
    # 创建星座画笔
    stars = turtle.Turtle()
    stars.speed(0)
    stars.hideturtle()
    stars.penup()

    # 设置星座位置（右上角）
    stars.goto(150, 150)

    # 绘制巨蟹座星图
    cancer_stars = [
        (0, 0), (30, 20), (60, 10), (90, 30),
        (20, -40), (50, -30), (80, -50)
    ]

    # 绘制星座连线
    connections = [(0, 1), (1, 2), (2, 3), (0, 4), (4, 5), (5, 6)]

    # 绘制星座线
    stars.color("#afeeee")
    stars.width(1)
    for start, end in connections:
        stars.goto(150 + cancer_stars[start][0], 150 + cancer_stars[start][1])
        stars.pendown()
        stars.goto(150 + cancer_stars[end][0], 150 + cancer_stars[end][1])
        stars.penup()

    # 绘制星座点
    for x, y in cancer_stars:
        stars.goto(150 + x, 150 + y)
        stars.dot(10, "#ffd700")  # 金色星星
        stars.dot(6, "#ffffff")  # 白色中心

    # 添加星座标签
    stars.goto(150 + cancer_stars[3][0] + 15, 150 + cancer_stars[3][1] + 15)
    stars.color("#ffffff")
    stars.write("巨蟹座", font=("Arial", 12, "bold"))


def draw_cake():
    # 设置画布
    screen = turtle.Screen()
    screen.bgcolor("#0a0a2a")  # 深蓝色星空背景
    screen.title("王佳生日快乐!")
    screen.colormode(255)

    # 先绘制星座背景
    draw_cancer_constellation()

    # 创建蛋糕画笔
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()

    # 绘制星空背景
    def draw_stars():
        star = turtle.Turtle()
        star.speed(0)
        star.hideturtle()
        star.penup()
        star.color("white")

        for _ in range(100):
            x = random.randint(-300, 300)
            y = random.randint(-200, 200)
            size = random.randint(1, 3)
            star.goto(x, y)
            star.dot(size)

        # 绘制几颗亮星
        for _ in range(5):
            x = random.randint(-300, 300)
            y = random.randint(-200, 200)
            star.goto(x, y)
            star.dot(8, "#ffff00")
            # 星芒效果
            for angle in range(0, 360, 45):
                star.setheading(angle)
                star.forward(10)
                star.backward(10)

    draw_stars()

    # 绘制蛋糕底座 - 添加3D效果
    def draw_cake_layer(x, y, width, height, color, shadow_color):
        # 侧面阴影
        pen.up()
        pen.goto(x, y)
        pen.down()
        pen.color(shadow_color)
        pen.begin_fill()
        pen.goto(x + width, y)
        pen.goto(x + width - 10, y + 10)
        pen.goto(x - 10, y + 10)
        pen.goto(x, y)
        pen.end_fill()

        # 顶部
        pen.up()
        pen.goto(x, y)
        pen.down()
        pen.color(color)
        pen.begin_fill()
        pen.goto(x + width, y)
        pen.goto(x + width, y + height)
        pen.goto(x, y + height)
        pen.goto(x, y)
        pen.end_fill()

    # 三层蛋糕带3D效果
    colors = ["#ff69b4", "#ff1493", "#c71585"]
    shadows = ["#d4588a", "#d4116b", "#a71267"]

    draw_cake_layer(-140, -180, 280, 50, colors[0], shadows[0])  # 底层
    draw_cake_layer(-120, -130, 240, 50, colors[1], shadows[1])  # 中层
    draw_cake_layer(-100, -80, 200, 50, colors[2], shadows[2])  # 顶层

    # 绘制奶油波浪边
    def draw_cream_wave(x, y, width, height=10):
        pen.up()
        pen.goto(x, y)
        pen.down()
        pen.color("white")
        pen.width(3)
        pen.begin_fill()

        segments = int(width / 20)
        for i in range(segments):
            pen.goto(x + i * 20, y + height if i % 2 == 0 else y)

        pen.goto(x + width, y)
        pen.goto(x + width, y + height / 2)

        # 波浪下降
        for i in range(segments, 0, -1):
            pen.goto(x + i * 20, y + height / 2 + (height / 2 if i % 2 == 0 else 0))

        pen.goto(x, y + height / 2)
        pen.end_fill()

    draw_cream_wave(-140, -130, 280)  # 底层奶油
    draw_cream_wave(-120, -80, 240)  # 中层奶油
    draw_cream_wave(-100, -30, 200)  # 顶层奶油

    # 绘制静态蛇图案
    def draw_snake_pattern():
        snake = turtle.Turtle()
        snake.speed(0)
        snake.hideturtle()

        # 蛇身曲线
        snake.penup()
        snake.goto(-120, -100)
        snake.pendown()
        snake.color("#4B8BBE")
        snake.width(15)

        # 绘制蛇身曲线
        points = [(-120, -100), (-90, -80), (-60, -100), (-30, -80),
                  (0, -100), (30, -80), (60, -100), (90, -80), (120, -100)]

        for x, y in points:
            snake.goto(x, y)
            snake.dot(12, "#306998")  # 蛇身节点

        # 蛇头
        snake.penup()
        snake.goto(120, -100)
        snake.dot(20, "#306998")
        # 蛇眼
        snake.goto(125, -95)
        snake.dot(5, "white")

        # 蛇舌
        snake.penup()
        snake.goto(130, -102)
        snake.pendown()
        snake.color("red")
        snake.width(2)
        snake.goto(135, -102)
        snake.goto(133, -100)
        snake.goto(137, -100)

    draw_snake_pattern()

    # 绘制蜡烛和火焰动画
    candle_colors = ["#ff0000", "#ffa500", "#ffff00", "#98fb98", "#9370db"]
    flames = []

    for i in range(5):
        x = -60 + i * 30
        # 蜡烛
        pen.up()
        pen.goto(x, -30)
        pen.down()
        pen.color(candle_colors[i])
        pen.begin_fill()
        pen.goto(x + 10, -30)
        pen.goto(x + 10, 20)
        pen.goto(x, 20)
        pen.goto(x, -30)
        pen.end_fill()

        # 蜡烛光晕
        pen.up()
        pen.goto(x + 5, 20)
        for size in range(15, 5, -5):
            pen.dot(size, (255, 255, min(100 + size * 10, 255)))

        # 火焰
        flame = turtle.Turtle()
        flame.hideturtle()
        flame.speed(0)
        flame.up()
        flame.goto(x + 5, 25)
        flame.color("gold")
        flame.dot(10)
        flames.append(flame)

    # 添加闪烁星星装饰
    twinkles = []
    for _ in range(10):
        twinkle = turtle.Turtle()
        twinkle.speed(0)
        twinkle.hideturtle()
        twinkle.penup()
        x = random.randint(-200, 200)
        y = random.randint(50, 200)
        twinkle.goto(x, y)
        twinkle.color("white")
        twinkle.dot(5)
        twinkles.append((twinkle, x, y))

    # 添加生日祝福文字
    pen.up()
    pen.goto(0, -220)
    pen.color("#ff69b4")
    pen.write("王佳生日快乐呀！", align="center", font=("楷体", 28, "bold"))

    pen.up()
    pen.goto(0, -250)
    pen.color("#9370db")
    pen.write("愿岁并谢，与友长兮!", align="center", font=("楷体", 16))

    # 动画效果
    def animate():
        # 火焰动画
        for flame in flames:
            size = random.randint(8, 12)
            r = random.randint(200, 255)
            g = random.randint(100, 200)
            b = random.randint(0, 50)
            flame.clear()
            flame.color(r, g, b)
            flame.dot(size)

            # 火焰跳动
            flame_x, flame_y = flame.pos()
            flame.goto(flame_x, 25 + random.randint(0, 5))

        # 星星闪烁
        for twinkle, x, y in twinkles:
            if random.random() > 0.7:
                twinkle.clear()
                size = random.randint(3, 7)
                twinkle.goto(x, y)
                twinkle.dot(size, "white")

        screen.ontimer(animate, 100)

    animate()

    # 保持窗口打开
    turtle.done()


draw_cake()