---
source: Instagram (akaun belum dikenal pasti)
platform: instagram
date: 2026-08-19
tags: [inbox, pending-extract]
status: perlu-login-dan-akaun-mungkin-private
link: https://www.instagram.com/reel/DZ71w_GqNkq/?igsh=MTZnbTdobTlwcXB3OQ==
---

## Apa knowledge ni
Belum dapat dikenal pasti. Reel ni **tidak boleh diakses tanpa login Instagram** — sudah disahkan pada level API, bukan sekadar masalah scraper.

## Kenapa penting
Masih pending — tak boleh nilai guna sampai content dibaca.

## Macam mana nak guna
Satu-satunya jalan: Fazir bagi **cookies Instagram** (export dari browser), atau screenshot/ringkasan. Kalau akaun tu private, cookies pun tak cukup — kena follow dulu.

## Content asal
Link reel: https://www.instagram.com/reel/DZ71w_GqNkq/
media_id: 3925967962940954922

## Bukti definitif (bukan masalah scraper)
Request `curl_cffi` (Chrome TLS impersonation + doc_id semasa + csrftoken + lsd token) ke `instagram.com/api/graphql` berjaya 200 OK, tapi return:
```json
{"data":{"xig_polaris_media":null},"extensions":{"is_final":true}}
```
`xig_polaris_media: null` pada HTTP 200 = Instagram sengaja tak serve media tanpa login. Ini bermakna reel ni salah satu daripada:
1. Akaun **private**
2. Post **dah delete/remove**
3. **Age/region-gated** (perlu login untuk sahkan umur/lokasi)

## Log penuh percubaan (semua gagal tanpa login)
| Method | Result |
|--------|--------|
| web_extract direct | Failed to fetch |
| curl direct (UA desktop) | Login wall |
| oEmbed api.instagram.com/oembed | 302 (perlu token) |
| Graph API graph.instagram.com | 400 perlu OAuth token |
| /embed/captioned/ | Login wall |
| /?__a=1&__d=dis | Page Not Found (endpoint mati) |
| ddinstagram.com proxy | 404 |
| allorigins.win proxy | 522 |
| yt-dlp (tanpa curl_cffi) | "empty media response" |
| yt-dlp (dengan curl_cffi) | "empty media response" |
| instaloader anonymous | "Fetching Post metadata failed" |
| curl_cffi direct + GraphQL | **200 OK tapi xig_polaris_media:null** (definitif) |
| iganony.io / imginn / greatfon | timeout / 403 / 404 |
| Wayback Machine | Tiada snapshot |

## Kesimpulan teknikal (untuk rujukan reel seterusnya)
- Instagram 2026: block IP datacenter + TLS fingerprinting (`requests`/`httpx` mati, kena `curl_cffi` impersonate Chrome).
- Cara betul test scrapeability: POST `instagram.com/api/graphql` dengan `doc_id` semasa + csrftoken + lsd, tengok `data.xig_polaris_media`.
- `null` = login-gated/private/removed. Ada `dict` = boleh scrape.
- doc_id semasa (Aug 2026): `27130156389949648` (friendly name `PolarisLoggedOutDesktopWWWPostRootContentQuery`). Ia rotate setiap 2-4 minggu.
- Kalau content PUBLIC: yt-dlp + `curl_cffi` dipasang sekali sudah cukup untuk scrape tanpa login.
