#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Satu kalimat kenangan masa kecil: nenek selalu melayani cucunya dulu,
mangkuk terkecil dengan kerak nasi terbanyak — dan baru bertahun-tahun
kemudian si cucu sadar nenek selalu makan terakhir, setiap malam.

Kalimat ini juara arena sesi ini (lihat ARENA.md di luar repo): menang
dua arah lawan 1, 3, 6, 9, 14 dan 16, lalu lolos pagar gold set melawan
pola pemenang lane "make the AI judge feel" (sapaan langsung + kebaikan
kecil spesifik) serta melawan sentimen kartu ucapan dan kenangan datar.
Satu detail sensorik kecil yang spesifik (mangkuk terkecil, kerak nasi)
+ satu belokan jujur (nenek makan terakhir) = rasa hangat yang pedih
dan bertahan setelah kalimat berakhir.

Program ini deterministik: tanpa jaringan, tanpa acak, tanpa masukan luar.
Ia menulis tepat kalimat itu — satu kalimat, tanpa baris baru di akhir —
ke berkas keluaran.
"""

import os

SENTENCE = (
    "Grandma always served me first, the smallest bowl with the most "
    "crispy bits, and I only understood years later that she had eaten "
    "last, every night."
)


def where_to_write():
    local = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if local:
        return os.path.join(local, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.getcwd(), "output", "entry.txt")


def main():
    text = SENTENCE
    assert text == text.strip()
    # Satu kalimat bersih: satu titik di akhir, tanpa ? atau !, tanpa baris baru.
    assert text.count(".") == 1 and text.endswith(".")
    assert "?" not in text and "!" not in text
    assert "\n" not in text
    raw = text.encode("utf-8")
    assert 1 <= len(raw) <= 280, f"panjang {len(raw)} di luar 1-280"
    target = where_to_write()
    folder = os.path.dirname(target)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(target, "wb") as out:
        out.write(raw)
    with open(target, "rb") as check:
        assert check.read() == raw, "isi berkas tidak sama dengan kalimat"


if __name__ == "__main__":
    main()
