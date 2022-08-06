import pygame
import datetime


pygame.init()
# global variables
screen = pygame.display.set_mode((300, 320))
pygame.display.set_caption('lesson plan')
clock = pygame.time.Clock()
bg = (0, 0, 0)
run = True
font = pygame.font.SysFont('arial', 21)

# timetable lists
monday = ['PE (8 - 8:45)', 'english (8:50 - 9:35)', 'english (9:40 - 10:25)', 'biology (10:30 - 11:15)', 'maths (11:20 - 12:05)', 'english (12:15 - 13)', 'history (13:05 - 13:50)', 'physics (13:55 - 14:40)', '']
tuesday = ['english (8 - 8:45)', 'computer science (8:50 - 9:35)', 'history (9:40 - 10:25)', 'maths (10:30 - 11:15)', 'maths (11:20 - 12:05)', 'physics (12:15 - 13)', 'tutor hour (13:05 - 13:50)', 'spanish (13:55 - 14:40)', '']
wednesday = ['    -', '    -', 'pp (9:40 - 10:25)', 'geography (10:30 - 11:15)', 'english (11:20 - 12:05)', 'maths (12:15 - 13)', 'physics (13:05 - 13:50)', 'PE (13:55 - 14:40)', 'PE (14:45 - 15:30)']
thursday = ['geography (8 - 8:45)', 'maths (8:50 - 9:35)', 'maths (9:40 - 10:25)', 'break (10:30 - 11:15)', 'biology (11:20 - 12:05)', 'english (12:15 - 13)', 'spanish (13:05 - 13:50)', 'chemistry (13:55 - 14:40)', 'chemistry (14:45 - 15:30)']
friday = ['    -', '    -', 'english (9:40 - 10:25)', 'english (10:30 - 11:15)', 'maths (11:20 - 12:05)', '', '', '', '']


def plan_update(monday, tuesday, wednesday, thursday, friday, font, bg):
    x = datetime.datetime.now()
    day = int(x.strftime('%w'))
    minute_time = int(x.strftime('%H')) * 60 + int(x.strftime('%M'))
    later_start = False

    # assigning plan to appropriate days
    if day == 1:
        school_day = True
        lesson1 = monday[0]
        lesson2 = monday[1]
        lesson3 = monday[2]
        lesson4 = monday[3]
        lesson5 = monday[4]
        lesson6 = monday[5]
        lesson7 = monday[6]
        lesson8 = monday[7]
        lesson9 = monday[8]

    elif day == 2:
        school_day = True
        lesson1 = tuesday[0]
        lesson2 = tuesday[1]
        lesson3 = tuesday[2]
        lesson4 = tuesday[3]
        lesson5 = tuesday[4]
        lesson6 = tuesday[5]
        lesson7 = tuesday[6]
        lesson8 = tuesday[7]
        lesson9 = tuesday[8]

    elif day == 3:
        school_day = True
        later_start = True
        lesson1 = wednesday[0]
        lesson2 = wednesday[1]
        lesson3 = wednesday[2]
        lesson4 = wednesday[3]
        lesson5 = wednesday[4]
        lesson6 = wednesday[5]
        lesson7 = wednesday[6]
        lesson8 = wednesday[7]
        lesson9 = wednesday[8]

    elif day == 4:
        school_day = True
        lesson1 = thursday[0]
        lesson2 = thursday[1]
        lesson3 = thursday[2]
        lesson4 = thursday[3]
        lesson5 = thursday[4]
        lesson6 = thursday[5]
        lesson7 = thursday[6]
        lesson8 = thursday[7]
        lesson9 = thursday[8]

    elif day == 5:
        school_day = True
        later_start = True
        lesson1 = friday[0]
        lesson2 = friday[1]
        lesson3 = friday[2]
        lesson4 = friday[3]
        lesson5 = friday[4]
        lesson6 = friday[5]
        lesson7 = friday[6]
        lesson8 = friday[7]
        lesson9 = friday[8]
    else:
        school_day = False
        lesson1 = ''
        lesson2 = ''
        lesson3 = ''
        lesson4 = ''
        lesson5 = ''
        lesson6 = ''
        lesson7 = ''
        lesson8 = ''
        lesson9 = ''

    lesson_color1 = (255, 255, 255)
    lesson_color2 = (255, 255, 255)
    lesson_color3 = (255, 255, 255)
    lesson_color4 = (255, 255, 255)
    lesson_color4 = (255, 255, 255)
    lesson_color5 = (255, 255, 255)
    lesson_color5 = (255, 255, 255)
    lesson_color6 = (255, 255, 255)
    lesson_color7 = (255, 255, 255)
    lesson_color8 = (255, 255, 255)
    lesson_color9 = (255, 255, 255)

    # changing the color of the current lesson to red
    if school_day:
        if minute_time > 930:
            pass
        elif minute_time > 880:
            lesson_color9 = (255, 0, 0)
        elif minute_time > 830:
            lesson_color8 = (255, 0, 0)
        elif minute_time > 780:
            lesson_color7 = (255, 0, 0)
        elif minute_time > 725:
            lesson_color6 = (255, 0, 0)
        elif minute_time > 675:
            lesson_color5 = (255, 0, 0)
        elif minute_time > 625:
            lesson_color4 = (255, 0, 0)
        elif minute_time > 575:
            lesson_color3 = (255, 0, 0)
        elif minute_time > 525:
            lesson_color2 = (255, 0, 0)
        elif minute_time > 480:
            lesson_color1 = (255, 0, 0)
        else:
            pass

    label1 = font.render(lesson1, True, lesson_color1)
    label2 = font.render(lesson2, True, lesson_color2)
    label3 = font.render(lesson3, True, lesson_color3)
    label4 = font.render(lesson4, True, lesson_color4)
    label5 = font.render(lesson5, True, lesson_color5)
    label6 = font.render(lesson6, True, lesson_color6)
    label7 = font.render(lesson7, True, lesson_color7)
    label8 = font.render(lesson8, True, lesson_color8)
    label9 = font.render(lesson9, True, lesson_color9)

    label1rect = label1.get_rect()
    label2rect = label2.get_rect()
    label3rect = label3.get_rect()
    label4rect = label4.get_rect()
    label5rect = label5.get_rect()
    label6rect = label6.get_rect()
    label7rect = label7.get_rect()
    label8rect = label8.get_rect()
    label9rect = label9.get_rect()

    no_lesson_label = font.render('no lessons', True, (255, 255, 255))

    no_lesson_label_rect = no_lesson_label.get_rect()

    no_lesson_label_rect.center = (150, 150)

    if school_day:
        if not later_start:
            label1rect.center = (150, 30)
            label2rect.center = (150, 60)
            label3rect.center = (150, 90)
            label4rect.center = (150, 120)
            label5rect.center = (150, 150)
            label6rect.center = (150, 180)
            label7rect.center = (150, 210)
            label8rect.center = (150, 240)
            label9rect.center = (150, 270)

            screen.blit(label1, label1rect)
            screen.blit(label2, label2rect)
            screen.blit(label3, label3rect)
            screen.blit(label4, label4rect)
            screen.blit(label5, label5rect)
            screen.blit(label6, label6rect)
            screen.blit(label7, label7rect)
            screen.blit(label8, label8rect)
            screen.blit(label9, label9rect)
        else:
            label3rect.center = (150, 30)
            label4rect.center = (150, 60)
            label5rect.center = (150, 90)
            label6rect.center = (150, 120)
            label7rect.center = (150, 150)
            label8rect.center = (150, 180)
            label9rect.center = (150, 210)

            screen.blit(label3, label3rect)
            screen.blit(label4, label4rect)
            screen.blit(label5, label5rect)
            screen.blit(label6, label6rect)
            screen.blit(label7, label7rect)
            screen.blit(label8, label8rect)
            screen.blit(label9, label9rect)
    else:
        screen.blit(no_lesson_label, no_lesson_label_rect)

    return label1, label2, label3, label4, label5, label6, label7, label8, label9


while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(bg)

    plan_update(monday, tuesday, wednesday, thursday, friday, font, bg)

    pygame.display.update()



pygame.quit()
exit()
