---
type: ops-doc
date: 2026-10-03
tags: [ads-ops, sop, daily]
status: belum-diisi
---

# 00 — SOP Harian

Rutin operasi harian media buyer. Bila hub automate, fail ni jadi **spesifikasi** untuk cron job.

## Checklist pagi (sebelum apa-apa)

- [ ] Semak **ad account health** — ada rejection / restriction baru?
- [ ] Semak **billing** — kad fail? spending limit kena?
- [ ] Semak **stok** (WooCommerce) — ada produk habis masa iklan masih jalan?
- [ ] Semak **campaign** — mana yang kena pause semalam?
- [ ] Semak **spend pacing** — over/under hari semalam

## Threshold & tindakan

| Keadaan | Tindakan | Auto / Manual |
|---|---|---|
| CPA > ___ (had) | | |
| ROAS < ___ | | |
| Frequency > ___ | | |
| Spend limit < ___% | | |
| Stok = 0 | | |
| Payment fail | | |

## Rule escalate ke Fazir

Bila hub kena berhenti dan tanya:

- Naik budget > ___%
- Matikan campaign yang spend > RM___
- Ubah creative pada ad set yang tengah menang
- Apa-apa yang melibatkan duit > RM___

## ⏰ Waktu

| Bila | Apa |
|---|---|
| Pagi (___ AM) | Checklist penuh |
| Tengah hari | Semak pacing |
| Malam (___ PM) | Ringkasan harian → Telegram |

## Belum diisi

Isi bahagian kosong (`___`) dengan nombor sebenar Fazir. Bila dah ada angka, hub boleh automate.
