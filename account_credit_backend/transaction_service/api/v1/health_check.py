from flask import (blueprints, current_app, jsonify)
from functools import reduce
import logging

health_check_blueprint = blueprints.Blueprint('health_check', __name__)

ONLINE = "ONLINE"
OFF_LINE = "OFF_LINE"
STATUS = "STATUS"
ERROR = "ERROR"


@health_check_blueprint.route('/health_check', methods=['GET'])
def health_check():
    db_healthy, db_state = get_pg_status()
    health_states = [db_healthy]
    return jsonify({
        "dependencies": {
            "database": db_state
        },
        "healthy": reduce(lambda acc, cur: (acc and cur), health_states)
    })


def get_pg_status() -> (bool, dict):
    try:
        logging.info("Health Checking Postgres")
        current_app.db.session.execute('SELECT 1')

        return True, {
            STATUS: ONLINE,
            ERROR: ""
        }
    except Exception as e:
        logging.error("Could not connect to the database: %", e)

        return False, {
            STATUS: OFF_LINE,
            ERROR: str(e)
        }
