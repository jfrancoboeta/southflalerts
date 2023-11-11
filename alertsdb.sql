-- Dumping database structure for alertsdb
CREATE DATABASE IF NOT EXISTS `alertsdb` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `alertsdb`;
-- Data exporting was unselected.

-- Dumping structure for table alertsdb.people
CREATE TABLE IF NOT EXISTS `people` (
  `URL` varchar(300) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `confirmation_email` int DEFAULT '0',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Data exporting was unselected.