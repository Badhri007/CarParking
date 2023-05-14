from carparking import app
# app.config['SECRET_KEY']='abcdefghijklmnop'
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
# app.config['TEMPLATES_AUTO_RELOAD'] = True

# db=SQLAlchemy(app)
# bcrypt=Bcrypt(app)
# login_manager=LoginManager(app)
# login_manager.login_view='login'
# login_manager.login_message_category='info'

	
if __name__=='__main__':
	app.run(debug=True)