from flask import Flask, render_template
from flask_login import login_required, logout_user, login_user, LoginManager, current_user
from werkzeug.utils import redirect

from data import db_session
from data.topics import Topics, Subtopics, Exercises, Subjects

from data.users import Users, User_exercises
from forms.answer import AnswerForm
from forms.users import RegisterForm, LoginForm

app = Flask(__name__)
db_session.global_init("db/info.db")
db_sess = db_session.create_session()

app.config['SECRET_KEY'] = 'project_web'

@app.route("/")
def index():
    return render_template("index.html", title="Главная")

@app.route("/<sbj_name>")
def topics(sbj_name):
    topics = db_sess.query(Topics).join(Subjects).filter(Subjects.name == sbj_name)
    return render_template("topics.html", title=sbj_name, topics=topics)


@app.route("/<topic>/subtopics")
def subtopic_page(topic):

    subtopics = db_sess.query(Subtopics).join(Topics).filter(Topics.name == topic)
    exercises = {}
    for sb in subtopics:
        exercises[sb.id] = {}
        for ex in db_sess.query(Exercises).filter(Exercises.subtopics_id == sb.id):
            if db_sess.query(User_exercises).filter(User_exercises.exercise_id == ex.id).first():
                exercises[sb.id][ex] = 1
            else:
                exercises[sb.id][ex] = 0
            print(ex.answer)
    return render_template("subtopics.html", title=topic, exercises=exercises, subtopics=subtopics)

@app.route("/<sb>/theory")
def theory(sb):
    sb = db_sess.query(Subtopics).filter(Subtopics.name == sb).first()
    file = f'static/theory_data/{sb.topic_id}.{sb.id}.pdf'
    return render_template("theory.html", title=sb.name, file=file, topic=sb.topics.name)

@app.route("/<sb>/exercise/<number>", methods=['GET', 'POST'])
def ex_page(sb, number):
    exercise = db_sess.query(Exercises).join(Subtopics).filter((Subtopics.name == sb), (Exercises.number == int(number))).first()
    topic = db_sess.query(Subtopics).filter(Subtopics.name == sb).first().topics.name

    num = db_sess.query(Exercises).filter((Subtopics.name == sb))[-1].number
    form = AnswerForm()
    if db_sess.query(User_exercises).filter((User_exercises.exercise_id == exercise.id), (User_exercises.user_id==current_user.id)).first():
        form.answer.data = exercise.answer
        message = "Решено"
    else:
        if form.validate_on_submit():
            if form.answer.data == exercise.answer:
                us_ex = User_exercises(exercise_id=exercise.id, user_id=current_user.id)
                db_sess.add(us_ex)
                db_sess.commit()
                return render_template('exercises.html',
                                       message="Правильный ответ",
                                       exercise=exercise,
                                       form=form, title=sb, num=num, topic=topic)

            else:
                return render_template('exercises.html',
                                       message="Неправильный ответ",
                                       exercise=exercise,
                                       form=form, title=sb, num=num, topic=topic)
        message='''Если ответов несколько, введите ответ через точку с запятой без пробелов.
        Десятичное число через запятую'''



    return render_template("exercises.html", exercise=exercise, form=form, title=sb, num=num, topic=topic, message=message)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(Users).filter(Users.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = Users(
            name=form.name.data,
            email=form.email.data,
            surname=form.surname.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(Users).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(Users).filter(Users.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/logout')
@login_required

def logout():
    logout_user()
    return redirect("/")



if __name__ == '__main__':

    app.run(port=8000, host='127.0.0.1')
