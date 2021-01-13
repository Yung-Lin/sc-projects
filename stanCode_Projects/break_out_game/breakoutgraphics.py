"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE0
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        self.brick_left = BRICK_COLS * BRICK_ROWS
        self.switch = 1
        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window.width - self.paddle.width) / 2,
                        self.window.height - self.paddle.height - paddle_offset)
        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=self.window.width / 2 - ball_radius, y=self.window.height / 2 - ball_radius)
        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0
        if random.random() > 0.5:
            self.__dx = -self.__dx
        # Initialize our mouse listeners.
        onmouseclicked(self.ball_start_moving)
        onmousemoved(self.move_paddle)
        # Draw bricks.
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.brick.filled = True
                if i < 2:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif 2 <= i < 4:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif 4 <= i < 6:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif 6 <= i < 8:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                self.window.add(self.brick, 0 + j * (self.brick.width + BRICK_SPACING),
                                BRICK_OFFSET + i * (self.brick.height + BRICK_SPACING))

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def reverse_dx(self):
        self.__dx = -self.__dx

    def reverse_dy(self):
        self.__dy = -self.__dy

    def move_paddle(self, mouse):
        self.paddle.x = mouse.x - self.paddle.width / 2
        if mouse.x >= self.window.width - self.paddle.width / 2:
            self.paddle.x = self.window.width - self.paddle.width
        elif mouse.x <= self.paddle.width / 2:
            self.paddle.x = 0

    def ball_start_moving(self, mouse):
        if self.switch == 1:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            self.switch = 0

    def reset_ball_location(self):
        self.ball.x = self.window.width / 2 - BALL_RADIUS
        self.ball.y = self.window.height / 2 - BALL_RADIUS
        self.__dx = 0
        self.__dy = 0

    def game_over(self):
        label = GLabel('GAMEOVER')
        label.font = 'Timesnewman-50-bold'
        self.window.add(label, (self.window.width - label.width) / 2, (self.window.height + label.height) / 2)

    def you_win(self):
        label = GLabel('YOU WIN!')
        label.font = 'Timesnewman-50-bold'
        self.window.add(label, (self.window.width - label.width) / 2, (self.window.height + label.height) / 2)
