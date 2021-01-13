"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    life = NUM_LIVES
    # Add animation loop here!
    while life > 0:
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        # reflection
        if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
            graphics.reverse_dx()
        # reflection
        if graphics.ball.y <= 0:
            graphics.reverse_dy()
        # die situation
        if graphics.ball.y >= graphics.window.height - graphics.ball.height:
            life -= 1
            graphics.reset_ball_location()
            graphics.switch = 1
        pause(FRAME_RATE)
        # set upper border
        if graphics.window.get_object_at(graphics.ball.x + graphics.ball.width / 2, graphics.ball.y - 0.1) is not None:
            # won't stuck in paddle
            if graphics.ball.y < graphics.paddle.y:
                graphics.reverse_dy()
            if graphics.ball.y < graphics.paddle.y - graphics.ball.height:
                graphics.window.remove(
                    graphics.window.get_object_at(graphics.ball.x + graphics.ball.width / 2, graphics.ball.y - 0.1))
                graphics.brick_left -= 1
        # set left border
        if graphics.window.get_object_at(graphics.ball.x - 0.1, graphics.ball.y + graphics.ball.height / 2) is not None:
            graphics.reverse_dx()
            if graphics.ball.y < graphics.paddle.y - graphics.ball.height:
                graphics.window.remove(graphics.window.get_object_at(graphics.ball.x - 0.1,
                                                                     graphics.ball.y + graphics.ball.height / 2))
                graphics.brick_left -= 1
        # set right border
        if graphics.window.get_object_at(graphics.ball.x + graphics.ball.width + 0.1,
                                         graphics.ball.y + graphics.ball.height / 2) is not None:
            graphics.reverse_dx()
            if graphics.ball.y < graphics.paddle.y - graphics.ball.height:
                graphics.window.remove(graphics.window.get_object_at(graphics.ball.x + graphics.ball.width + 0.1,
                                                                     graphics.ball.y + graphics.ball.height / 2))
                graphics.brick_left -= 1
        # set lower border
        if graphics.window.get_object_at(graphics.ball.x + graphics.ball.width / 2,
                                         graphics.ball.y + graphics.ball.height + 0.1) is not None:
            # won't stuck in paddle
            if graphics.get_dy() > 0:
                graphics.reverse_dy()
            if graphics.ball.y < graphics.paddle.y - graphics.ball.height:
                graphics.window.remove(graphics.window.get_object_at(graphics.ball.x + graphics.ball.width / 2,
                                                                     graphics.ball.y + graphics.ball.height + 0.1))
                graphics.brick_left -= 1
        if graphics.brick_left == 0:
            graphics.window.clear()
            graphics.you_win()
            break
    if graphics.brick_left != 0:
        graphics.window.clear()
        graphics.game_over()


if __name__ == '__main__':
    main()
