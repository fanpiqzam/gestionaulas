import logging
from xml.dom import minidom
from odoo.exceptions import ValidationError
import psycopg2
_logger = logging.getLogger(__name__)

def insertar_asignaturas(archivo, host, db, usuario, contrasenya):
    try:
        conn = None
        conn = psycopg2.connect(host=host, database=db, user=usuario, password=contrasenya)
        cur = conn.cursor()

        postgres_insert_asig = """INSERT INTO gestion_aulas_asignatura_model (id, name, abreviatura) VALUES (%s,%s,%s)"""

        doc = minidom.parse(archivo)
        items = doc.getElementsByTagName('ASIGNATURA')

        for elem in items:
            num_int_as = elem.attributes['num_int_as'].value
            abreviatura = elem.attributes['abreviatura'].value
            nombre_asig = elem.attributes['nombre'].value
            record_to_insert = (num_int_as, nombre_asig, abreviatura)
            cur.execute(postgres_insert_asig,record_to_insert)
            conn. commit()
            count = cur.rowcount

    except (Exception, psycopg2.Error) as error:
        raise ValidationError(error)
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_grupos(archivo, host, db, usuario, contrasenya):
    try:
        conn = None
        conn = psycopg2.connect(host=host, database=db, user=usuario, password=contrasenya)
        cur = conn.cursor()

        postgres_insert_gr = """INSERT INTO gestion_aulas_grupo_model (id, name, abreviatura) VALUES (%s,%s,%s)"""

        doc = minidom.parse(archivo)
        items = doc.getElementsByTagName('GRUPO')

        for elem in items:
            num_int_gr = elem.attributes['num_int_gr'].value
            abreviatura = elem.attributes['abreviatura'].value
            nombre_grupo = elem.attributes['nombre'].value
            record_to_insert = (num_int_gr, nombre_grupo, abreviatura)
            cur.execute(postgres_insert_gr,record_to_insert)
            conn. commit()
            count = cur.rowcount
        print
    except (Exception, psycopg2.Error) as error:
        raise ValidationError(error)
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_aulas(archivo, host, db, usuario, contrasenya):
    try:
        conn = None
        conn = psycopg2.connect(host=host, database=db, user=usuario, password=contrasenya)
        cur = conn.cursor()

        postgres_insert_au = """INSERT INTO gestion_aulas_aulas_model (id, name, abreviatura) VALUES (%s,%s,%s)"""

        doc = minidom.parse(archivo)
        items = doc.getElementsByTagName('AULA')

        for elem in items:
            num_int_au = elem.attributes['num_int_au'].value
            abreviatura = elem.attributes['abreviatura'].value
            nombre_aula = elem.attributes['nombre'].value
            record_to_insert = (num_int_au, nombre_aula, abreviatura)
            cur.execute(postgres_insert_au,record_to_insert)
            conn. commit()
            count = cur.rowcount
        print
    except (Exception, psycopg2.Error) as error:
        raise ValidationError(error)
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_profesores(archivo, host, db, usuario, contrasenya):
    try:
        conn = None
        conn = psycopg2.connect(host=host, database=db, user=usuario, password=contrasenya)
        cur = conn.cursor()

        postgres_insert_pr = """INSERT INTO gestion_aulas_profesor_model (id, name, abreviatura) VALUES (%s,%s,%s)"""

        doc = minidom.parse(archivo)
        items = doc.getElementsByTagName('PROFESOR')

        for elem in items:
            num_int_pr = elem.attributes['num_int_pr'].value
            abreviatura = elem.attributes['abreviatura'].value
            nombre_prof = elem.attributes['nombre'].value
            record_to_insert = (num_int_pr, nombre_prof, abreviatura)
            cur.execute(postgres_insert_pr,record_to_insert)
            conn. commit()
            count = cur.rowcount
        print
    except (Exception, psycopg2.Error) as error:
        raise ValidationError(error)
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_tramos(archivo, host, db, usuario, contrasenya):
    try:
        conn = None
        conn = psycopg2.connect(host=host, database=db, user=usuario, password=contrasenya)
        cur = conn.cursor()

        postgres_insert_tr = """INSERT INTO gestion_aulas_tramo_model (numero, dia, hora) VALUES (%s,%s,%s)"""

        doc = minidom.parse(archivo)
        items = doc.getElementsByTagName('TRAMO')
        horas_dia = {
        1:"08:00",2:"08:55",3:"09:50",4:"10:45",5:"11:15",6:"12:10",7:"13:05",8:"14:00",9:"14:55",
        10:"08:00",11:"08:55",12:"09:50",13:"10:45",14:"11:15",15:"12:10",16:"13:05",17:"14:00",18:"14:55",
        19:"08:00",20:"08:55",21:"09:50",22:"10:45",23:"11:15",24:"12:10",25:"13:05",26:"14:00",27:"14:55",
        28:"08:00",29:"08:55",30:"09:50",31:"10:45",32:"11:15",33:"12:10",34:"13:05",35:"14:00",36:"14:55",
        37:"08:00",38:"08:55",39:"09:50",40:"10:45",41:"11:15",42:"12:10",43:"13:05",44:"14:00",45:"14:55",
        }
        dia = ""

        for elem in items:
            num_tr = (int(elem.attributes['num_tr'].value))
            if num_tr == 1:
                dia="lunes"
            if num_tr == 10:
                dia ="martes"
            if num_tr == 19:
                dia ="miercoles"
            if num_tr == 28:
                dia ="jueves"
            if num_tr == 37:
                dia ="viernes"
            record_to_insert = (num_tr, dia, horas_dia[num_tr])
            cur.execute(postgres_insert_tr,record_to_insert)
            conn. commit()
            count = cur.rowcount
        print
    except (Exception, psycopg2.Error) as error:
        raise ValidationError(error)
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_horario(archivo, host, db, usuario, contrasenya):
    try:
        conn = None
        conn = psycopg2.connect(host=host, database=db, user=usuario, password=contrasenya)
        cur = conn.cursor()

        postgres_insert_hr = """INSERT INTO gestion_aulas_horario_model (grupo_id, aula_id, tramo_id, asignatura_id) VALUES (%s,%s,%s,%s)"""

        mydoc = minidom.parse(archivo)
        items = mydoc.getElementsByTagName('HORARIO_GRUP')
        
        for elem in items:
            grupo_id = elem.attributes['hor_num_int_gr'].value
            
            for act in elem.childNodes:
                if type(act)==minidom.Element:
                    tramo_id = int(act.attributes['tramo'].value)
                    asignatura_id = act.attributes['asignatura'].value
                    aula_id = act.attributes['aula'].value
                    record_to_insert = (grupo_id, aula_id, tramo_id, asignatura_id)
                    _logger.info(postgres_insert_hr)
                    _logger.info(record_to_insert)
                    cur.execute(postgres_insert_hr,record_to_insert)
                    conn. commit()
                    count = cur.rowcount
    except (Exception, psycopg2.Error) as error:
        raise ValidationError(error)
    finally:
        if conn:
            cur.close()
            conn.close()