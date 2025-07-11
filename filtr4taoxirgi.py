import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Butterworth filtri funksiyasi
def butter_bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs  # Nyquist chastotasi
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, data)

# Fayldan signalni o‘qish
file_path = "test2.txt"  # Bu yerda fayl nomini kerakli qilib o‘zgartirish zarur
data = np.loadtxt(file_path)  # Signalni o‘qish
fs = 10  # Namuna olish chastotasi (Hz) - agar boshqa bo‘lsa, o‘zgartiring
t = np.arange(len(data)) / fs  # Vaqt vektori

# Har bir organ uchun chastota diapazonlari va ranglar
freq_bands = {
    "Yo'g'on ichak": (0.02, 0.05),
    "Oshqozon": (0.03, 0.09),
    "Ingichka ichak": (0.07, 0.15),
    "O'n ikki barmoqli ichak": (0.13, 0.21)
}

colors = ["red", "blue", "green", "purple"]  # Har bir grafik uchun ranglar

# Grafik tayyorlash
plt.figure(figsize=(10, 10))

# 1-qator: Filtrlanmagan signal
plt.subplot(5, 1, 1)
plt.plot(t, data, color="black",  linewidth=1.2)
plt.ylabel("Amplituda")
plt.xlabel("Vaqt (soniya)")
plt.title("Filtrlanmagan signal")
plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1))
plt.grid()

# Keyingi 4 qator: Filtrlangan signallar
for i, ((organ, (low, high)), color) in enumerate(zip(freq_bands.items(), colors)):
    filtered_signal = butter_bandpass_filter(data, low, high, fs)
    plt.subplot(5, 1, i + 2)
    plt.plot(t, filtered_signal, color=color, linewidth=1.2)
    plt.ylabel("Amplituda")
    plt.xlabel("Vaqt (soniya)")
    plt.title(f"{organ}: ({low}-{high} Hz)")
    plt.grid()

plt.suptitle("Gastroenterologik signal filtrlash (Butterworth)")
plt.tight_layout()
plt.show()
