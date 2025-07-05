import flask
from source import llama4
from source import definitions
app = flask.Flask(__name__)
key = str(open('secrets.txt', mode='r').readline())
key = key[:len(key)-1]
print(key)
app.route("/")
def test():

    promt = flask.request.args.get('a', '')
    promt = promt.replace("+", " ")
    querry = definitions.config(key, promt)    
    return(llama4.run(querry))

@app.route("/short/<promt>")
def short(promt: str):
    promt = promt.replace("+", " ")
    promt = llama4.run(querry=definitions.config(key, 'my space bar broke what could this sentence be please only respond with the sentence with spaces: ' + promt))
    querry = definitions.config(key, 'please keep your responses short and quick only replying with things the user asked for here is the promt:' + promt)    
    return(llama4.run(querry))

@app.route("/shorter/<promt>")
def shorter(promt: str):
    promt = promt.replace("+", " ")
    promt = llama4.run(querry=definitions.config(key, 'my space bar broke what could this sentence be please only respond with the sentence with spaces: ' + promt))
    querry = definitions.config(key, 'please keep your responses really short only respond with the things you have to and remove every unesesery thing the user dosent need here is the promt:' + promt)    
    return(llama4.run(querry))


#print(base(modell, "some testing please respond short"))
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
