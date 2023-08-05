
import pandas as pd
import uniplot
import argparse
import requests
import os
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('--data-url', type=str, default=None, help='url to data')
parser.add_argument('--sleep', type=int, default=10, help='sleep time between requests (seconds)')
parser.add_argument('--tail', type=int, default=None, help='data tail')
parser.add_argument('--width', type=int, default=60, help='plot width')
args = parser.parse_args()


df = pd.DataFrame(columns=['successes', 'failures', 'success_inc', 'failures_inc'])


def get_data() -> dict:
    while True:
        try:
            response = requests.get(args.data_url)
            return response.json()
        except:
            print('connection error')
            sleep(1)


while True:
    data: dict = get_data()
    if not df.empty:
        last = df.iloc[-1]
    else:
        last = {'successes': data['successes'], 'failures': data['failures']}

    data['success_inc'] = data['successes'] - last['successes']
    data['failures_inc'] = data['failures'] - last['failures']
    new_row = pd.Series(data)
    df = pd.concat([df, new_row.to_frame().T], ignore_index=True)

    if args.tail:
        df = df.tail(args.tail)
        os.system('clear')
        print(df)
    else:
        df = df.tail(args.width)
        successes = df['success_inc'].tail(args.width).tolist()
        faliures = df['failures_inc'].tail(args.width).tolist()
        width = args.width
        uniplot.plot([successes, faliures], height=10, lines=True, width=width)

    sleep(args.sleep)
