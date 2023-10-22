import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Menampilkan beberapa baris pertama data
print(df.head())

# Menampilkan informasi tentang DataFrame
print(df.info())

# Analisis Tren Penjualan Berdasarkan Bulan
df['Tanggal'] = pd.to_datetime(df['Tanggal'])  # Mengonversi kolom Tanggal ke tipe data datetime
df['Bulan'] = df['Tanggal'].dt.to_period('M')  # Menambahkan kolom Bulan yang berisi periode bulan
monthly_sales = df.groupby('Bulan')['Jumlah'].sum()
print("Analisis Tren Penjualan Berdasarkan Bulan:")
print(monthly_sales)

# Visualisasi Tren Penjualan Bulanan
monthly_sales.plot(kind='line', marker='o')
plt.title('Tren Penjualan Bulanan')
plt.xlabel('Bulan')
plt.ylabel('Total Penjualan')
plt.xticks(rotation=45)
plt.show()

# Produk Terlaris
top_products = df.groupby('Produk')['Jumlah'].sum().sort_values(ascending=False)
print("Produk Terlaris:")
print(top_products)

# Analisis Harga dan Jumlah Terjual
plt.scatter(df['Harga'], df['Jumlah'], alpha=0.5)
plt.title('Hubungan Harga dan Jumlah Terjual')
plt.xlabel('Harga')
plt.ylabel('Jumlah Terjual')
plt.show()

# Analisis Wilayah Penjualan
region_sales = df.groupby('Wilayah')['Jumlah'].sum()
print("Analisis Wilayah Penjualan:")
print(region_sales)

# Visualisasi Penjualan per Wilayah
region_sales.plot(kind='bar')
plt.title('Penjualan per Wilayah')
plt.xlabel('Wilayah')
plt.ylabel('Total Penjualan')
plt.xticks(rotation=0)
plt.show()

# Analisis Churn Pelanggan (Contoh Dummy)
df['Churn'] = df['Tanggal'].apply(lambda x: '2023-01-01' in str(x))
print(df)

# Simpan DataFrame yang telah diperbarui ke file CSV
df.to_csv('hasil_analisis_penjualan.csv', index=False)
