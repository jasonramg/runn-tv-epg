# 📺 RunnTV EPG Toolkit

An automatic **XMLTV** and **M3U playlist** generator for **RunnTV**.

The toolkit downloads the latest RunnTV EPG, converts it into XMLTV format, generates a compatible M3U playlist, and publishes everything to GitHub.

---

## ✨ Features

- ✅ XMLTV (`epg.xml`)
- ✅ Compressed XMLTV (`epg.xml.gz`)
- ✅ M3U Playlist (`playlist.m3u`)
- ✅ Channel catalog (`channels.json`)
- ✅ Build statistics (`stats.json`)
- ✅ Build manifest (`manifest.json`)
- ✅ Automatic Git publishing
- ✅ Android (Termux) support
- ✅ Windows support

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

## 📥 Downloads

After each successful update, the following files are generated:

| File | Description |
|------|-------------|
| `epg.xml` | XMLTV EPG |
| `epg.xml.gz` | Compressed XMLTV |
| `playlist.m3u` | IPTV playlist |
| `channels.json` | Channel catalog |
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

## 📱 Android

The toolkit works on Android using **Termux**.

```bash
pkg install python git
pip install -r requirements.txt

python update.py
```

---

## 💻 Windows

Clone the repository:

```bash
git clone https://github.com/jasonramg/runn-tv-epg.git

cd runn-tv-epg
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python update.py
```

---

## 📊 Generated Files

The toolkit automatically generates:

- XMLTV
- Compressed XMLTV
- IPTV Playlist
- Channel catalog
- Statistics
- Manifest

---

## 🌐 GitHub Pages

A project dashboard is available through GitHub Pages.

It displays:

- Channel count
- Programme count
- Last update time
- Download links

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Contributing

Issues and pull requests are welcome.

---

## 🛣 Roadmap

### v1.2

- Professional documentation
- GitHub Pages
- Validation improvements

### v1.3

- Better XMLTV metadata
- Improved logging

### v2.0

- Additional provider support