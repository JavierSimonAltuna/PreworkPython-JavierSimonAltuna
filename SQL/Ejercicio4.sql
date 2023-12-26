"""Nivel de dificultad: Experto"""
"""1. Crea una tabla llamada "Pedidos" con las columnas: "id" (entero, clave
primaria), "id_usuario" (entero, clave foránea de la tabla "Usuarios") y
"id_producto" (entero, clave foránea de la tabla "Productos")."""

"""CREATE TABLE Pedidos (
    id SERIAL PRIMARY KEY,
    id_usuario INT REFERENCES Usuarios(id),
    id_producto INT REFERENCES Productos(id)
);"""

"""2. Inserta al menos tres registros en la tabla "Pedidos" que relacionen usuarios con
productos."""

"""INSERT INTO Pedidos (id_usuario, id_producto) VALUES
(1, 1),
(2, 4),
(2, 3);"""

"""3. Realiza una consulta que muestre los nombres de los usuarios y los nombres de
los productos que han comprado, incluidos aquellos que no han realizado
ningún pedido (utiliza LEFT JOIN y COALESCE)."""

"""SELECT Usuarios.nombre AS nombre_usuario, COALESCE(Productos.nombre, 'No ha realizado ningún pedido') AS nombre_producto
FROM Usuarios
LEFT JOIN Pedidos ON Usuarios.id = Pedidos.id_usuario
LEFT JOIN Productos ON Pedidos.id_producto = Productos.id;"""

"""4. Realiza una consulta que muestre los nombres de los usuarios que han
realizado un pedido, pero también los que no han realizado ningún pedido
(utiliza LEFT JOIN)."""

"""SELECT Usuarios.nombre AS nombre_usuario
FROM Usuarios
LEFT JOIN Pedidos ON Usuarios.id = Pedidos.id_usuario
GROUP BY Usuarios.nombre;"""

"""5. Agrega una nueva columna llamada "cantidad" a la tabla "Pedidos" y actualiza
los registros existentes con un valor (utiliza ALTER TABLE y UPDATE)"""

"""ALTER TABLE Pedidos
ADD cantidad INT;"""

"""UPDATE Pedidos
SET cantidad = 10;"""