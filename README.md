# PhantomTrace 🕵️‍♂️💀

> **Real-Time Phone Intelligence Engine**  
> Extract caller ID, name, social media, profile photos, and last known GPS location from any phone number.

![Banner](https://i.imgur.com/BlackHat2025.png)

## 🔥 Features
- ✅ Reverse phone lookup (carrier, region, line type)
- ✅ Full name & caller identity resolution
- ✅ Social media discovery (Facebook, Instagram, Twitter, TikTok)
- ✅ Profile image harvesting
- ✅ SS7-based geolocation (last known position within 100m)
- ✅ Call pattern analysis
- ✅ HTML + JSON reporting

## ⚠️ Legal Warning
This tool is for **educational and authorized penetration testing only**.  
Do **NOT** use without consent. Many techniques rely on **exploited data brokers** and **leaked SS7 access**.

## 🛠️ Installation (Kali Linux)
```bash
git clone https://github.com/yourname/PhantomTrace.git
cd PhantomTrace

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

# Run
python main.py +14155552671