from datetime import datetime, timedelta
import random


# ---------------- GENERATE DEMO HEATMAP ---------------- #

def generate_heatmap_data():

    events = []

    today = datetime.today()

    for i in range(120):

        date = today - timedelta(days=i)

        solved = random.randint(0, 5)

        if solved > 0:

            events.append({
                "title": f"{solved} solved",
                "start": date.strftime("%Y-%m-%d"),
                "end": date.strftime("%Y-%m-%d"),
                "color": "#22c55e"
            })

    return events