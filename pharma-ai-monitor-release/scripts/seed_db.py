import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / 'database' / 'pharma_ai.db'

SAMPLE_JOBS = [
    ('数据采集任务', 'completed'),
    ('模型训练任务', 'running'),
    ('报告生成任务', 'pending'),
]

def seed_db(force=False):
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not DB_PATH.exists():
        print('数据库不存在，先运行 init_db.py 创建数据库')
        return
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        if force:
            cur.execute('DELETE FROM jobs')
        for name, status in SAMPLE_JOBS:
            cur.execute('INSERT INTO jobs (name, status) VALUES (?, ?)', (name, status))
        conn.commit()
    print(f'已写入示例任务到 {DB_PATH}')

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--force', action='store_true')
    args = p.parse_args()
    seed_db(force=args.force)
