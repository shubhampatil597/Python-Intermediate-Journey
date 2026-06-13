from abc import ABC
from abc import abstractmethod


class BackupSystem(ABC):

    @abstractmethod
    def backup(self):

        pass


class DatabaseBackup(BackupSystem):

    def backup(self):

        print("Database Backup Completed")


class FileBackup(BackupSystem):

    def backup(self):

        print("File Backup Completed")


class VMBackup(BackupSystem):

    def backup(self):

        print("Virtual Machine Backup Completed")


backups = [

    DatabaseBackup(),

    FileBackup(),

    VMBackup()

]


for backup in backups:

    backup.backup()