from flask import Flask, render_template, request, redirect

app = Flask(__name__)

batteries = []

@app.route("/")
def home():
    return render_template("index.html", batteries=batteries)

@app.route("/add", methods=["POST"])
def add_battery():
    battery_type = request.form["battery_type"]
    quantity = request.form["quantity"]
    location = request.form["location"]

    batteries.append({
        "type": battery_type,
        "quantity": quantity,
        "location": location,
        "status": "Pending Collection"
    })

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)