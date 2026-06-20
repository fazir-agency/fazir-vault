# RunPod + ComfyUI Setup — Complete Guide

**Date:** 2026-06-20
**Setup by:** CEO (Claude)
**Status:** ✅ Live

## Pod Details

| Item | Value |
|------|-------|
| Pod ID | `m03p3zrur4e4ni` |
| GPU | RTX A6000 (48GB VRAM) |
| Cost | $0.33/hr |
| Image | `runpod/comfyui:latest` |
| ComfyUI URL | https://m03p3zrur4e4ni-8188.proxy.runpod.net |
| Jupyter URL | https://m03p3zrur4e4ni-8888.proxy.runpod.net |
| Jupyter PW | `comfy123` |

## Models Downloaded

| Model | File | Size | Purpose |
|-------|------|------|---------|
| Wan2.1 T2V 14B fp8 | `Wan2_1-T2V-14B_fp8.safetensors` | 14GB | Text-to-Video |
| Wan2.1 I2V 14B 720P fp8 | `Wan2_1-I2V-14B-720P_fp8.safetensors` | 16GB | Image-to-Video |

**Model path in pod:** `/workspace/runpod-slim/ComfyUI/models/diffusion_models/`

**Source repo:** `Kijai/WanVideo_comfy` (NOT `Wan2.1_comfy` — repo dah bertukar nama)

## Watchdog Auto-Pause

Cron job `b1fb29b8568b` berjalan every 5 minit. Auto-pause pod bila idle 5 minit. Script: `~/.hermes/scripts/runpod_watchdog.sh`

## Key Lessons Learned

### 1. Repo Lama 404
Old repo `Kijai/Wan2.1_comfy` → 404. Repo baru: `Kijai/WanVideo_comfy`

### 2. HuggingFace Token Required
Model-model Kijai perlukan HF token. Token format: `hf_xxx...`
Download command:
```bash
curl -L -H "Authorization: Bearer HF_TOKEN" \
  "https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/FILENAME" \
  -o /path/to/output
```

### 3. GPU Stock
L40 sering SUPPLY_CONSTRAINT. Fallback order:
1. RTX A6000 (48GB, $0.33/hr) ← terbaik value
2. L40S
3. RTX 6000 Ada
4. A100 PCIe

### 4. Jupyter Login via WS
Nak run commands dalam pod tanpa browser:
1. Login via HTTP cookie (xsrf token)
2. Create terminal via `/api/terminals`
3. Connect WebSocket ke `/terminals/websocket/{name}`
4. Send commands as `["stdin", "command\n"]`

### 5. ComfyUI-Manager API
`runpod/comfyui:latest` ada `/cm-model-download-url` endpoint.
`runpod/comfyui:cuda12.8` (slim) — **TIDAK ada** endpoint ni.

## API Key Storage

RunPod API key disimpan kat `/home/agent-runner/.env`
```
RUNPOD_API_KEY=rpa_xxx...
```

## Resume Pod

```bash
curl -s "https://api.runpod.io/graphql?api_key=KEY" \
  -H "Content-Type: application/json" \
  -d '{"query":"mutation { podResume(input: { podId: \"m03p3zrur4e4ni\", gpuCount: 1 }) { id desiredStatus } }"}'
```
