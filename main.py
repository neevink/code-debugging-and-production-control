import math
import time

from prometheus_client import start_http_server, Gauge


if __name__ == '__main__':
    start_http_server(8000)
    temperature = Gauge('air_temperature', 'Air temperature', labelnames=['place'])
    x = 0

    while True:
        temperature.labels(place='garden').set(
            10 * math.cos(x)
        )

        x += 0.1
        time.sleep(3)
