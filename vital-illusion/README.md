<div align="center">

```
██╗   ██╗██╗████████╗ █████╗ ██╗          ██╗██╗     ██╗     ██╗   ██╗███████╗██╗ ██████╗ ███╗   ██╗
██║   ██║██║╚══██╔══╝██╔══██╗██║          ██║██║     ██║     ██║   ██║██╔════╝██║██╔═══██╗████╗  ██║
██║   ██║██║   ██║   ███████║██║          ██║██║     ██║     ██║   ██║███████╗██║██║   ██║██╔██╗ ██║
╚██╗ ██╔╝██║   ██║   ██╔══██║██║          ██║██║     ██║     ██║   ██║╚════██║██║██║   ██║██║╚██╗██║
 ╚████╔╝ ██║   ██║   ██║  ██║███████╗     ██║███████╗███████╗╚██████╔╝███████║██║╚██████╔╝██║ ╚████║
  ╚═══╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                              ◈ The Illusion of the Living ◈
```

<p><em>"Cloning, immortality, and the murder of the original."</em></p>

<p>
  <img src="https://img.shields.io/badge/baudrillard-suite-9B30FF?style=for-the-badge" alt="suite">
  <img src="https://img.shields.io/badge/vital--illusion-deepfake%20detection-FF0066?style=for-the-badge" alt="vital-illusion">
  <img src="https://img.shields.io/badge/python-3.10+-00FF41?style=for-the-badge&logo=python&logoColor=white" alt="python">
</p>

**Deepfake & Synthetic Media Detection - Spotting artificial life**

</div>

---

## 🔮 Concept

In "The Vital Illusion," Baudrillard explored cloning and the death of the original. When copies can exist without originals, what is "authentic"?

**Vital-Illusion** detects synthetic media—deepfakes, AI-generated content, voice cloning—by searching for the absence of life. The artificial lacks something ineffable: the vital illusion.

---

## ⚡ Detection Philosophy

### The Vital Signs We Seek
Real humans have micro-expressions, breath variations, blood flow, unconscious tells. AI lacks the "noise of being alive."

### What We Detect
- **Video Deepfakes**: Face swaps, lip sync, full synthetic
- **Audio Clones**: Voice synthesis, cloned speech
- **Text Generation**: AI-written content detection
- **Image Synthesis**: GAN/diffusion artifacts
- **Live Stream Manipulation**: Real-time deepfake detection

---

## 🛠️ Modules

### 🎭 face-oracle
*Deepfake video detection*

```bash
vital-illusion face --input video.mp4
```

- **Temporal coherence**: Do features flow naturally across frames?
- **Micro-expression analysis**: Are unconscious expressions present?
- **Lighting consistency**: Does skin react to light realistically?
- **Physiological signals**: Can we detect pulse from face color?
- **Artifact hunting**: GAN fingerprints, blending seams

### 🔊 voice-seance
*Synthetic voice detection*

```bash
vital-illusion voice --input audio.wav
```

- **Breath detection**: Real humans breathe, AI doesn't
- **Emotional authenticity**: Are micro-tremors present?
- **Formant analysis**: Natural vs synthetic vocal tract
- **Clone fingerprinting**: Identify the source model
- **Liveness detection**: Is this a recording or live?

### ✍️ ghost-writer
*AI text detection*

```bash
vital-illusion text --input document.txt
```

- **Perplexity analysis**: Human writing is unpredictable
- **Burstiness detection**: Humans vary sentence complexity
- **Semantic fingerprinting**: AI has telltale patterns
- **Model attribution**: Which AI wrote this?

### 🖼️ dream-catcher
*Synthetic image detection*

```bash
vital-illusion image --input photo.jpg
```

- **GAN artifact detection**: Checkerboard patterns, frequency anomalies
- **Diffusion fingerprints**: Stable Diffusion, Midjourney, DALL-E
- **Physical impossibilities**: Impossible reflections, broken physics
- **Metadata archaeology**: Was this image ever "real"?

---

## 📊 Output Example

```
██╗   ██╗██╗████████╗ █████╗ ██╗          ██╗██╗     ██╗     ██╗   ██╗███████╗██╗ ██████╗ ███╗   ██╗
[EXAMINING] Searching for vital signs...

◈ AUTHENTICITY ANALYSIS ◈

Target: ceo_announcement.mp4
Duration: 2:34
Resolution: 1920x1080

┌─────────────────────────────────────────────────────────────────────┐
│ VERDICT: SYNTHETIC MEDIA DETECTED                                   │
├─────────────────────────────────────────────────────────────────────┤
│ Confidence:       ████████░░ 94.7%                                  │
│ Type:             Face swap deepfake                                │
│ Technique:        First-order motion model (likely)                 │
│ Source face:      Unknown individual                                │
│ Target face:      Matches "John Smith" (LinkedIn photo)             │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ VITAL SIGNS ANALYSIS                                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│ Micro-expressions:                                                  │
│   Expected:       47 ± 12 per minute (human baseline)               │
│   Detected:       8 per minute                                      │
│   Assessment:     ⚠️  ABNORMALLY LOW                                │
│                                                                     │
│ Pulse detection (rPPG):                                             │
│   Expected:       60-100 BPM detectable from face                   │
│   Detected:       NO PULSE SIGNAL                                   │
│   Assessment:     ☠️  CRITICAL - No vital signs                     │
│                                                                     │
│ Blink rate:                                                         │
│   Expected:       15-20 per minute                                  │
│   Detected:       4 per minute                                      │
│   Assessment:     ⚠️  ABNORMALLY LOW                                │
│                                                                     │
│ Eye tracking:                                                       │
│   Saccades:       Unnaturally smooth                                │
│   Pupil response: No light adaptation detected                      │
│   Assessment:     ⚠️  NON-HUMAN PATTERNS                            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ TECHNICAL ARTIFACTS                                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│ Face boundary:                                                      │
│   Frames 127-134: Visible blending artifact at jawline              │
│   Frames 892-901: Face tracking failure, visible glitch             │
│                                                                     │
│ Audio sync:                                                         │
│   Lip sync score: 0.73 (threshold: 0.90)                            │
│   Phoneme timing: 23ms average drift (suspicious)                   │
│                                                                     │
│ Frequency analysis:                                                 │
│   GAN fingerprint detected in face region                           │
│   Compression artifacts inconsistent with claimed camera            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

◈ EVIDENCE PACKAGE ◈
Exported to: ceo_announcement_analysis.pdf
- Frame-by-frame anomaly visualization
- Audio waveform analysis
- Artifact highlight video
- Chain of custody metadata
- Expert witness summary

"The clone is more alive than the original—which is why we must kill it."
```

---

## 🚀 Installation

```bash
git clone https://github.com/bad-antics/vital-illusion
cd vital-illusion
pip install -e .

# Download detection models
vital-illusion download-models

# Run analysis
vital-illusion --input media_file
```

---

## 🎯 Use Cases

- **Corporate Security**: Verify video calls are real
- **Journalism**: Authenticate sources before publication
- **Legal**: Expert analysis for court proceedings
- **Personal**: Check if "that video" is really your friend
- **Research**: Advance deepfake detection science

---

<div align="center">
  <img src="https://img.shields.io/badge/made%20for-authenticity-9B30FF?style=for-the-badge" alt="authenticity">
  <p><em>"The vital illusion is the only thing that separates us from our clones."</em></p>
</div>
