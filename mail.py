import requests
import csv

def send_simple_message(x,y):
	return requests.post(
		"https://api.eu.mailgun.net/v3/MG.YOURDOMAIN.COM/messages",
		auth=("api", "YOUR_API_KEY"),
		files=[("attachment", ("{id}.txt".format(id=y), open("files/{id}.txt".format(id=y),"rb").read())),],
		data={"from": "Excited User <mailgun@YOURDOMAIN.com>",
			"to": [x, "TEST@YOURDOMAIN.com"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!",})

with open('test.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            x=row[0]
            y=row[2]
            send_simple_message(x,y)
            line_count += 1
    print(f'Processed {line_count} lines.')
