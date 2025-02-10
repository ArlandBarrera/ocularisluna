from flask import Flask, request, jsonify, render_template
from modules.fases_luna import get_moon_phases

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_moon_phases", methods=["GET"])
def fetch_moon_phases():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    if not start_date or not end_date:
        return jsonify({"error": "Falta fecha de inicio o fin."})

    try:
        results, plot_url = get_moon_phases(start_date, end_date)
        return jsonify({"phases": results, "plot": plot_url})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
