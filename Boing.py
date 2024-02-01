import tkinter as tk
import time, random, math
root = tk.Tk()
Frame_Width = 400
Frame_Height = 400
g = print((Frame_Width, Frame_Height))
root.geometry(g)
canvas = tk.Canvas(root)
canvas. pack()
canvas.config(width = Frame_Width, height = Frame_Height)
root.title("Boing")
SIZE = 50
balls = []
Num_balls = 20
for i in range(20):
    balls.append({
        'x': random.uniform(50, 400),
        'y': random.uniform(50, 400),
        'radius': 10,
        'dx': 2,
        'dy': 2,
        'still': False
    })
while(1):
    canvas.delete("all")
    red_ball_x, red_ball_y = 400 // 2, 400 // 2
    red_ball_radius = 10
    canvas.create_oval(
        red_ball_x - red_ball_radius,
        red_ball_y - red_ball_radius,
        red_ball_x + red_ball_radius,
        red_ball_y + red_ball_radius,
        fill="red",
        tags="ball"
    )
    canvas['bg'] = "gray"
    for ball in balls:
        ball['x'] = ball['x'] + ball['dx']
        ball['x'] = ball['x'] + ball['dx']
        x2 = ball['x'] + SIZE
        y2 = ball['y'] + SIZE
        ball['x'] += ball['dx']
        ball['y'] += ball['dy']
        for i in balls:
            distance = math.sqrt((ball['x'] - red_ball_x) ** 2 + (ball['y'] - red_ball_y) ** 2)
            if distance < ball['radius'] + red_ball_radius:
                ball['still'] = True
                ball['dx'], ball['dy'] = 0, 0
            distance2 = math.sqrt((ball['x'] - i['x']) ** 2 + (ball['y'] - i["y"]) ** 2)
            if distance2 < ball['radius'] + red_ball_radius and i["still"]:
                ball['still'] = True
                ball['dx'], ball['dy'] = 0, 0
        if ball['x'] + ball['radius'] >= Frame_Width or ball['x'] - ball['radius'] <= 0:
            if ball['dx'] < 0:
                ball['dx'] = -ball['dx'] + random.uniform(0.1, 0.5)
            else:
                ball['dx'] = -ball['dx'] - random.uniform(0.1, 0.5)
        if ball['y'] + ball['radius'] >= Frame_Height or ball['y'] - ball['radius'] <= 0:
            if ball['dy'] < 0:
                ball['dy'] = -ball['dy'] + random.uniform(0.1, 0.5)
            else:
                ball['dy'] = -ball['dy'] - random.uniform(0.1, 0.5)
        if ball['still']:
            canvas.create_oval(ball['x'] - ball['radius'],
                                ball['y'] - ball['radius'],
                                ball['x'] + ball['radius'],
                                ball['y'] + ball['radius'],
                                fill="Red"
            )
        else:
            canvas.create_oval(ball['x'] - ball['radius'],
                               ball['y'] - ball['radius'],
                               ball['x'] + ball['radius'],
                               ball['y'] + ball['radius'],
                               fill="Blue"
            )
    count = 0
    for j in balls:
        if j['still']:
            count += 1
    if count >= Num_balls:
        for k in range(20):
            balls.append({
                'x': random.uniform(50, 400),
                'y': random.uniform(50, 400),
                'radius': 10,
                'dx': 2,
                'dy': 2,
                'still': False
            })
        Num_balls = len(balls)
    time.sleep(0.01)
    canvas.update()
root.destroy()
