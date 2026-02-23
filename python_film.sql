-- phpMyAdmin SQL Dump
-- version 5.2.1deb3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Waktu pembuatan: 23 Des 2025 pada 13.17
-- Versi server: 8.0.44-0ubuntu0.24.04.2
-- Versi PHP: 8.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_film`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `film`
--

CREATE TABLE `film` (
  `idfilm` int NOT NULL,
  `namafilm` varchar(255) NOT NULL,
  `posterfilm` varchar(255) NOT NULL,
  `videofilm` varchar(255) NOT NULL,
  `idgenre` int NOT NULL,
  `tahunrilis` varchar(255) DEFAULT NULL,
  `deskripsi` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `filmtype` varchar(255) NOT NULL,
  `sutradara` varchar(255) NOT NULL,
  `artis` varchar(255) NOT NULL,
  `total_penonton` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `film`
--

INSERT INTO `film` (`idfilm`, `namafilm`, `posterfilm`, `videofilm`, `idgenre`, `tahunrilis`, `deskripsi`, `filmtype`, `sutradara`, `artis`, `total_penonton`) VALUES
(3, 'Ejen Ali Movie 2', 'ejenali.webp', '1_Minute_of_Nothing.mp4', 5, '2025', 'Di Ejen Ali the Movie 2, seorang agen rahasia muda dipilih untuk mengoperasikan setelan eksperimental canggih yang ditingkatkan oleh kecerdasan buatan. Setelan ini dirancang untuk merevolusi operasi rahasia, memberinya kekuatan dan kemampuan luar biasa.', 'animated', 'Usamah Zaid Yasin,Nazmi Yatim', 'Ida Rahayu Yusoff, Noorhayati Maslini, Shafiq Isa', 11),
(5, 'The Astronout', 'theastronout.webp', '1_Minute_of_Nothing.mp4', 6, '2025', 'Dalam film \"The Astronaut\" (2025), seorang astronot crash-lands kembali ke Bumi dan ditempatkan di karantina oleh seorang Jenderal untuk rehabilitasi dan pengujian. Namun, kejadian mengerikan mulai terjadi, membuat astronot tersebut takut bahwa sesuatu yang tidak dari Bumi telah mengikutinya pulang', 'movie', 'Jess Varley', 'Kate Mara, Laurence Fishburne, Gabriel Luna', 3),
(7, 'De Balloonist', 'deballonist.webp', '1_Minute_of_Nothing.mp4', 5, '2025', 'Dalam film \"De Ballonvaarder\" (2025), komedi drama yang menghibur, kehidupan Gaby yang tenang sebagai pemelihara ayam warisan berubah drastis ketika seorang pilot balon udara yang sombong jatuh di kandang ayamnya. Kecelakaan itu mengungkap konflik keluarga yang tersembunyi dan memaksa Gaby untuk menghadapi pilot balon udara tersebut serta menghadapi kenyataan tentang dirinya sendiri. Dengan humor yang tajam dan sentuhan emosional, \"De Ballonvaarder\" menjanjikan petualangan penuh tawa dan renungan yang tak terduga. Penasaran bagaimana Gaby menghadapi tantangan ini?', 'movie', '', '', 9),
(8, 'Superman ', 'superman.webp', '1_Minute_of_Nothing.mp4', 2, '2025', 'Dalam \"Superman\" (2025), aksi petualangan dimulai ketika Superman harus memilih antara warisan Kryptonian dan masa kecilnya di Bumi sebagai Clark Kent. Sebagai simbol kebenaran dan keadilan, ia menghadapi dunia yang meragukan nilai-nilai tersebut. Apakah Superman masih bisa menjadi harapan manusia? Budget: $225,000,000 (estimated) Worldwide Gross: $615,636,363 Soundtrack: Original Superman Theme (By John Williams)', 'movie', '', '', 2),
(9, 'F1 The Movie', 'f1.webp', '1_Minute_of_Nothing.mp4', 2, '2025', 'Di \"F1: The Movie\" (2025), seorang pembalap Formula One legendaris keluar dari pensiun untuk melatih dan bergabung dengan pembalap muda berbakat. Dengan aksi yang seru dan dramatis, mereka harus mengatasi tantangan di lintasan balap dan konflik pribadi untuk mencapai kejayaan. Apakah mereka bisa menjadi juara? Awards: 7 nominations total Budget: $182,848,183', 'movie', '', '', 3),
(10, 'Clown in a Cornfields', 'clown.webp', '1_Minute_of_Nothing.mp4', 6, '2025', 'Di kota kecil Midwestern yang terlupakan, Frendo si badut, simbol kesuksesan masa lalu, kembali muncul sebagai teror yang mengerikan. Ia menghantui ladang jagung, membunuh siapa saja yang berani menginjakkan kaki di sana. Rasa takut dan misteri meliputi kota, membuat warganya hidup dalam ketakutan. Apa rahasia di balik kebangkitan Frendo? Budget: $1,000,000 (estimated) Worldwide Gross: $13,334,281 Soundtrack: What Do I Owe (Written by Michael John Barnicle and Mark De Rosa)', 'movie', 'Eli Craig', 'Katie Douglas, Aaron Abrams, Carson MacCormac', 5);

-- --------------------------------------------------------

--
-- Struktur dari tabel `genre`
--

CREATE TABLE `genre` (
  `idgenre` int NOT NULL,
  `tipegenre` varchar(255) NOT NULL,
  `cur` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `genre`
--

INSERT INTO `genre` (`idgenre`, `tipegenre`, `cur`) VALUES
(1, 'Romance', 'romance'),
(2, 'Adventure', 'adventure'),
(3, 'Comedy', 'comedy'),
(5, 'Action', 'action'),
(6, 'Horror', 'horror'),
(7, 'Sci-Fi', 'sci-fi'),
(14, 'Crime', 'crime'),
(15, 'Musikal', 'musikal'),
(16, 'War', 'war'),
(17, 'Western', 'western'),
(18, 'History', 'history'),
(19, 'Mystery', 'mystery'),
(20, 'Biography', 'biography'),
(21, 'Sport', 'sport'),
(22, 'Thriller', 'thriller'),
(24, '', '');

-- --------------------------------------------------------

--
-- Struktur dari tabel `komentar`
--

CREATE TABLE `komentar` (
  `idkomentar` int NOT NULL,
  `nama` varchar(255) NOT NULL,
  `komentar` text NOT NULL,
  `idfilm` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `komentar`
--

INSERT INTO `komentar` (`idkomentar`, `nama`, `komentar`, `idfilm`) VALUES
(2, 'raka', 'kerennnn', 3),
(3, 'budi', 'kerennnn', 3),
(9, 'raka', 'oke', 8);

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `iduser` int NOT NULL,
  `user` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('user','admin') NOT NULL DEFAULT 'user'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`iduser`, `user`, `username`, `password`, `role`) VALUES
(1, 'admin', 'admin', 'scrypt:32768:8:1$23j9YSrkPYSVUT4W$27b27a053d72cb4615e780f449fe07982d372aedfe4eedba50a33f13fa708d49e5b39391643665680a7225c0e870a11c63b9df7f70d2c57681901469a26e37c6', 'admin'),
(2, '231312', '123', 'scrypt:32768:8:1$n2YW2WHxyACRsrG1$b96d76b49069e43f9031213d7676fa57c1af2ba447ee4773d2cb8f252aef8590de9aba9db9457c4f2b89d12dfc5f2189bcd8b90baa297274d2ba35db291f7c04', 'admin'),
(4, 'admin', 'admins', 'scrypt:32768:8:1$VhURtRf5l4WqqMaH$52b15d67248b586bad3d650de7311ea59a8c0ef5c9ee57498eea3aa2cc9d8724c442d817f9d7cf39b35c8a389a802728427303a86fe59ddc7e2e2f60c0cd6489', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `film`
--
ALTER TABLE `film`
  ADD PRIMARY KEY (`idfilm`),
  ADD KEY `idgenre` (`idgenre`);

--
-- Indeks untuk tabel `genre`
--
ALTER TABLE `genre`
  ADD PRIMARY KEY (`idgenre`);

--
-- Indeks untuk tabel `komentar`
--
ALTER TABLE `komentar`
  ADD PRIMARY KEY (`idkomentar`),
  ADD KEY `idfilm` (`idfilm`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`iduser`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `film`
--
ALTER TABLE `film`
  MODIFY `idfilm` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT untuk tabel `genre`
--
ALTER TABLE `genre`
  MODIFY `idgenre` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT untuk tabel `komentar`
--
ALTER TABLE `komentar`
  MODIFY `idkomentar` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT untuk tabel `user`
--
ALTER TABLE `user`
  MODIFY `iduser` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `film`
--
ALTER TABLE `film`
  ADD CONSTRAINT `film_ibfk_1` FOREIGN KEY (`idgenre`) REFERENCES `genre` (`idgenre`);

--
-- Ketidakleluasaan untuk tabel `komentar`
--
ALTER TABLE `komentar`
  ADD CONSTRAINT `komentar_ibfk_1` FOREIGN KEY (`idfilm`) REFERENCES `film` (`idfilm`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
