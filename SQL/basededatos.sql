-- Base de datos: `bd_big_bread`
-- Estructura de tabla para la tabla `insumos`


CREATE TABLE `insumos` (
  `id_insumos` int(11) NOT NULL,
  `nombre` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;




-- Volcado de datos para la tabla `insumos`




INSERT INTO `insumos` (`id_insumos`, `nombre`) VALUES
(1, 'Oregano'),
(2, 'Pimenton'),
(3, 'Tomate'),
(4, 'Queso Mozzarella'),
(12339, 'anana'),
(12342, 'aceituna'),
(12343, 'aceituna');


-- --------------------------------------------------------




-- Estructura de tabla para la tabla `produccion_diaria`




CREATE TABLE `produccion_diaria` (
  `id_pd` int(11) NOT NULL,
  `fecha` date NOT NULL DEFAULT current_timestamp(),
  `cantidad` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;




-- Volcado de datos para la tabla `produccion_diaria`




INSERT INTO `produccion_diaria` (`id_pd`, `fecha`, `cantidad`, `id_producto`) VALUES
(3, '2023-06-06', 50, 160),
(7, '2023-06-06', 10, 2),
(8, '2023-06-08', 20, 160);


-- --------------------------------------------------------


--
-- Estructura de tabla para la tabla `productos`
--


CREATE TABLE `productos` (
  `id_producto` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


--
-- Volcado de datos para la tabla `productos`
--


INSERT INTO `productos` (`id_producto`, `nombre`) VALUES
(2, 'Muzza'),
(160, 'napo'),
(163, 'Especial');


-- --------------------------------------------------------




-- Estructura de tabla para la tabla `recetas`




CREATE TABLE `recetas` (
  `id_receta` int(11) NOT NULL,
  `pizza_nro` int(11) NOT NULL,
  `cantidad_insumos` int(11) NOT NULL,
  `id_insumos` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;




-- Volcado de datos para la tabla `recetas`




INSERT INTO `recetas` (`id_receta`, `pizza_nro`, `cantidad_insumos`, `id_insumos`) VALUES
(64, 160, 3, 1),
(65, 160, 5, 3),
(66, 2, 7, 2),
(67, 2, 15, 12339),
(68, 2, 13, 12342);










ALTER TABLE `insumos`
  ADD PRIMARY KEY (`id_insumos`);


ALTER TABLE `produccion_diaria`
  ADD PRIMARY KEY (`id_pd`),
  ADD KEY `id_producto` (`id_producto`);


ALTER TABLE `productos`
  ADD PRIMARY KEY (`id_producto`);


ALTER TABLE `recetas`
  ADD PRIMARY KEY (`id_receta`),
  ADD KEY `id_insumos` (`id_insumos`),
  ADD KEY `cf_pizza_nro` (`pizza_nro`);




--
-- AUTO_INCREMENT de la tabla `insumos`
--
ALTER TABLE `insumos`
  MODIFY `id_insumos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12344;


--
-- AUTO_INCREMENT de la tabla `produccion_diaria`
--
ALTER TABLE `produccion_diaria`
  MODIFY `id_pd` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;


--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=164;


--
-- AUTO_INCREMENT de la tabla `recetas`
--
ALTER TABLE `recetas`
  MODIFY `id_receta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;




--
-- Filtros para la tabla `produccion_diaria`
--
ALTER TABLE `produccion_diaria`
  ADD CONSTRAINT `id_producto` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`);


--
-- Filtros para la tabla `recetas`
--
ALTER TABLE `recetas`
  ADD CONSTRAINT `cf_pizza_nro` FOREIGN KEY (`pizza_nro`) REFERENCES `productos` (`id_producto`),
  ADD CONSTRAINT `id_insumos` FOREIGN KEY (`id_insumos`) REFERENCES `insumos` (`id_insumos`);
COMMIT;




