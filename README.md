# Capture! ByPass (TryHackme CTF)

<p align="center"><img src="images/capture-logo.png" alt="vkm-logo" style='width:150px;height:150px;'></p>


<div align="center">
    <img src="https://img.shields.io/badge/Code%20By%2014Wual-8338ec">
    <img src="https://img.shields.io/github/downloads/14wual/capture/total">
    <img src="https://img.shields.io/github/license/14wual/capture">
    <img src="https://img.shields.io/tokei/lines/github/14wual/capture">
    <img src="https://img.shields.io/github/stars/14wual/capture">
</div>

**Author**: Carlos Padilla (14wual)

**Download**: https://github.com/14wual/capture#Install

**Room Title**: Capture this!

**Room Link**: [URL](https://tryhackme.com/room/capture!)

**Room Author**: [toxicat0r](https://tryhackme.com/p/toxicat0r) && [https://tryhackme.com/p/tryhackme](tryhackme)


# Table of Contents

1. [Download](https://github.com/14wual/capture#Download)
2. [Usage](https://github.com/14wual/capture#Usage)
3. [Usage Example](https://github.com/14wual/capture#Example)
4. [Output](https://github.com/14wual/capture#Output)
5. [License](https://github.com/14wual/capture/LICENSE)


# Download

```
git clone https://github.com/14wual/capture/
cd capture/ && pip install -r requirements.txt

```

# Usage

```bash
┌──(wual㉿kali)-[~/capture]
└─$ python bypass.py --help  

usage: bypass.py [-h] [-p PASSLIST] [-u USERLIST] --url URL

CaptureByPass Args

options:
  -h, --help            show this help message and exit
  -p PASSLIST, --passlist PASSLIST
  -u USERLIST, --userlist USERLIST
  --url URL 
```

`--url URL` Is Required.

## Examples

```bash
python bypass.py --passlist passwords.txt --userlist usernames.txt --url 10.10.10.10
```

<details>
  <summary>See More</summary>

```bash
python bypass.py -p passwords.txt --u usernames.txt --url 10.10.10.10/login
```

```bash
python bypass.py -u usernames.txt --url http://10.10.10.10
```

```bash
python bypass.py -p passwords.txt --url http://10.10.10.10/login
```

```bash
python bypass.py --url http://10.10.10.10/login # http://10.10.10.10 or 10.10.10.10
```
    
</details>

# Output

```
==============================================
Capture!ByPass         Carlos Padilla (14wual)
==============================================
   _____                _                   _ 
  / ____|   /\         | |  ByPass Script  | |
 | |       /  \   _ __ | |_ _ __ _   _  ___| |
 | |      / /\ \ | '_ \| __| '__| | | |/ _ \ |
 | |____ / ____ \| |_) | |_| |  | |_| |  __/_|
  \_____/_/    \_\ .__/ \__|_|   \__,_|\___(_)
                 | |                          
                 |_| (Code by 14Wual)
==============================================
Author Web: https://14wual.github.io/
CTF Room: https://tryhackme.com/room/capture
==============================================
TARGET: http://10.10.206.228
==============================================
PassList Size: 1567
UserList Size: 878
==============================================
[Info] Started at: 30:01/2024 - 00:34:02
[Info] Captchat enabled.
[*] Trying Username: hunter with the test password.
...
[Info] Discovered username: n******.
[*] Trying Password: michaela for n******.
...
[Info] Discovered password: s***
==============================================
[CREDENTIALS] n******:s*******
==============================================
[Info] Opening New Browser Tab

```
