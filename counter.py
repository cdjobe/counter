from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.count_key = 0 


@app.route('/')
def index_count():

    if 'app.count_key' in session:
        print('key exists')
    
    else:
        print("key 'key_name' does NOT exist")
    print(session)
    app.count_key = app.count_key + 1
    print(app.count_key)
    return render_template("index.html", count=app.count_key)

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)
