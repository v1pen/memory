from PyQt5.QtCore import Qt
from random import randint
from random import shuffle
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, 
                           QVBoxLayout, QRadioButton, QHBoxLayout, QGroupBox, QButtonGroup)
app = QApplication([])
main_win = QWidget()
main_win.cur_question = -1
main_win.score = 0
main_win.total = 0


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


question_list = []
q1 = Question('вопрос1', 'ответ1', 'ответ2', 'ответ3', 'ответ4')
question_list.append(q1)
q2 = Question('вопрос2', 'ответ1', 'ответ2', 'ответ3', 'ответ4')
question_list.append(q2)
q3 = Question('вопрос3', 'ответ1', 'ответ2', 'ответ3', 'ответ4')
question_list.append(q3)




btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответов')


rbtn_2 = QRadioButton('Энцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Чульмцы')
rbtn_1 = QRadioButton('Алеуты')



layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)






layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результаты теста')
lb_Result = QLabel('прав ты или нет ')

lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)



layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.show()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)





layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=1)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)

layout_card.setSpacing(5)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следущий вопрос')


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


def start_test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()
#btn_OK.clicked.connect(start_test)



def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()




def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
        print(' Колличество вопросов:', main_win.total , ' Колличество правельных ответов:', main_win.score)
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
    print('Рейтинг:',round(main_win.score/main_win.total*100,2), '%')


def show_correct(res):
    lb_Result.setText(res)
    show_result()


def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
    
def next_question():
    main_win.total +=1
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)
AnsGroupBox.hide()

main_win.setLayout(layout_card)
main_win.setWindowTitle('Memory Card')

#q = Question('вопрос1', 'ответ1', 'ответ2', 'ответ3', 'ответ4')
#ask(q)

#ask('вопрос', 'ответ1', 'ответ2', 'ответ3', 'ответ4')

btn_OK.clicked.connect(click_ok)
next_question()
main_win.show()
app.exec()