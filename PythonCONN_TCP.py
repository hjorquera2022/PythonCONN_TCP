import psutil

# Obtener todas las conexiones de red
conexiones = psutil.net_connections()

# Recorrer las conexiones y mostrar información relevante para las conexiones TCP
for conn in conexiones:
    # Filtrar las conexiones TCP
    if conn.type == psutil.CONN_TCP:
        print("Estado:", conn.status)
        print("Direccion local:", conn.laddr)
        print("Direccion remota:", conn.raddr)
        print("PID:", conn.pid)
        print("Nombre del proceso:", psutil.Process(conn.pid).name())
        print("---------------------------")