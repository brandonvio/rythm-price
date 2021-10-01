import os
import glob
import requests
import gzip
import shutil

# Construct the years, weeks and symbol lists required for the scraper.
years = [2017, 2018, 2019, 2020]
weeks = list(range(1, 53))
symbols = []
symbols.append("EURUSD", "EURJPY", "USDCHF", "USDCAD")

# # Scrape time
directory = "/datadrive/data/fx-files/"

for symbol in symbols:
    for year in years:
        for week in weeks:
            url = f"https://tickdata.fxcorporate.com/{symbol}/{year}/{week}.csv.gz"
            print(url)
            r = requests.get(url, stream=True)
            with open(f"{directory}{symbol}_{year}_w{week}.csv.gz", 'wb') as file:
                for chunk in r.iter_content(chunk_size=1024):
                    file.write(chunk)

# Check all the files for each currency pair was downloaded (should be 104 for each)
total = 0
for symbol in symbols:
    count = 0
    for file in os.listdir(directory):
        if file[:6] == symbol:
            count += 1
    total += count
    print(f"{symbol} files downloaded = {count} ")
print(f"\nTotal files downloaded = {total}")

gz_files = glob.glob(f"{directory}/*.gz")
for gz_file in gz_files:
    print(gz_file)
    try:
        with gzip.open(gz_file, 'rb') as f_in:
            csv_file = gz_file.replace(".gz", "")
            with open(csv_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        os.remove(gz_file)
    except Exception as e:
        print(f"There was an exception processing {gz_file}.")
        print(e)

print(gz_files)
