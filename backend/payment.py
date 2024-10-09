# backend/payment.py
from supabase_client import supabase

# Función para insertar un nuevo pago en la tabla 'payment'
def insert_payment(user_id, amount, payment_method, status):
    try:
        response = supabase.table('payment').insert([{
            'user_id': user_id,
            'amount': amount,
            'payment_method': payment_method,
            'status': status
        }]).execute()

        if response.data:
            print('Pago creado con éxito:', response.data)
            return response.data
        else:
            print('Error al crear el pago:', response)
            return None
    except Exception as e:
        print(f"Error al insertar el pago: {e}")
        return None

# Función para obtener todos los pagos de un usuario
def get_payments_by_user(user_id):
    try:
        response = supabase.table('payment').select('*').eq('user_id', user_id).execute()

        if response.data:
            print(f"Pagos encontrados para el usuario {user_id}:", response.data)
            return response.data
        else:
            print(f"No se encontraron pagos para el usuario {user_id}.")
            return []
    except Exception as e:
        print(f"Error al obtener los pagos: {e}")
        return []

# Función para actualizar el estado de un pago
def update_payment_status(payment_id, new_status):
    try:
        response = supabase.table('payment').update({
            'status': new_status
        }).eq('payment_id', payment_id).execute()

        if response.data:
            print(f"Estado del pago actualizado con éxito: {response.data}")
            return response.data
        else:
            print('Error al actualizar el estado del pago:', response)
            return None
    except Exception as e:
        print(f"Error al actualizar el estado del pago: {e}")
        return None

# Función para eliminar un pago
def delete_payment(payment_id):
    try:
        response = supabase.table('payment').delete().eq('payment_id', payment_id).execute()

        if response.data:
            print('Pago eliminado con éxito:', response.data)
            return response.data
        else:
            print('Error al eliminar el pago:', response)
            return None
    except Exception as e:
        print(f"Error al eliminar el pago: {e}")
        return None
