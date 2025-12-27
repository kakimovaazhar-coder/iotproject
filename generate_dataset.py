import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)
start_time = datetime.now() - timedelta(hours=24)
timestamps = [start_time + timedelta(minutes=15 * i) for i in range(96)]

temperatures = np.random.normal(25, 5, 96)
humidities = np.random.normal(60, 10, 96)

data = pd.DataFrame({
    'timestamp': timestamps,
    'temperature': temperatures,
    'humidity': humidities
})

data.to_csv('iot_sensor_data.csv', index=False)
print("Dataset generated and saved to 'iot_sensor_data.csv'")