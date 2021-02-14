from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required


class LoginForm(Form):
    """Accepts a nickname and a room."""
    name = StringField('ユーザー名', validators=[Required()])
    room = StringField('部屋名', validators=[Required()])
    submit = SubmitField('部屋に入ってチャットを開始する')
