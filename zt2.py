import mig_util as mu

# conn_dooodb = mu.get_mysql_conn('dooodb')
conn_dadb = mu.get_mysql_conn('dadb')

# read from source db
with conn_dadb:
    cur = conn_dadb.cursor()

    cur.execute(sql)
