import pandas as pd
from hdfs import InsecureClient

#Krok 1 - utworzenie DataFrame, przesłanie danych do pliku csv
data = {
    'Imię':['Anna','Jan','Klara'],
    'Wiek':[20,34,50],
    'Miasto':['Warszawa','Lublin','Kraków']
}

df = pd.DataFrame(data)
print(df.head())

df.to_csv('dane.csv',index=False)

#Krok 2 - przesyłanie i weryfikacja pliku w HDFS

hdf_url = 'http://namenode:50070'

#inicjalizacja klienta HDFS
client = InsecureClient(hdf_url,user='hadoop_user')

#ścieżka docelowa
hdfs_path = 'user/hadoop/dane.csv'

#wysłanie pliku do HDFS

with open('dane.csv','rb') as local_file:
    client.write(hdfs_path, local_file, overwrite=True)
    
#wpisz w wierszu poleceń HADOOP
# hdfs dfs -ls/user/hadoop/dane.csv

print(f"plik {hdfs_path} został przesłany do HDFS")
