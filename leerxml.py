from xml.dom import minidom
doc = minidom.parse("archivo.xml")
#nombre = doc.getElementsByTagName("nombre")[0]
#print(nombre.firstChild.data)
empleados = doc.getElementsByTagName("empleado")
for empleado in empleados:
    sid = empleado.getAttribute("id")
    username = empleado.getElementsByTagName("username")[0]
    password = empleado.getElementsByTagName("password")[0]
    puesto = empleado.getElementsByTagName("puesto")[0]
    if puesto.firstChild.data == "VP":
        print(f"id: {sid}")
        print(f"username: {username.firstChild.data}")
        print(f"password: {password.firstChild.data}")
        print(f"puesto: {puesto.firstChild.data}")
