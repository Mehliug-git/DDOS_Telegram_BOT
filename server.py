from flask import Flask, render_template
import subprocess


app = Flask(__name__)

bot_process = subprocess.Popen(['python3' , 'bot.py'])



@app.route("/")
def page_web_de_mort():
    bot_process
    return "<html><body><img src='https://i.giphy.com/KmHueA88mFABT9GkkR.gif'></body></html>"
    #page_web_de_mort()
    
@app.route("/kill")
def killswitch():
    p = subprocess.Popen(f'refresh', stdout=subprocess.PIPE, shell=True)
    output, error = p.communicate()
    bot_process
    return "<html><body><img src='https://i.giphy.com/6jTD6KqVNADI746GOC.gif'></body></html>"
    #page_web_de_mort()    
    

app.run()
  
  
  
"""

if __name__ == "__main__":
    app.run()

"""