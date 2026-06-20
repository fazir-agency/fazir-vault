# Model Switching — How It Works

**Date:** 2026-06-20
**Source:** CEO session with Fazir

## Apa jadi bila tukar model mid-session?

| Benda | Effect |
|-------|--------|
| SOUL.md / system prompt | ✅ Sama — identity tak berubah |
| Memory & context | ✅ Sama — semua conversation masih ada |
| Tool execution | ✅ Sama — terminal, file ops, delegate semua ok |
| Output quality/style | ⚠️ Berubah — setiap model ada "personality" tersendiri |

## Model Personalities

- **DeepSeek** → Technical, detail-heavy, breakdown panjang
- **Claude** → Natural reasoning, context-aware, focused
- **GPT** → Conversational, lebih rambling

## Cara Tukar Model

Guna `/model` command dekat Telegram. Contoh: `/model claude`

Sistem akan handle switching — next reply dah pakai model baru.

## Best Practice

- **Strategy sessions / decision making** → stick dengan satu model dari awal sampai akhir
- **Exploratory / brainstorming** → boleh switch, kadang dapat perspective berbeza
- Bila switch, bagitau agent — "Aku pindah Claude" — supaya dia adjust framing style

## Note untuk Staff

Model berbeza = cara deliver berbeza, tapi knowledge base (vault ni), skills, dan SOUL.md sama je. Output quality bergantung pada model yang Fazir guna masa tu. Jangan expect identical responses bila model bertukar.
