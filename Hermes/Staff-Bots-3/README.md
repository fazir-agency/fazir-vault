# Staff Bots v3 — 3-Bot Structure (DRAF)

Rancangan penyusunan semula: 14 bot → 3 bot untuk jimat RAM VPS.

## 3 Bot Baru

| Bot | Gabungan dari | Model |
|-----|--------------|-------|
| [[Creative]] | creative-strategist + copywriter + scriptwriter + social + designer + video | DeepSeek V4 Pro |
| [[Intelligence]] | research + trend + data-analyst + media-buyer + affiliate-manager + report | DeepSeek V4 Pro |
| [[TechOps]] | developer + ops | DeepSeek V4 Pro |

> Semua bot guna DeepSeek V4 Pro — tak pakai Claude buat masa ni (jimat kos).

## Kenapa Pembahagian Ini

- **Creative** — semua yang "keluarkan content" (strategi → copy → script → social → design → video)
- **Intelligence** — semua yang "tahu pasaran + kira duit" (research → trend → data → media buy → affiliate → report)
- **TechOps** — semua yang "jaga infrastruktur" (developer + ops)

## Penjimatan RAM

- 14 proses Hermes (~75-110MB setiap satu) = ~1.1GB
- 3 proses = ~250-300MB
- JIMAT ~800MB+ RAM

## Nota Penting

- Ini DRAF SOUL.md sahaja. Belum deploy ke VPS.
- Folder `Staff-SOUL/` (yang lama, 14 fail asal) TIDAK disentuh.
- Setiap bot gabungan ada "Role Modes" section — bila dapat task, ia switch ke mode yang betul (cth: Mode B = Copywriter).

## Langkah Seterusnya (belum buat)

1. Semak draf 3 SOUL ini dengan Fazir
2. Archive SOUL.md asal 14 bot (bukan delete)
3. Bina profile baru di VPS untuk 3 bot
4. Matikan 14 bot lama (jimat RAM)
5. Verify + test
