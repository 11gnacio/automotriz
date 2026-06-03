SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema registroautomotriz
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS registroautomotriz DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE registroautomotriz ;

-- -----------------------------------------------------
-- Table registroautomotriz.estados_pago_multa (Reemplaza al ENUM)
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS registroautomotriz.estados_pago_multa (
  estado_pago_id INT NOT NULL AUTO_INCREMENT,
  nombre_estado VARCHAR(20) NOT NULL,
  -- Campos de Auditoría Solicitados
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  created_by INT NOT NULL DEFAULT 1, -- ID del usuario del sistema que crea el registro
  deleted TINYINT(1) NOT NULL DEFAULT 0, -- 0 = Activo, 1 = Borrado lógico
  PRIMARY KEY (estado_pago_id),
  UNIQUE INDEX nombre_estado_UNIQUE (nombre_estado ASC)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table registroautomotriz.estados_vehiculo
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS registroautomotriz.estados_vehiculo (
  estado_id INT NOT NULL AUTO_INCREMENT,
  nombre_estado VARCHAR(40) NOT NULL,
  -- Campos de Auditoría Solicitados
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  created_by INT NOT NULL DEFAULT 1,
  deleted TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (estado_id),
  UNIQUE INDEX nombre_estado_UNIQUE (nombre_estado ASC)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table registroautomotriz.marcas
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS registroautomotriz.marcas (
  marca_id INT NOT NULL AUTO_INCREMENT,
  nombre_marca VARCHAR(50) NOT NULL,
  -- Campos de Auditoría Solicitados
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  created_by INT NOT NULL DEFAULT 1,
  deleted TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (marca_id),
  UNIQUE INDEX nombre_marca_UNIQUE (nombre_marca ASC)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table registroautomotriz.modelos
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS registroautomotriz.modelos (
  modelo_id INT NOT NULL AUTO_INCREMENT,
  marca_id INT NOT NULL,
  nombre_modelo VARCHAR(50) NOT NULL,
  -- Campos de Auditoría Solicitados
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  created_by INT NOT NULL DEFAULT 1,
  deleted TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (modelo_id),
  INDEX fk_modelos_marcas_idx (marca_id ASC),
  CONSTRAINT fk_modelos_marcas
    FOREIGN KEY (marca_id)
    REFERENCES registroautomotriz.marcas (marca_id)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table registroautomotriz.tipos_combustible
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS registroautomotriz.tipos_combustible (
  combustible_id INT NOT NULL AUTO_INCREMENT,
  nombre_combustible VARCHAR(30) NOT NULL,
  -- Campos de Auditoría Solicitados
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  created_by INT NOT NULL DEFAULT 1,
  deleted TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (combustible_id),
  UNIQUE INDEX nombre_combustible_UNIQUE (nombre_combustible ASC)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table registroautomotriz.monedas
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS registroautomotriz.monedas (
  moneda_id VARCHAR(5) NOT NULL,
  nombre_moneda VARCHAR(50) NOT NULL,
  -- Campos de Auditoría Solicitados
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  created_by INT NOT NULL DEFAULT 1,
  deleted TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (moneda_id)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table registroautomotriz.propietarios
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS registroautomotriz.propietarios (
  propietario_id INT NOT NULL AUTO_INCREMENT,
  documento_identidad VARCHAR(20) NOT NULL,
  nombre VARCHAR(50) NOT NULL,
  apellido VARCHAR(50) NOT NULL,
  telefono VARCHAR(20) NULL DEFAULT NULL,
  email VARCHAR(100) NULL DEFAULT NULL,
  direccion TEXT NULL DEFAULT NULL,
  -- Campos de Auditoría Solicitados
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  created_by INT NOT NULL DEFAULT 1,
  deleted TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (propietario_id),
  UNIQUE INDEX documento_identidad_UNIQUE (documento_identidad ASC)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table registroautomotriz.vehiculos
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS registroautomotriz.vehiculos (
  vehiculo_id INT NOT NULL AUTO_INCREMENT,
  patente_dominio VARCHAR(15) NOT NULL,
  vin_chasis VARCHAR(17) NOT NULL,
  modelo_id INT NOT NULL,
  combustible_id INT NOT NULL,
  moneda_id VARCHAR(5) NOT NULL,
  estado_id INT NOT NULL,
  anio_fabricacion INT NOT NULL,
  color VARCHAR(20) NULL DEFAULT 'Blanco',
  precio_adquisicion DECIMAL(12,2) NOT NULL DEFAULT 0.00,
  valor_fiscal DECIMAL(12,2) NULL DEFAULT 0.00,
  kilometraje INT NOT NULL DEFAULT 0,
  fecha_adquisicion DATE NOT NULL,
  propietario_actual_id INT NULL DEFAULT NULL,
  -- Campos de Auditoría Solicitados
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  created_by INT NOT NULL DEFAULT 1,
  deleted TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (vehiculo_id),
  UNIQUE INDEX patente_dominio_UNIQUE (patente_dominio ASC),
  UNIQUE INDEX vin_chasis_UNIQUE (vin_chasis ASC),
  INDEX fk_vehiculos_modelos_idx (modelo_id ASC),
  INDEX fk_vehiculos_combustibles_idx (combustible_id ASC),
  INDEX fk_vehiculos_monedas_idx (moneda_id ASC),
  INDEX fk_vehiculos_estados_idx (estado_id ASC),
  INDEX fk_vehiculos_propietarios_idx (propietario_actual_id ASC),
  CONSTRAINT fk_vehiculos_modelos
    FOREIGN KEY (modelo_id)
    REFERENCES registroautomotriz.modelos (modelo_id),
  CONSTRAINT fk_vehiculos_combustibles
    FOREIGN KEY (combustible_id)
    REFERENCES registroautomotriz.tipos_combustible (combustible_id),
  CONSTRAINT fk_vehiculos_monedas
    FOREIGN KEY (moneda_id)
    REFERENCES registroautomotriz.monedas (moneda_id),
  CONSTRAINT fk_vehiculos_estados
    FOREIGN KEY (estado_id)
    REFERENCES registroautomotriz.estados_vehiculo (estado_id),
  CONSTRAINT fk_vehiculos_propietarios
    FOREIGN KEY (propietario_actual_id)
    REFERENCES registroautomotriz.propietarios (propietario_id)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table registroautomotriz.ventas
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS registroautomotriz.ventas (
  venta_id INT NOT NULL AUTO_INCREMENT,
  vehiculo_id INT NOT NULL,
  vendedor_id INT NULL DEFAULT NULL,
  comprador_id INT NOT NULL,
  fecha_venta DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  precio_venta DECIMAL(12,2) NOT NULL,
  moneda_id VARCHAR(5) NOT NULL,
  -- Campos de Auditoría Solicitados
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  created_by INT NOT NULL DEFAULT 1,
  deleted TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (venta_id),
  INDEX fk_ventas_vehiculos_idx (vehiculo_id ASC),
  INDEX fk_ventas_vendedor_idx (vendedor_id ASC),
  INDEX fk_ventas_comprador_idx (comprador_id ASC),
  INDEX fk_ventas_monedas_idx (moneda_id ASC),
  CONSTRAINT fk_ventas_vehiculos
    FOREIGN KEY (vehiculo_id)
    REFERENCES registroautomotriz.vehiculos (vehiculo_id),
  CONSTRAINT fk_ventas_vendedor
    FOREIGN KEY (vendedor_id)
    REFERENCES registroautomotriz.propietarios (propietario_id),
  CONSTRAINT fk_ventas_comprador
    FOREIGN KEY (comprador_id)
    REFERENCES registroautomotriz.propietarios (propietario_id),
  CONSTRAINT fk_ventas_monedas
    FOREIGN KEY (moneda_id)
    REFERENCES registroautomotriz.monedas (moneda_id)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table registroautomotriz.multas
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS registroautomotriz.multas (
  multa_id INT NOT NULL AUTO_INCREMENT,
  vehiculo_id INT NOT NULL,
  fecha_infraccion DATETIME NOT NULL,
  descripcion TEXT NOT NULL,
  monto DECIMAL(10,2) NOT NULL,
  estado_pago_id INT NOT NULL DEFAULT 1,
  -- Campos de Auditoría
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  created_by INT NOT NULL DEFAULT 1,
  deleted TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (multa_id),
  INDEX fk_multas_vehiculos_idx (vehiculo_id ASC),
  INDEX fk_multas_estados_pago_idx (estado_pago_id ASC),
  CONSTRAINT fk_multas_vehiculos
    FOREIGN KEY (vehiculo_id)
    REFERENCES registroautomotriz.vehiculos (vehiculo_id),
  CONSTRAINT fk_multas_estados_pago
    FOREIGN KEY (estado_pago_id)
    REFERENCES registroautomotriz.estados_pago_multa (estado_pago_id)
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Llenar tablas de información (DML)
-- -----------------------------------------------------

-- 1. Estados de pago
INSERT INTO registroautomotriz.estados_pago_multa (estado_pago_id, nombre_estado) VALUES 
(1, 'Pendiente'), (2, 'Pagado'), (3, 'Apelado');

-- 2. Estados del vehículo
INSERT INTO registroautomotriz.estados_vehiculo (nombre_estado) VALUES 
('Excelente'), ('Buen Estado'), ('Regular'), ('En Reparación');

-- 3. Marcas
INSERT INTO registroautomotriz.marcas (nombre_marca) VALUES 
('Toyota'), ('Ford'), ('Volkswagen');

-- 4. Modelos
INSERT INTO registroautomotriz.modelos (marca_id, nombre_modelo) VALUES 
(1, 'Corolla'), (2, 'Mustang'), (3, 'Golf');

-- 5. Tipos de Combustible
INSERT INTO registroautomotriz.tipos_combustible (nombre_combustible) VALUES 
('Nafta / Gasolina'), ('Diesel'), ('Híbrido'), ('Eléctrico');

-- 6. Monedas
INSERT INTO registroautomotriz.monedas (moneda_id, nombre_moneda) VALUES 
('USD', 'Dólar Estadounidense'), ('ARS', 'Peso Argentino'), ('EUR', 'Euro');

-- 7. Propietarios
INSERT INTO registroautomotriz.propietarios (documento_identidad, nombre, apellido, telefono, email, direccion) VALUES 
('11223344', 'Juan', 'Pérez', '555-1234', 'juan@email.com', 'Calle Falsa 123'),
('55667788', 'María', 'Gómez', '555-5678', 'maria@email.com', 'Av. Siempre Viva 742');

-- 8. Vehículos
INSERT INTO registroautomotriz.vehiculos (patente_dominio, vin_chasis, modelo_id, combustible_id, moneda_id, estado_id, anio_fabricacion, color, precio_adquisicion, valor_fiscal, kilometraje, fecha_adquisicion, propietario_actual_id) VALUES 
('ABC123_XYZ', 'VIN12345678901234', 1, 3, 'USD', 1, 2022, 'Gris', 25000.00, 24000.00, 15000, '2023-01-15', 1),
('DEF456_WXY', 'VIN98765432109876', 2, 1, 'USD', 2, 2020, 'Rojo', 45000.00, 42000.00, 30000, '2021-06-20', 2);

-- 9. Ventas
INSERT INTO registroautomotriz.ventas (vehiculo_id, vendedor_id, comprador_id, precio_venta, moneda_id) VALUES 
(1, NULL, 1, 26000.00, 'USD');

-- 10. Multas
INSERT INTO registroautomotriz.multas (vehiculo_id, fecha_infraccion, descripcion, monto) VALUES 
(1, '2026-06-02 14:30:00', 'Exceso de velocidad en autopista', 150.00);

-- SELECCIONADOR
SELECT * FROM marcas;
SELECT * FROM vehiculos;

-- SUPER MOGOLLON ULTRA GOD XRD INNER JOIN CHAD!!!!
SELECT 
    v.vehiculo_id,
    v.patente_dominio AS Patente,
    ma.nombre_marca AS Marca,
    mo.nombre_modelo AS Modelo,
    tc.nombre_combustible AS Combustible,
    ev.nombre_estado AS Estado_Vehiculo,
    v.anio_fabricacion AS Anio,
    CONCAT(p.nombre, ' ', p.apellido) AS Propietario_Actual
FROM registroautomotriz.vehiculos v
-- 1. Traemos la información del modelo
INNER JOIN registroautomotriz.modelos mo 
    ON v.modelo_id = mo.modelo_id
-- 2. Desde el modelo, saltamos a la marca
INNER JOIN registroautomotriz.marcas ma 
    ON mo.marca_id = ma.marca_id
-- 3. Traemos el tipo de combustible
INNER JOIN registroautomotriz.tipos_combustible tc 
    ON v.combustible_id = tc.combustible_id
-- 4. Traemos el estado físico del vehículo
INNER JOIN registroautomotriz.estados_vehiculo ev 
    ON v.estado_id = ev.estado_id
-- 5. Usamos LEFT JOIN para el propietario (por si el auto está en stock y no tiene dueño aún)
LEFT JOIN registroautomotriz.propietarios p 
    ON v.propietario_actual_id = p.propietario_id
-- Filtramos para mostrar solo los registros que no estén borrados lógicamente
WHERE v.deleted = 0;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;