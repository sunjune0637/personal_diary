class UserLoginForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired()])