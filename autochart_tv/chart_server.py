from .chart import Chart
from .model import ChartModel, db
from flask import Flask, render_template, url_for, request, redirect
from pathlib import Path
import json


class ChartServer:

    @classmethod
    def get_server(cls):
        app = Flask(__name__)

        @app.route('/')
        def home():
            # filename = Path(app.static_folder) / 'json' / 'tickers.json'
            # with open(filename, 'r') as file:
                # tickers = json.loads(file.read())

            tickers = ChartModel.query()
            print(tickers)

            charts = [Chart(symbol=ticker) for ticker in reversed(tickers)]

            return render_template('index.html', title='autochart-tv', charts=charts, container_id='tradingview_f53c8')

        return app


if __name__ == '__main__':
    app = chart_server.get_server()
    app.run(debug=True)
