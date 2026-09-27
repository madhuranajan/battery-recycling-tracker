from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

records = []


@app.route("/")
def home():
    total_batteries = sum(record["quantity"] for record in records)
    total_records = len(records)
    waste_diverted = round(total_batteries * 0.05, 2)

    return render_template(
        "index.html",
        total_batteries=total_batteries,
        total_records=total_records,
        waste_diverted=waste_diverted,
        records=records
    )


@app.route("/add", methods=["POST"])
def add_record():

    battery_type = request.form["battery_type"]
    quantity = int(request.form["quantity"])
    condition = request.form["condition"]
    location = request.form["location"]

    records.append({
        "battery_type": battery_type,
        "quantity": quantity,
        "condition": condition,
        "location": location
    })

    return redirect("/")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)