from gamestar import db


class User(db.Model):
    """Schema for the User model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.username


class Game(db.Model):
    """Schema for the Task model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    artwork = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Boolean, default=False, nullable=False)
    igdb_id = db.Column(db.Integer, unique=True, nullable=False)
    cover_art = db.Column(db.Text, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.name


class Review(db.Model):
    """Schema for the review model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=False
        )
    game_id = db.Column(
        db.Integer, db.ForeignKey('game.id'), nullable=False
    )
    rating = db.Column(db.Float, nullable=False)
    heading = db.Column(db.Text, nullable=False)
    liked_text = db.Column(db.Text, nullable=False)
    disliked_text = db.Column(db.Text, nullable=False)
    hours = db.Column(db.Integer, nullable=False)
    likes = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=True
        )
    dislikes = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=True
        )

    def __repr__(self):
        # __repr__ to represent itself in the for of a string
        return self.heading