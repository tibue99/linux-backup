# Locations to back up
backup_dirs = ["/home"]

# Exclude files or directories from backup
exclude = ["__pycache__", "venv"]

# Location for final backup
backup_location = "/media/backup"

# File name for final backup
backup_name_format = "%date%_%backupName%"

# Date format for file name
date_format = "%Y-%m-%d_%H-%M"

# Delete old backups?
clear_backups = False

# MySQL
mysql_backup = False
mysql_user = "root"
mysql_password = ""
