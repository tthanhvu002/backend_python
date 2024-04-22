-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th4 06, 2024 lúc 03:17 PM
-- Phiên bản máy phục vụ: 10.4.27-MariaDB
-- Phiên bản PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `doanchinh`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `accounts`
--

CREATE TABLE `accounts` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(191) NOT NULL,
  `createdAt` datetime(3) DEFAULT current_timestamp(3),
  `updatedAt` datetime(3) DEFAULT NULL,
  `is_verified` tinyint(1) NOT NULL DEFAULT 0,
  `otpCode` varchar(191) DEFAULT NULL,
  `otpExpires` datetime(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `author`
--

CREATE TABLE `author` (
  `id` int(11) NOT NULL,
  `name` varchar(191) NOT NULL,
  `image` varchar(191) DEFAULT NULL,
  `description` varchar(191) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `author`
--

INSERT INTO `author` (`id`, `name`, `image`, `description`) VALUES
(1, 'Tuh', 'https://i.ibb.co/b15xsRG/male-author-2.jpg', 'Great author'),
(2, 'Nhi', 'https://i.ibb.co/7Yggnmn/female-author.jpg', 'Great author'),
(3, 'Tuấn', 'https://i.ibb.co/VV1MZgL/male-author.jpg', 'Great author'),
(6, 'Quỳnh', 'https://i.ibb.co/VpHsRRQ/female-author-2.jpg', 'Great author');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `book`
--

CREATE TABLE `book` (
  `id` int(11) NOT NULL,
  `name` varchar(191) NOT NULL,
  `description` varchar(191) DEFAULT NULL,
  `rating` int(11) NOT NULL DEFAULT 0,
  `progress` double NOT NULL DEFAULT 0,
  `published_year` int(11) NOT NULL,
  `image` varchar(191) DEFAULT NULL,
  `language` varchar(191) NOT NULL DEFAULT 'Unknown',
  `book_type` enum('PREMIUM','NORMAL') NOT NULL DEFAULT 'NORMAL',
  `lyric` mediumtext DEFAULT NULL,
  `srcAudio` varchar(191) NOT NULL,
  `primaryColor` varchar(191) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `book`
--

INSERT INTO `book` (`id`, `name`, `description`, `rating`, `progress`, `published_year`, `image`, `language`, `book_type`, `lyric`, `srcAudio`, `primaryColor`) VALUES
(17, 'Shape of you', NULL, 0, 0, 2018, 'https://i.ibb.co/t3Jjm0c/shape-of-you.png', 'English', 'NORMAL', NULL, 'https://voicereplay-backgroundmusics.s3.ap-southeast-1.amazonaws.com/media/Believer+-+Imagine+Dragons.mp3', NULL),
(18, 'Peter Pan', NULL, 0, 0, 2018, 'https://i.ibb.co/wWNwQjy/book.jpg', 'English', 'NORMAL', NULL, 'https://voicereplay-backgroundmusics.s3.ap-southeast-1.amazonaws.com/media/Believer+-+Imagine+Dragons.mp3', NULL),
(19, 'Book Test', NULL, 0, 0, 2016, NULL, 'Unknown', 'NORMAL', NULL, 'null', NULL),
(20, 'Book Test', NULL, 0, 0, 2016, NULL, 'Unknown', 'NORMAL', NULL, 'null', NULL),
(21, 'Book Test', NULL, 0, 0, 2016, NULL, 'Unknown', 'NORMAL', NULL, 'null', NULL),
(22, 'Book Test', NULL, 0, 0, 2016, NULL, 'Unknown', 'NORMAL', NULL, 'null', NULL),
(23, 'Book Test', NULL, 0, 0, 2016, NULL, 'Unknown', 'NORMAL', NULL, 'null', NULL),
(24, 'Book Test', NULL, 0, 0, 2016, NULL, 'Unknown', 'NORMAL', NULL, 'null', NULL),
(25, 'Book Test', NULL, 0, 0, 2016, NULL, 'Unknown', 'NORMAL', NULL, 'null', NULL),
(26, 'Book Test', NULL, 0, 0, 2016, NULL, 'Unknown', 'NORMAL', NULL, 'null', NULL),
(27, 'Book Test', NULL, 0, 0, 2016, NULL, 'Unknown', 'NORMAL', NULL, 'null', NULL),
(28, 'Book Test', NULL, 0, 0, 2016, NULL, 'Unknown', 'NORMAL', NULL, 'null', NULL),
(29, 'Book Test', NULL, 0, 0, 2016, NULL, 'Unknown', 'NORMAL', NULL, 'null', NULL),
(30, 'Book Test', NULL, 0, 0, 2016, NULL, 'Unknown', 'NORMAL', NULL, 'null', NULL),
(31, 'Book Test', NULL, 0, 0, 2016, NULL, 'Unknown', 'NORMAL', NULL, 'null', NULL);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `book_author`
--

CREATE TABLE `book_author` (
  `id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `book_author`
--

INSERT INTO `book_author` (`id`, `book_id`, `author_id`) VALUES
(8, 18, 2),
(9, 17, 3);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `book_genre`
--

CREATE TABLE `book_genre` (
  `id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `book_genre`
--

INSERT INTO `book_genre` (`id`, `book_id`, `genre_id`) VALUES
(9, 18, 8),
(10, 17, 2);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `genre`
--

CREATE TABLE `genre` (
  `id` int(11) NOT NULL,
  `name` varchar(191) NOT NULL,
  `icon` varchar(191) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `genre`
--

INSERT INTO `genre` (`id`, `name`, `icon`) VALUES
(1, 'romance', 'https://i.ibb.co/fHC2rVM/icon-shake-hand.png'),
(2, 'history', 'https://i.ibb.co/fHC2rVM/icon-shake-hand.png'),
(3, 'funny', 'https://i.ibb.co/fHC2rVM/icon-shake-hand.png'),
(4, 'horror', 'https://i.ibb.co/fHC2rVM/icon-shake-hand.png'),
(5, 'Genre 6', 'https://i.ibb.co/fHC2rVM/icon-shake-hand.png'),
(6, 'Genre 6', 'https://i.ibb.co/fHC2rVM/icon-shake-hand.png'),
(7, 'Genre 6', NULL),
(8, 'Genre 6', NULL),
(9, 'Genre 6', NULL),
(10, 'Genre 6', NULL),
(11, 'Genre 6', NULL),
(12, 'Genre 6', NULL),
(13, 'Genre 6', NULL),
(14, 'Genre 6', NULL),
(15, 'Genre 6', NULL),
(16, 'Genre 6', NULL),
(17, 'Genre 6', NULL);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `subcription`
--

CREATE TABLE `subcription` (
  `id` int(11) NOT NULL,
  `duration` double NOT NULL,
  `price_per_month` double NOT NULL,
  `type` varchar(191) NOT NULL,
  `limit_book_mark` int(11) NOT NULL,
  `book_type` enum('PREMIUM','NORMAL') DEFAULT 'NORMAL',
  `subcription_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `subcription_history`
--

CREATE TABLE `subcription_history` (
  `id` int(11) NOT NULL,
  `name` varchar(191) NOT NULL,
  `price` double NOT NULL,
  `start` datetime(3) DEFAULT NULL,
  `end` datetime(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phoneNumber` varchar(191) DEFAULT NULL,
  `address` varchar(191) DEFAULT NULL,
  `createdAt` datetime(3) DEFAULT current_timestamp(3),
  `updatedAt` datetime(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `users`
--

INSERT INTO `users` (`id`, `name`, `phoneNumber`, `address`, `createdAt`, `updatedAt`) VALUES
(1, 'tuh', '0908773513', '123', '2024-04-03 11:06:09.869', '2024-04-03 11:06:09.869'),
(2, 'tuh', '+0908773513', '123', '2024-04-03 11:07:09.028', '2024-04-03 11:07:09.028'),
(3, 'tuh', '+84908773513', '123', '2024-04-03 11:07:12.525', '2024-04-03 11:07:12.525'),
(4, 'tuh', '+84908773513', '123', '2024-04-03 11:07:54.852', '2024-04-03 11:07:54.852'),
(5, 'tuh', '+84908773513', '123', '2024-04-03 11:09:19.483', '2024-04-03 11:09:19.483'),
(6, 'tuh', '+84908773513', '123', '2024-04-03 11:09:58.909', '2024-04-03 11:09:58.909'),
(7, 'tuh', '+84908773513', '123', '2024-04-03 11:10:17.227', '2024-04-03 11:10:17.227'),
(8, 'tuh', '+84908773513', '123', '2024-04-03 11:12:18.865', '2024-04-03 11:12:18.865'),
(9, 'tuh', '+84908773513', '123', '2024-04-03 11:15:03.379', '2024-04-03 11:15:03.379'),
(10, 'tuh', '+84908773513', '123', '2024-04-03 11:16:23.334', '2024-04-03 11:16:23.334'),
(11, 'tuh', '+84908773513', '123', '2024-04-03 11:16:39.628', '2024-04-03 11:16:39.628'),
(12, 'tuh', '+84908773513', '123', '2024-04-03 11:17:31.309', '2024-04-03 11:17:31.309');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `_prisma_migrations`
--

CREATE TABLE `_prisma_migrations` (
  `id` varchar(36) NOT NULL,
  `checksum` varchar(64) NOT NULL,
  `finished_at` datetime(3) DEFAULT NULL,
  `migration_name` varchar(255) NOT NULL,
  `logs` text DEFAULT NULL,
  `rolled_back_at` datetime(3) DEFAULT NULL,
  `started_at` datetime(3) NOT NULL DEFAULT current_timestamp(3),
  `applied_steps_count` int(10) UNSIGNED NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `_prisma_migrations`
--

INSERT INTO `_prisma_migrations` (`id`, `checksum`, `finished_at`, `migration_name`, `logs`, `rolled_back_at`, `started_at`, `applied_steps_count`) VALUES
('4979289f-d768-4a1c-a572-c972a1c78cf9', 'fc8434024c6aa8460a835f4a59ad0392c19e84271b7456d3b1b087b9a05a90ef', '2024-03-28 02:37:19.482', '20240328023719_update_book', NULL, NULL, '2024-03-28 02:37:19.471', 1),
('6aad9e78-234a-4e35-9822-102a7037c650', '5b7279f00a2a29990bf097e555be9212cf44c31d58a82e24f1419a9c4989a9f6', '2024-03-28 06:12:53.566', '20240328061253_update_book_primarycolor', NULL, NULL, '2024-03-28 06:12:53.543', 1),
('94d5b287-4726-4f59-8520-51ee3bb31998', 'a59bbf9c4e7209751f56279883a16e1d029f69bcbb65c3285cac1edf35460a17', '2024-03-28 15:04:30.739', '20240328150430_update_genre_icon', NULL, NULL, '2024-03-28 15:04:30.725', 1),
('9d2a3f3b-72bb-4f64-8dc6-3505a59afa15', '05672be105987339cd17fd816b5e8f65e90881d7c1827cec9404d5696412cfbe', '2024-02-27 15:45:41.352', '20240227154540_generate_database', NULL, NULL, '2024-02-27 15:45:40.737', 1);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `accounts_user_id_fkey` (`user_id`);

--
-- Chỉ mục cho bảng `author`
--
ALTER TABLE `author`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `book_author`
--
ALTER TABLE `book_author`
  ADD PRIMARY KEY (`id`),
  ADD KEY `book_author_book_id_fkey` (`book_id`),
  ADD KEY `book_author_author_id_fkey` (`author_id`);

--
-- Chỉ mục cho bảng `book_genre`
--
ALTER TABLE `book_genre`
  ADD PRIMARY KEY (`id`),
  ADD KEY `book_genre_book_id_fkey` (`book_id`),
  ADD KEY `book_genre_genre_id_fkey` (`genre_id`);

--
-- Chỉ mục cho bảng `genre`
--
ALTER TABLE `genre`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `subcription`
--
ALTER TABLE `subcription`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Subcription_subcription_id_fkey` (`subcription_id`);

--
-- Chỉ mục cho bảng `subcription_history`
--
ALTER TABLE `subcription_history`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `_prisma_migrations`
--
ALTER TABLE `_prisma_migrations`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `accounts`
--
ALTER TABLE `accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `author`
--
ALTER TABLE `author`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT cho bảng `book`
--
ALTER TABLE `book`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT cho bảng `book_author`
--
ALTER TABLE `book_author`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT cho bảng `book_genre`
--
ALTER TABLE `book_genre`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT cho bảng `genre`
--
ALTER TABLE `genre`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT cho bảng `subcription`
--
ALTER TABLE `subcription`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `subcription_history`
--
ALTER TABLE `subcription_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `accounts`
--
ALTER TABLE `accounts`
  ADD CONSTRAINT `accounts_user_id_fkey` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Các ràng buộc cho bảng `book_author`
--
ALTER TABLE `book_author`
  ADD CONSTRAINT `book_author_author_id_fkey` FOREIGN KEY (`author_id`) REFERENCES `author` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `book_author_book_id_fkey` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Các ràng buộc cho bảng `book_genre`
--
ALTER TABLE `book_genre`
  ADD CONSTRAINT `book_genre_book_id_fkey` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `book_genre_genre_id_fkey` FOREIGN KEY (`genre_id`) REFERENCES `genre` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Các ràng buộc cho bảng `subcription`
--
ALTER TABLE `subcription`
  ADD CONSTRAINT `Subcription_subcription_id_fkey` FOREIGN KEY (`subcription_id`) REFERENCES `subcription_history` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
