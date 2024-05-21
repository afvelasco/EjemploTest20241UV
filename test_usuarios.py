from conexion import *
from models.usuarios import usuarios
import hashlib
import pytest

'''
    def setup():
        # Se ejecuta una vez antes de cada prueba en la clase

    def teardown():
        # Se ejecuta una vez después de cada prueba en la clase

    def setup_class():
        # Se ejecuta una vez antes de todas pruebas de la clase

    def teardown_class():
        # Se ejecuta una vez después de todas pruebas de la clase
'''

class Test_Usuarios:
    @pytest.mark.parametrize(
            ["id","contra","id_entrada","contra_entrada","esperado"],
            [("afv","hola","afv","hola",True),
            ("afv","hola","afv","1234",False),
            ("afv","hola","dsa","2342",False)]
    )

    def test_valida_login(id,contra,id_entrada,contra_entrada,esperado):
        # Prepreparar entorno de prueba
        cifrada = hashlib.sha512(contra.encode("UTF-8")).hexdigest()
        sql = f"INSERT INTO usuarios (id,contrasena,nombre,rol) VALUES ('{id}','{cifrada}','AF Velaso',1)"
        cursor = mi_DB.cursor()
        cursor.execute(sql)
        mi_DB.commit()
        # Ejecutar el método a probar (la prueba)
        resultado = usuarios.valida_login(id_entrada, contra_entrada)
        # Limpiar la base de datos
        sql=f"DELETE FROM usuarios WHERE id='{id}'"
        cursor.execute(sql)
        mi_DB.commit()
        # Verificar resultados
        assert resultado == esperado
