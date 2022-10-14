from flask import Flask, request, make_response, render_template
from flask import send_from_directory
from markupsafe import escape

app = Flask(__name__)

def addCSP(response):
    csp = "default-src 'none'; script-src 'self'; connect-src 'self'; img-src 'self'; "
    csp += "style-src 'self'; base-uri 'self'; form-action 'self'"
    print(csp)
    responseWithCSP = make_response(response)
    responseWithCSP.headers['Content-Security-Policy'] = csp
    return responseWithCSP

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
  <script src="/static/controller.js"></script>
</html>
"""

main_page_markup = """
<form action="" method="GET">
  <input id="query" name="query" value="Enter query here...">
  <input id="button" type="submit" value="Search">
</form>
"""

app = Flask(__name__)

@app.route("/")
def search():
    if not request.args.get('query'):
        # Show main search page
        return addCSP(page_header + main_page_markup + page_footer)
    else:
        query = escape(request.args.get('query'))
        # Our search engine broke, we found no results :-(
        message = f"Sorry, no results were found for <b> {query} </b>."
        message += " <a href='?'>Try again</a>."
        # Display the results page
        return addCSP(page_header + message + page_footer)

@app.route('/favicon.ico')
def send_icon():
    return send_from_directory(directory='static', path='favicon.ico')