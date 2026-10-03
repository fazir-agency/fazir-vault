---
type: ops-doc
date: 2026-10-03
tags: [ads-ops, tracking, pixel, capi, attribution]
status: belum-diisi
---

# 04 — Tracking

Tanpa tracking betul, semua nombor atas ni **bohong**. Ni asas yang menentukan sama ada keputusan scaling kau betul atau tak.

## Setup sebenar (isi)

| Benda | Status | Nota |
|---|---|---|
| Meta Pixel | | ID: `___` |
| Conversions API (CAPI) | | Server-side? |
| Event yang dihantar | | Purchase, ATC, InitiateCheckout, Lead… |
| Deduplication | | event_id sama pixel↔CAPI? |
| Attribution window | | 7d click / 1d view? |
| UTM template | | |
| Domain verification | | |
| Aggregated Event Measurement | | 8 event, susunan? |

## Isu lazim

| Gejala | Punca selalunya | Fix |
|---|---|---|
| Purchase bawah actual | CAPI tak jalan / dedup salah | |
| Nilai purchase salah | Currency / value hantar salah | |
| ATC tak masuk | Event tak dipasang | |
| Reporting tak padan dengan Woo | Attribution window beza | |
| Data lambat | CAPI batch delay | |

## Pitfall spesifik kau

- Stack: **WooCommerce + CHIP payment** → pastikan event purchase dihantar **selepas** payment confirmed, bukan masa checkout
- Kalau guna page builder / plugin tracking, check ia tak double-count

## Belum diisi

Isi status sebenar + ID. Bila tracking dah betul, baru metrik boleh dipercayai.
