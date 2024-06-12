from app.database import db

class Reserva(db.Model):
    __tablename__ = "reserva"
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,nullable = False)
    restaurant_id = db.Column(db.Integer,nullable = False)
    reservation_date = db.Column(db.Date,nullable = False)
    num_guests = db.Column(db.Integer,nullable = False)
    special_request = db.Column(db.String(50),nullable=False)
    status = db.Column(db.String(50),nullable = False)

    def __init__(self,user_id,restaurant_id,reservation_date,num_guests,special_request,status):
        self.user_id = user_id
        self.restaurant_id = restaurant_id
        self.reservation_date = reservation_date
        self.num_guests = num_guests
        self.special_request = special_request
        self.status = status

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self,user_id = None,restaurant_id = None,reservation_date = None,num_guests = None,special_request = None,status = None):
        if user_id is not None:
            self.user_id = user_id
        if restaurant_id is not None:
            self.restaurant_id = restaurant_id
        if reservation_date is not None:
            self.reservation_date = reservation_date
        if num_guests is not None:
            self.num_guests = num_guests
        if special_request is not None:
            self.special_request = special_request
        if status is not None:
            self.status = status
        
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_all_reservaciones():
        return Reserva.query.all()

    @staticmethod
    def get_id_reservacion(id):
        return Reserva.query.get(id)
