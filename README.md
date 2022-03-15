# Linux Backup Script

A script to create backups on linux systems.

## How to use the script

- Install [rClone](https://rclone.org/downloads/) and set up the preferred cloud storage
```shell
curl https://rclone.org/install.sh | sudo bash
rclone config
```
- Install screen and create new screen for [mounting](https://rclone.org/commands/rclone_mount/)
```shell
apt install screen
screen -S backup
rcloune mount Name: /path/to/folder --vfs-cache-mode writes
```
- Clone this repository and edit `config.py`
```shell
git clone https://github.com/tibue99/linux-backup
```
- End mounting
```shell
fusermount -uz /linux/path
```

## Manual backup
```shell
python3 backup.py
```

## Automatic backup
Set a cronjob to backup periodically. This [cronjob](https://crontab.guru/#0_3_*_*_*) creates a backup every day at 3 AM.
```shell
crontab -e
0 3 * * * python3 /path/to/backup.py

# View cronjobs
crontab -l
```

## Credits

This repository is based on the code of [Tutorialwork](https://github.com/Tutorialwork/Linux-Backup-Script).