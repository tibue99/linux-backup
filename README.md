# Linux Backup Script

A script to create backups on linux systems.

## How to use the script

Install [rClone](https://rclone.org/downloads/) and set up your preferred cloud storage
```shell
curl https://rclone.org/install.sh | sudo bash
rclone config
```

- To use a specific folder in your cloud storage, fill in the `root_folder_id` value
    - **Example:** If you use [pCloud]((https://www.pcloud.com/login)), you can navigate to a folder and copy the folder ID from the url bar
- If you are on a headless machine, you might need to download rClone on a device with access to an internet browser
    - In Windows, open `cmd` and navigate to the folder with the `rclone.exe` file
    - Paste the displayed command into `cmd` and paste the response back into the rClone configuration.

Install tmux and create new session for [mounting](https://rclone.org/commands/rclone_mount/)
```shell
apt install tmux
tmux new -s backup

# <name> is the name you chose for the remote in the rclone config
rcloune mount <name>: /path/to/empty/folder --vfs-cache-mode writes
```
Clone this repository and edit `config.py`
```shell
git clone https://github.com/tibue99/linux-backup
```
End mounting
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