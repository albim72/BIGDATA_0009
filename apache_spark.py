from pyspark.sql import SparkSession

# Tworzenie sesji Spark
spark = SparkSession.builder \
    .appName("Batch Processing Example") \
    .getOrCreate()

# Wczytywanie pliku tekstowego (zakładamy, że plik jest zapisany w HDFS lub lokalnym systemie plików)
data = spark.read.text("path_to_your_file.txt")

# Konwersja danych z pliku tekstowego na liczby
numbers = data.rdd.map(lambda row: float(row[0]))

# Obliczanie sumy i liczby elementów
sum_and_count = numbers.aggregate(
    (0, 0),  # Inicjalizacja (suma, liczba elementów)
    lambda acc, value: (acc[0] + value, acc[1] + 1),  # Funkcja dla każdego elementu (suma, licznik)
    lambda acc1, acc2: (acc1[0] + acc2[0], acc1[1] + acc2[1])  # Redukcja (łączenie wyników)
)

# Obliczanie średniej
total_sum, count = sum_and_count
average = total_sum / count if count != 0 else float('nan')

print(f"Średnia wartość: {average}")

# Zakończenie sesji Spark
spark.stop()

