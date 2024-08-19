from flask import Flask, render_template_string
import snowflake.connector

app = Flask(__name__)

# Make the Snowflake connection
def connect() -> snowflake.connector.SnowflakeConnection:
    creds = {
            'account': "SZ21568",
            'user': 'linda',
            'password': "Galdalete1",
            'warehouse': "DATA_API",
            'database': "SYSTEM_SERVICES",
            'schema': "ELASTICSEARCH",
            'host' : "sz21568.us-east-2.aws.snowflakecomputing.com",
            'client_session_keep_alive': True
        }
    return snowflake.connector.connect(**creds)


def print_data(level):
    query = f'SELECT MESSAGE FROM APPLICATION_LOGS WHERE "Log Level" = \'{level}\''
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(query)
        result = cur.fetchall()
        return [row[0] for row in result]
    finally:
        cur.close()
        conn.close()

@app.route("/")
def home():
    info_logs = print_data('INFO')
    warning_logs = print_data('WARNING')
    error_logs = print_data('ERROR')

    html_template = '''
    <h1>Application Logs</h1>
    <h2>INFO Logs</h2>
    <ul>
        {% for log in info_logs %}
        <li>{{ log }}</li>
        {% endfor %}
    </ul>
    <h2>WARNING Logs</h2>
    <ul>
        {% for log in warning_logs %}
        <li>{{ log }}</li>
        {% endfor %}
    </ul>
    <h2>ERROR Logs</h2>
    <ul>
        {% for log in error_logs %}
        <li>{{ log }}</li>
        {% endfor %}
    </ul>
    '''

    return render_template_string(html_template, info_logs=info_logs, warning_logs=warning_logs, error_logs=error_logs)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')