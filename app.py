from flask import Flask, render_template, request, jsonify,blueprints
from flask_mysqldb import MySQL
from views.authorRoutes import author_bp
from views.accountRoutes import account_bp
from views.userRoutes import user_bp
from views.bookRoutes import book_bp
from views.genreRoutes import genre_bp
from views import accountRoutes
from views import userRoutes
from views import bookRoutes
from views import genreRoutes

app = Flask(__name__)
accountRoutes.init_app(app)
userRoutes.init_app(app)
bookRoutes.init_app(app)
genreRoutes.init_app(app)
# Cấu hình kết nối đến cơ sở dữ liệu MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'doanchinh'

app.config['mysql'] = MySQL(app)  #

""" authors """
app.register_blueprint(author_bp)
""" accounts """
app.register_blueprint(account_bp)

""" auth """
""" book """
app.register_blueprint(book_bp)

""" bookAuthor """
""" bookGenre """
app.register_blueprint(genre_bp)

""" bookRating """
""" bookReview """
""" bookType """
""" genre """
""" paymentHistory """
""" payment """
""" subcriptionHistory """
""" subcription """
""" user """

app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(port=9999,debug=True)