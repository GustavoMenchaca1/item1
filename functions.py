def leer_datos(animals):
    import csv

    datos_dict = []
    try:
        f = open(animals, 'rt', enconding = 'utf8')
        filas = csv.reader(f)
        cabecera = next(filas)
        for fila in filas:
            item = dict(zip(cabecera, fila))
            datos_dict.append(item)
        f.close()
    except Exception as e:
        datos_dict.append(f'Sucedio un error {e}')
    finally:
        return datos_dict