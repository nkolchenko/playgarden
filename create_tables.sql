create database siplog_parser character set utf8;
CREATE TABLE siplog_parser.sip_requests (id INT PRIMARY KEY AUTO_INCREMENT, direction VARCHAR(2), src_ip INT UNSIGNED, dst_ip INT UNSIGNED, CLI VARCHAR(30));
