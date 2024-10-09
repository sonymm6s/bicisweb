# backend/payment.py
from supabase_client import supabase

# Función para insertar un nuevo pago en la tabla 'payment'
def insert_payment(transaction_id, amount, payment_method, payment_status):
    try:
        # Verificar que el estado es un valor permitido
        if payment_status not in ['pending', 'approved', 'failed']:
            print(f"Error: El estado '{payment_status}' no es válido.")
            return None

        # Insertar el pago en la tabla 'payments'
        response = supabase.table('payments').insert([{
            'transaction_id': transaction_id,
            'amount': amount,
            'payment_method': payment_method,
            'payment_status': payment_status
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
        # Verificar que el nuevo estado es un valor permitido
        if new_status not in ['pending', 'approved', 'failed']:
            print(f"Error: El estado '{new_status}' no es válido.")
            return None

        # Actualizar el estado del pago en la tabla 'payments'
        response = supabase.table('payments').update({
            'payment_status': new_status
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

# Función para actualizar el estado del pago cuando se complete
def complete_payment(payment_id):
    response = supabase.table('payments').update({
        'payment_status': 'completed'
    }).eq('payment_id', payment_id).execute()

    if response.data:
        print(f"Pago {payment_id} actualizado a 'completed'")
        return True
    else:
        print(f"Error al actualizar el pago {payment_id}")
        return False

