"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This program draws the diagram based on the data of the baby names with corresponding ranks and years
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    return GRAPH_MARGIN_SIZE + (width - GRAPH_MARGIN_SIZE * 2) * year_index / len(YEARS)


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=f'{YEARS[i]}', anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # Write your code below this line
    #################################
    # record the color has been used
    color_index = 0
    # for each name
    for n in lookup_names:
        year_index = 0
        for i in range(len(YEARS) - 1):
            # the first and the second dots are not listed on the name data
            if str(YEARS[i]) not in name_data[n] and str(YEARS[i + 1]) not in name_data[n]:
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year_index), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                   get_x_coordinate(CANVAS_WIDTH, year_index + 1), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                   width=LINE_WIDTH, fill=COLORS[color_index])
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year_index) + TEXT_DX,
                                   CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=f'{n} *', fill=COLORS[color_index],
                                   anchor=tkinter.SW)
                year_index += 1
            # the first dot is not listed on the name data while the second one is listed
            elif str(YEARS[i]) not in name_data[n] and str(YEARS[i + 1]) in name_data[n]:
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year_index), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                   get_x_coordinate(CANVAS_WIDTH, year_index + 1), GRAPH_MARGIN_SIZE +
                                   (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * int(
                                    name_data[n][str(YEARS[i + 1])]) / MAX_RANK,
                                   width=LINE_WIDTH, fill=COLORS[color_index])
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year_index) + TEXT_DX,
                                   CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=f'{n} *', fill=COLORS[color_index],
                                   anchor=tkinter.SW)
                year_index += 1
            # the first dot is listed on the name data while the second one is not
            elif str(YEARS[i]) in name_data[n] and str(YEARS[i + 1]) not in name_data[n]:
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year_index), GRAPH_MARGIN_SIZE +
                                   (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * int(
                                    name_data[n][str(YEARS[i])]) / MAX_RANK,
                                   get_x_coordinate(CANVAS_WIDTH, year_index + 1), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                   width=LINE_WIDTH, fill=COLORS[color_index])
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year_index) + TEXT_DX, GRAPH_MARGIN_SIZE +
                                   (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * int(
                                    name_data[n][str(YEARS[i])]) / MAX_RANK,
                                   text=f'{n} {name_data[n][str(YEARS[i])]}', fill=COLORS[color_index],
                                   anchor=tkinter.SW)
                year_index += 1
            # both dots are listed on the name data
            else:
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year_index),
                                   GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * int(
                                       name_data[n][str(YEARS[i])]) / MAX_RANK,
                                   get_x_coordinate(CANVAS_WIDTH, year_index + 1),
                                   GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * int(
                                       name_data[n][str(YEARS[i + 1])]) / MAX_RANK, width=LINE_WIDTH,
                                   fill=COLORS[color_index])
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year_index) + TEXT_DX,
                                   GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * int(
                                       name_data[n][str(YEARS[i])]) / MAX_RANK,
                                   text=f'{n} {name_data[n][str(YEARS[i])]}', fill=COLORS[color_index],
                                   anchor=tkinter.SW)
                year_index += 1
            # create the text of the last point
            if i == len(YEARS) - 2:
                if str(YEARS[i + 1]) in name_data[n]:
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year_index) + TEXT_DX,
                                       GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * int(
                                           name_data[n][str(YEARS[i + 1])]) / MAX_RANK,
                                       text=f'{n} {name_data[n][str(YEARS[i + 1])]}', fill=COLORS[color_index],
                                       anchor=tkinter.SW)
                else:
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year_index) + TEXT_DX,
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=f'{n} *', fill=COLORS[color_index],
                                       anchor=tkinter.SW)
                color_index += 1
                if color_index == len(COLORS):
                    color_index = 0


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
