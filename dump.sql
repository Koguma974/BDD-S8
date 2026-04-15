/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-12.2.2-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: TP_SecuBDD_Tayllamin_Justine
-- ------------------------------------------------------
-- Server version	12.2.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `animaux`
--

DROP TABLE IF EXISTS `animaux`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `animaux` (
  `nom` varchar(20) DEFAULT NULL,
  `proprietaire` varchar(20) DEFAULT NULL,
  `espece` varchar(20) DEFAULT NULL,
  `genre` char(1) DEFAULT NULL,
  `naissance` date DEFAULT NULL,
  `mort` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `animaux`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `animaux` WRITE;
/*!40000 ALTER TABLE `animaux` DISABLE KEYS */;
INSERT INTO `animaux` VALUES
('Fluffy','Harold','chat','f','2013-02-04',NULL),
('Claws','Gwen','chat','m','2014-03-17',NULL),
('Buffy','Harod','chien','f','2019-05-13',NULL),
('Fang','Benny','chien','m','2010-08-27',NULL),
('Bowser','Diane','chien','m','2018-08-31','2021-07-29'),
('Chirpy','Gwen','oiseau','f','2018-09-11',NULL),
('Whistler','Gwen','oiseau',NULL,'2017-12-09',NULL),
('Slim','Benny','serpent','m','2016-04-29',NULL),
('Puffball','Diane','hamster','f','2019-03-30',NULL),
('Fluffy','Harold','chat','f','2013-02-04',NULL),
('Claws','Gwen','chat','m','2014-03-17',NULL),
('Buffy','Harod','chien','f','2019-05-13',NULL),
('Fang','Benny','chien','m','2010-08-27',NULL),
('Bowser','Diane','chien','m','2018-08-31','2021-07-29'),
('Chirpy','Gwen','oiseau','f','2018-09-11',NULL),
('Whistler','Gwen','oiseau',NULL,'2017-12-09',NULL),
('Slim','Benny','serpent','m','2016-04-29',NULL),
('Puffball','Diane','hamster','f','2019-03-30',NULL);
/*!40000 ALTER TABLE `animaux` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `persons`
--

DROP TABLE IF EXISTS `persons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `persons` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `name` char(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persons`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `persons` WRITE;
/*!40000 ALTER TABLE `persons` DISABLE KEYS */;
INSERT INTO `persons` VALUES
(1,'Antonio Paz'),
(2,'Lilliana Angelovska'),
(3,'Antonio Paz'),
(4,'Antonio Paz'),
(5,'Lilliana Angelovska'),
(6,'Laurent Marot');
/*!40000 ALTER TABLE `persons` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `shirts`
--

DROP TABLE IF EXISTS `shirts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `shirts` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `style` enum('t-shirt','polo','dress') NOT NULL,
  `color` enum('red','blue','orange','white','black') NOT NULL,
  `owner` smallint(5) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `owner` (`owner`),
  CONSTRAINT `1` FOREIGN KEY (`owner`) REFERENCES `persons` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shirts`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `shirts` WRITE;
/*!40000 ALTER TABLE `shirts` DISABLE KEYS */;
INSERT INTO `shirts` VALUES
(1,'polo','blue',3),
(2,'dress','white',3),
(3,'t-shirt','blue',3),
(4,'polo','blue',4),
(5,'dress','white',4),
(6,'t-shirt','blue',4),
(7,'dress','orange',6),
(8,'polo','red',6),
(9,'dress','blue',6),
(10,'t-shirt','white',6);
/*!40000 ALTER TABLE `shirts` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `shop`
--

DROP TABLE IF EXISTS `shop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop` (
  `article` int(4) unsigned zerofill NOT NULL DEFAULT 0000,
  `dealer` char(20) NOT NULL DEFAULT '',
  `price` double(16,2) NOT NULL DEFAULT 0.00,
  PRIMARY KEY (`article`,`dealer`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `shop` WRITE;
/*!40000 ALTER TABLE `shop` DISABLE KEYS */;
INSERT INTO `shop` VALUES
(0001,'A',3.45),
(0001,'B',3.99),
(0002,'A',10.99),
(0003,'B',1.45),
(0003,'C',1.69),
(0003,'D',1.25),
(0004,'D',19.95);
/*!40000 ALTER TABLE `shop` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2026-04-07 16:02:40
