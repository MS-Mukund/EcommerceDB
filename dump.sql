-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: localhost    Database: BUYNOW
-- ------------------------------------------------------
-- Server version	8.0.27-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Agency_Deliverable_Pincode`
--

DROP TABLE IF EXISTS `Agency_Deliverable_Pincode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Agency_Deliverable_Pincode` (
  `Deliverable_Pincode` char(6) DEFAULT NULL,
  `A_Agency_ID` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Agency_Deliverable_Pincode`
--

LOCK TABLES `Agency_Deliverable_Pincode` WRITE;
/*!40000 ALTER TABLE `Agency_Deliverable_Pincode` DISABLE KEYS */;
/*!40000 ALTER TABLE `Agency_Deliverable_Pincode` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Category1_Mobiles`
--

DROP TABLE IF EXISTS `Category1_Mobiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Category1_Mobiles` (
  `Category1_ProductID` int DEFAULT NULL,
  `Battery` varchar(128) DEFAULT NULL,
  `Camera` varchar(128) DEFAULT NULL,
  `Processor` varchar(128) DEFAULT NULL,
  `RAM` varchar(128) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Category1_Mobiles`
--

LOCK TABLES `Category1_Mobiles` WRITE;
/*!40000 ALTER TABLE `Category1_Mobiles` DISABLE KEYS */;
/*!40000 ALTER TABLE `Category1_Mobiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Category2`
--

DROP TABLE IF EXISTS `Category2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Category2` (
  `Category2_ProductID` int DEFAULT NULL,
  `Attrib_1` varchar(128) DEFAULT NULL,
  `Attrib_2` varchar(128) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Category2`
--

LOCK TABLES `Category2` WRITE;
/*!40000 ALTER TABLE `Category2` DISABLE KEYS */;
/*!40000 ALTER TABLE `Category2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Category3`
--

DROP TABLE IF EXISTS `Category3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Category3` (
  `Category3_ProductID` int DEFAULT NULL,
  `Attrib_1` varchar(128) DEFAULT NULL,
  `Attrib_2` varchar(128) DEFAULT NULL,
  `Attrib_3` varchar(128) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Category3`
--

LOCK TABLES `Category3` WRITE;
/*!40000 ALTER TABLE `Category3` DISABLE KEYS */;
/*!40000 ALTER TABLE `Category3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Delivery_Agency`
--

DROP TABLE IF EXISTS `Delivery_Agency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Delivery_Agency` (
  `Agency_ID` int NOT NULL,
  `Company_Name` varchar(128) NOT NULL,
  PRIMARY KEY (`Agency_ID`),
  UNIQUE KEY `Agency_ID` (`Agency_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Delivery_Agency`
--

LOCK TABLES `Delivery_Agency` WRITE;
/*!40000 ALTER TABLE `Delivery_Agency` DISABLE KEYS */;
INSERT INTO `Delivery_Agency` VALUES (0,'DelhiVery'),(1,'SpeedPost'),(2,'DHL'),(3,'FedEx'),(4,'TNT'),(5,'UPS'),(6,'USPS');
/*!40000 ALTER TABLE `Delivery_Agency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Item`
--

DROP TABLE IF EXISTS `Item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Item` (
  `Item_Description` varchar(4096) NOT NULL,
  `I_Product_ID` int NOT NULL,
  UNIQUE KEY `I_Product_ID` (`I_Product_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Item`
--

LOCK TABLES `Item` WRITE;
/*!40000 ALTER TABLE `Item` DISABLE KEYS */;
/*!40000 ALTER TABLE `Item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Orders`
--

DROP TABLE IF EXISTS `Orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Orders` (
  `Placed_Date` date NOT NULL,
  `Amount_Paid` int DEFAULT NULL,
  `Is_it_delivered` bit(1) DEFAULT NULL,
  `Date_of_Delivery` date DEFAULT NULL,
  `O_Agency_ID` int NOT NULL,
  `O_SupplierID` int NOT NULL,
  `O_Username` varchar(128) NOT NULL,
  `O_Product_ID` int NOT NULL,
  `Order_ID` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Orders`
--

LOCK TABLES `Orders` WRITE;
/*!40000 ALTER TABLE `Orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `Orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Products`
--

DROP TABLE IF EXISTS `Products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Products` (
  `Product_ID` int NOT NULL,
  `Name` varchar(128) NOT NULL,
  `Warranty` varchar(128) NOT NULL,
  `Company` varchar(128) NOT NULL,
  `Price` int NOT NULL,
  PRIMARY KEY (`Product_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Products`
--

LOCK TABLES `Products` WRITE;
/*!40000 ALTER TABLE `Products` DISABLE KEYS */;
INSERT INTO `Products` VALUES (0,'Lenovo IdeaPad L340','2 years','Lenovo',71999),(1,'HP Pavilion','2 years','HP',59999),(2,'Dell Inspiron','3 years','Dell',69999),(3,'Samsung Galaxy','1 years','Samsung',79999),(4,'Sony Xperia','4 years','Sony',89999),(5,'Apple iPhone','1 years','Apple',99999),(6,'Nokia Lumia','3 years','Nokia',89999),(7,'LG Smart TV','1 years','LG',51997),(8,'Sony-Ericsson Ipod','6 months','Sony',1997),(9,'Samsung Galaxy Tab','6 months','Samsung',21997),(10,'iWatch','4 months','Apple',12998),(11,'Kindle','1 year','Amazon',8999),(12,'T-shirt M-size','','Allen Solly',199),(13,'T-shirt L-size','','Van Heusen',299),(14,'T-shirt XL-size','','US POLO',399);
/*!40000 ALTER TABLE `Products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Purchase_Transaction`
--

DROP TABLE IF EXISTS `Purchase_Transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Purchase_Transaction` (
  `PT_Agency_ID` int NOT NULL,
  `PT_Supplier_ID` int NOT NULL,
  `PT_Username` varchar(128) NOT NULL,
  `PT_Product_ID` int NOT NULL,
  `PT_Order_ID` int NOT NULL,
  PRIMARY KEY (`PT_Agency_ID`,`PT_Supplier_ID`,`PT_Username`,`PT_Product_ID`,`PT_Order_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Purchase_Transaction`
--

LOCK TABLES `Purchase_Transaction` WRITE;
/*!40000 ALTER TABLE `Purchase_Transaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `Purchase_Transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Return_Order`
--

DROP TABLE IF EXISTS `Return_Order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Return_Order` (
  `Return_ID` int NOT NULL,
  `Date_of_Order` date DEFAULT NULL,
  `Product_ID` int DEFAULT NULL,
  `Refund_Amount` int DEFAULT NULL,
  `R_Agency_ID` int NOT NULL,
  `R_SupplierID` int NOT NULL,
  `R_Username` varchar(128) NOT NULL,
  PRIMARY KEY (`R_Username`,`R_SupplierID`,`R_Agency_ID`),
  UNIQUE KEY `Return_ID` (`Return_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Return_Order`
--

LOCK TABLES `Return_Order` WRITE;
/*!40000 ALTER TABLE `Return_Order` DISABLE KEYS */;
/*!40000 ALTER TABLE `Return_Order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Return_Transaction`
--

DROP TABLE IF EXISTS `Return_Transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Return_Transaction` (
  `RT_Agency_ID` int NOT NULL,
  `RT_Supplier_ID` int NOT NULL,
  `RT_Username` varchar(128) NOT NULL,
  `RT_Product_ID` int NOT NULL,
  `RT_Return_ID` int NOT NULL,
  PRIMARY KEY (`RT_Agency_ID`,`RT_Supplier_ID`,`RT_Username`,`RT_Product_ID`,`RT_Return_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Return_Transaction`
--

LOCK TABLES `Return_Transaction` WRITE;
/*!40000 ALTER TABLE `Return_Transaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `Return_Transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Supplied_by`
--

DROP TABLE IF EXISTS `Supplied_by`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Supplied_by` (
  `SB_SupplierID` int NOT NULL,
  `Available_Quantity` int NOT NULL,
  `Discount` int NOT NULL,
  `Final_Cost` int NOT NULL,
  `SB_ProductID` int NOT NULL,
  PRIMARY KEY (`SB_SupplierID`,`SB_ProductID`),
  UNIQUE KEY `SB_SupplierID` (`SB_SupplierID`),
  UNIQUE KEY `SB_ProductID` (`SB_ProductID`),
  CONSTRAINT `Supplied_by_chk_1` CHECK ((`Discount` < 70))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Supplied_by`
--

LOCK TABLES `Supplied_by` WRITE;
/*!40000 ALTER TABLE `Supplied_by` DISABLE KEYS */;
/*!40000 ALTER TABLE `Supplied_by` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Suppliers`
--

DROP TABLE IF EXISTS `Suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Suppliers` (
  `SupplierID` int NOT NULL,
  `Name` varchar(128) NOT NULL,
  `Address_Line1` varchar(128) NOT NULL,
  `Address_Line2` varchar(128) DEFAULT NULL,
  `Pincode` int NOT NULL,
  PRIMARY KEY (`SupplierID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Suppliers`
--

LOCK TABLES `Suppliers` WRITE;
/*!40000 ALTER TABLE `Suppliers` DISABLE KEYS */;
INSERT INTO `Suppliers` VALUES (0,'Fibtronics','pursaivalkam','chennai, Tamil Nadu',511342),(1,'Duracell Batteries','old fort road','chengalpattu, Tamil Nadu',521345),(2,'Bajaj','Rabindranath Tagore road','Race course road, New Delhi',500354),(3,'Muthoot FinCorp','Honesty vally','Darjeeling, Sikkim',234921),(4,'Tata Salt','bahadur street','Mumbai, Maharashtra',534342),(5,'Wrogn Private Limited','Jaffna nagar','Pune, Maharashtra',594342),(6,'Tata Power','Kanpur road','Lucknow, Uttar Pradesh',523114),(7,'Tata Steel','Sharma road','Kanpur, Uttar Pradesh',513214),(8,'Tata Motors','Sardar Palace','Indore, Madhya Pradesh',511236);
/*!40000 ALTER TABLE `Suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `Username` varchar(128) NOT NULL,
  `Phone_number` char(10) NOT NULL,
  `First_name` varchar(128) NOT NULL,
  `Middle_name` varchar(128) DEFAULT NULL,
  `Last_name` varchar(128) NOT NULL,
  `Email` varchar(328) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Password` varchar(32) NOT NULL,
  `Premium_Subscription` bit(1) DEFAULT NULL,
  `Address_Line1` varchar(1024) NOT NULL,
  `Address_Line2` varchar(1024) DEFAULT NULL,
  `Pincode` char(6) NOT NULL,
  PRIMARY KEY (`Username`,`Phone_number`),
  UNIQUE KEY `Username` (`Username`),
  UNIQUE KEY `Phone_number` (`Phone_number`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `Email_2` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES ('jsmith','9238419244','john','','smith','a@gmail.com','oewrsflkl',_binary '','church tower','office street, tuni','527622'),('mukundm','8074719244','sai','mukund','meka','mukundmeka3456@gmail.com','oewrlvprdil',_binary '\0','sri prakash apartments','payakaraopeta','531126'),('namrath_ace','9347729442','sai','namrath','polakampalli','namrath123@gmail.com','ssdfmparil',_binary '','sangareddy nagar','khammam','532234'),('sdffft','7234779133','van','tom','heusen','harrypotter@gmail.com','chadflkd',_binary '\0','134/34, sprint apartements','nainital, vizag','514282'),('snuhft','9234429133','allen','','solly','sdfdkekw@gmail.com','2kbsdfly',_binary '','c-2/4, prakash nagar','gandepalli, vizag','514282'),('sudheer1','9848055442','sudheer','reddy','padala','psrmail@gmail.com','srmparil',_binary '\0','adi lakshmi nagar','ravulapalem, east godavari district','542303'),('vamsis','9234752334','sivam','','sunkara','savyasachi@gmail.com','okbrouonly',_binary '\0','b-1/2, vikas nagar','guntapalli, vizag','503282'),('vmjain','923412334','bhidit','mukeshwar','jain','b@gmail.com','somename',_binary '','hosur, halibeedu, karnataka','','500082');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-26 16:45:25
