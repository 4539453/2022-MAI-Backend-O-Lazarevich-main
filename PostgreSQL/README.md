# PostgreSQL

## Installation

```bash
$ 
...
Success. You can now start the database server using:

    pg_ctlcluster 13 main start

Ver Cluster Port Status Owner    Data directory              Log file
13  main    5432 down   postgres /var/lib/postgresql/13/main /var/log/postgresql/postgresql-13-main.log
update-alternatives: using /usr/share/postgresql/13/man/man1/postmaster.1.gz to provide /usr/share/man/man1/postmaster.1.gz (postmaster.1.gz) in auto mode
Setting up postgresql (13+225) ...
Setting up sysstat (12.5.2-2) ...

Creating config file /etc/default/sysstat with new version
update-alternatives: using /usr/bin/sar.sysstat to provide /usr/bin/sar (sar) in auto mode
Created symlink /etc/systemd/system/sysstat.service.wants/sysstat-collect.timer → /lib/systemd/system/sysstat-collect.timer.
Created symlink /etc/systemd/system/sysstat.service.wants/sysstat-summary.timer → /lib/systemd/system/sysstat-summary.timer.
Created symlink /etc/systemd/system/multi-user.target.wants/sysstat.service → /lib/systemd/system/sysstat.service.
```
---

[postgresql#Linux downloads (Debian)](https://www.postgresql.org/download/linux/debian)

# Create

---

[postgresql#Schemas](https://www.postgresql.org/docs/current/ddl-schemas.html)

[postgresql#createuser](https://www.postgresql.org/docs/current/app-createuser.html)

[postgresql#dropuser](https://www.postgresql.org/docs/current/app-dropuser.html)

# LSP

---

[github#sql-language-server](https://github.com/joe-re/sql-language-server#usage)
