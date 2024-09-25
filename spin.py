import turtle
import time
 
angle = 270
 
def tai():
    r = 200  # 设置半径
    turtle.penup()  # 拿起画笔
    turtle.goto(0, 0)  # 到画布中心
    turtle.setheading(angle)# 设置当前朝向为angle角度
    turtle.fd(r)  # 前进r的距离
    turtle.pendown()  # 放下画笔
    turtle.right(90)  # 调整海龟角度
 
    # 画阳鱼
    turtle.fillcolor("white")  # 填充为白色
    turtle.begin_fill()  # 开始填充
    turtle.circle(-r / 2, 180)
    turtle.circle(r / 2, 180)
    turtle.circle(r, 180)
    turtle.end_fill()  # 填充结束
 
    # 画阴鱼
    turtle.fillcolor("black")  # 填充为黑色
    turtle.begin_fill()
    turtle.circle(r, 180)
    turtle.right(180)
    turtle.circle(-r / 2, 180)
    turtle.circle(r / 2, 180)
    turtle.end_fill()
 
    # 画阴鱼眼
    turtle.penup()
    turtle.setheading(angle)
    turtle.fd(-r / 2)
    turtle.pendown()
    turtle.dot(r / 4, "white")  # dot()绘制具有特定大小和颜色的圆点
 
    # 画阳鱼眼
    turtle.penup()
    turtle.fd(-r)
    turtle.pendown()
    turtle.dot(r / 4, "black")
    turtle.penup()
 
turtle.tracer(0)  # 将刷新率置为0，即不刷新
for i in range(10000000):  # 这里设置了1w次，也可以是其他次数
    tai()
    turtle.update()  # 更新绘图
    turtle.clear()  # 清空画布
    angle += 1
