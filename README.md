# check_mssql-size
A Monitoring Plugin for Checking MSSQL Database Size

```markdown
./check_mssql_database_size.py -h
usage: check_mssql_database_size.py [-h] -s SERVER -d DATABASE -u USER -p PASSWORD

Connect to MSSQL and execute 'sp_spaceused'.

options:
  -h, --help            show this help message and exit
  -s SERVER, --server SERVER
                        The SQL Server address (e.g., 'localhost' or 'server-name')
  -d DATABASE, --database DATABASE
                        The database name to connect to
  -u USER, --user USER  The username for authentication
  -p PASSWORD, --password PASSWORD
                        The password for authentication
```
That is all thank you goodbye.
