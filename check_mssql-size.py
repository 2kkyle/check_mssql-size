#!/usr/bin/env python

import pymssql
import argparse
import time

parser = argparse.ArgumentParser(description="Connect to MSSQL and execute 'sp_spaceused'.")
parser.add_argument('-s', '--server, required=True, help="The SQL Server address (e.g., 'localhost' or 'server-name')")
parser.add_argument('-d', '--database', required=True, help="The database name to connect to")
parser.add_argument('-u' , '--user', required=True, help="The username for authentication")
parser.add_argument('-p', '--password', required=True, help="The password for authentication")

#TODO: Add arguments for warn and critical

args = parser.parse_args()

try:
    conn = pymssql.connect(server=args.server, user=args.user, password=args.password, database=args.database)
    cursor = conn.cursor()

    start_time = time.time()

    cursor.execute("EXEC sp_spaceused")

    result = cursor.fetchone()
#    print(result[1])

    elapsed_time = time.time() - start_time

    # Result 1 is the size, we need to clean it up.
    value, unit = result[1].strip().split()
    value = float(value)
    if unit == "MB":
        result_in_gb = value / 1024  # Convert MB to GB
    elif unit == "KB":
        result_in_gb = value / (1024 * 1024)  # Convert KB to GB
    elif unit == "GB":
        result_in_gb = value  # No conversion needed for GB
    else:
        raise ValueError("Unknown unit: {}".format(unit))

#TODO: Compare result_in_gb to warn and critical

    print("OK | ", f"{result_in_gb:.4f}", " | ", f"{elapsed_time:.4f}")

except pymssql.Error as e:
    print(f"Error connecting to SQL Server: {e}")
finally:
    # Close the connection
    if conn:
        conn.close()

#TODO: Return warn or critical status code
/data/monitoring-plugins # cat check_mssql_database
check_mssql_database.py       check_mssql_database_size.py
/data/monitoring-plugins # cat check_mssql_database_size.py
#!/usr/bin/env python

import pymssql
import argparse
import time

parser = argparse.ArgumentParser(description="Connect to MSSQL and execute 'sp_spaceused'.")
parser.add_argument('-H', '--hostname', required=True, help="The SQL Server address (e.g., 'localhost' or 'server-name')")
parser.add_argument('-d', '--database', required=True, help="The database name to connect to")
parser.add_argument('-u' , '--user', required=True, help="The username for authentication")
parser.add_argument('-p', '--password', required=True, help="The password for authentication")


#TODO: Add arguments for warn and critical

args = parser.parse_args()

# Establish connection to the database
try:
    conn = pymssql.connect(server=args.hostname, user=args.user, password=args.password, database=args.database)
    cursor = conn.cursor()

    start_time = time.time()

    cursor.execute("EXEC sp_spaceused")

    result = cursor.fetchone()
#    print(result[1])

    elapsed_time = time.time() - start_time

    # Result 1 is the size, we need to clean it up.
    value, unit = result[1].strip().split()
    value = float(value)
    if unit == "MB":
        result_in_gb = value / 1024  # Convert MB to GB
    elif unit == "KB":
        result_in_gb = value / (1024 * 1024)  # Convert KB to GB
    elif unit == "GB":
        result_in_gb = value  # No conversion needed for GB
    else:
        raise ValueError("Unknown unit: {}".format(unit))

#TODO: Compare result_in_gb to warn and critical

    print("OK | ", f"{result_in_gb:.4f}", " | ", f"{elapsed_time:.4f}")

except pymssql.Error as e:
    print(f"Error connecting to SQL Server: {e}")
finally:
    if conn:
        conn.close()

#TODO: Return warn or critical status code
