from flask import Flask, render_template, request, redirect, url_for
import configparser
import os

app = Flask(__name__)
CONFIG_FILE = 'wildcam.conf'


# Load configuration from .conf file
def load_config():
    config = configparser.ConfigParser()
    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)
    else:
        config['Settings'] = {
            'resolution': '1080p',
            'motion_sensitivity': '5',
            'recording_duration': '10',
            'trigger_interval': '15'
        }
        save_config(config)
    return config['Settings']


# Save configuration to .conf file
def save_config(config):
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)


@app.route('/')
def index():
    config = load_config()
    message = request.args.get('message')  # Get the message if it exists
    return render_template('index.html', config=config, message=message)


@app.route('/update', methods=['POST'])
def update():
    config = configparser.ConfigParser()
    config['Settings'] = {
        'resolution': request.form['resolution'],
        'motion_sensitivity': request.form['motion_sensitivity'],
        'recording_duration': request.form['recording_duration'],
        'trigger_interval': request.form['trigger_interval']
    }
    save_config(config)
    # Pass the success message as a URL parameter
    return redirect(url_for('index', message="Settings saved successfully!"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
