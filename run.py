from App import app, db
from App.model import tables

if __name__ == "__main__":
    with app.test_request_context():
        db.create_all()sa
    db.update(tables.Publi)
    db.update(tables.User)
    app.run()