from app import db

class Book(db.Model):

    __tablename__ = "book"

    isbn = db.Column(db.String(12), primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    created = db.Column(db.Date, nullable=False)
    price = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)

    def __init__(self, title, created, price, author_id=None):
        self.title = title
        self.created = created
        self.price = price
        self.author_id = author_id

    def __repr__(self):
        return f"<Book {self.title}>"

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Book.query.get(id)

    @staticmethod
    def get_all():
        return Book.query.all()



class Author(db.Model):

    __tablename__ = "author"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def __repr__(self):
        return f"<Author {self.name}>"

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Author.query.get(id)

    @staticmethod
    def get_all():
        return Author.query.all()
