import psutil   #to get cpus resource utilization
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    message = None
    if cpu_percent>80 or memory_percent>80:
        message = "High CPU or High Memory Utilization Detected! Please scale up"
    return render_template("index.html",cpu_metric=cpu_percent,mem_metric=memory_percent,message=message)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

