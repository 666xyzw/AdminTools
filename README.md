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
Copies the created backups to a designated backup server or NAS.
