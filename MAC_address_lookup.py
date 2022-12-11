import requests

with open(''Desktop/your_file.txt here'', 'r') as f:
    with open(''Desktop/output.txt here'', 'wt') as wf:
        for eachline in f:
            eachline = eachline.rstrip()

            url = ('https://'website name'' + eachline + '?apiKey='your API Key')

            r = requests.get(url)
            print(r.text)
            print(r.text,file=wf)

print('all done')


#print(r.text)
