def render_restaurantes(restaurantes):
    return [
        {
            "id":restaurante.id,
            "name":restaurante.name,
            "address":restaurante.address,
            "city":restaurante.city,
            "phone":restaurante.phone,
            "description":restaurante.description,
            "rating":restaurante.rating
        } for restaurante in restaurantes
    ]

def render_detail_restaurante(restaurante):
    return {
            "id":restaurante.id,
            "name":restaurante.name,
            "address":restaurante.address,
            "city":restaurante.city,
            "phone":restaurante.phone,
            "description":restaurante.description,
            "rating":restaurante.rating
    }