# AdminTools 

Is a collection of Bash, Perl, Python, PowerShell scripts that can help to ease up some mundane tasks on GNU/Linux or Windows machines.

## Bash

### add_domain
Adds a domain to the `helo_checks` or an email address to the `sender_access` Postfix files.

Usage:
```
  add_domain example@domain.com sender_access
  add_domain *@domain.com sender_access
  add_domain domain.net helo_checks
  add_domain *.local helo_checks
```

### block
Adds an IPv4 address to the Firewalld configuration file, with the `drop` rule, after which it will restart the firewall.

Usage:
```
block 192.168.1.102
```

`Warning:` If you have a system with limited resources and a lot of IPs already on the firewall, then it is better to comment out the `reload` process and make it as a separate cronjob, because otherwise you will have some downtime.

### cleaner
Deletes old backups on the system, and keeps only the last 7 of them (by default, this value can be changed).

Configure it as a cronjob.

### log-stat
Gathers log messages from `/var/log/messages` and the `/etc/passwd` file and writes them to a specified place on the system, given by the admin.
These files can be later parsed by the `ports.py` and `differ.py` scripts.

Configure it as a cronjob as `root` user, othervise it will not have access to the system log files.

### nice-firewall
Changes the Firewalld reload process niceness to `-10` so the process terminates faster. Usefull on systems with low processing power.

Configure it as a cronjob.

### pack
Creates a `tar.bz2` compressed file. The file names structure must be the following `name_backup.ext` so the script can generate the compressed files name correctly. If the file is sql type then the output extension will be `*.sql.tar.bz2` otherwise just `*.tar.bz2`.

Usage:
```
pack exampldb_backup.sql

Output: exampledb_backup_date.sql.tar.bz2
```

### sys-check
Script to check the status of:
+ MariaDB
+ Postfix
+ Amavisd
+ Spamassassin
+ OpenDKIM

This list can either pe shortened or expanded, depending of the admins needs.

## Perl

### backing
Copies the created backups to a designated backup server or NAS. For easier usage it is recomended that you configure an ssh key based login to the backup server.

Configure it as a cronjob.

### bblock
Is used to block multiple IPs on the Firewalld system from a file, in batch format (hence bblock [batch block]). It uses the `block` bash script for this operation.

`Warning:` If you have a system with limited resources and a lot of IPs, then it is better to comment out the `reload` process and make it as a separate cronjob, because otherwise you will have some downtime.    

### dbb
Database backup script. Will create backups of databases specified in the file.

Configure it as a cronjob.

### package
Will compress the backed up databases. It uses the `pack` bash script.

Configure it as a cronjob.


## PowerShell

### Microsoft.PowerShell_profile
This script will run each time you open a powershell console. To do this it has to be placed under `~/WindowsPowerShell`. It will search a remote drive for
files and will display only those that are not in the exclude list (do not forget to open the file and set the necesarry parameters).

### Search-Drive
This script does the same as the `Microsoft.PowerShell_profile` the only difference is that it has to be run manually. It only contains the search function. If placed under `~/WindowsPowerShell`, it can be invoked like this `Search-Drive \path\to\drive \extensions\to\be\excluded\from\search`.

## Python

### IP_filter
Script that processes data from `/var/log/secure` (RHEL) or `/var/log/auth.log` (Debian), by filtering those IPs that have tried to login on the system (by bruteforce); the filtered IPs are compiled into a csv file.

### differ
Script compares two files; kind off a home made "diff" command from the GNU/Linux system, but not that sophisticated.

One is a local copy the other is a copy form the respective server (produced by `log-stat` script).

It is used to see if something has changed over night on the respective server (what type of ports have been opened/closed or did the passwd file change; these are ICs [Indicators of Compromise]). In case something is of, the script will notify you, otherwise it will just tell, that "All lines match" and exit.

 The script recognizes 3 "types of servers":

+ Production (prod)
+ Development (dev)
+ Clients (cli)


### ports
The script is used to process the output from `netstat`, which is run on the remote server, it will create a new file called "new_open_ports", this file will be used by the `differ.py` script, to compare the local copy of the data (about which you know that is solid) with the new data from the remote machine.
