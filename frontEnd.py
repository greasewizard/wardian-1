from flask import *
from flask_bootstrap import Bootstrap
from flask_moment import Moment

#import sensors and triggers
import am2302
import fogger
import lights

#initialize the app and addons
app = Flask(__name__)
app.secret_key = 'B@DKSDk213?S$($(213?S===&222'
bootstrap = Bootstrap(app)
moment = Moment(app)


#main function for index
@app.route('/', methods=['GET', 'POST'])
def index():
    humidity, temp = am2302.getReading()
    temp = float(temp) * 9/5.0 + 32
    
    lightState = lights.getState()
    foggerState = fogger.getState()
    return render_template('index.html', humidity=str(humidity)[:4], temp=str(temp)[:4], lightState=lightState, foggerState=foggerState)

#helper function for turning on Lights
@app.route('/lightsOn')
def lightsOn():
    flash('Lights On')
    lights.on()
    return redirect(url_for('.index'))

@app.route('/lightsOff')
def lightsOff():
    flash('Lights Off')
    lights.off()
    return redirect(url_for('.index'))

@app.route('/foggerOn')
def foggerOn():
    flash('Fogger On')
    fogger.on()
    return redirect(url_for('.index'))

@app.route('/foggerOff')
def foggerOff():
    flash('Fogger Off')
    fogger.off()
    return redirect(url_for('.index'))



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
        
