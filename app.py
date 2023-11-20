from flask import Flask
app=Flask("__name__")


@app.route("/test")
def test():
    return "<h1> This is my V.E program </h1>"

if __name__=='__main__':
    app.run()
    