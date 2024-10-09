# backend/images.py
from supabase_client import supabase

# Función para subir una imagen a Supabase Storage
def upload_image(file_path, file_name):
    try:
        # Accedemos a la carpeta de almacenamiento 'imagenes_bicicletas'
        storage = supabase.storage()
        response = storage.from_('imagenes_bicicletas').upload(file_name, open(file_path, 'rb'))

        # Verificar si ocurrió un error
        if 'error' in response:
            print('Error al subir la imagen:', response['error'])
        else:
            print('Imagen subida con éxito:', response['data'])
    except Exception as e:
        print(f"Excepción al subir la imagen: {e}")

# Función para obtener la URL pública de una imagen almacenada en Supabase
def get_image_url(file_name):
    try:
        # Obtener la URL pública de la imagen
        storage = supabase.storage()
        response = storage.from_('imagenes_bicicletas').get_public_url(file_name)

        # Verificar si ocurrió un error
        if 'error' in response:
            print('Error al obtener la URL de la imagen:', response['error'])
        else:
            return response['publicURL']
    except Exception as e:
        print(f"Excepción al obtener la URL de la imagen: {e}")
        return None
