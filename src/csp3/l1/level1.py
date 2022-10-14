from flask import Flask
from flask import request, make_response, render_template
from flask import send_from_directory
from markupsafe import escape

import base64
import os

page_header = """
<!doctype html>
<html>
  <head>
    <link rel="stylesheet" href="static/game-frame-styles.css" />
  </head>
 
  <body id="level1">
    <img src="static/logos/level1.png">
      <div>
"""

page_footer = """
    </div>
  </body>
  <script src="/static/controller.js" nonce="%s"></script>
</html>
"""

main_page_markup = """
<form action="" method="GET">
  <input id="query" name="query" value="Enter query here...">
  <input id="button" type="submit" value="Search">
</form>
"""

# reference: https://csp.withgoogle.com/docs/faq.html
def GetCspNonce():
   """Returns a random nonce."""
   NONCE_LENGTH = 16
   return base64.b64encode(os.urandom(NONCE_LENGTH)).decode()

def addCSP(response, n1):
    cspheader = "script-src 'self' "
    cspheader += "'nonce-%s' ;" % n1
    responseWithCSP = make_response(response)
    responseWithCSP.headers['Content-Security-Policy'] = cspheader
    return responseWithCSP

app = Flask(__name__)

@app.route("/")
def search():
    n1 = GetCspNonce()
    if not request.args.get('query'):
        # Show main search page
        return addCSP(page_header + main_page_markup + page_footer%n1, n1)
    else:
        query = escape(request.args.get('query'))
        # Our search engine broke, we found no results :-(
        message = f"Sorry, no results were found for <b> {query} </b>."
        message += " <a href='?'>Try again</a>."
        # Display the results page
        return addCSP(page_header + message + page_footer%n1, n1)

@app.route('/favicon.ico')
def send_icon():
    return send_from_directory(directory='static', path='favicon.ico')