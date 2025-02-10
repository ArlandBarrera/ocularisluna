# modules/moon_phases.py
from skyfield.api import load
from skyfield.almanac import find_discrete, moon_phases
import matplotlib.pyplot as plt
import io
import base64


def get_moon_phases(start_date, end_date):
    """
    Calcula las fases de la luna entre star y end (date).
    Retorna lista de fases lunares e immagen de la grafica.
    """
    eph = load("de421.bsp")
    ts = load.timescale()

    # Convert string to Skyfield time objects
    start = ts.utc(*map(int, start_date.split("-")))
    end = ts.utc(*map(int, end_date.split("-")))

    # Calculate phases
    phase_times, phases = find_discrete(start, end, moon_phases(eph))
    phase_labels = ["Luna Nueva", "Cuarto Creciente", "Luna Llena", "Cuarto Menguante"]

    # Prepare result data
    results = [
        {"date": t.utc_iso(), "phase": phase_labels[p]}
        for t, p in zip(phase_times, phases)
    ]

    # Generate plot
    plt.figure(figsize=(10, 5))
    plt.plot(phase_times.utc_datetime(), phases, "o", label="Fases de la Luna")
    plt.yticks(range(4), phase_labels)
    plt.xticks(rotation=45)
    plt.xlabel("Fecha")
    plt.ylabel("Fases")
    plt.title("Fases de la Luna")
    plt.grid()
    plt.tight_layout()

    # Convert plot to base64
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return results, f"data:image/png;base64,{plot_url}"
