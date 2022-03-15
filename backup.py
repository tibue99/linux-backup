import os
import time
from sys import platform

import config
from logger import Logger

date = time.strftime(config.date_format)
logger = Logger("backup.log")


def os_check():
    """Check if the script is running on a unix based operating system"""
    if platform.startswith('linux') or platform == 'darwin':
        return True
    else:
        return False


def mysql_backup():
    logger.log("INFO", "Starting backup for MySQL database...")
    tmp_check = os.system(f"cd {config.backup_location}")
    if tmp_check == 0:
        mysql_backup_file_name = f"{get_file_name('mysqlBackup')}.sql"
        create_backup = os.system(
            f"cd {config.backup_location} && mysqldump -u {config.mysql_user} -p'{config.mysql_password}'"
            f" --all-databases > {mysql_backup_file_name}")

        if create_backup == 0:
            logger.log("SUCCESS", "MySQL database backup created successfully")
        else:
            logger.log("ERROR", "MySQL database backup failed")
            os.system(f"cd {config.backup_location} && rm mysqlbackup-{date}.sql")
    else:
        logger.log("ERROR", "Mount not exits")


def backup():
    logger.log("INFO", f"Starting backup for {len(config.backup_dirs)} directories...")
    if len(config.backup_dirs) == 0:
        logger.log("INFO", "No directories to backup")
    else:
        exclude_str = ""
        for file in config.exclude:
            exclude_str += f"--exclude '{file}' "

        for index, folder in enumerate(config.backup_dirs):
            backup_file_name = get_file_name(f"backup{index + 1}.tar.gz")
            logger.log("INFO", f"Starting backup for {folder}...")
            status = os.system(
                f"cd {config.backup_location} && tar {exclude_str} -czvf {backup_file_name} {folder}"
            )
            if status == 0:
                logger.log("SUCCESS", f"Backup for {folder} created successfully")
            else:
                logger.log("ERROR", f"Failed to backup {folder}")


def clear_backups():
    logger.log("INFO", "Cleaning backup dir...")
    for file in os.listdir(config.backup_location):
        if os.path.isfile(file):
            os.remove(file)
        elif os.path.isdir(file):
            os.rmdir(file)
        else:
            logger.log("ERROR", f"{file} can't be deleted!")
    logger.log("SUCCESS", "Successfully deleted old backup files")


def get_file_name(name):
    file_name = config.backup_name_format
    file_name = file_name.replace('%date%', date)
    file_name = file_name.replace('%backupName%', name)
    print(file_name)
    return file_name


if os_check():
    if os.path.exists(config.backup_location):
        if config.clear_backups:
            clear_backups()
        if config.mysql_backup:
            mysql_backup()
        backup()
    else:
        logger.log("ERROR", "Failed to create backup")
        logger.log("ERROR", f"{config.backup_location} does not exist")
    logger.close_file()
else:
    logger.log("ERROR", "Sorry, this script is only for Linux or macOS")
    logger.close_file()
