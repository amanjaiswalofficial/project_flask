# Import the database object (db) from the main application module
from marshmallow import fields

from app import db, ma
from app.auth.constants import ErrorMessage


class Base(db.Model):
    """
     Define a base model for other database tables to inherit
    """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )


class User(Base):
    """
    Define a User model
    """

    __tablename__ = "auth_user"

    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)

    @staticmethod
    def create(name, email, password):
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(name=name,
                        email=email,
                        password=password)
            db.session.add(user)
            db.session.commit()
            return user_schema.dump(user)
        else:
            raise ValueError(ErrorMessage.EMAIL_ALREADY_EXISTS)

    def __repr__(self):
        return "<User %r>" % self.name


class UserSchema(ma.SQLAlchemyAutoSchema):
    """
    Defined User schema
    """
    # password will not be send in response.
    password = fields.Str(load_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'date_created',
                  'date_modified')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
