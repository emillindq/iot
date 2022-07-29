import flask
import matplotlib.pyplot as plt
from io import BytesIO
from werkzeug.wsgi import FileWrapper

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    return """<p>pelle!</p>
              <img src="graph.png">"""

@app.route("/graph.png")
def graph():
    plt.plot([1,2,3])
    #plt.show()
    bio = BytesIO()
    plt.savefig(bio, format="png")

    #    bio.seek(0)
    #    print(bio.read())                  FIRST print
    bio.seek(0)
    w = FileWrapper(bio)
    return flask.Response(w, mimetype="image/png", direct_passthrough=True)
