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

    cur.execute('SELECT * FROM soundcloud_widget_metadata')
    soundcloud_widget_metadata = cur.fetchall()
    soundcloud_widget_metadata.sort(key=lambda item: item['priority'], reverse=True)

    

    cur.execute('SELECT * FROM projects_metadata')
    projects_metadata = cur.fetchall()
    projects_metadata.sort(key=lambda item: item['priority'], reverse=True)

    cur.close()
    conn.close()

    return render_template(
        'index.html',
        soundcloud_widget_metadata=soundcloud_widget_metadata,
        projects_metadata=projects_metadata
    )
