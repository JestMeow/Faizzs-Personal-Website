from flask import (
    Blueprint, render_template
)

from .db import get_connection
from psycopg2.extras import RealDictCursor


home = Blueprint(
    'home',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@home.route('/')
def create_home():
    conn = get_connection()

    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute('SELECT * FROM soundcloud_preview_data')
    soundcloud_preview_data = cur.fetchall()

    cur.execute('SELECT * FROM projects_metadata')
    projects_metadata = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        'index.html',
        soundcloud_preview_data=soundcloud_preview_data,
        projects_metadata=projects_metadata
    )
