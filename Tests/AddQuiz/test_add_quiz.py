import time
import os
from selenium import webdriver
from Tests.Pages.loginPage import LoginPage
from Tests.Pages.addQuizPage import AddQuizPage


class Test_Add_Quiz:
    driver = webdriver.Chrome('../../chromedriver/chromedriver.exe')
    question_dict = {"5 x 5 ?" : ['25','24','0','7','6'],
                     "10 * 0" : ['0','4','2','7','8'],
                     "3^3?" : ['27','4','2','0','5'],}

    def test_quiz_add(self):
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:8000/')
        loginP = LoginPage(self.driver)
        loginP.click_on_login_button()
        loginP.enter_username('teacher')
        loginP.enter_password('teacher')
        loginP.confirm_login_button()
        quizP = AddQuizPage(self.driver)
        quizP.go_to_quiz_add_page()
        quizP.enter_quiz_name("TEST QUIZ2")
        quizP.pick_subject()
        quizP.save_quiz_name_and_subject()
        for i in range(len(self.question_dict)):
            key_list = list(self.question_dict.keys())
            value_list = list(self.question_dict.values())
            quizP.goto_add_question_page()
            quizP.enter_question_text(key_list[i])
            #იგივე ლოკატორი აქვს და მერე ჩავამატებ ცალკე მეთოდად
            quizP.save_quiz_name_and_subject()
            anwser_inputs = self.driver.find_elements_by_xpath('//input[@class="textinput textInput form-control"]')
            for j in range(len(anwser_inputs)):
                time.sleep(1)
                anwser_inputs[j].send_keys(value_list[i][j])
            quizP.choose_correct_anwser()
            quizP.add_answers_all()






