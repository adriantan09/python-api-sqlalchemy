from app import db

class Game(db.Model):
    __tablename__ = "games"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    publisher = db.Column(db.Text, nullable=False)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f"Name: {self.name}, Price: {self.price}, Publisher: {self.publisher}"
