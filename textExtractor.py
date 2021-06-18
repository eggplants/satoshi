import csv, glob, time, re
from itertools import islice

csv_path = glob.glob('data/*dryrun/*.csv')[0]
tweets = []
url = re.compile(
    r'(https?:)?\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)', re.IGNORECASE)

with open(csv_path, encoding='utf_8', errors='replace') as w:
	for row in csv.DictReader(islice(w, 5, None), delimiter=',',
	                          doublequote=True, lineterminator='\r\n',
	                          quotechar='"', skipinitialspace=True):
		try:
			tweets.append(row['Tweet content'])
		except UnicodeDecodeError:
			pass

tweets = [re.sub(r'[@＠][a-zA-Z0-9_]{1,15}\s*', '', t) for t in tweets]
tweets = [re.sub(url, '', t) for t in tweets]
print("\n".join(tweets))
