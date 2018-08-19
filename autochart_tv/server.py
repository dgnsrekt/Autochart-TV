from .chart import Chart
from .config import Configuration
from .model import AutoChartModel
from flask import Flask, render_template, url_for, request, redirect
import logging
from pathlib import Path
import random
import string
import structlog
import json


class ChartServer:
    chart_config = Configuration()
    if chart_config.get_server_setting('debug') == False:
        logger = logging.getLogger('werkzeug')
        logger.setLevel(logging.ERROR)
    else:
        logger = structlog.get_logger()

    @classmethod
    def get_server(cls):

        app = Flask(__name__)

        @app.route('/')
        def home():
            tickers = AutoChartModel.query()
            settings = ChartServer.chart_config.get_settings()
            ChartServer.logger.info(f'current settings: {str(settings)}')
            ChartServer.logger.info(f'open charts: {str(tickers)}')

            charts = [Chart(symbol=ticker, settings=settings) for ticker in reversed(tickers)]
            con_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)).lower()
            ChartServer.logger.info(f'CID: {con_id}')

            return render_template('index.html',
                                    title='autochart-tv',
                                    charts=charts,
                                    container_id=f'tradingview_{con_id}')

        return app
