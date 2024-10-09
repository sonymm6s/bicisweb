# backend/transactions.py
from supabase_client import supabase

# Función para insertar una nueva transacción
def insert_transaction(payment_id, transaction_date, amount, status):
    try:
        response = supabase.table('transactions').insert([{
            'payment_id': payment_id,
            'transaction_date': transaction_date,
            'amount': amount,
            'status': status
        }]).execute()

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
