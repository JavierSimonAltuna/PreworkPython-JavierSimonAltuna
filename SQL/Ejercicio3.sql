"""Nivel de dificultad: Difícil"""

"""1. Crea una tabla llamada "Productos" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "precio" (numérico)."""

"""CREATE TABLE Productos (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    precio NUMERIC
);""" 

"""2. Inserta al menos cinco registros en la tabla "Productos"."""

"""INSERT INTO Productos (nombre, precio) VALUES
('Producto 1', 10.50),
('Producto 2', 15.25),
('Producto 3', 7.30),
('Producto 4', 11.75),
('Producto 5', 8.60);"""

"""3. Actualiza el precio de un producto en la tabla "Productos"."""

"""UPDATE Productos
SET precio = 20.00
WHERE id = 1;"""

"""4. Elimina un producto de la tabla "Productos"."""

"""DELETE FROM Productos
WHERE id = 2;"""

"""5. Realiza una consulta que muestre los nombres de los usuarios junto con los
nombres de los productos que han comprado (utiliza un INNER JOIN con la
tabla "Productos")."""

"""SELECT Usuarios.nombre AS nombre_usuario, Productos.nombre AS nombre_producto
FROM Compras
INNER JOIN Usuarios ON Compras.id_usuario = Usuarios.id
INNER JOIN Productos ON Compras.id_producto = Productos.id;"""

