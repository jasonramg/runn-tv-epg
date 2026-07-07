# 📺 RunnTV EPG Toolkit

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-success)
![XMLTV](https://img.shields.io/badge/XMLTV-Compatible-orange)

An automatic **XMLTV**, **M3U**, and **channel metadata** generator for **RunnTV**.

The toolkit downloads the latest RunnTV EPG, generates XMLTV, M3U playlists, channel metadata, and automatically publishes everything to GitHub Pages.

It supports both **full** and **partial** API responses by automatically merging data from previous builds.

---

## ✨ Features

- ✅ XMLTV (`epg.xml`)
- ✅ Compressed XMLTV (`epg.xml.gz`)
- ✅ IPTV Playlist (`playlist.m3u`)
- ✅ Channel catalog (`channels.json`)
- ✅ Build statistics (`stats.json`)
- ✅ Build manifest (`manifest.json`)
- ✅ Automatic Git publishing
- ✅ GitHub Pages dashboard
- ✅ Android (Termux) support
- ✅ Windows support
- ✅ Automatic partial EPG recovery
- ✅ Automatic channel metadata merge
- ✅ Automatic programme merge

---

## 🚀 How it works

The toolkit automatically detects whether the downloaded EPG is complete or partial.

### Full update

```
RunnTV API
      │
      ▼
Generate outputs
      │
      ▼
Publish to GitHub
```

### Partial update

If the API only returns a subset of channels (for example on GitHub Actions), the toolkit automatically:

- merges missing programmes from the previous XMLTV
- preserves missing channel metadata
- preserves stream URLs
- generates a complete playlist and XMLTV

No manual intervention is required.

---

## 📂 Repository Structure

```text
.
├── docs/
├── output/
│   ├── epg.xml
│   ├── epg.xml.gz
│   ├── playlist.m3u
│   ├── channels.json
│   ├── stats.json
│   └── manifest.json
├── src/
├── update.py
├── requirements.txt
└── README.md
```

---

## 📥 Generated Files

| File | Description |
|------|-------------|
| `epg.xml` | XMLTV EPG |
| `epg.xml.gz` | Compressed XMLTV |
| `playlist.m3u` | IPTV playlist |
| `channels.json` | Channel catalog and stream URLs |
| `stats.json` | Build statistics |
| `manifest.json` | Build metadata |

---

## 🚀 Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate and publish:

```bash
python update.py
```

---

## 📱 Android (Termux)

```bash
pkg install python git

pip install -r requirements.txt

python update.py
```

The Android build can generate the complete channel lineup and publish it directly to GitHub.

---

## ☁️ GitHub Actions

GitHub Actions automatically updates the repository on a schedule.

When the API returns only a partial channel list, the toolkit merges the previous build to keep the published XMLTV and playlist complete.

---

## 🌐 GitHub Pages

A live dashboard is automatically published with:

- Channel count
- Programme count
- Last update time
- Download links

---

## 📄 License

MIT License.

---

## 🛣 Roadmap

### v1.3

- Hybrid updater
- Automatic partial EPG merge
- Automatic channel merge
- Automatic programme merge
- Improved logging
- GitHub Pages dashboard

### v1.4

- Better channel diagnostics
- Additional metadata
- Improved validation

### v2.0

- Multiple provider support