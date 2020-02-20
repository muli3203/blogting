from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required, DataRequired


class BlogForm(FlaskForm):
    category = SelectField(
        "Select Category",
        choices=[
            ("product", "Product"),
            ("interview", "Interview"),
            ("promotion", "Promotion"),
        ],
    )
    content = TextAreaField("Your Blog")
    submit = SubmitField("Create Blog")


class CommentForm(FlaskForm):
    comment = TextAreaField("Comment")
    submit = SubmitField("Submit")


class UpdateProfile(FlaskForm):
    username = StringField("Username")
    bio = TextAreaField("Tell us about yourself")
    submit = SubmitField("Update")
