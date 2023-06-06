CREATE database bd_big_bread;
USE bd_big_bread;
CREATE TABLE `insumos` (
 `id_insumos` int(11) NOT NULL,
 `descripcion` varchar(70) NOT NULL,
 `cantidad_insumos` int(11) NOT NULL
);
CREATE TABLE `produccion_diaria` (
 `id_fecha` date NOT NULL DEFAULT current_timestamp(),
 `producto` int(11) NOT NULL,
 `cantidad` int(11) NOT NULL
);
CREATE TABLE `productos` (
 `id_producto` int(11) NOT NULL,
 `receta` int(11) NOT NULL,
 `nombre` varchar(30) NOT NULL
);
CREATE TABLE `recetas` (
 `id_receta` int(11) NOT NULL,
 `id_insumos` int(11) NOT NULL,
 `cantidad` int(11) NOT NULL,
 `nombre` varchar(30) NOT NULL
);
ALTER TABLE `insumos`
 ADD PRIMARY KEY (`id_insumos`);
ALTER TABLE `produccion_diaria`
 ADD PRIMARY KEY (`id_fecha`);
ALTER TABLE `productos`
 ADD PRIMARY KEY (`id_producto`);
-- AUTO_INCREMENT de las tablas volcadas
ALTER TABLE `insumos`
 MODIFY `id_insumos` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `productos`
 MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

SELECT * FROM insumos;
INSERT INTO bd_big_bread.insumos (id_insumos, descripcion, cantidad_insumos)VALUES(NULL, 'm', 300);
