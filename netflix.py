import pandas as pd

dF = pd.read_csv('dados.csv')


print(dF.shape)

print(dF.head(10))
#Profile Name,Start Time,Duration,Attributes,Title,Supplemental Video Type,Device Type,Bookmark,Latest Bookmark,Country											


dF = dF .drop['Profile Name','Attributes','Supplemental','Bookmark','Latest','Bookmark','Country']
print(dF.head(10))

dF['star time'] = pd.to_datetime(dF['start time'], utc=True)
print(dF.dtypes)

