

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";



--
-- Base de datos: `bd_big_bread`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `insumos`
--

CREATE TABLE `insumos` (
  `id_insumos` int(11) NOT NULL,
  `nombre` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `insumos`
--

INSERT INTO `insumos` (`id_insumos`, `nombre`) VALUES
(1, 'Aceitunas Verdes'),
(2, 'Dientes de ajo picado'),
(3, 'Queso Muzzarella'),
(4, 'Rodajas de Anana'),
(5, 'Salsa de tomates'),
(6, 'Cebolla'),
(7, 'Fetas de Jamon crudo'),
(8, 'Morron en tiras'),
(9, 'Rucula'),
(10, 'Champiñones'),
(11, 'Fetas de Jamon cocido'),
(12, 'Oregano disecado'),
(13, 'Rodajas de tomate'),
(14, 'Provenzal'),
(15, 'Aceitunas negras'),
(16, 'Queso Provolone'),
(17, 'Rodajas de salame'),
(18, 'Masa'),
(19, 'Cerezas'),
(20, 'Provenzal disecado'),
(21, 'Queso Roquefort'),
(22, 'Huevo duro picado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `produccion_diaria`
--

CREATE TABLE `produccion_diaria` (
  `id_pd` int(11) NOT NULL,
  `fecha` date NOT NULL DEFAULT current_timestamp(),
  `cantidad` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `produccion_diaria`
--

INSERT INTO `produccion_diaria` (`id_pd`, `fecha`, `cantidad`, `id_producto`) VALUES
(8, '2023-06-08', 20, 160),
(11, '2023-06-15', 3, 159),
(12, '2023-06-16', 5, 166),
(13, '2023-06-19', 1, 165),
(14, '2023-06-19', 10, 163);

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
(159, 'Fugazzeta'),
(160, 'Muzzarella'),
(163, 'Carioca'),
(165, 'Rucula'),
(166, 'Especial'),
(167, 'Champiñones'),
(168, 'Primavera'),
(169, 'Provenzal'),
(170, 'Calabresa'),
(171, 'Napolitana'),
(172, 'pizza prueba');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recetas`
--

CREATE TABLE `recetas` (
  `id_receta` int(11) NOT NULL,
  `pizza_nro` int(11) NOT NULL,
  `cantidad_insumos` int(11) NOT NULL,
  `id_insumos` int(11) NOT NULL,
  `unidad_de_medida` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `recetas`
--

INSERT INTO `recetas` (`id_receta`, `pizza_nro`, `cantidad_insumos`, `id_insumos`, `unidad_de_medida`) VALUES
(64, 160, 150, 1, 'grs'),
(65, 160, 250, 3, 'grs'),
(66, 163, 250, 3, 'grs'),
(70, 159, 10, 12, 'grs'),
(72, 163, 10, 7, 'u'),
(73, 165, 500, 18, 'grs'),
(74, 159, 2, 6, 'u'),
(75, 159, 150, 1, 'grs'),
(76, 160, 500, 18, 'grs'),
(77, 159, 500, 18, 'grs'),
(78, 160, 10, 12, 'grs'),
(79, 163, 500, 18, 'grs'),
(80, 163, 250, 3, 'grs'),
(81, 163, 150, 5, 'grs'),
(82, 163, 8, 4, 'u'),
(83, 163, 100, 19, 'grs'),
(84, 163, 150, 15, 'grs'),
(85, 165, 250, 3, 'grs'),
(86, 165, 150, 5, 'grs'),
(87, 165, 10, 7, 'u'),
(88, 165, 200, 9, 'grs'),
(89, 165, 150, 16, 'grs'),
(90, 165, 150, 15, 'grs'),
(91, 166, 500, 18, 'grs'),
(92, 166, 250, 3, 'grs'),
(93, 166, 150, 5, 'grs'),
(94, 166, 10, 11, 'u'),
(95, 166, 8, 8, 'u'),
(96, 166, 10, 12, 'grs'),
(97, 166, 150, 1, 'grs'),
(98, 167, 500, 18, 'grs'),
(99, 167, 250, 3, 'grs'),
(100, 167, 150, 5, 'grs'),
(101, 167, 150, 10, 'grs'),
(102, 167, 5, 2, 'u'),
(103, 167, 150, 20, 'grs'),
(104, 167, 150, 21, 'grs'),
(105, 167, 10, 12, 'grs'),
(106, 167, 150, 1, 'grs'),
(107, 168, 500, 18, 'grs'),
(108, 168, 150, 5, 'grs'),
(109, 168, 250, 3, 'grs'),
(110, 168, 8, 13, 'grs'),
(111, 168, 2, 22, 'u'),
(112, 168, 150, 16, 'grs'),
(113, 168, 10, 12, 'grs'),
(114, 168, 150, 1, 'grs'),
(115, 169, 500, 18, 'grs'),
(116, 169, 250, 3, 'grs'),
(117, 169, 4, 2, 'u'),
(118, 169, 30, 20, 'grs'),
(119, 169, 150, 5, 'grs'),
(120, 169, 8, 13, 'u'),
(121, 170, 500, 18, 'grs'),
(122, 170, 150, 5, 'grs'),
(123, 170, 250, 3, 'grs'),
(124, 170, 20, 17, 'u'),
(125, 170, 10, 20, 'grs'),
(126, 170, 10, 12, 'grs'),
(127, 170, 150, 1, 'grs'),
(128, 171, 500, 18, 'grs'),
(129, 171, 150, 5, 'grs'),
(130, 171, 250, 3, 'grs'),
(131, 171, 8, 13, 'u'),
(132, 171, 250, 16, 'grs'),
(133, 171, 10, 20, 'grs'),
(134, 171, 10, 12, 'grs'),
(135, 171, 150, 1, 'grs'),
(137, 172, 10, 22, 'u'),
(138, 172, 3, 6, 'u');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `insumos`
--
ALTER TABLE `insumos`
  ADD PRIMARY KEY (`id_insumos`);

--
-- Indices de la tabla `produccion_diaria`
--
ALTER TABLE `produccion_diaria`
  ADD PRIMARY KEY (`id_pd`),
  ADD KEY `id_producto` (`id_producto`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id_producto`);

--
-- Indices de la tabla `recetas`
--
ALTER TABLE `recetas`
  ADD PRIMARY KEY (`id_receta`),
  ADD KEY `cf_pizza_nro` (`pizza_nro`),
  ADD KEY `id_insumos` (`id_insumos`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `insumos`
--
ALTER TABLE `insumos`
  MODIFY `id_insumos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `produccion_diaria`
--
ALTER TABLE `produccion_diaria`
  MODIFY `id_pd` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=173;

--
-- AUTO_INCREMENT de la tabla `recetas`
--
ALTER TABLE `recetas`
  MODIFY `id_receta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=139;

--
-- Restricciones para tablas volcadas
--

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

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
