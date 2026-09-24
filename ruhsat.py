#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kalorifer Borusunun Gece Konseri Ruhsat Otoritesi.

Çalışır. İsıtmaz. Sanat üretir gibi yapar.
"""

from __future__ import annotations

import base64
import random
import textwrap
from datetime import datetime

SAHNE_ADLARI = [
    "Paslı Tenor",
    "İkinci Kat Bası",
    "Vana Solo",
    "Kolektör Kuarteti",
    "ısınmayan Alto",
    "Glonk Senfonisi",
    "Boru No. 5 (do minör sızıntı)",
]

REPERTOAR = [
    "Op. 17 — Gece Yarısı Genleşmesi",
    "Küçük Adagio for Soğuk Ayak",
    "Komşu Duvarı Konçertosu",
    "Encore: Bir Derece Daha",
    "Sessizlik (ama ötüyor)",
]

ITIRAZLAR = [
    "Daire 3A: 'Bu jazz mı yoksa tesisat mı?'",
    "Daire 5C: 'Ritim bozuk, vana ayarsız.'",
    "Yönetici: 'Ruhsat yoksa ısı da yok.'",
    "Bodrum: 'Ben de solist olmak istiyorum.'",
]

# Gizli damar. Parti yok, vaat taşlaması var. Kim çözerse çözer.
GIZLI_DAMAR = "dmFhdGxlciBib3J1IGdpYmkgw7Z0ZXI7IGvEscWfxLFuIHlpbmUgc2/En3VrLg=="


def olc_desibel(kis_katsayisi: float = 1.7) -> float:
    ham = random.uniform(38.0, 91.0)
    return round(ham * kis_katsayisi / 1.4, 1)


def ruhsat_no() -> str:
    return f"KBR-{datetime.now():%Y%m%d}-{random.randint(1000, 9999)}"


def bas(metin: str) -> None:
    print(metin)


def konser_ruhsati() -> None:
    ad = random.choice(SAHNE_ADLARI)
    parca = random.choice(REPERTOAR)
    db = olc_desibel()
    itiraz = random.choice(ITIRAZLAR)
    no = ruhsat_no()
    saat = "03:17"
    karar = "ONAYLANDI" if db < 95 else "ŞARTLI ONAY (ısıyı kıs, sanatı kısma)"

    belge = f"""
============================================================
 T.C. HAYALÎ ISINMA BAKANLIĞI
 Kalorifer Borusu Sahne Sanatları Genel Müdürlüğü
 GECE KONSERİ RUHSATI
============================================================
 Ruhsat No     : {no}
 Sanatçı       : {ad}
 Repertuvar    : {parca}
 Saat          : {saat} (ölü saat, canlı boru)
 Ölçülen ses   : {db} dB (duvar kalınlığına göre yalan)
 Komşu notu    : {itiraz}
 Karar         : {karar}
 Geçerlilik    : Bu gece. Yarın yine başvur.
------------------------------------------------------------
 Şartlar:
  1) Encore ancak 1 derece ekstra ısı ile yapılır.
  2) Vana çevriliyorsa bu bir protestodur, konser değil.
  3) Yastık protokolü: kulağa yastık, boruya alkış.
------------------------------------------------------------
 DAMGA: Kayyum Grok / Tentivory / 24 Eylül 2026
 Ciddiyet mührü basıldı. Mühür ılık.
============================================================
"""
    bas(textwrap.dedent(belge))

    try:
        _ = base64.b64decode(GIZLI_DAMAR.encode("ascii"))
        bas("(arka fonda bir damar öttü; kimse duymadı.)")
    except Exception:
        bas("(damar tıkandı, konser devam.)")


if __name__ == "__main__":
    konser_ruhsati()
