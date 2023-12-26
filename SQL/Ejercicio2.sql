"""1. Crea una base de datos llamada "MiBaseDeDatos"."""

"""CREATE DATABASE MiBaseDeDatos;"""

"""2. Crea una tabla llamada "Usuarios" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "edad" (entero)."""

"""CREATE TABLE Usuarios (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER
);"""

"""3. Inserta dos registros en la tabla "Usuarios"."""

"""INSERT INTO Usuarios (id, nombre, edad) VALUES
(1, 'Javier', 32),
(2, 'Cristina', 29);"""

"""4. Actualiza la edad de un usuario en la tabla "Usuarios"."""

"""UPDATE Usuarios
SET edad = 25
WHERE nombre = 'Javier';"""

"""5. Elimina un usuario de la tabla "Usuarios"."""

"""DELETE FROM Usuarios
WHERE nombre = 'Cristina';"""

"""Nivel de dificultad Moderado """

"""1. Crea una tabla llamada "Ciudades" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "pais" (texto)."""

"""CREATE TABLE Ciudades (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    pais TEXT
);"""

"""2. Inserta al menos tres registros en la tabla "Ciudades"."""

    """INSERT INTO Ciudades (id, nombre, pais) VALUES
    (1, 'Cantabria', 'España'),
    (2, 'Madrid', 'España'),
    (3, 'Barcelona', 'España');"""

"""3. Crea una foreign key en la tabla "Usuarios" que se relacione con la columna "id"
de la tabla "Ciudades"."""

"""ALTER TABLE Usuarios
ADD CONSTRAINT fk_ciudades
FOREIGN KEY (id) REFERENCES Ciudades(id);"""

"""4. Realiza una consulta que muestre los nombres de los usuarios junto con el
nombre de su ciudad y país (utiliza un LEFT JOIN)."""

"""SELECT Usuarios.nombre, Ciudades.nombre AS ciudad, Ciudades.pais
FROM Usuarios
LEFT JOIN Ciudades ON Usuarios.id = Ciudades.id;"""

""". Realiza una consulta que muestre solo los usuarios que tienen una ciudad
asociada (utiliza un INNER JOIN)."""

"""SELECT Usuarios.nombre, Ciudades.nombre AS ciudad, Ciudades.pais
FROM Usuarios
INNER JOIN Ciudades ON Usuarios.id = Ciudades.id;"""