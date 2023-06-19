-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 19, 2023 at 06:59 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `login`
--

-- --------------------------------------------------------

--
-- Table structure for table `computer`
--

CREATE TABLE `computer` (
  `id` smallint(5) UNSIGNED NOT NULL,
  `nama` varchar(100) NOT NULL,
  `NPM` varchar(50) DEFAULT NULL,
  `Username` varchar(100) DEFAULT NULL,
  `Password` varchar(255) NOT NULL,
  `Level` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `computer`
--

INSERT INTO `computer` (`id`, `nama`, `NPM`, `Username`, `Password`, `Level`) VALUES
(45, 'Admin', '0000001', 'admin@mail.com', 'pbkdf2:sha256:600000$waZ4ozbQnU2gkDeE$e93b76a5f8fc5eae3f7036e6825844fb878baf4099aacfaab76ba07364688c40', 'Admin'),
(46, 'Bagas Dwi Santosa', '212103006', 'bagas@mail.com', 'pbkdf2:sha256:600000$WKqeqqG1fnXGayRM$30c17cc60a2062638a813d5af68aee03a02194a4e027a46c6da6da890054df37', 'Mahasiswa'),
(47, 'Avril Putra Mahardika', '212103024', 'avril@mail.com', 'pbkdf2:sha256:600000$CcCbxUz6qvUFNDOh$e61a74a726842517f2bb2421618a3ff26e9f362ded4cb4250aaee013c0d55057', 'Mahasiswa'),
(48, 'Bara Falah Adikaputra', '212103023', 'bara@mail.com', 'pbkdf2:sha256:600000$x8CkXSQGV7JuiPFh$5d34e0238dc8ec41396dd39c92a8b0a9311acebaf81fc6627ccb90a93df0caac', 'Mahasiswa'),
(49, 'Nurul Fatimah', '212103013', 'nurul@mail.com', 'pbkdf2:sha256:600000$VTgSGEuidlbkMm8C$c0084e3ba135f7c3917a59549c01b8d5f3911d0904fef1cd330796a94d029d22', 'Mahasiswa'),
(50, 'Maylani Ambar Wahyuni', '212103010', 'may@mail.com', 'pbkdf2:sha256:600000$Cs2p19uVUTESrO7Z$a0f1f57e24030aaae1eea271728be24c3307a9a8364d17f5e9d1a2c28c1963d8', 'Mahasiswa'),
(51, 'Kharisma, S.T., M.Cs.', '123456789', 'kharisma@mail.com', 'pbkdf2:sha256:600000$81Ahec3XFivW9hPH$6d7d4991b2ec16fbe6a44abe986d4dee3a1f59bc1d33abe3e1364ca4f374e963', 'Dosen'),
(52, 'Ulfi Saidata Aesyi, S.Kom., M.Cs.', '987654321', 'ulfi@mail.com', 'pbkdf2:sha256:600000$0fEF1zVCBaen0GeL$4b42b88b938a592521513dca0026d076344f5f54324297d249e6cb0f6ee7139b', 'Dosen'),
(53, 'Puji Winar Cahyo, S.Kom.', '135798642', 'cahyo@mail.com', 'pbkdf2:sha256:600000$2HkWwS9574shWkoA$db40e97c5242ffd2d06abd0ddc716dbfcb51be4e7a102d07614ef7d701ba31ce', 'Dosen'),
(54, 'Roykhul', '1982719', 'roy@mail.com', 'pbkdf2:sha256:600000$atYc7nbEsh47l4Y7$158994d433f607eef974cd69ae8b5eb30f49c97f0272b08e4f7db9cf41e83c1d', 'Dosen'),
(56, 'Jono Joni', '1728271', 'jono@mail.com', 'pbkdf2:sha256:600000$KAQRzh3eHfd57wdO$5d6d2d402153c5a1d87eac11ef24339a316bfeb8f31ebba40c9830d4fc1f5af5', 'Mahasiswa'),
(57, 'Rendi Ju', '1727272', 'rendi@mail.com', 'pbkdf2:sha256:600000$RJ5spP4BvRAAlh8u$727503d3abdd8faca03e2dc150ceeb30e114a2a5e3bc9b7527c6454d87f9a83f', 'Mahasiswa'),
(58, 'Rama yana', '91817272', 'rama@mail.com', 'pbkdf2:sha256:600000$DQ51O4kvoGKuYADK$b57702642955ac439df7d6e4fca5b78fb034c2ae5180f63b7537f01acf8fd158', 'Dosen'),
(59, 'Matahari', '2189818', 'mat@mail.com', 'pbkdf2:sha256:600000$4l9C9o2jb12bFGBu$abafe59ac74d2d3e87531099c80a45b9f14b6e58d7d249d4a60b3068df98068d', 'Mahasiswa'),
(60, 'Joko ndo', '918291', 'joko@mail.com', 'pbkdf2:sha256:600000$D2SicAvKAA8t3yBX$210452b854ecb9fb50ee95c11ad2eeefcce6c1541d82470280b2e6a9c11e02fe', 'Mahasiswa'),
(61, 'Lesly Brody', '9189182', 'lesly@mail.com', 'pbkdf2:sha256:600000$hIBNrd2fRpgFtDDQ$7049285883ab33a60a0bb7cd4f6d5cfbf811231c08cd2f9828b6804cc898e6b6', 'Mahasiswa'),
(62, 'Change chan', '1812910', 'change@mail.com', 'pbkdf2:sha256:600000$On71NfFc2lvhO922$9b9cd81abc8dbfe20a853866a61c3f6c247d2ef725d0f18dd7b23fbc2c146288', 'Mahasiswa'),
(63, 'Mahardika', '832749827', 'dika@mail.com', 'pbkdf2:sha256:600000$lKHqMMcq2u8PV8Br$641c0a7604656e19314f5ac07733224bb787bd8db9caf32463d7be3dd35575a6', 'Mahasiswa');

-- --------------------------------------------------------

--
-- Table structure for table `matakuliah`
--

CREATE TABLE `matakuliah` (
  `id` smallint(5) NOT NULL,
  `nama_matkul` varchar(100) NOT NULL,
  `sks` int(2) NOT NULL,
  `dosen` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `matakuliah`
--

INSERT INTO `matakuliah` (`id`, `nama_matkul`, `sks`, `dosen`) VALUES
(2, 'Pemrograman Web', 4, 'Kharisma, S.Kom., M.Eng.'),
(3, 'Analisis Proses Bisnis', 3, 'Ulfi Saidata Aesyi, S.Kom., M.Cs.'),
(4, 'Pemrograman Basis Data', 3, 'Ahmad Hanafi, S.T., M.Eng.'),
(5, 'Rekayasa Perangkat Lunak', 4, 'Irmma Dwijayanti, S.Kom., M.Cs.'),
(6, 'UI UX DESIGN', 2, 'Ahmad Hanafi, S.T., M.Eng.');

-- --------------------------------------------------------

--
-- Table structure for table `note`
--

CREATE TABLE `note` (
  `id` smallint(5) NOT NULL,
  `note` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `note`
--

INSERT INTO `note` (`id`, `note`) VALUES
(2, 'Tugas PAWL'),
(3, 'Besok KUIS PBD'),
(4, 'Besok Libur');

-- --------------------------------------------------------

--
-- Table structure for table `penilaian`
--

CREATE TABLE `penilaian` (
  `mahasiswa` varchar(255) NOT NULL,
  `matkul` varchar(255) NOT NULL,
  `presensi` int(3) NOT NULL,
  `uts` int(3) NOT NULL,
  `uas` int(3) NOT NULL,
  `tugas_besar` int(3) NOT NULL,
  `tugas_kecil` int(3) NOT NULL,
  `bobot` int(3) DEFAULT NULL,
  `hasil` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `penilaian`
--

INSERT INTO `penilaian` (`mahasiswa`, `matkul`, `presensi`, `uts`, `uas`, `tugas_besar`, `tugas_kecil`, `bobot`, `hasil`) VALUES
('Avril Putra Mahardika', 'Analisis Proses Bisnis', 75, 85, 60, 100, 78, 82, 'A-'),
('Avril Putra Mahardika', 'Pemrograman Web', 70, 70, 60, 70, 70, 68, 'B'),
('Avril Putra Mahardika', 'Rekayasa Perangkat Lunak', 75, 70, 60, 70, 60, 66, 'B-'),
('Bagas Dwi Santosa', 'Analisis Proses Bisnis', 100, 100, 100, 100, 100, 100, 'A'),
('Mahardika', 'Pemrograman Web', 30, 20, 10, 60, 40, 35, 'E'),
('Nurul Fatimah', 'Pemrograman Basis Data', 30, 20, 60, 60, 80, 53, 'D');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `level` enum('Admin','Dosen','Mahasiswa') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password`, `level`) VALUES
(2, 'bg@gmail.com', 'bg@gmail.com', 'pbkdf2:sha256:260000$mcDedX8lCNLoUDA7$50b53db5696b5f5f9551e6723e4571b39855341c1d6f862ef9bdd015643308bc', 'Mahasiswa'),
(3, 'b@mail.com', 'b@mail.com', 'pbkdf2:sha256:260000$5nib1vIumTSOHkQ6$1001927228c9eab519ab42a07c7c54ecc82f3fa3b89ac3e10d7671043123e98c', 'Admin'),
(4, 'a@mail.com', 'a@mail.com', 'pbkdf2:sha256:260000$DRSqF0GFm66kSb3b$b38b2916a1faccf24c76291c209e97c5c8516ead57d99b2e3376f73f7c54e94f', 'Mahasiswa'),
(5, 'c@mail.com', 'c@mail.com', 'pbkdf2:sha256:260000$xAwmlKvUU8vPhxq6$e28835a44db523a16c6adcd6eb6abed031a87e74b04d8552fd0b0f001e327c6a', 'Dosen'),
(6, '2121203006', 'bagas@mail.com', 'pbkdf2:sha256:260000$wdrecfAQKEe3KvrK$a49e3654544f990c4514cdc58e711f455b0acd561c4f9e04e7b01395bbd4ea39', 'Mahasiswa'),
(7, 'Bagas Dwi Santosa', '6', 'd@mail.com', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `computer`
--
ALTER TABLE `computer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `matakuliah`
--
ALTER TABLE `matakuliah`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `note`
--
ALTER TABLE `note`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `computer`
--
ALTER TABLE `computer`
  MODIFY `id` smallint(5) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

--
-- AUTO_INCREMENT for table `matakuliah`
--
ALTER TABLE `matakuliah`
  MODIFY `id` smallint(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `note`
--
ALTER TABLE `note`
  MODIFY `id` smallint(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
