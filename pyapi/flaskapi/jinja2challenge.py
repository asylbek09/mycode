#!/usr/bin/python3
from flask import Flask, render_template
from flask import session
from flask import redirect
from flask import url_for
from flask import escape
from flask import request

app = Flask(__name__)

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

@app.route('/hosts')
def index():
    return render_template('jinja2challenge.html', pages=groups) # or use hosts.j2 instead of jinja2challenge.html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)