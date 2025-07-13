# dnsgitbruter

# dnsgitbruter

`dnsgitbruter` is a simple Python-based subdomain brute-forcing tool that resolves DNS records using a wordlist. It supports both local files and remote wordlist URLs (e.g. from GitHub SecLists).

---


# Create a virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt



## 📦 Features

- Brute-force subdomains using DNS resolution
- Accepts a wordlist from a local file or URL
- Lightweight and easy to set up with a virtual environment

---

## 🚀 Setup Instructions

### 1. Clone or download the script
```bash
git clone <your_repo_url>
cd dnsgitbruter'''

#### Usage

python dnsgitbruter.py -d example.com --url https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Discovery/DNS/subdomains-top1million-110000.txt






