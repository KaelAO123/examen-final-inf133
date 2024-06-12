def render_reservas(reservas):
    return [
        {
            "id":reserva.id,
            "user_id":reserva.user_id,
            "restaruant_id":reserva.restaruant_id,
            "reservation_date":reserva.reservation_date,
            "num_guest":reserva.num_guest,
            "special_requests":reserva.special_requests,
            "status":reserva.status
        } for reserva in reservas
    ]

def render_detail_reserva(reserva):
    return {
            "id":reserva.id,
            "user_id":reserva.user_id,
            "restaruant_id":reserva.restaruant_id,
            "reservation_date":reserva.reservation_date,
            "num_guest":reserva.num_guest,
            "special_requests":reserva.special_requests,
            "status":reserva.status
    }