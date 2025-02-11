import requests
from collections import Counter
import numpy as np

arguments = [
    "/predict?age=0.070769&sex=0.050680&bmi=0.012117&blood_pressure=0.056301&s1=0.034206&s2=0.049416&s3=-0.039719&s4=0.034309&s5=0.027364&s6=-0.001078",
    "/predict?age=-0.009147&sex=0.050680&bmi=-0.018062&blood_pressure=-0.033213&s1=-0.020832&s2=0.012152&s3=-0.072854&s4=0.071210&s5=0.000272&s6=0.019633",
    "/predict?age=0.005383&sex=-0.044642&bmi=0.049840&blood_pressure=0.097615&s1=-0.015328&s2=-0.016345&s3=-0.006584&s4=-0.002592&s5=0.017036&s6=-0.013504",
    "/predict?age=-0.027310&sex=-0.044642&bmi=-0.035307&blood_pressure=-0.029770&s1=-0.056607&s2=-0.058620&s3=0.030232&s4=-0.039493&s5=-0.049872&s6=-0.129483",
    "/predict?age=-0.023677&sex=-0.044642&bmi=-0.065486&blood_pressure=-0.081413&s1=-0.038720&s2=-0.053610&s3=0.059685&s4=-0.076395&s5=-0.037129&s6=-0.042499",
    "/predict?age=-0.096328&sex=-0.044642&bmi=-0.076264&blood_pressure=-0.043542&s1=-0.045599&s2=-0.034821&s3=0.008142&s4=-0.039493&s5=-0.059471&s6=-0.083920",
    "/predict?age=0.005383&sex=0.050680&bmi=0.030440&blood_pressure=0.083844&s1=-0.037344&s2=-0.047347&s3=0.015505&s4=-0.039493&s5=0.008641&s6=0.015491",
    "/predict?age=0.030811&sex=-0.044642&bmi=-0.020218&blood_pressure=-0.005670&s1=-0.004321&s2=-0.029497&s3=0.078093&s4=-0.039493&s5=-0.010903&s6=-0.001078",
    "/predict?age=-0.012780&sex=-0.044642&bmi=-0.023451&blood_pressure=-0.040099&s1=-0.016704&s2=0.004636&s3=-0.017629&s4=-0.002592&s5=-0.038460&s6=-0.038357",
    "/predict?age=-0.092695&sex=-0.044642&bmi=0.028284&blood_pressure=-0.015999&s1=0.036958&s2=0.024991&s3=0.056003&s4=-0.039493&s5=-0.005142&s6=-0.001078"
]


def get_predictions(urls):
    predictions = []
    
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if 'prediction' in data:
                predictions.append(data['prediction'])
        except requests.RequestException as e:
            print(f"Error with request to {url}: {e}")
    return predictions


weights = np.array([1.0, 1.0, 1.0, 1.0])
balances = np.array([1000.0, 1000.0, 1000.0, 1000.0])


model_urls = [
    "https://8e9c-92-169-192-254.ngrok-free.app",
    "https://54bb-2a04-cec2-a-5ee3-9cdf-d03e-8cb9-1039.ngrok-free.app",
    "https://3312-2a01-e34-ec54-b5f0-1ed-2339-12c4-f846.ngrok-free.app",
    "https://8245-2a01-cb00-1401-e900-3552-1c20-acea-899d.ngrok-free.app"
]

for arg in arguments:
    urls = [url + arg for url in model_urls]
    predictions = get_predictions(urls)

    if predictions:
        predictions = np.array(predictions)

        mean_prediction = np.average(predictions, weights=weights)
        print(f"Predictions: {predictions}")
        print(f"Weighted Mean Prediction: {mean_prediction}")

        errors = np.abs(predictions - mean_prediction)
        new_weights = np.exp(-errors)

        alpha = 0.2
        weights = (1 - alpha) * weights + alpha * new_weights
        weights /= weights.sum()

        total_money = balances.sum()
        new_balances = total_money * weights 

        print(f"Updated model weights: {weights}")
        print(f"Updated balances: {new_balances}")

        balances = new_balances 
    else:
        print("No valid predictions received.")
