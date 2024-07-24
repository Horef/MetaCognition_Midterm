import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

from settings import *

def plot_movements(dots: np.ndarray, name: str | int, question: int) -> None:
    plt.figure(figsize=(10, 10))
    xs = dots[:, 0]
    ys = dots[:, 1]
    # changing the y-axis to be from top to bottom
    ys = [-y for y in ys]

    # having the final plot include all the points of the screen
    plt.axis((0., SCREEN_WIDTH, -SCREEN_HEIGHT, 0.))

    # drawing the squares that are present in the screen
    rect1 = patches.Rectangle((ORIGINAL_X, -ORIGINAL_Y-SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE, linewidth=1,
                             edgecolor='blue', facecolor='blue', alpha=0.3)
    plt.gca().add_patch(rect1)

    rect3 = patches.Rectangle((SCREEN_WIDTH-ORIGINAL_X-SQUARE_SIZE, -ORIGINAL_Y-SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE, linewidth=1,
                             edgecolor='blue', facecolor='blue', alpha=0.3)
    plt.gca().add_patch(rect3)

    plt.plot(xs, ys, 'o-', color='black')
    # # changing the color of the dots depending on how close they are to one another
    # for i in range(1, len(xs)):
    #     if abs(xs[i] - xs[i-1]) < 100 and abs(ys[i] - ys[i-1]) < 100:
    #         plt.plot(xs[i], ys[i], 'o-', color='green')
    #     else:
    #         plt.plot(xs[i], ys[i], 'o-', color='red')

    # making the first point red and slightly bigger
    plt.plot(xs[0], ys[0], 'o-', color='red', markersize=10)
    # plot a decision boundary at y = -400
    plt.axhline(y=-400, color='r', linestyle='--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(f'results/{name}/{question}_movements.png')