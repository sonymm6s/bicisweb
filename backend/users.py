# backend/users.py
import os
from supabase_client import supabase

def insert_user(user_name, email, password):
    try:
        # Imprimir los datos que se van a insertar
        print(f"Intentando insertar: user_name={user_name}, email={email}, password={password}")
        # Insertar el usuario en la tabla 'users'
        response = supabase.table('users').insert({
            'user_name': user_name,  # Campo correcto
            'email': email,  # Campo correcto
            'password': password  # Campo correcto
        }).execute()
        # Imprimir la respuesta completa para ver qué ocurrió
        print(f"Respuesta de Supabase: {response}")

        # Verificar si la inserción fue exitosa
        if response.data:
            print('Usuario creado con éxito:', response.data)
        else:
            print('No se insertó ningún dato.')
    except Exception as e:
        print(f"Error al insertar usuario: {e}")

