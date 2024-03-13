-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server versie:                11.4.0-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Versie:              12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Databasestructuur van sensor_data wordt geschreven
CREATE DATABASE IF NOT EXISTS `sensor_data` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;
USE `sensor_data`;

-- Structuur van  tabel sensor_data.auth_group wordt geschreven
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumpen data van tabel sensor_data.auth_group: ~0 rows (ongeveer)

-- Structuur van  tabel sensor_data.auth_group_permissions wordt geschreven
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumpen data van tabel sensor_data.auth_group_permissions: ~0 rows (ongeveer)

-- Structuur van  tabel sensor_data.auth_permission wordt geschreven
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumpen data van tabel sensor_data.auth_permission: ~32 rows (ongeveer)
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add user', 4, 'add_user'),
	(14, 'Can change user', 4, 'change_user'),
	(15, 'Can delete user', 4, 'delete_user'),
	(16, 'Can view user', 4, 'view_user'),
	(17, 'Can add content type', 5, 'add_contenttype'),
	(18, 'Can change content type', 5, 'change_contenttype'),
	(19, 'Can delete content type', 5, 'delete_contenttype'),
	(20, 'Can view content type', 5, 'view_contenttype'),
	(21, 'Can add session', 6, 'add_session'),
	(22, 'Can change session', 6, 'change_session'),
	(23, 'Can delete session', 6, 'delete_session'),
	(24, 'Can view session', 6, 'view_session'),
	(25, 'Can add data point', 7, 'add_datapoint'),
	(26, 'Can change data point', 7, 'change_datapoint'),
	(27, 'Can delete data point', 7, 'delete_datapoint'),
	(28, 'Can view data point', 7, 'view_datapoint'),
	(29, 'Can add device data', 8, 'add_devicedata'),
	(30, 'Can change device data', 8, 'change_devicedata'),
	(31, 'Can delete device data', 8, 'delete_devicedata'),
	(32, 'Can view device data', 8, 'view_devicedata');

-- Structuur van  tabel sensor_data.auth_user wordt geschreven
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumpen data van tabel sensor_data.auth_user: ~1 rows (ongeveer)
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$720000$uZxwGQcxAyqoQc9TEAKPHP$7kbJTCg46PkUXyO9r1QNaFH9J6Yo3W1oOtMTOj6vGDw=', '2024-02-28 13:32:27.564497', 1, 'edwin', '', '', '', 1, 1, '2024-02-28 13:32:09.355819');

-- Structuur van  tabel sensor_data.auth_user_groups wordt geschreven
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumpen data van tabel sensor_data.auth_user_groups: ~0 rows (ongeveer)

-- Structuur van  tabel sensor_data.auth_user_user_permissions wordt geschreven
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumpen data van tabel sensor_data.auth_user_user_permissions: ~0 rows (ongeveer)

-- Structuur van  tabel sensor_data.datapoint wordt geschreven
CREATE TABLE IF NOT EXISTS `datapoint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` int(11) DEFAULT NULL,
  `gate_way_receive_time` datetime DEFAULT current_timestamp(),
  `device` int(11) DEFAULT NULL,
  `value` decimal(10,0) DEFAULT NULL,
  `human_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_datapoint_data` (`timestamp`,`gate_way_receive_time`,`device`,`value`,`human_name`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumpen data van tabel sensor_data.datapoint: ~42 rows (ongeveer)
INSERT INTO `datapoint` (`id`, `timestamp`, `gate_way_receive_time`, `device`, `value`, `human_name`) VALUES
	(7, 1709706116, '2024-03-06 10:48:30', 322, 4, 'battery_voltage_events'),
	(13, 1709706116, '2024-03-06 10:48:42', 322, 4, 'battery_voltage_events'),
	(19, 1709706116, '2024-03-06 10:50:38', 322, 4, 'battery_voltage_events'),
	(25, 1709706116, '2024-03-06 10:54:52', 322, 4, 'battery_voltage_events'),
	(10, 1709718094, '2024-03-06 10:48:33', 322, 0, 'soil_electric_conductivity_events'),
	(11, 1709718094, '2024-03-06 10:48:34', 322, 1, 'soil_relative_permittivity_events'),
	(12, 1709718094, '2024-03-06 10:48:35', 322, 25, 'soil_temperature_events'),
	(16, 1709718094, '2024-03-06 10:48:46', 322, 0, 'soil_electric_conductivity_events'),
	(17, 1709718094, '2024-03-06 10:48:47', 322, 1, 'soil_relative_permittivity_events'),
	(18, 1709718094, '2024-03-06 10:48:48', 322, 25, 'soil_temperature_events'),
	(22, 1709718094, '2024-03-06 10:50:42', 322, 0, 'soil_electric_conductivity_events'),
	(23, 1709718094, '2024-03-06 10:50:43', 322, 1, 'soil_relative_permittivity_events'),
	(24, 1709718094, '2024-03-06 10:50:44', 322, 25, 'soil_temperature_events'),
	(28, 1709718094, '2024-03-06 10:54:56', 322, 0, 'soil_electric_conductivity_events'),
	(29, 1709718094, '2024-03-06 10:54:57', 322, 1, 'soil_relative_permittivity_events'),
	(30, 1709718094, '2024-03-06 10:54:58', 322, 25, 'soil_temperature_events'),
	(8, 1709718361, '2024-03-06 10:48:31', 256, 0, 'par_events'),
	(9, 1709718361, '2024-03-06 10:48:32', 256, 42, 'relative_humidity_events'),
	(14, 1709718361, '2024-03-06 10:48:44', 256, 0, 'par_events'),
	(15, 1709718361, '2024-03-06 10:48:45', 256, 42, 'relative_humidity_events'),
	(20, 1709718361, '2024-03-06 10:50:40', 256, 0, 'par_events'),
	(21, 1709718361, '2024-03-06 10:50:41', 256, 42, 'relative_humidity_events'),
	(26, 1709718361, '2024-03-06 10:54:54', 256, 0, 'par_events'),
	(27, 1709718361, '2024-03-06 10:54:55', 256, 42, 'relative_humidity_events'),
	(34, 1710324458, '2024-03-13 11:23:04', 322, 0, 'soil_electric_conductivity_events'),
	(35, 1710324458, '2024-03-13 11:23:05', 322, 1, 'soil_relative_permittivity_events'),
	(36, 1710324458, '2024-03-13 11:23:06', 322, 14, 'soil_temperature_events'),
	(40, 1710324458, '2024-03-13 11:25:13', 322, 0, 'soil_electric_conductivity_events'),
	(41, 1710324458, '2024-03-13 11:25:14', 322, 1, 'soil_relative_permittivity_events'),
	(42, 1710324458, '2024-03-13 11:25:15', 322, 14, 'soil_temperature_events'),
	(46, 1710324458, '2024-03-13 11:27:50', 322, 0, 'soil_electric_conductivity_events'),
	(47, 1710324458, '2024-03-13 11:27:51', 322, 1, 'soil_relative_permittivity_events'),
	(48, 1710324458, '2024-03-13 11:27:52', 322, 14, 'soil_temperature_events'),
	(52, 1710324458, '2024-03-13 11:28:04', 322, 0, 'soil_electric_conductivity_events'),
	(53, 1710324458, '2024-03-13 11:28:05', 322, 1, 'soil_relative_permittivity_events'),
	(54, 1710324458, '2024-03-13 11:28:06', 322, 14, 'soil_temperature_events'),
	(58, 1710324458, '2024-03-13 11:30:13', 322, 0, 'soil_electric_conductivity_events'),
	(59, 1710324458, '2024-03-13 11:30:14', 322, 1, 'soil_relative_permittivity_events'),
	(60, 1710324458, '2024-03-13 11:30:15', 322, 14, 'soil_temperature_events'),
	(64, 1710324458, '2024-03-13 11:30:52', 322, 0, 'soil_electric_conductivity_events'),
	(65, 1710324458, '2024-03-13 11:30:53', 322, 1, 'soil_relative_permittivity_events'),
	(66, 1710324458, '2024-03-13 11:30:54', 322, 14, 'soil_temperature_events'),
	(70, 1710324458, '2024-03-13 11:31:31', 322, 0, 'soil_electric_conductivity_events'),
	(71, 1710324458, '2024-03-13 11:31:32', 322, 1, 'soil_relative_permittivity_events'),
	(72, 1710324458, '2024-03-13 11:31:33', 322, 14, 'soil_temperature_events'),
	(76, 1710324458, '2024-03-13 11:32:09', 322, 0, 'soil_electric_conductivity_events'),
	(77, 1710324458, '2024-03-13 11:32:10', 322, 1, 'soil_relative_permittivity_events'),
	(78, 1710324458, '2024-03-13 11:32:11', 322, 14, 'soil_temperature_events'),
	(31, 1710324477, '2024-03-13 11:23:00', 322, 4, 'battery_voltage_events'),
	(37, 1710324477, '2024-03-13 11:25:09', 322, 4, 'battery_voltage_events'),
	(43, 1710324477, '2024-03-13 11:27:46', 322, 4, 'battery_voltage_events'),
	(49, 1710324477, '2024-03-13 11:28:00', 322, 4, 'battery_voltage_events'),
	(55, 1710324477, '2024-03-13 11:30:09', 322, 4, 'battery_voltage_events'),
	(61, 1710324477, '2024-03-13 11:30:48', 322, 4, 'battery_voltage_events'),
	(67, 1710324477, '2024-03-13 11:31:26', 322, 4, 'battery_voltage_events'),
	(73, 1710324477, '2024-03-13 11:32:05', 322, 4, 'battery_voltage_events'),
	(32, 1710325132, '2024-03-13 11:23:01', 256, 0, 'par_events'),
	(33, 1710325132, '2024-03-13 11:23:03', 256, 65, 'relative_humidity_events'),
	(38, 1710325431, '2024-03-13 11:25:10', 256, 0, 'par_events'),
	(39, 1710325431, '2024-03-13 11:25:12', 256, 65, 'relative_humidity_events'),
	(44, 1710325431, '2024-03-13 11:27:48', 256, 0, 'par_events'),
	(45, 1710325431, '2024-03-13 11:27:49', 256, 65, 'relative_humidity_events'),
	(50, 1710325431, '2024-03-13 11:28:01', 256, 0, 'par_events'),
	(51, 1710325431, '2024-03-13 11:28:03', 256, 65, 'relative_humidity_events'),
	(56, 1710325431, '2024-03-13 11:30:11', 256, 0, 'par_events'),
	(57, 1710325431, '2024-03-13 11:30:12', 256, 65, 'relative_humidity_events'),
	(62, 1710325431, '2024-03-13 11:30:49', 256, 0, 'par_events'),
	(63, 1710325431, '2024-03-13 11:30:51', 256, 65, 'relative_humidity_events'),
	(68, 1710325431, '2024-03-13 11:31:28', 256, 0, 'par_events'),
	(69, 1710325431, '2024-03-13 11:31:29', 256, 65, 'relative_humidity_events'),
	(74, 1710325431, '2024-03-13 11:32:06', 256, 0, 'par_events'),
	(75, 1710325431, '2024-03-13 11:32:08', 256, 65, 'relative_humidity_events');

-- Structuur van  tabel sensor_data.devicedata wordt geschreven
CREATE TABLE IF NOT EXISTS `devicedata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `device_id` int(11) DEFAULT NULL,
  `serialnumber` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `label` varchar(255) DEFAULT NULL,
  `last_seen` datetime DEFAULT NULL,
  `last_battery_voltage` float DEFAULT NULL,
  `human_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_devicedata_data` (`device_id`,`last_seen`,`last_battery_voltage`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumpen data van tabel sensor_data.devicedata: ~4 rows (ongeveer)
INSERT INTO `devicedata` (`id`, `device_id`, `serialnumber`, `name`, `label`, `last_seen`, `last_battery_voltage`, `human_name`) VALUES
	(3, 256, '0033889B1BAB1169', 'firefly2_0051', 'The Field', '2024-03-03 09:44:32', 4.08059, 'devices'),
	(4, 322, '006FE1FC316ED7D8', 'firefly2_0111', 'The Field', '2024-03-03 09:41:47', 4.09402, 'devices'),
	(8, 256, '0033889B1BAB1169', 'firefly2_0051', 'The Field', '2024-03-12 08:27:47', 4.07082, 'devices'),
	(9, 322, '006FE1FC316ED7D8', 'firefly2_0111', 'The Field', '2024-03-12 08:25:32', 4.09035, 'devices');

-- Structuur van  tabel sensor_data.django_admin_log wordt geschreven
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumpen data van tabel sensor_data.django_admin_log: ~0 rows (ongeveer)

-- Structuur van  tabel sensor_data.django_content_type wordt geschreven
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumpen data van tabel sensor_data.django_content_type: ~8 rows (ongeveer)
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(5, 'contenttypes', 'contenttype'),
	(7, 'myapp', 'datapoint'),
	(8, 'myapp', 'devicedata'),
	(6, 'sessions', 'session');

-- Structuur van  tabel sensor_data.django_migrations wordt geschreven
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumpen data van tabel sensor_data.django_migrations: ~22 rows (ongeveer)
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2024-02-28 13:30:17.125541'),
	(2, 'auth', '0001_initial', '2024-02-28 13:30:17.923617'),
	(3, 'admin', '0001_initial', '2024-02-28 13:30:18.098011'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2024-02-28 13:30:18.106622'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-02-28 13:30:18.113251'),
	(6, 'contenttypes', '0002_remove_content_type_name', '2024-02-28 13:30:18.224244'),
	(7, 'auth', '0002_alter_permission_name_max_length', '2024-02-28 13:30:18.297240'),
	(8, 'auth', '0003_alter_user_email_max_length', '2024-02-28 13:30:18.339736'),
	(9, 'auth', '0004_alter_user_username_opts', '2024-02-28 13:30:18.348742'),
	(10, 'auth', '0005_alter_user_last_login_null', '2024-02-28 13:30:18.412274'),
	(11, 'auth', '0006_require_contenttypes_0002', '2024-02-28 13:30:18.416686'),
	(12, 'auth', '0007_alter_validators_add_error_messages', '2024-02-28 13:30:18.430145'),
	(13, 'auth', '0008_alter_user_username_max_length', '2024-02-28 13:30:18.507933'),
	(14, 'auth', '0009_alter_user_last_name_max_length', '2024-02-28 13:30:18.554964'),
	(15, 'auth', '0010_alter_group_name_max_length', '2024-02-28 13:30:18.605100'),
	(16, 'auth', '0011_update_proxy_permissions', '2024-02-28 13:30:18.616136'),
	(17, 'auth', '0012_alter_user_first_name_max_length', '2024-02-28 13:30:18.663106'),
	(18, 'myapp', '0001_initial', '2024-02-28 13:30:18.827692'),
	(19, 'myapp', '0002_soil_electric_conductivity_events_timestamp', '2024-02-28 13:30:18.871382'),
	(20, 'myapp', '0003_soil_temperature_events', '2024-02-28 13:30:18.901690'),
	(21, 'myapp', '0004_datapoint_devicedata_delete_battery_voltage_events_and_more', '2024-02-28 13:30:19.080179'),
	(22, 'sessions', '0001_initial', '2024-02-28 13:30:19.158297');

-- Structuur van  tabel sensor_data.django_session wordt geschreven
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumpen data van tabel sensor_data.django_session: ~1 rows (ongeveer)
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('kjde07ol258ay5f2zyubp5urt0iiedy5', '.eJxVjEEOwiAQRe_C2hCwHSgu3fcMZGAGqRpISrsy3r1t0oVu_3vvf4THdcl-bTz7icRNaHH53QLGF5cD0BPLo8pYyzJPQR6KPGmTYyV-30_37yBjy3vtnEtd0m5ApSB1NATW5FgBU48MES33QVsFcGWKEMkYUCmhMcYGYhDfDfToOKQ:1rfK2t:pJm97vfEZYZPccYx7AeUQQaQm3chmJiIlpixFNLwPI8', '2024-03-13 13:32:27.569485');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
