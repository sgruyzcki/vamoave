import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Lista de activos argentinos (Acciones y CEDEARs)
tickers = ["GGAL.BA", "YPFD.BA", "PAMP.BA", "AAPL.BA"] # Apple es un CEDEAR aquí

# Descarga masiva de datos
data = yf.download(tickers, period="6mo", interval="1d")['Close']

# Limpieza rápida: Eliminar valores nulos (días no laborables localmente)
data = data.dropna()

print("Últimas cotizaciones en ARS:")
print(data.tail())

# Visualización de rendimiento normalizado (Base 100)
(data / data.iloc[0] * 100).plot(figsize=(12, 6), title="Rendimiento Relativo Merval")
plt.ylabel("Base 100")
plt.grid(True)
plt.show()
