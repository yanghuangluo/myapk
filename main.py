import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
import random

# 定义网格大小和蛇的速度
GRID_SIZE = 20
WINDOW_SIZE = 400
SNAKE_SPEED = 1 # 秒/步

class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.reset_game()
        self.start_game()
        
    def reset_game(self):
        # 蛇的初始状态：三个身体节点，向右移动
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = 'right'
        self.next_direction = 'right'
        self.food = self.generate_food()
        self.is_game_over = False
        self.score = 0

    

    def start_game(self):
        # 每 SNAKE_SPEED 秒调用一次 update
        self.event = Clock.schedule_interval(self.update, SNAKE_SPEED)

    def generate_food(self):
        # 随机生成食物位置（对齐网格）
        while True:
            x = random.randint(0, (WINDOW_SIZE // GRID_SIZE) - 1) * GRID_SIZE
            y = random.randint(0, (WINDOW_SIZE // GRID_SIZE) - 1) * GRID_SIZE
            if (x, y) not in self.snake:
                return (x, y)

    def update(self, dt):
        if self.is_game_over:
            return

        self.direction = self.next_direction
        head_x, head_y = self.snake[0]

        # 计算新头部位置
        if self.direction == 'up':
            new_head = (head_x, head_y + GRID_SIZE)
        elif self.direction == 'down':
            new_head = (head_x, head_y - GRID_SIZE)
        elif self.direction == 'left':
            new_head = (head_x - GRID_SIZE, head_y)
        elif self.direction == 'right':
            new_head = (head_x + GRID_SIZE, head_y)

        # 检查是否撞墙
        if (new_head[0] < 0 or new_head[0] >= WINDOW_SIZE or
            new_head[1] < 0 or new_head[1] >= WINDOW_SIZE or
            new_head in self.snake):
            self.game_over()
            return

        # 把新头部插入到最前面
        self.snake.insert(0, new_head)

        # 检查是否吃到食物
        if new_head == self.food:
            self.food = self.generate_food()
            self.score += 1
        else:
            # 没吃到就删掉尾巴
            self.snake.pop()

        self.draw()

    def game_over(self):
        self.is_game_over = True
        Clock.unschedule(self.event)
        with self.canvas:
            Color(1, 0, 0)
            self.game_over_label = Label(text=f"Game Over! Score: {self.score}", font_size='30sp', pos=self.center)

    def draw(self):
        self.canvas.clear()
        # 画背景
        with self.canvas:
            Color(0.1, 0.1, 0.1)
            Rectangle(pos=(0, 0), size=(WINDOW_SIZE, WINDOW_SIZE))

            # 画食物
            Color(1, 0, 0)
            Rectangle(pos=self.food, size=(GRID_SIZE, GRID_SIZE))

            # 画蛇
            Color(0, 1, 0)
            for segment in self.snake:
                Rectangle(pos=segment, size=(GRID_SIZE, GRID_SIZE))

        # 如果游戏结束，显示分数
        if self.is_game_over:
            self.add_widget(Label(text=f"游戏结束\n得分: {self.score}", font_size='30sp', halign='center'))

    # --- 触摸操作控制 (适配手机) ---
    def on_touch_down(self, touch):
        if self.is_game_over:
            return False
        
        # 根据触摸位置相对于屏幕中心的偏移来判断方向
        center_x, center_y = self.center
        dx = touch.x - center_x
        dy = touch.y - center_y

        if abs(dx) > abs(dy):
            if dx > 0 and self.direction != 'left':
                self.next_direction = 'right'
            elif dx < 0 and self.direction != 'right':
                self.next_direction = 'left'
        else:
            if dy > 0 and self.direction != 'down':
                self.next_direction = 'up'
            elif dy < 0 and self.direction != 'up':
                self.next_direction = 'down'
        return True

class SnakeApp(App):
    def build(self):
        self.title = "贪吃蛇"
        # 使用 FloatLayout 让游戏区域居中
        root = BoxLayout(orientation='vertical')
        self.game = SnakeGame()
        root.add_widget(self.game)
        return root

if __name__ == '__main__':
    SnakeApp().run()