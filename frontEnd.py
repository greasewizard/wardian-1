from flask import *
from flask_bootstrap import Bootstrap
from flask_moment import Moment


#initialize the app and addons
app = Flask(__name__)
app.secret_key = 'B@DKSDk213?S$($(213?S===&222'
bootstrap = Bootstrap(app)
moment = Moment(app)


#main function for index
@app.route('/', methods=['GET', 'POST'])
def index():
    #state = getState()
    state = False
    return render_template('index.html', state=state)

#helper function for turning on Lights
@app.route('/lightsOn')
def lightsOn():
    flash('Lights On')
    return redirect(url_for('.index'))

@app.route('/lightsOff')
def lightsOff():
    flash('Lights Off')
    return redirect(url_for('.index'))

@app.route('/foggerOn')
def foggerOn():
    flash('Fogger On')
    return redirect(url_for('.index'))

@app.route('/foggerOff')
def foggerOff():
    flash('Fogger Off')
    return redirect(url_for('.index'))





if __name__ == '__main__':
    app.run(debug=True)
    