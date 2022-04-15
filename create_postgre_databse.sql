DROP TABLE IF EXISTS pc_status_info.network_info;
DROP TABLE IF EXISTS pc_status_info.storage_info;
DROP TABLE IF EXISTS pc_status_info.check_record;
DROP TABLE IF EXISTS pc_status_info.system_info;


CREATE TABLE IF NOT EXISTS pc_status_info.system_info(
MAC_addr                VARCHAR(50)			NOT NULL    PRIMARY KEY,
host_name               VARCHAR(50)         NOT NULL,
operating_system        VARCHAR(50)         NOT NULL,
CPU_model               VARCHAR(50)         NOT NULL
);

CREATE TABLE IF NOT EXISTS pc_status_info.check_record(
check_ID                SERIAL               NOT NULL    PRIMARY KEY,
check_time              TIMESTAMP            NOT NULL,
fk_MAC_addr             VARCHAR(50)			NOT NULL,    
FOREIGN KEY(fk_MAC_addr)
REFERENCES system_info(MAC_addr)
ON DELETE CASCADE
ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS pc_status_info.network_info(
fk_check_ID             INT                 NOT NULL,
IP_addr                 VARCHAR(20)         NOT NULL,
connection_status       VARCHAR(20)			NOT NULL,    
FOREIGN KEY(fk_check_ID)
REFERENCES pc_status_info.check_record(check_ID)
ON DELETE CASCADE
ON UPDATE CASCADE,
PRIMARY KEY(fk_check_ID,IP_addr)
);

CREATE TABLE IF NOT EXISTS pc_status_info.storage_info(
fk_check_ID             INT                 NOT NULL,
disk_partition          VARCHAR(5)          NOT NULL,
used                    VARCHAR(20)			NOT NULL,    
free                    VARCHAR(20)			NOT NULL,    
total                   VARCHAR(20)			NOT NULL,    
FOREIGN KEY(fk_check_ID)
REFERENCES pc_status_info.check_record(check_ID)
ON DELETE CASCADE
ON UPDATE CASCADE,
PRIMARY KEY(fk_check_ID, disk_partition)
);