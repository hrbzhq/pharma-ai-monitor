import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / 'database' / 'pharma_ai.db'
SCHEMA = Path(__file__).resolve().parents[1] / 'database' / 'schema.sql'

def init_db(force=False):
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    if DB_PATH.exists() and not force:
        print(f"数据库已存在：{DB_PATH}")
        return
    with sqlite3.connect(DB_PATH) as conn:
        sql = SCHEMA.read_text(encoding='utf-8')
        conn.executescript(sql)
    print(f"已创建数据库：{DB_PATH}")

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--force', action='store_true', help='覆盖已存在的数据库')
    args = p.parse_args()
    init_db(force=args.force)
