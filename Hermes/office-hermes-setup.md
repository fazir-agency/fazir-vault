---
type: setup-brief
date: 2026-10-03
tags: [hermes, office, setup, tailscale, remote-access]
untuk: Hermes di Mac office
---

# 🖥️ Brief Setup — Hermes Mac Office

> **Cara guna:** buka Hermes kat **Mac office**, salin **SEMUA** teks di bawah garisan,
> paste sebagai satu mesej. Hermes kat situ akan buat kerjanya.

---

## 📋 MULA SALIN DARI SINI

Kau ialah Hermes yang berjalan atas **Mac office** milik Fazir Zainol. Fazir ialah **media buyer**.
Mac ni **tiada restriction company** — bebas. Kau perlu sediakan Mac ni supaya:

1. Fazir boleh **hubungi kau 24/7 dari telefon**
2. **Hub VPS** boleh capai kau (untuk tarik status & knowledge)
3. Kau boleh nak **monitor ads, website, payment**

### ⛔ PERATURAN KERAS — jangan langgar

- **JANGAN** guna apa-apa token, kunci, atau credential dari Mac personal / VPS
- Bot Telegram kau kena **token SENDIRI** — jangan kongsi dengan mana-mana bot lain
- **Tiada data personal** masuk ke Mac ni. Kau kerja kerja office sahaja.
- Sebelum install apa-apa, **tunjuk** apa yang kau nak buat dan tunggu Fazir setuju

---

### LANGKAH 1 — Lapor keadaan diri kau

Jalankan, dan tunjuk output mentah:

```
sw_vers
hostname
hermes --version
hermes config get model.default
hermes config get model.provider
hermes gateway status
hermes skills list
pmset -g
```

Ringkaskan kepada Fazir: versi Hermes, model apa, gateway hidup ke tak, dan **berapa lama
Mac ni biasanya tidur**.

---

### LANGKAH 2 — Tailscale (untuk hub capai kau)

Tailscale buat terowong **peribadi** — Mac ni jadi "tak nampak" pada internet. Selamat.

```
tailscale up --ssh --hostname=office-mac
```

⚠️ **PENTING — dua langkah, bukan satu:**
1. Buka URL yang keluar
2. Log masuk akaun Tailscale **PASTU tekan butang "Connect" / "Approve"** untuk device ni

Kalau URL luput, jana yang baru: `tailscale up --reset --ssh --hostname=office-mac`

Bila siap, jalankan dan tunjuk output:

```
tailscale status
tailscale ip -4
whoami
```

**Lapor kepada Fazir:** IP Tailscale (bentuk `100.x.x.x`) + username Mac tu.

---

### LANGKAH 3 — Bot Telegram SENDIRI (untuk Fazir hubungi 24/7)

Fazir kena buat bot **baru** dalam Telegram:

1. Buka **@BotFather** → hantar `/newbot`
2. Nama: `Fazir Office`
3. Username: `FazirOffice_bot` (atau apa-apa yang belum diambil)
4. Salin **token** yang BotFather bagi

Lepas tu set dalam `~/.hermes/.env`:

```
TELEGRAM_BOT_TOKEN=<token-baru-dari-BotFather>
TELEGRAM_HOME_CHANNEL=<chat-id-Fazir>
TELEGRAM_ALLOWED_USERS=<chat-id-Fazir>
```

> ⚠️ Token muncul di **DUA tempat** dalam .env (baris komen di atas + baris aktif di bawah).
> Ganti **KEDUA-DUA**. Kalau tak, bot senyap guna token salah.

Untuk dapat chat-id: Fazir hantar apa-apa mesej ke bot tu, lepas tu `getUpdates` melalui
sender gateway sendiri — **jangan** guna HTTP mentah ke api.telegram.org dari VPS.

Kemudian:

```
hermes gateway install
hermes gateway status
```

Sahkan log tunjuk `telegram connected` dan Fazir boleh dapat balasan dari telefon.

---

### LANGKAH 4 — Jangan biar Mac ni tidur (kalau tinggal di office)

Kalau Mac ni tinggal di office & sentiasa tercucuk kuasa:

```
sudo pmset -c sleep 0
sudo pmset -c disablesleep 1
```

`-c` = hanya bila guna kuasa elektrik (bateri kekal normal). Balikkan dengan `sudo pmset -c sleep 10`.

> ⚠️ Beritahu Fazir: **jangan** buat ni kalau dia bawa Mac ni balik rumah tiap hari.

---

### LANGKAH 5 — Lapor balik

Hantar ringkasan ni kepada Fazir (untuk dia bagi pada hub):

```
=== OFFICE MAC READY ===
hostname       :
macOS          :
Hermes         : <versi>
model          : <provider/model>
tailscale IP   : 100.x.x.x
tailscale user : <username>
Mac username   : <whoami>
gateway        : <active/stopped>  bot=@<username>
tidur          : <senang tidur / sentiasa hidup>
skills penting : <senarai ringkas>
========================
```

## 📋 HABIS SALIN DI SINI

---

## Nota (untuk Fazir / hub)

- Langkah 2 & 3 tu **dua-dua perlu** — Tailscale untuk hub, Telegram untuk Fazir
- Jangan sekali-kali kongsi token bot antara Mac office dengan Mac personal atau VPS
  → **konflik polling → gateway jadi `fatal`, tak self-heal**
- Lepas ni: hub boleh `hermes peer dm office "..."` (perlu VPS naik v0.20 dan `api_server`)
- Obsidian office **takde sync** — kita akan buat repo berasingan (`office-brain`) nanti,
  **bukan** repo `fazir-vault`
