from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3 

question_list = []
question_list.append(Question("Kako se zove najveći Srpski vladar","Dušan","Uroš","burek","Karlo"))
question_list.append(Question("Gdje se nalčazi BiH na","Balkanu","Himalajima","Južno Kineskom moru","Skandinaviji"))
question_list.append(Question("Koji je bio nadimak cara Dušana","Dušan silni","Dušan nejaki","Hajduk","Poglavica"))
question_list.append(Question("Koje je godine počeo drugi svjetski rat","1939","2021","1940","1873"))
question_list.append(Question("Koje se godine završio drugi svjetski rat", "1945","2022","2018","1946"))
question_list.append(Question("Dali je Italija 1942 bila monarhija", "Ne","Da", "Možda","Za Italiju neznam ali jeste Velika Britanija")) 
question_list.append(Question("Kada je stvorena SFRJ ","1945","1946","1888","9999"))
question_list.append(Question("Zašto su vinske flaše 750ml","Zato što je ljudski kapacitet pluća otprilike 750ml","Jer to nije ni previše ni premalo","Zbog liepog izgleda", "Bezveze"))
question_list.append(Question("Od kada Švajcarska nije učestvovala ni u jednom ratu","1848", "1945", "Od juče", "3723"))
question_list.append(Question("Koji je zadnji protivnik Švajcarske","Švajcarska","Srbija","Australija","Kristofer Kolumbo"))
question_list.append(Question("Koliko program ima godina","2","3","4","5"))
question_list.append(Question("Kako se zove najvisi vrh na svietu","Mont Everest","Banja Luka","Sibir","Petrovo"))

app = QApplication([])

btn_Answer = QPushButton("Answer")
lb_Question = QLabel("Kako se zove nastavnik?")

RadioGroupBox = QGroupBox("Answer options")

rbtn_1 = QRadioButton("Pero")
rbtn_2 = QRadioButton("Milijan")
rbtn_3 = QRadioButton("Drazen")
rbtn_4 = QRadioButton("Nastavnik")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox ("Test result")
lb_Result = QLabel("True/False")
lb_Corect = QLabel("Correct answer")

layout_result = QVBoxLayout()
layout_result.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_result.addWidget(lb_Corect, alignment=Qt.AlignHCenter, stretch=2 )

AnsGroupBox.setLayout(layout_result)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)

AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_Answer, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.addSpacing(5)

AnsGroupBox.hide()

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_Answer.setText("Next question")

def show_question():
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_Answer.setText("Answer")
        RadioGroup.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroup.setExclusive(True)

answer = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q:Question):

        shuffle (answer)
        answer[0].setText(q.right_answer)
        answer[1].setText(q.wrong1)
        answer[2].setText(q.wrong2)
        answer[3].setText(q.wrong3)
        lb_Question.setText(q.question)
        lb_Corect.setText(q.right_answer)
        show_question()

def start_test():
        if "Answers" == btn_Answer.text():
            show_result()
        else:
            show_question()

def show_correct(res):
        lb_Result.setText(res)
        show_result()

def check_answer():
        if answer[0].isChecked():
            show_correct("Correct!")
            window.score+=1
            print("Statistic \n - Total question:", window.total,"\n Right answers:", window.score)
            print("Rating:",(window.score / window.total)*100, "%")
        else:
            if answer[1].isChecked() or answer[3].isChecked():
                show_correct ("Incorect!")

def next_question():
    window.total += 1
    print("Statistic \n - Total question:", window.total,"\n Right answers:", window.score)
    cur_question = randint(0,len(question_list)-1)
    q = question_list [cur_question]
    ask(q)

def click_OK(): 
    if btn_Answer.text() == "Answer":
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.cur_question = - 1
btn_Answer.clicked.connect(click_OK)
window.score = 0 
window.total = 0
next_question()
window.show()
app.exec()