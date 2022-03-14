# MySQL credentials (backup all databases to .sql file)
mysql_user = "root"
mysql_password = ""

# Location for final backup
backup_location = "/media/backup"
# Locations to back up
backup_dirs = ["/home"]

# Should the script do a MySQL Database backup?
mysql_backup = False
# Should the script delete old backups?
clear_backups = False

# Format for the date in the filename
date_format = "%Y-%m-%d_%H-%M"
# Backup filename
backup_name_format = "%date%_%backupName%"
