import duckdb

sql = f"""
    select 'gajraj'
"""

duckdb.sql(sql).show()