import zipfile
import zlib

with open("Ashley-Madison.txt", "r", encoding="utf-8") as f:
    passwords = [line.strip() for line in f if line.strip()]

with zipfile.ZipFile("whitehouse_secrets.zip") as zf:
    for pw_str in passwords:
        password = pw_str.encode("ascii")
        try:
            zf.extractall(pwd=password)
            print("Password found:", pw_str)
            break
        except (RuntimeError, zlib.error):
            continue
        
    
  