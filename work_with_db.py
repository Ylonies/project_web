from data import db_session
#в файле происходит работа с базой данных
from data.topics import Subtopics, Topics, Exercises, Subjects

db_session.global_init("db/info.db")

# db_sess = db_session.create_session()
# sbj = Subjects(name="Алгебра")
# topic = Topics(name="Алгебраические уравнения", subjects_id=1)
# subtopic = Subtopics(name="Квадратные уравнения. Теорема Виета", theory="1_1.pdf", topic_id=1)
# subtopic2 = Subtopics(name="Многочлены", theory="1_2.pdf", topic_id=1)
# db_sess.add(sbj)
# db_sess.add(topic)
# db_sess.add(subtopic)
# db_sess.add(subtopic2)

# ex = Exercises(subtopics_id=, text = "",
#                answer="", number=)
# ex1 = Exercises(subtopics_id=1, text="Чему равен больший корень уравнения x2+1001x+1000=0?",
#                answer="-1", number=1)
# ex2 = Exercises(subtopics_id=1, text="Коэффициенты уравнения x2 + px + q = 0 подобраны так, что p + q = 30, и уравнение имеет целые корни. Найдите все возможные значения q.",
#                answer="0;64", number=2)
# ex3 = Exercises(subtopics_id=1, text= """Петя и Вася придумали десять квадратных трёхчленов. Затем Вася по очереди называл последовательные натуральные числа (начиная с некоторого), а Петя каждое названное число подставлял в один из трёхчленов по своему выбору и записывал полученные значения на доску слева направо. Оказалось, что числа, записанные на доске, образуют арифметическую прогрессию (именно в этом порядке).
# Какое максимальное количество чисел Вася мог назвать?""", answer="20", number=3, subtopics=subtopic)
# ex4 = Exercises(subtopics_id=2, text = "При каком значении a многочлен x^100500 + ax^77 + 7 делится на x + 1? ",
#                answer="8", number=1)
# ex5 = Exercises(subtopics_id=2, text = "Квадратные трехчлены P(x) = x 2 + x 2 + b и Q(x) = x 2 + cx + d с вещественными коэффициентами таковы, что P(x)Q(x) = Q(P(x)) для всех x. Найдите все вещественные корни уравнения P(Q(x)) = 0.",
#                answer="0,5;1", number=2)
# ex6 = Exercises(subtopics_id=2, text="Дан многочлен P(x) с целыми коэффициентами. Известно, что P(1) = 2013, P(2013) = 1, P(k) = k, где k — некоторое целое число. Найдите k.",
#                 answer="1007", number=3)
# db_sess.add(ex1)
# db_sess.add(ex2)
# db_sess.add(ex3)
# db_sess.add(ex4)
# db_sess.add(ex5)
# db_sess.add(ex6)
# db_sess.commit()