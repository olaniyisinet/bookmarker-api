export FLASK_ENV=development
export FLASK_APP=src
#export SQLALCHEMY_DB_URI=sqlite:///bookmarks.db
export SQLALCHEMY_DB_URI=postgresql://postgres:postgres@localhost/APITest
export JWT_SECRET_KEY='JWT_SECRET_KEY'
