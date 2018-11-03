/*
 Navicat Premium Data Transfer

 Source Server         : 192.168.100.129
 Source Server Type    : MySQL
 Source Server Version : 50724
 Source Host           : 192.168.100.129:3306
 Source Schema         : onlinejudge

 Target Server Type    : MySQL
 Target Server Version : 50724
 File Encoding         : 65001

 Date: 24/10/2018 21:17:56
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 69 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add permission', 1, 'add_permission');
INSERT INTO `auth_permission` VALUES (2, 'Can change permission', 1, 'change_permission');
INSERT INTO `auth_permission` VALUES (3, 'Can delete permission', 1, 'delete_permission');
INSERT INTO `auth_permission` VALUES (4, 'Can add group', 2, 'add_group');
INSERT INTO `auth_permission` VALUES (5, 'Can change group', 2, 'change_group');
INSERT INTO `auth_permission` VALUES (6, 'Can delete group', 2, 'delete_group');
INSERT INTO `auth_permission` VALUES (7, 'Can view group', 2, 'view_group');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 1, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add log entry', 3, 'add_logentry');
INSERT INTO `auth_permission` VALUES (10, 'Can change log entry', 3, 'change_logentry');
INSERT INTO `auth_permission` VALUES (11, 'Can delete log entry', 3, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (12, 'Can view log entry', 3, 'view_logentry');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO `auth_permission` VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO `auth_permission` VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO `auth_permission` VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO `auth_permission` VALUES (21, 'Can add 用户', 6, 'add_user');
INSERT INTO `auth_permission` VALUES (22, 'Can change 用户', 6, 'change_user');
INSERT INTO `auth_permission` VALUES (23, 'Can delete 用户', 6, 'delete_user');
INSERT INTO `auth_permission` VALUES (24, 'Can add user profile', 7, 'add_userprofile');
INSERT INTO `auth_permission` VALUES (25, 'Can change user profile', 7, 'change_userprofile');
INSERT INTO `auth_permission` VALUES (26, 'Can delete user profile', 7, 'delete_userprofile');
INSERT INTO `auth_permission` VALUES (27, 'Can view 用户', 6, 'view_user');
INSERT INTO `auth_permission` VALUES (28, 'Can view user profile', 7, 'view_userprofile');
INSERT INTO `auth_permission` VALUES (29, 'Can add 题目', 8, 'add_problems');
INSERT INTO `auth_permission` VALUES (30, 'Can change 题目', 8, 'change_problems');
INSERT INTO `auth_permission` VALUES (31, 'Can delete 题目', 8, 'delete_problems');
INSERT INTO `auth_permission` VALUES (32, 'Can add problem tag', 9, 'add_problemtag');
INSERT INTO `auth_permission` VALUES (33, 'Can change problem tag', 9, 'change_problemtag');
INSERT INTO `auth_permission` VALUES (34, 'Can delete problem tag', 9, 'delete_problemtag');
INSERT INTO `auth_permission` VALUES (35, 'Can view 题目', 8, 'view_problems');
INSERT INTO `auth_permission` VALUES (36, 'Can view problem tag', 9, 'view_problemtag');
INSERT INTO `auth_permission` VALUES (37, 'Can add 用户收藏', 10, 'add_usercollect');
INSERT INTO `auth_permission` VALUES (38, 'Can change 用户收藏', 10, 'change_usercollect');
INSERT INTO `auth_permission` VALUES (39, 'Can delete 用户收藏', 10, 'delete_usercollect');
INSERT INTO `auth_permission` VALUES (40, 'Can view 用户收藏', 10, 'view_usercollect');
INSERT INTO `auth_permission` VALUES (41, 'Can add 比赛', 11, 'add_contests');
INSERT INTO `auth_permission` VALUES (42, 'Can change 比赛', 11, 'change_contests');
INSERT INTO `auth_permission` VALUES (43, 'Can delete 比赛', 11, 'delete_contests');
INSERT INTO `auth_permission` VALUES (44, 'Can view 比赛', 11, 'view_contests');
INSERT INTO `auth_permission` VALUES (45, 'Can add 提交记录', 12, 'add_submissions');
INSERT INTO `auth_permission` VALUES (46, 'Can change 提交记录', 12, 'change_submissions');
INSERT INTO `auth_permission` VALUES (47, 'Can delete 提交记录', 12, 'delete_submissions');
INSERT INTO `auth_permission` VALUES (48, 'Can view 提交记录', 12, 'view_submissions');
INSERT INTO `auth_permission` VALUES (49, 'Can add Bookmark', 13, 'add_bookmark');
INSERT INTO `auth_permission` VALUES (50, 'Can change Bookmark', 13, 'change_bookmark');
INSERT INTO `auth_permission` VALUES (51, 'Can delete Bookmark', 13, 'delete_bookmark');
INSERT INTO `auth_permission` VALUES (52, 'Can add User Setting', 14, 'add_usersettings');
INSERT INTO `auth_permission` VALUES (53, 'Can change User Setting', 14, 'change_usersettings');
INSERT INTO `auth_permission` VALUES (54, 'Can delete User Setting', 14, 'delete_usersettings');
INSERT INTO `auth_permission` VALUES (55, 'Can add User Widget', 15, 'add_userwidget');
INSERT INTO `auth_permission` VALUES (56, 'Can change User Widget', 15, 'change_userwidget');
INSERT INTO `auth_permission` VALUES (57, 'Can delete User Widget', 15, 'delete_userwidget');
INSERT INTO `auth_permission` VALUES (58, 'Can add log entry', 16, 'add_log');
INSERT INTO `auth_permission` VALUES (59, 'Can change log entry', 16, 'change_log');
INSERT INTO `auth_permission` VALUES (60, 'Can delete log entry', 16, 'delete_log');
INSERT INTO `auth_permission` VALUES (61, 'Can view Bookmark', 13, 'view_bookmark');
INSERT INTO `auth_permission` VALUES (62, 'Can view log entry', 16, 'view_log');
INSERT INTO `auth_permission` VALUES (63, 'Can view User Setting', 14, 'view_usersettings');
INSERT INTO `auth_permission` VALUES (64, 'Can view User Widget', 15, 'view_userwidget');
INSERT INTO `auth_permission` VALUES (65, 'Can add Token', 17, 'add_token');
INSERT INTO `auth_permission` VALUES (66, 'Can change Token', 17, 'change_token');
INSERT INTO `auth_permission` VALUES (67, 'Can delete Token', 17, 'delete_token');
INSERT INTO `auth_permission` VALUES (68, 'Can view Token', 17, 'view_token');

-- ----------------------------
-- Table structure for authtoken_token
-- ----------------------------
DROP TABLE IF EXISTS `authtoken_token`;
CREATE TABLE `authtoken_token`  (
  `key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `created` datetime(0) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`) USING BTREE,
  UNIQUE INDEX `user_id`(`user_id`) USING BTREE,
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for contests
-- ----------------------------
DROP TABLE IF EXISTS `contests`;
CREATE TABLE `contests`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contest_id` int(11) NOT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `start_time` datetime(0) NOT NULL,
  `end_time` datetime(0) NOT NULL,
  `create_time` datetime(0) NOT NULL,
  `create_by_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `title`(`title`) USING BTREE,
  INDEX `contests_contest_id_bc00dd36`(`contest_id`) USING BTREE,
  INDEX `contests_create_by_id_37cf2704_fk_users_user_id`(`create_by_id`) USING BTREE,
  CONSTRAINT `contests_create_by_id_37cf2704_fk_users_user_id` FOREIGN KEY (`create_by_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(0) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (3, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (1, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (17, 'authtoken', 'token');
INSERT INTO `django_content_type` VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (11, 'contests', 'contests');
INSERT INTO `django_content_type` VALUES (8, 'problems', 'problems');
INSERT INTO `django_content_type` VALUES (9, 'problems', 'problemtag');
INSERT INTO `django_content_type` VALUES (5, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (12, 'submissions', 'submissions');
INSERT INTO `django_content_type` VALUES (6, 'users', 'user');
INSERT INTO `django_content_type` VALUES (7, 'users', 'userprofile');
INSERT INTO `django_content_type` VALUES (10, 'user_operation', 'usercollect');
INSERT INTO `django_content_type` VALUES (13, 'xadmin', 'bookmark');
INSERT INTO `django_content_type` VALUES (16, 'xadmin', 'log');
INSERT INTO `django_content_type` VALUES (14, 'xadmin', 'usersettings');
INSERT INTO `django_content_type` VALUES (15, 'xadmin', 'userwidget');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 32 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2018-10-15 10:11:05');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2018-10-15 10:11:05');
INSERT INTO `django_migrations` VALUES (3, 'auth', '0001_initial', '2018-10-15 10:11:06');
INSERT INTO `django_migrations` VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2018-10-15 10:11:06');
INSERT INTO `django_migrations` VALUES (5, 'auth', '0003_alter_user_email_max_length', '2018-10-15 10:11:06');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0004_alter_user_username_opts', '2018-10-15 10:11:06');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0005_alter_user_last_login_null', '2018-10-15 10:11:06');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0006_require_contenttypes_0002', '2018-10-15 10:11:06');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2018-10-15 10:11:06');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0008_alter_user_username_max_length', '2018-10-15 10:11:06');
INSERT INTO `django_migrations` VALUES (11, 'users', '0001_initial', '2018-10-15 10:11:08');
INSERT INTO `django_migrations` VALUES (12, 'admin', '0001_initial', '2018-10-15 10:11:08');
INSERT INTO `django_migrations` VALUES (13, 'admin', '0002_logentry_remove_auto_add', '2018-10-15 10:11:08');
INSERT INTO `django_migrations` VALUES (14, 'authtoken', '0001_initial', '2018-10-15 10:11:09');
INSERT INTO `django_migrations` VALUES (15, 'authtoken', '0002_auto_20160226_1747', '2018-10-15 10:11:09');
INSERT INTO `django_migrations` VALUES (16, 'contests', '0001_initial', '2018-10-15 10:11:09');
INSERT INTO `django_migrations` VALUES (17, 'contests', '0002_contests_create_by', '2018-10-15 10:11:10');
INSERT INTO `django_migrations` VALUES (18, 'problems', '0001_initial', '2018-10-15 10:11:11');
INSERT INTO `django_migrations` VALUES (19, 'sessions', '0001_initial', '2018-10-15 10:11:11');
INSERT INTO `django_migrations` VALUES (20, 'submissions', '0001_initial', '2018-10-15 10:11:11');
INSERT INTO `django_migrations` VALUES (21, 'submissions', '0002_submissions_user', '2018-10-15 10:11:12');
INSERT INTO `django_migrations` VALUES (22, 'user_operation', '0001_initial', '2018-10-15 10:11:12');
INSERT INTO `django_migrations` VALUES (23, 'user_operation', '0002_auto_20181015_1010', '2018-10-15 10:11:13');
INSERT INTO `django_migrations` VALUES (24, 'xadmin', '0001_initial', '2018-10-15 10:11:14');
INSERT INTO `django_migrations` VALUES (25, 'xadmin', '0002_log', '2018-10-15 10:11:14');
INSERT INTO `django_migrations` VALUES (26, 'xadmin', '0003_auto_20160715_0100', '2018-10-15 10:11:15');
INSERT INTO `django_migrations` VALUES (27, 'users', '0002_auto_20181022_1357', '2018-10-22 13:57:34');
INSERT INTO `django_migrations` VALUES (28, 'submissions', '0003_auto_20181024_1057', '2018-10-24 10:57:25');
INSERT INTO `django_migrations` VALUES (29, 'users', '0003_auto_20181024_1057', '2018-10-24 10:57:25');
INSERT INTO `django_migrations` VALUES (30, 'submissions', '0004_remove_submissions_submission_id', '2018-10-24 11:57:20');
INSERT INTO `django_migrations` VALUES (31, 'submissions', '0005_auto_20181024_1210', '2018-10-24 12:10:27');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(0) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('ytmtjiftpari1j0jxyowe3wbn9qbuuw1', 'ZWQxNWUxY2ExMmY4NGFmM2ZiZDljZDAzMTkyNTM0ZmVjNDRhZDkxMDp7Il9hdXRoX3VzZXJfaWQiOiIxNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJzLnZpZXdzLkN1c3RvbUJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkOTQ5MTM4Y2VjYzk1OTIwYWI5NmZkMDVjOTFhYThhNzQ4NjM5ZGIwIn0=', '2018-11-05 15:22:10');

-- ----------------------------
-- Table structure for problem_tag
-- ----------------------------
DROP TABLE IF EXISTS `problem_tag`;
CREATE TABLE `problem_tag`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for problems
-- ----------------------------
DROP TABLE IF EXISTS `problems`;
CREATE TABLE `problems`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `problem_id` int(11) NOT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `description` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `input_description` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `output_description` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sample_input` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sample_output` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `time_limit` int(11) NOT NULL,
  `memory_limit` int(11) NOT NULL,
  `submission_number` int(11) NOT NULL,
  `accepted_number` int(11) NOT NULL,
  `wrong_answer_number` int(11) NOT NULL,
  `time_limit_number` int(11) NOT NULL,
  `memory_limit_number` int(11) NOT NULL,
  `runtime_error_number` int(11) NOT NULL,
  `output_limit_number` int(11) NOT NULL,
  `compile_error_number` int(11) NOT NULL,
  `presentation_error_number` int(11) NOT NULL,
  `create_time` datetime(0) NOT NULL,
  `contest_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `title`(`title`) USING BTREE,
  INDEX `problems_contest_id_2f866235_fk_contests_id`(`contest_id`) USING BTREE,
  INDEX `problems_problem_id_ab1dfed2`(`problem_id`) USING BTREE,
  CONSTRAINT `problems_contest_id_2f866235_fk_contests_id` FOREIGN KEY (`contest_id`) REFERENCES `contests` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of problems
-- ----------------------------
INSERT INTO `problems` VALUES (1, 1, 'A+B Problem1', '给你两个整数，求两个整数之和。', '一行，两个整数a,b。', '一行，a+b的值', '5 7', '12', 1000, 64, 1, 1, 0, 0, 0, 0, 0, 0, 0, '2018-10-18 17:29:24', NULL);
INSERT INTO `problems` VALUES (2, 2, 'A+B Problem2', '给你两个整数，求两个整数之和。', '一行，两个整数a,b。', '一行，a+b的值', '5 7', '12', 1000, 64, 1, 1, 0, 0, 0, 0, 0, 0, 0, '2018-10-18 17:30:08', NULL);
INSERT INTO `problems` VALUES (3, 3, 'A+B Problem3', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', 1000, 64, 1, 1, 0, 0, 0, 0, 0, 0, 0, '2018-10-18 17:30:58', NULL);
INSERT INTO `problems` VALUES (4, 4, 'A+B Problem4', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', 1000, 64, 1, 1, 0, 0, 0, 0, 0, 0, 0, '2018-10-18 17:31:24', NULL);
INSERT INTO `problems` VALUES (5, 5, 'A+B Problem5', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', 1000, 64, 1, 1, 0, 0, 0, 0, 0, 0, 0, '2018-10-18 17:32:30', NULL);
INSERT INTO `problems` VALUES (6, 6, 'A+B Problem6', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', 1000, 64, 1, 1, 0, 0, 0, 0, 0, 0, 0, '2018-10-18 17:32:52', NULL);
INSERT INTO `problems` VALUES (7, 7, 'A+B Problem7', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', 1000, 64, 1, 1, 0, 0, 0, 0, 0, 0, 0, '2018-10-18 17:33:09', NULL);
INSERT INTO `problems` VALUES (8, 8, 'A+B Problem8', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', 1000, 64, 1, 1, 0, 0, 0, 0, 0, 0, 0, '2018-10-18 17:33:34', NULL);
INSERT INTO `problems` VALUES (9, 9, 'A+B Problem9', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', 1000, 64, 1, 1, 0, 0, 0, 0, 0, 0, 0, '2018-10-18 17:33:59', NULL);
INSERT INTO `problems` VALUES (10, 10, 'A+B Problem10', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', 1000, 64, 1, 1, 0, 0, 0, 0, 0, 0, 0, '2018-10-18 17:34:22', NULL);
INSERT INTO `problems` VALUES (11, 11, 'A+B Problem11', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', 1000, 64, 1, 1, 0, 0, 0, 0, 0, 0, 0, '2018-10-18 17:34:38', NULL);
INSERT INTO `problems` VALUES (12, 12, 'A+B Problem12', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', 1000, 64, 1, 1, 0, 0, 0, 0, 0, 0, 0, '2018-10-18 17:34:58', NULL);
INSERT INTO `problems` VALUES (13, 13, 'A+B Problem13', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', 1000, 64, 1, 1, 0, 0, 0, 0, 0, 0, 0, '2018-10-18 17:35:15', NULL);
INSERT INTO `problems` VALUES (14, 14, 'A+B Problem14', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', '给你两个整数，求两个整数之和。', 1000, 64, 1, 1, 0, 0, 0, 0, 0, 0, 0, '2018-10-18 17:35:32', NULL);

-- ----------------------------
-- Table structure for problems_tags
-- ----------------------------
DROP TABLE IF EXISTS `problems_tags`;
CREATE TABLE `problems_tags`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `problems_id` int(11) NOT NULL,
  `problemtag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `problems_tags_problems_id_problemtag_id_8f74b288_uniq`(`problems_id`, `problemtag_id`) USING BTREE,
  INDEX `problems_tags_problemtag_id_c4c638f9_fk_problem_tag_id`(`problemtag_id`) USING BTREE,
  CONSTRAINT `problems_tags_problems_id_f7510a71_fk_problems_id` FOREIGN KEY (`problems_id`) REFERENCES `problems` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `problems_tags_problemtag_id_c4c638f9_fk_problem_tag_id` FOREIGN KEY (`problemtag_id`) REFERENCES `problem_tag` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for submissions
-- ----------------------------
DROP TABLE IF EXISTS `submissions`;
CREATE TABLE `submissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `submit_time` datetime(0) NOT NULL,
  `result` int(11) NOT NULL,
  `memory_cost` int(11) NOT NULL,
  `time_cost` int(11) NOT NULL,
  `code` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `contest_id` int(11) NULL DEFAULT NULL,
  `problem_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `submissions_problem_id_f3412834_fk_problems_id`(`problem_id`) USING BTREE,
  INDEX `submissions_result_a82d139c`(`result`) USING BTREE,
  INDEX `submissions_user_id_14b0d84e_fk_users_user_id`(`user_id`) USING BTREE,
  INDEX `submissions_contest_id_3c8de7a5_fk_contests_id`(`contest_id`) USING BTREE,
  CONSTRAINT `submissions_contest_id_3c8de7a5_fk_contests_id` FOREIGN KEY (`contest_id`) REFERENCES `contests` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `submissions_problem_id_f3412834_fk_problems_id` FOREIGN KEY (`problem_id`) REFERENCES `problems` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `submissions_user_id_14b0d84e_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 47 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of submissions
-- ----------------------------
INSERT INTO `submissions` VALUES (1, '2018-10-24 12:10:33', 4, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (2, '2018-10-24 12:12:24', 1, 1, 1, '5', NULL, 1, 16);
INSERT INTO `submissions` VALUES (3, '2018-10-24 13:13:21', 1, 2, 1, '5', NULL, 1, 1);
INSERT INTO `submissions` VALUES (4, '2018-10-24 15:12:03', 1, 1, 1, '222222', NULL, 1, 1);
INSERT INTO `submissions` VALUES (5, '2018-10-24 16:15:46', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (6, '2018-10-24 16:16:30', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (7, '2018-10-24 16:17:04', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (8, '2018-10-24 16:19:17', 2, 2, 2, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (9, '2018-10-24 16:20:20', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (10, '2018-10-24 16:20:38', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (11, '2018-10-24 16:21:01', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (12, '2018-10-24 16:21:07', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (13, '2018-10-24 16:22:03', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (14, '2018-10-24 16:22:51', 2, 2, 2, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (15, '2018-10-24 16:23:39', 2, 2, 2, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (16, '2018-10-24 16:24:35', 2, 2, 2, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (17, '2018-10-24 16:25:30', 2, 2, 2, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (18, '2018-10-24 16:26:03', 2, 2, 2, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (19, '2018-10-24 16:32:44', 2, 2, 2, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (20, '2018-10-24 16:36:35', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (21, '2018-10-24 16:36:48', 2, 2, 2, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (22, '2018-10-24 16:38:07', 2, 2, 2, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (23, '2018-10-24 16:44:10', 1, 1, 1, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (24, '2018-10-24 16:46:00', 1, 1, 1, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (25, '2018-10-24 16:46:27', 1, 1, 1, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (26, '2018-10-24 16:47:32', 1, 1, 1, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (27, '2018-10-24 16:49:43', 1, 1, 2, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (28, '2018-10-24 16:50:55', 1, 1, 2, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (29, '2018-10-24 16:52:29', 1, 1, 2, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (30, '2018-10-24 16:56:10', 1, 1, 2, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (31, '2018-10-24 16:56:55', 1, 1, 2, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (32, '2018-10-24 16:57:34', 1, 1, 2, '2', NULL, 1, 1);
INSERT INTO `submissions` VALUES (33, '2018-10-24 17:37:50', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (34, '2018-10-24 17:43:55', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (35, '2018-10-24 17:45:14', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (36, '2018-10-24 17:45:37', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (37, '2018-10-24 17:45:47', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (38, '2018-10-24 17:46:21', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (39, '2018-10-24 17:48:14', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (40, '2018-10-24 17:49:29', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (41, '2018-10-24 17:51:18', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (42, '2018-10-24 17:54:19', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (43, '2018-10-24 18:19:59', 5, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (44, '2018-10-24 18:21:01', 5, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (45, '2018-10-24 18:26:54', 1, 1, 1, '1', NULL, 1, 1);
INSERT INTO `submissions` VALUES (46, '2018-10-24 18:27:15', 5, 1, 1, '1', NULL, 1, 1);

-- ----------------------------
-- Table structure for user_collect
-- ----------------------------
DROP TABLE IF EXISTS `user_collect`;
CREATE TABLE `user_collect`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(0) NOT NULL,
  `problems_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_collect_user_id_problems_id_f34ad191_uniq`(`user_id`, `problems_id`) USING BTREE,
  INDEX `user_collect_problems_id_9e521a4b_fk_problems_id`(`problems_id`) USING BTREE,
  CONSTRAINT `user_collect_problems_id_9e521a4b_fk_problems_id` FOREIGN KEY (`problems_id`) REFERENCES `problems` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `user_collect_user_id_4deac90d_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for users_user
-- ----------------------------
DROP TABLE IF EXISTS `users_user`;
CREATE TABLE `users_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(0) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(0) NOT NULL,
  `email` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE,
  UNIQUE INDEX `users_user_email_243f6e77_uniq`(`email`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 26 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of users_user
-- ----------------------------
INSERT INTO `users_user` VALUES (1, 'pbkdf2_sha256$36000$CFaNxauLoDiL$6dg9xJKLq0MuFVgbToTLWftoxeQ7jbVzYuL/dinN6D8=', '2018-10-19 17:16:33', 1, 'admin', '', '', 1, 1, '2018-10-18 17:28:02', '957824770@qq.com');
INSERT INTO `users_user` VALUES (16, 'pbkdf2_sha256$36000$Y65aPoBJ85Ww$JOPIHrKe+cw56mU3QvXjU1/GAbFUPKWdZ0qTlBn9LPA=', '2018-10-22 15:22:10', 0, 'test', '', '', 0, 1, '2018-10-22 14:46:28', '1@qq.com');
INSERT INTO `users_user` VALUES (17, 'pbkdf2_sha256$36000$bVSXKzOlkCvA$ECIBX8+6QrlVrBSKhr4eiLbSmy79sUhwd5wyPiMlnkE=', NULL, 0, 'test1', '', '', 0, 1, '2018-10-22 16:36:24', '123456@qq.com');
INSERT INTO `users_user` VALUES (18, 'pbkdf2_sha256$36000$vy1bxAjO0WhW$Q465pT5SK6O9jGdzAxWgJ2M/N7K4uX81Y51E3e0LnOA=', NULL, 0, '1', '', '', 0, 1, '2018-10-22 16:39:27', '12@qq.com');
INSERT INTO `users_user` VALUES (19, 'pbkdf2_sha256$36000$wslQN1uCQ0nG$HgM9KHsEF2cu9QGDS8AcnlrlX/VDnQxFgz2SrwlZGl4=', NULL, 0, '12', '', '', 0, 1, '2018-10-22 16:42:02', '123@qq.com');
INSERT INTO `users_user` VALUES (20, 'pbkdf2_sha256$36000$2qGxCcYai1O6$7asqfGwLfzz9bElr6hG1d/mcMSnYvsGnV/SAF0WVDAw=', NULL, 0, '1234', '', '', 0, 1, '2018-10-22 16:43:41', '1111@qq.com');
INSERT INTO `users_user` VALUES (21, 'pbkdf2_sha256$36000$5zECnZq1ExBv$Or2BBPAk9FwzWm7kflJCdXuVe7v8RaOQ33/7+deDK7k=', NULL, 0, '123456', '', '', 0, 1, '2018-10-22 16:46:07', '11111@qq.com');
INSERT INTO `users_user` VALUES (22, 'pbkdf2_sha256$36000$cWLeLNQHeBA0$hKk1TesJwPxsztbKqSJvIKQnURn5hK4ZGrqxCUDDvwE=', NULL, 0, 'test22', '', '', 0, 1, '2018-10-24 11:13:58', '111@qq.com');
INSERT INTO `users_user` VALUES (23, '123456', NULL, 0, '111', '', '', 0, 1, '2018-10-24 11:17:32', '222@qq.com');
INSERT INTO `users_user` VALUES (24, 'pbkdf2_sha256$36000$qghU4qyUTSKv$6RBCcu2/z6wdb2QB6u+5/lVjtFPKXlWZlW3mrbKV6Uk=', NULL, 0, '22222', '', '', 0, 1, '2018-10-24 11:18:43', '22222@qq.com');
INSERT INTO `users_user` VALUES (25, 'pbkdf2_sha256$36000$QPK7vCSesGUf$W4mCcNh9xqiWQpsF9ggJfVG9JKl6LAsK43RWXNQKjns=', NULL, 0, 'test444', '', '', 0, 1, '2018-10-24 11:25:39', '555@qq.com');

-- ----------------------------
-- Table structure for users_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `users_user_groups`;
CREATE TABLE `users_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `users_user_groups_user_id_group_id_b88eab82_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `users_user_groups_group_id_9afc8d0e_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `users_user_groups_user_id_5f6f5a90_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for users_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `users_user_user_permissions`;
CREATE TABLE `users_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `users_user_user_permissions_user_id_permission_id_43338c45_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `users_user_user_perm_permission_id_0b93982e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `users_user_user_permissions_user_id_20aca447_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for users_userprofile
-- ----------------------------
DROP TABLE IF EXISTS `users_userprofile`;
CREATE TABLE `users_userprofile`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `avatar` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `accepted_number` int(11) NOT NULL,
  `submission_number` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_id`(`user_id`) USING BTREE,
  CONSTRAINT `users_userprofile_user_id_87251ef1_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for xadmin_bookmark
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_bookmark`;
CREATE TABLE `xadmin_bookmark`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `url_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `query` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_share` tinyint(1) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `user_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `xadmin_bookmark_content_type_id_60941679_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `xadmin_bookmark_user_id_42d307fc_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `xadmin_bookmark_content_type_id_60941679_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `xadmin_bookmark_user_id_42d307fc_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for xadmin_log
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_log`;
CREATE TABLE `xadmin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(0) NOT NULL,
  `ip_addr` char(39) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id`(`content_type_id`) USING BTREE,
  INDEX `xadmin_log_user_id_bb16a176_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `xadmin_log_user_id_bb16a176_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of xadmin_log
-- ----------------------------
INSERT INTO `xadmin_log` VALUES (1, '2018-10-18 17:29:24', '127.0.0.1', '1', 'A+B Problem', 'create', '已添加。', 8, 1);
INSERT INTO `xadmin_log` VALUES (2, '2018-10-18 17:29:30', '127.0.0.1', '1', 'A+B Problem', 'change', '没有字段被修改。', 8, 1);
INSERT INTO `xadmin_log` VALUES (3, '2018-10-18 17:30:08', '127.0.0.1', '2', 'A + B', 'create', '已添加。', 8, 1);
INSERT INTO `xadmin_log` VALUES (4, '2018-10-18 17:30:26', '127.0.0.1', '2', 'A+B Problem1', 'change', '修改 title', 8, 1);
INSERT INTO `xadmin_log` VALUES (5, '2018-10-18 17:30:58', '127.0.0.1', '3', 'A+B Problem2', 'create', '已添加。', 8, 1);
INSERT INTO `xadmin_log` VALUES (6, '2018-10-18 17:31:24', '127.0.0.1', '4', 'A+B Problem4', 'create', '已添加。', 8, 1);
INSERT INTO `xadmin_log` VALUES (7, '2018-10-18 17:31:30', '127.0.0.1', '3', 'A+B Problem3', 'change', '修改 title', 8, 1);
INSERT INTO `xadmin_log` VALUES (8, '2018-10-18 17:31:33', '127.0.0.1', '2', 'A+B Problem2', 'change', '修改 title', 8, 1);
INSERT INTO `xadmin_log` VALUES (9, '2018-10-18 17:31:36', '127.0.0.1', '1', 'A+B Problem1', 'change', '修改 title', 8, 1);
INSERT INTO `xadmin_log` VALUES (10, '2018-10-18 17:32:30', '127.0.0.1', '5', 'A+B Problem5', 'create', '已添加。', 8, 1);
INSERT INTO `xadmin_log` VALUES (11, '2018-10-18 17:32:52', '127.0.0.1', '6', 'A+B Problem6', 'create', '已添加。', 8, 1);
INSERT INTO `xadmin_log` VALUES (12, '2018-10-18 17:33:09', '127.0.0.1', '7', 'A+B Problem7', 'create', '已添加。', 8, 1);
INSERT INTO `xadmin_log` VALUES (13, '2018-10-18 17:33:34', '127.0.0.1', '8', 'A+B Problem8', 'create', '已添加。', 8, 1);
INSERT INTO `xadmin_log` VALUES (14, '2018-10-18 17:33:59', '127.0.0.1', '9', 'A+B Problem9', 'create', '已添加。', 8, 1);
INSERT INTO `xadmin_log` VALUES (15, '2018-10-18 17:34:22', '127.0.0.1', '10', 'A+B Problem10', 'create', '已添加。', 8, 1);
INSERT INTO `xadmin_log` VALUES (16, '2018-10-18 17:34:38', '127.0.0.1', '11', 'A+B Problem11', 'create', '已添加。', 8, 1);
INSERT INTO `xadmin_log` VALUES (17, '2018-10-18 17:34:58', '127.0.0.1', '12', 'A+B Problem12', 'create', '已添加。', 8, 1);
INSERT INTO `xadmin_log` VALUES (18, '2018-10-18 17:35:15', '127.0.0.1', '13', 'A+B Problem13', 'create', '已添加。', 8, 1);
INSERT INTO `xadmin_log` VALUES (19, '2018-10-18 17:35:32', '127.0.0.1', '14', 'A+B Problem14', 'create', '已添加。', 8, 1);

-- ----------------------------
-- Table structure for xadmin_usersettings
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_usersettings`;
CREATE TABLE `xadmin_usersettings`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `value` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `xadmin_usersettings_user_id_edeabe4a_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `xadmin_usersettings_user_id_edeabe4a_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of xadmin_usersettings
-- ----------------------------
INSERT INTO `xadmin_usersettings` VALUES (1, 'dashboard:home:pos', '', 1);
INSERT INTO `xadmin_usersettings` VALUES (2, 'site-theme', 'https://bootswatch.com/3/paper/bootstrap.min.css', 1);

-- ----------------------------
-- Table structure for xadmin_userwidget
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_userwidget`;
CREATE TABLE `xadmin_userwidget`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `widget_type` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `value` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `xadmin_userwidget_user_id_c159233a_fk_users_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `xadmin_userwidget_user_id_c159233a_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
