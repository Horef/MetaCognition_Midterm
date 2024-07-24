import pandas as pd
import numpy as np
import pygame as pg
import pygame_widgets as pw
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox as pgTextBox
import os
from time import time

from helpers import *
from settings import *
from questions import *

from textbox import TextBox


class Questions_Controller(object):
    def __init__(self):
        pg.init()
        pg.display.set_caption("Questionare")
        self.screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.font = pygame.font.SysFont('Arial', 25) #Arial #Times New Roman

        # defining colors
        self.black_color = (0, 0, 0)
        self.white_color = (255, 255, 255)

        self.done = False
        pg.key.set_repeat(*KEY_REPEAT_SETTING)

        # user properties
        self.id = None

        # current question properties
        self.current_question_num = 0
        self.current_question = ""
        self.is_conflict = False
        self.ans_a = ""
        self.ans_b = ""
        self.correct_answer = ""
        self.sureness = 0
        self.chosen_answer = ""

        # whether we are in a question or confidence stage
        self.in_question = True

        # maintaining the properties
        self.mouse_movements = pd.DataFrame(columns=['question', 'x', 'y', 'dist_to_ans_a', 'dist_to_ans_b'])
        self.answers = pd.DataFrame(columns=['question_num', 'question', 'is_conflict', 'opt_a', 'opt_b', 'chosen_answer',
                                             'correct_answer', 'sureness', 'ans_time'])

    def blit_text(self, surface, text, pos, font, color=pygame.Color('black')):
        """
        This function will blit text to a surface, with word wrapping
        :param surface: surface to blit the text to
        :param text: text to blit
        :param pos: position to blit the text at
        :param font: font to use
        :param color: color of the text
        :return: nothing
        """

        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 1, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

    def run_questions(self, conflict_questions: [Question], non_conflict_questions: [Question]):
        """
        Run the questions
        :param conflict_questions: list of conflict questions
        :param non_conflict_questions: list of non conflict questions
        :return:
        """
        # randomly choose which question to run at each step
        for i in range(len(conflict_questions) + len(non_conflict_questions)):
            # reset the mouse position
            pygame.mouse.set_pos((SCREEN_WIDTH // 2, ORIGINAL_Y + SQUARE_SIZE // 2))

            conflict = np.random.choice([True, False])
            # to check that we have questions to ask
            if conflict and len(conflict_questions) == 0:
                conflict = False
            if not conflict and len(non_conflict_questions) == 0:
                conflict = True
            question = conflict_questions.pop() if conflict else non_conflict_questions.pop()
            self.current_question_num += 1
            time_start = time()
            self.run_question(self.current_question_num, question, conflict)
            time_end = time()
            self.ask_confidence()

            # adding new values to the answers dataframe
            new_row = pd.DataFrame([[self.current_question_num, self.current_question, conflict, self.ans_a, self.ans_b, self.chosen_answer,
                                     self.correct_answer, self.sureness, time_end - time_start]],
                                   columns=['question_num', 'question', 'is_conflict', 'opt_a', 'opt_b', 'chosen_answer', 'correct_answer',
                                            'sureness', 'ans_time'])
            self.answers = pd.concat([self.answers, new_row], ignore_index=True)

    def info_screen(self):
        """
        Show the user the instructions for the task
        :return: nothing
        """
        self.screen.fill(self.white_color)

        info_text = """
In a big research project a number of studies were carried out where short personality descriptions of the participants were made. 
In every study there were participants from two population groups (e.g., carpenters and policemen).
In each study one participant was drawn at random from the sample.\n
You’ll get to see the personality description of this randomly chosen participant.
You’ll also get information about the composition of the population groups tested in the study in question. 
You’ll be asked to indicate to which population group the participant most likely belongs.
        
    Please press the 'enter' key to continue.
        """

        # draw the text with multiple lines
        text = self.font.render(info_text, True, self.black_color)
        self.blit_text(self.screen, info_text, (20, 10), self.font)

        while True and not self.done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.done = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        return
            pg.display.update()
            self.clock.tick(self.fps)

    def login_screen(self):
        """
        Run a simple login screen to ask the user for their id
        :return: nothing, saves the id to the class
        """
        self.screen.fill(self.white_color)

        # draw the question
        question = self.font.render('Please enter your ID:', True, self.black_color)
        self.screen.blit(question, (10, 10))
        enter_to_continue = self.font.render('Press enter to continue', True, self.black_color)
        self.screen.blit(enter_to_continue, (10, 40))

        # draw the text box
        self.input = TextBox((100, 100, 150, 30), command=self.save_id,
                             clear_on_enter=True, inactive_on_enter=False)

        while self.id is None and not self.done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.done = True
                self.input.get_event(event)
            self.input.update()
            self.input.draw(self.screen)
            pg.display.update()
            self.clock.tick(self.fps)

    def draw_question(self, question_num: int, question_container: Question, conflict: bool) -> None:
        """
        Draw the question on the screen
        :param question_num: number of the question
        :param question_container: container with the question
        :param conflict: whether the question is a conflict question
        :return: nothing
        """

        self.screen.fill((255, 255, 255))

        # draw the question
        question_index = self.font.render('Question ' + str(question_num), True, self.black_color)
        self.screen.blit(question_index, (10, 10))
        self.current_question = question_container.get_conflict_version() if conflict else question_container.get_non_conflict_version()

        # print the possible answers
        self.correct_answer = question_container.get_correct_conflict_answer() if conflict else question_container.get_correct_non_conflict_answer()
        wrong_answer = question_container.get_wrong_conflict_answer() if conflict else question_container.get_wrong_non_conflict_answer()
        correct_place = question_container.get_correct_answer_place()

        question_answers = self.current_question

        self.ans_a = self.correct_answer if correct_place == 1 else wrong_answer
        question_answers += '\n' + 'A: ' + self.ans_a
        self.ans_b = self.correct_answer if correct_place == 2 else wrong_answer
        question_answers += '\n' + 'B: ' + self.ans_b

        self.blit_text(self.screen, question_answers, (10, 40), self.font)

        # draw the squares
        pygame.draw.rect(self.screen, (0, 0, 255), square_1, SQUARE_SIZE)
        # add the text to the square
        text_a = self.font.render('A', True, self.white_color)
        self.screen.blit(text_a, (square_1[0] + SQUARE_SIZE // 2.5, square_1[1] + SQUARE_SIZE // 2.5))

        pygame.draw.rect(self.screen, (0, 0, 255), square_3, SQUARE_SIZE)
        # add the text to the square
        text_b = self.font.render('B', True, self.white_color)
        self.screen.blit(text_b, (square_3[0] + SQUARE_SIZE // 2.5, square_3[1] + SQUARE_SIZE // 2.5))

        # flip the display
        pygame.display.flip()

    def run_question(self, question_num: int, question_container: Question, conflict: bool):
        frame = 0

        while True and not self.done:
            for event in pygame.event.get():
                # if the game is quit
                if event.type == pygame.QUIT:
                    self.done = True

                # if something is clicked, check if it is one of the squares
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if square_1.collidepoint(event.pos):
                        self.chosen_answer = self.ans_a
                        print('Chosen answer A')
                        return
                    if square_3.collidepoint(event.pos):
                        self.chosen_answer = self.ans_b
                        print('Chosen answer B')
                        return

            if frame % 15 == 0:
                # print("Mouse moved to", pygame.mouse.get_pos())
                new_row = pd.DataFrame([[question_num, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1],
                                         self.distance_to_square(pygame.mouse.get_pos(), square_1),
                                         self.distance_to_square(pygame.mouse.get_pos(), square_3)]],
                                       columns=['question', 'x', 'y', 'dist_to_ans_a', 'dist_to_ans_b'])
                self.mouse_movements = pd.concat([self.mouse_movements, new_row], ignore_index=True)

            self.draw_question(question_num, question_container, conflict)

            frame += 1

    def ask_confidence(self):
        """
        Ask the user for their confidence in their answer by using a slider with values from 0 to 100 %
        :return: nothing
        """
        # creating the slider
        slider = Slider(self.screen, 100, 100, 200, 15, min=0, max=100, step=1, initial=50)
        output = pgTextBox(self.screen, 175, 130, 50, 35, fontSize=20)

        output.disable()

        while True and not self.done:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.done = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.sureness = slider.getValue()
                        return

            self.screen.fill((255, 255, 255))

            # draw the question
            confidence_text = ("How sure are you in your answer?\nAfter selecting desired confidence, press 'enter' to "
                               "continue.")
            self.blit_text(self.screen, confidence_text, (10, 10), self.font)

            output.setText(slider.getValue())

            pw.update(events)
            pg.display.update()
            self.clock.tick(self.fps)

    def save_id(self, inner_id, id: str) -> None:
        self.id = id
        # in the results folder create a folder with the id
        os.mkdir(f'results/{id}')

    def save_results(self):
        self.answers.to_csv(f'results/{self.id}/answers.csv')
        self.mouse_movements.to_csv(f'results/{self.id}/mouse_movements.csv')

    def distance_to_square(self, pos, square):
        """
        Calculate the distance from the position to the square
        :param pos: position
        :param square: square
        :return: distance
        """
        return np.sqrt((pos[0] - square[0]) ** 2 + (pos[1] - square[1]) ** 2)


if __name__ == "__main__":
    questionare = Questions_Controller()
    questions = create_questions()
    # choose half of the questions to have the correct answer placed in the first square
    correct_first = np.random.choice(questions, len(questions) // 2, replace=False)
    correct_second = [q for q in questions if q not in correct_first]
    for q in correct_first:
        q.set_correct_answer_place(1)

    for q in correct_second:
        q.set_correct_answer_place(2)

    # selecting which questions will be conflict versions, and which are not, such that exactly half are conflict
    conflict_questions = np.random.choice(questions, len(questions) // 2, replace=False).tolist()
    non_conflict_questions = [q for q in questions if q not in conflict_questions]

    questionare.info_screen()
    questionare.login_screen()
    questionare.run_questions(conflict_questions, non_conflict_questions)
    questionare.save_results()
    pg.quit()
