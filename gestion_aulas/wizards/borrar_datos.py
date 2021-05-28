import logging
from xml.dom import minidom
import psycopg2
_logger = logging.getLogger(__name__)


def borrar_reservas(host, db, usuario, contrasenya):
    try:
        conn = None
        conn = psycopg2.connect(host=host, database=db, user=usuario, password=contrasenya)
        cur = conn.cursor()
        cur.execute("DELETE FROM gestion_aulas_reserva_model")
        conn. commit()
    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()

def borrar_horario(host, db, usuario, contrasenya):
    try:
        conn = None
        conn = psycopg2.connect(host=host, database=db, user=usuario, password=contrasenya)
        cur = conn.cursor()
        cur.execute("DELETE FROM gestion_aulas_horario_model")
        conn. commit()
    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()

def borrar_tramos(host, db, usuario, contrasenya):
    try:
        conn = None
        conn = psycopg2.connect(host=host, database=db, user=usuario, password=contrasenya)
        cur = conn.cursor()
        cur.execute("DELETE FROM gestion_aulas_tramo_model")
        conn. commit()
    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()

def borrar_profesores(host, db, usuario, contrasenya):
    try:
        conn = None
        conn = psycopg2.connect(host=host, database=db, user=usuario, password=contrasenya)
        cur = conn.cursor()
        cur.execute("DELETE FROM gestion_aulas_profesor_model")
        conn. commit()
    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()

def borrar_grupos(host, db, usuario, contrasenya):
    try:
        conn = None
        conn = psycopg2.connect(host=host, database=db, user=usuario, password=contrasenya)
        cur = conn.cursor()
        cur.execute("DELETE FROM gestion_aulas_grupo_model")
        conn. commit()
    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()

def borrar_aulas(host, db, usuario, contrasenya):
    try:
        conn = None
        conn = psycopg2.connect(host=host, database=db, user=usuario, password=contrasenya)
        cur = conn.cursor()
        cur.execute("DELETE FROM gestion_aulas_aulas_model")
        conn. commit()
    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()

def borrar_asignatura(host, db, usuario, contrasenya):
    try:
        conn = None
        conn = psycopg2.connect(host=host, database=db, user=usuario, password=contrasenya)
        cur = conn.cursor()
        cur.execute("DELETE FROM gestion_aulas_asignatura_model")
        conn. commit()
    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()

def alter_secuencias(host, db, usuario, contrasenya):
    try:
        conn = None
        conn = psycopg2.connect(host=host, database=db, user=usuario, password=contrasenya)
        cur = conn.cursor()
        #sql = "ALTER SEQUENCE gestion_aulas_tramo_model_id_seq RESTART WITH 1;"
        cur.execute("ALTER SEQUENCE gestion_aulas_tramo_model_id_seq RESTART WITH 1;")
        cur.execute("ALTER SEQUENCE gestion_aulas_aulas_model_id_seq RESTART WITH 1;")
        cur.execute("ALTER SEQUENCE gestion_aulas_asignatura_model_id_seq RESTART WITH 1;")
        cur.execute("ALTER SEQUENCE gestion_aulas_grupo_model_id_seq RESTART WITH 1;")
        conn. commit()
    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()