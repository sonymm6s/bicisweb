# backend/adds.py
from supabase_client import supabase

def insert_add(title, description, price, image_url, location, lock_code, user_id):
    try:
        # Realizar la inserción en la tabla 'adds'
        response = supabase.table('adds').insert([{
            'title': title,
            'description': description,
            'price': price,
            'image': image_url,
            'location': location,
            'lock_code': lock_code,
            'user_id': user_id
        }]).execute()

        # Devolver la respuesta completa
        return response
    except Exception as exception:
        # En caso de error, devolver la excepción
        return exception
    
# Función para actualizar el precio de un anuncio
def update_add_price(add_id, new_price):
    try:
        # Realizar la actualización del precio en la tabla 'adds'
        response = supabase.table('adds').update({
            'price': new_price
        }).eq('add_id', add_id).execute()

        # Devolver la respuesta completa
        return response
    except Exception as exception:
        # En caso de error, devolver la excepción
        return exception

def get_seller_adds(user_id):
    try:
        response = supabase.table('adds').select('*').eq('user_id', user_id).execute()

        if response.data:
            return response.data
        else:
            return []
    except Exception as e:
        print(f"Error al obtener los anuncios del vendedor: {e}")
        return []
    
def update_add_price(add_id, new_price):
    try:
        response = supabase.table('adds').update({
            'price': new_price
        }).eq('add_id', add_id).execute()

        return response
    except Exception as e:
        return e
    
def delete_add(add_id, user_id):
    try:
        # Verificamos que el anuncio pertenezca al vendedor (user_id)
        response = supabase.table('adds').delete().eq('add_id', add_id).eq('user_id', user_id).execute()

        # Verificamos si la eliminación fue exitosa
        if response.data:
            return {"status": "success", "message": "Anuncio eliminado con éxito", "data": response.data}
        else:
            return {"status": "error", "message": "No se pudo eliminar el anuncio o no existe"}
    except Exception as e:
        return {"status": "error", "message": str(e)}