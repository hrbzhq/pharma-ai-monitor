import os
import sys
import pytest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app import create_standalone_app


@pytest.fixture
def client():
    app = create_standalone_app()
    app.testing = True
    with app.test_client() as c:
        yield c


def test_index(client):
    r = client.get('/')
    assert r.status_code in (200, 302)


def test_stats(client):
    r = client.get('/api/stats')
    assert r.status_code == 200
    j = r.get_json()
    assert j.get('success') is True


def test_db_jobs(client):
    # ensure DB is present and seeded
    from scripts.init_db import init_db
    from scripts.seed_db import seed_db
    init_db()
    seed_db(force=True)
    r = client.get('/api/db/jobs')
    assert r.status_code == 200
    j = r.get_json()
    assert j.get('success') is True
    assert isinstance(j.get('data'), list)
