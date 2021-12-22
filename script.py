import subprocess, json

file = open('input.json')
data = json.load(file)

dryRun = data["dryRun"]
bucket = data["bucket"]
items = data["items"]

for item in items:
    if dryRun:
        subprocess.call(f' python s3-pit-restore -b {bucket} -B {bucket} -p {item["prefix"]} -t "{item["timestamp"]}" -v --dry-run', shell=True)
    else:
        subprocess.call(f' python s3-pit-restore -b {bucket} -B {bucket} -p {item["prefix"]} -t "{item["timestamp"]}" -v', shell=True)

