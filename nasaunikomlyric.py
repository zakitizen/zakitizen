import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)  # Delay before the lyric starts
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("KITA BANGGA, BERSAMA UNIKOM", 0.15),
        ("SELALU BERKARYA BERSAMA UNIKOM", 0.11),
        ("MELANGKAH MAJU BERSAMA UNIKOM", 0.11),
        ("UNIVERSITAS KOMPUTER, PASTI UNIKOM", 0.15),
        ("SUDAH WAKTUNYA", 0.13),
        ("KUBEKALI", 0.12),
        ("MENGHADAPI TANTANGAN", 0.10),
        ("DUNIA INI", 0.13),
        ("KUSIAPKAN", 0.12),
        ("AMUNISI", 0.13),
        ("SEMUA SERBA", 0.12),
        ("KOMPUTERISASI", 0.11),
        ("PERKEMBANGAN DUNIA, BEGITU CEPAT", 0.08),
        ("JANGAN SAMPAI KITA TERLAMBAT", 0.05),
        ("MELANGKAH BERSAMA UNIKOM", 0.08),
        ("MELANGKAH BERSAMA UNIKOM", 0.08)
    ]

    threads = []
    for lyric, speed in lyrics:
        t = Thread(target=sing_lyric, args=(lyric, 0, speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
