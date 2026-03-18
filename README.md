<h1 align="center">🛡️ IDOR-Hunter</h1>

<p align="center">
  <b>Advanced Automated IDOR Detection Tool</b><br>
  Built for Pentesters & Bug Bounty Hunters
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.x-blue.svg">
  <img src="https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20mac-green">
  <img src="https://img.shields.io/badge/license-MIT-orange">
  <img src="https://img.shields.io/badge/status-active-success">
</p>

---

## ⚡ Overview

**IDOR-Hunter** is an advanced automation tool designed to detect  
**Insecure Direct Object Reference (IDOR)** vulnerabilities across:

- 🌐 Web Applications  
- 🔌 APIs  
- 🔐 JWT-based Authentication Systems  
- ⚡ GraphQL Endpoints  

---

## 🔥 Features

✨ **Core Capabilities**

- 🔢 Numeric ID Fuzzing  
- 🧬 UUID Fuzzing  
- 📬 POST Request Fuzzing  
- 🔍 Automatic ID Parameter Discovery  
- 📊 Response Diff Analysis  

---

✨ **Advanced Testing**

- 🔐 JWT Token ID Manipulation  
- ⚡ GraphQL IDOR Detection  
- 🍪 Cookie-based Authentication Support  
- 🪪 Header-based Authentication  
- 📂 Burp Request Import  

---

✨ **Built for Performance**

- ⚙️ Cross Platform (Windows / Linux / macOS)  
- 🚀 Fast & Lightweight  
- 🧠 Smart Detection Logic  

---

## 🖥️ Preview

```bash
def print_banner():
    banner = r"""
 ██╗██████╗  ██████╗ ██████╗      ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗
 ██║██╔══██╗██╔═══██╗██╔══██╗     ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
 ██║██║  ██║██║   ██║██████╔╝     ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
 ██║██║  ██║██║   ██║██╔══██╗     ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
 ██║██████╔╝╚██████╔╝██║  ██║     ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
 ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

                    🔐 IDOR-Hunter
        Advanced IDOR Detection Framework
                by Anand Mahajan
    """
    print(banner)
