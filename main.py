import smtplib
import os

login = 'serhii.alieksieiev@yandex.ru'
password = os.getenv("PASSWORD")
email_from = 'serhii.alieksieiev@yandex.ru'
email_to = 'se.alieksieiev@gmail.com'

link = "dvmn.org"
friend_name = "Сергей"
my_name = "Сергей Алексеев"
headlines = """\
From:{0} 
To:{1} 
Subject: Курс Python на Devman
Content-Type: text/plain; charset="UTF-8";
""".format(email_from, email_to)

message_template = """
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""
message_with_text = message_template.replace("%website%", link)
message_with_text = message_with_text.replace("%friend_name%", friend_name)
message_with_text = message_with_text.replace("%my_name%", my_name)

letter = "{0}{1}".format(headlines, message_with_text)
encoded_letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
server.sendmail(email_from, email_to, encoded_letter)
server.quit()
