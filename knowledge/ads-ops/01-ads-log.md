---
type: ops-doc
date: 2026-10-03
tags: [ads-ops, ads-log, google-sheets]
status: belum-diisi
---

# 01 — Ads Log (Google Sheet)

Fazir tengah bina **Google Sheet** sebagai ads log. Fail ni dokumen *kontrak* antara sheet dengan hub.

## Kenapa sheet lebih baik dari nota

| Nota markdown | Google Sheet |
|---|---|
| Bagus untuk cerita & pengajaran | Bagus untuk **data berulang** |
| Susah nak kira | Senang nak pivot, banding, kira trend |
| — | Hub boleh baca melalui **Sheets API** — takde Tailscale, takde SSH |

## Tab yang cadang

| Tab | Lajur |
|---|---|
| `Campaigns` | date, account, campaign, objective, budget, spend, impressions, clicks, CTR, CPM, purchases, CPA, ROAS, status |
| `Creatives` | date, ad name, format, hook, angle, spend, hook rate, hold rate, CTR, CPA |
| `Decisions` | date, apa yang diubah, kenapa, sebelum, selepas, hasil |
| `Incidents` | date, jenis (reject/restrict/billing/stock), kesan, masa pulih |
| `Hub-Export` | ringkasan bersih khas untuk hub baca |

> 💡 `Hub-Export` tu penting — tab ni sengaja dikemas untuk hub. Kalau hub baca tab mentah, ia kena teka struktur. Satu tab bersih = bacaan tepat.

## Cara hub sambung

```
Hub (VPS) ──► Google Sheets API ──► baca tab Hub-Export
```

Setup: Google Cloud OAuth + share sheet **read-only** dengan akaun hub.

**Belum diisi:** ID sheet, nama tab sebenar, lajur sebenar.
