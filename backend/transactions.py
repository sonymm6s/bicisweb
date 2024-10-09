# backend/transactions.py
from supabase_client import supabase

# Función para insertar una nueva transacción
def insert_transaction(transaction_id, add_id, user_id, date, price, status):
    try:
        # Insertar la transacción en la tabla 'transactions'
        response = supabase.table('transactions').insert([{
            'transaction_id': transaction_id,  # ID único de la transacción
            'add_id': add_id,                  # ID del anuncio (add_id)
            'user_id': user_id,                # ID del usuario (user_id)
            'date': date,                      # Fecha de la transacción
            'price': price,                    # Precio de la transacción
            'status': status                   # Estado de la transacción
        }]).execute()

        # Verificar si la transacción fue creada exitosamente
        if response.data:
            print('Transacción creada con éxito:', response.data)
            return response.data
        else:
            print('Error al crear la transacción:', response)
            return None
    except Exception as e:
        print(f"Error al insertar la transacción: {e}")
        return None

# Función para actualizar el estado de una transacción
def update_transaction_status(transaction_id, new_status):
    try:
        response = supabase.table('transactions').update({
            'status': new_status
        }).eq('transaction_id', transaction_id).execute()

        if response.data:
            print(f"Estado de la transacción actualizado con éxito: {response.data}")
            return response.data
        else:
            print('Error al actualizar el estado de la transacción:', response)
            return None
    except Exception as e:
        print(f"Error al actualizar el estado de la transacción: {e}")
        return None
