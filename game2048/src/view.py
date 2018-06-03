'''
    This is view module, as in MVC pattern.
    Handles GUI using Tkinter
'''

import tkinter
from src.polygon import polygon

class View:
    def __init__(self, window, boardsize):
        self.window = window
        self.tile_padding = 10
        self.canvas_padding = 20
        self.tile_size = 80

        self.canvas_width = 2*self.canvas_padding + (boardsize-1)*self.tile_padding + (boardsize)*80
        self.canvas_height = 2*self.canvas_padding + (boardsize-1)*self.tile_padding + (boardsize)*80

        self.bgcolor = "#BBADA0"
        self.canvas = tkinter.Canvas(self.window, width=self.canvas_width, height=self.canvas_height, bg=self.bgcolor)
        self.canvas.grid(row=0, column=0)

        score_width = 200
        score_height = self.canvas_height
        score_color = "#EDE0C8"
        self.score_canvas = tkinter.Canvas(self.window, width=score_width, height=score_height, bg=score_color)
        self.score_canvas.grid(row=0, column=1)
        self.score_canvas.create_text(100, 250, font=("Helvetica", 16), text="Up arrow = UP")
        self.score_canvas.create_text(100, 270, font=("Helvetica", 16), text="Down arrow = DOWN")
        self.score_canvas.create_text(100, 290, font=("Helvetica", 16), text="Left arrow = LEFT")
        self.score_canvas.create_text(100, 310, font=("Helvetica", 16), text="Right arrow = RIGHT")
        self.score_canvas.create_text(100, 330, font=("Helvetica", 16), text="r = Restart")
        self.score_canvas.create_text(100, 350, font=("Helvetica", 16), text="p = Robot Play")

        self.debug_canvas = tkinter.Canvas(self.window, width=self.canvas_width + score_width, height="80",bg=score_color)
        self.debug_canvas.grid(row=1, columnspan=2)

    def robotAvailable(self):
        self.debug_canvas.delete('robotavail')
        self.debug_canvas.create_text(100,40, font=("Helvetica", 16), text="Connection Available",tags=("robotavail"))

    def robotUnavailable(self):
        self.debug_canvas.delete('robotavail')
        self.debug_canvas.create_text(100,40, font=("Helvetica", 16), text="Connection Unavailable",tags=("robotavail"))

    def lose(self):
        self.canvas.create_rectangle(0, self.canvas_height/2 - 40, self.canvas_width, self.canvas_height/2 + 40, fill="#ff0000", tags=("gameover"))
        self.canvas.create_text(self.canvas_width/2, self.canvas_height/2, font=("Helvetica", 64), text="Game Over", tags=('gameover'))

    def robotOff(self):
        self.score_canvas.delete('Robot')

    def robotOn(self, move):
        self.score_canvas.delete('Robot')
        self.score_canvas.create_text(100, 200, font=("Helvetica", 18), text="Robot is playing \n move #"+str(move+1)+"/20", tags=("Robot"))

    def render(self, boardMatrix, score):
        self.canvas.delete('gameover')
        for i in range(len(boardMatrix)):
            for j in range(len(boardMatrix)):
                xpos = self.canvas_padding + i*(self.tile_size) + i*(self.tile_padding)
                ypos = self.canvas_padding + j*(self.tile_size) + j*(self.tile_padding)
                polygon.drawtile(self.canvas, boardMatrix[j][i], self.tile_size, xpos, ypos)
        self.drawScore(score)

    def drawScore(self, score):
        text_xpos = 100
        text_ypos = 100
        self.score_canvas.delete('score')
        self.score_canvas.create_text(text_xpos, text_ypos, font=("Helvetica", 32), text=score, tags=('score'))
