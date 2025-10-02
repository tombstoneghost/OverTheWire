# OverTheWire Bandit Solutions

## Connecting to the Machine

- SSH to port 2220 with the target user
- Use the password found in the previous level

---

### Level 0 &rarr; 1

**Steps:**

- Connect: `ssh bandit0@bandit.labs.overthewire.org -p 2220`
- Password: `bandit0`
- Read the "readme" file: `cat readme`

**Password:** `ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If`

---

### Level 1 &rarr; 2

**Steps:**

- Connect to the machine
- There is a file named `-`
- Use: `cat ./-`

**Password:** `263JGJPfgU6LtdEvgfWU1XP5yac29mFx`

---

### Level 2 &rarr; 3

**Steps:**

- Connect to the machine
- File: `--spaces in this filename--`
- Use: `cat ./--spaces\ in\ this\ filename--`

**Password:** `MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx`

---

### Level 3 &rarr; 4

**Steps:**

- Connect to the machine
- Folder `inhere` is empty
- Use `ls -la` to find hidden file
- Read the file

**Password:** `2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ`

---

### Level 4 &rarr; 5

**Steps:**

- Connect to the machine
- Folder `inhere` contains files
- Use: `strings inhere/-file0*`

**Password:** `4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw`

---

### Level 5 &rarr; 6

**Steps:**

- Connect to the machine
- Folder `inhere` contains many folders
- Use: `find . -size 1033c`
- Then: `cat ./maybehere07/.file2`

**Password:** `HWasnPhtq9AVKe0dmk45nxy20cvUa6EG`

---

### Level 6 &rarr; 7

**Steps:**

- Connect to the machine
- Use: `find / -size 33c -user bandit7 2>/dev/null`
- Then: `cat /var/lib/dpkg/info/bandit7.password`

**Password:** `morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj`

---

### Level 7 &rarr; 8

**Steps:**

- Connect to the machine
- Use: `cat data.txt | grep millionth`

**Password:** `dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc`

---

### Level 8 &rarr; 9

**Steps:**

- Connect to the machine
- Use: `sort data.txt | uniq -c | sort -r`

**Password:** `4CKMh1JI91bUIZZPXDqGanal4xvAg0JM`

---

### Level 9 &rarr; 10

**Steps:**

- Connect to the machine
- Use: `strings data.txt | grep =`

**Password:** `FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey`

---

### Level 10 &rarr; 11

**Steps:**

- Connect to the machine
- Use: `cat data.txt | base64 -d`

**Password:** `dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr`

---

### Level 11 &rarr; 12

**Steps:**

- Connect to the machine
- Use CyberChef to perform Rot13 on data.txt

**Password:** `7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4`

---

### Level 12 &rarr; 13

**Steps:**

- Connect to the machine
- Create temp dir: `mktemp -d`
- Convert hexdump: `cat data.txt | xxd -r > data2.bin`
- Convert to gzip: `mv data2.bin data2.gz`
- Decompress: `gzip -d data2.gz`
- Convert to bzip: `mv data2 data2.bz2`
- Decompress: `bzip2 -d data2.bz2`
- Repeat with relevant tools

**Password:** `FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn`

---

### Level 13 &rarr; 14

**Steps:**

- Connect to the machine
- SSH to user bandit14 with private key:  
  `ssh -i sshkey.private bandit14@localhost -p 2220`
- Read password in `/etc/bandit_pass/bandit14`

**Password:** `MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS`

---

### Level 14 &rarr; 15

**Steps:**

- Connect to the machine
- Connect to service on port 30000: `nc localhost 30000`
- Submit password for current level

**Password:** `8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo`

---

### Level 15 &rarr; 16

**Steps:**

- Connect to the machine
- Connect using openssl: `openssl s_client -connect localhost:30001`
- Submit password for current level

**Password:** `kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx`

---

### Level 16 &rarr; 17

**Steps:**

- Connect to the machine
- Use nmap: `nmap localhost -p 31000-32000`
- Run openssl with found port: `openssl s_client -connect localhost:31790 -ign_eof`
- Get SSH Private Key and login:  
  `ssh -i level17.key bandit17@bandit.labs.overthewire.org -p 2220`

---

### Level 17 &rarr; 18

**Steps:**

- Connect to the machine
- Use: `diff passwords.old passwords.new`

**Password:** `x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO`

---

### Level 18 &rarr; 19

**Steps:**

- Login:  
  `ssh bandit18@bandit.labs.overthewire.org -p 2220 "bash --noprofile --norc"`
- No banner, use Linux command
- `cat readme`

**Password:** `cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8`

---

### Level 19 &rarr; 20

**Steps:**

- Connect to the machine
- SUID binary: `bandit20-do`
- Use: `./bandit20-do cat /etc/bandit_pass/bandit20`

**Password:** `0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO`

---

### Level 20 &rarr; 21

**Steps:**

- Connect to the machine
- Send password to port 1234:  
  `echo -n "0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO" | nc -lp 1234 &`
- Connect using the binary to port 1234

**Password:** `EeoULMCra2q0dSkYj561DX7s1CpBuOBt`

---

### Level 21 &rarr; 22

**Steps:**

- Connect to the machine
- Check cron for level 22: `/etc/cron.d/cronjob_bandit22`
- Find password location in script

**Password:** `tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q`

---

### Level 22 &rarr; 23

**Steps:**

- Connect to the machine
- Check cron for level 23: `/etc/cron.d/cronjob_bandit23`
- Command: `echo I am user bandit23 | md5sum | cut -d ' ' -f 1`
- Execute locally, get password in filename

**Password:** `0Zf11ioIjMVN551jX3CmStKLYqjk54Ga`

---

### Level 23 &rarr; 24

**Steps:**

- Connect to the machine
- Check cron for level 24: `/etc/cron.d/cronjob_bandit24`
- Script deletes files in `/var/spool/bandit24/foo`
- Write a script to copy password to temp directory
- Set permissions: `chmod 777 /tmp/tmp.VDBvAS7DQd`
- Create pass file: `touch pass; chmod 777 pass`
- Script:  
  `echo "cat /etc/bandit_pass/bandit24 >> /tmp/tmp.VDBvAS7DQd/pass" > script.sh`
- Copy script: `cp script.sh /var/spool/bandit24/foo`
- After a minute, get password from file

**Password:** `gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8`

---

### Level 24 &rarr; 25

**Steps:**

- Connect to the machine
- Use script:
  ```bash
  for i in $(seq 1 9999); do
      num=$(printf "%04d" "$i");
      response=$( printf '%s %s\r\n' "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8" "$num" | nc -N localhost 30002 2>/dev/null); 
      if [[ "$response" != *"Wrong!"* ]]; then 
          echo $response; 
      fi
  done;
  ```
- After a few seconds, get password

**Password:** `iCi86ttT4KSNe1armKiwbQNmB3YJP3q4`

---

### Level 25 &rarr; 26

**Steps:**

- Connect to the machine
- Home folder contains SSH Keys for Bandit26
- Can't login due to different shell
- Check shell: `cat /etc/passwd | grep bandit26`
- Shell is `/usr/bin/showtext`
- Make terminal smaller before SSH, get into interactive command with `v`
- Use `:e /etc/bandit_pass/bandit26`
- To get shell: `:set shell=/bin/bash` then `:shell`

**Password:** `s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ`

---

### Level 26 &rarr; 27

**Steps:**

- From shell from level 26, file `bandit27-do` in home directory
- Use: `./bandit27-do cat /etc/bandit_pass/bandit27`

**Password:** `upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB`

---

### Level 27 &rarr; 28

**Steps:**

- Connect to the machine
- Temp dir: `mktemp -d`
- Clone repo:  
  `git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo`
- Password is in README

**Password:** `Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN`

---

### Level 28 &rarr; 29

**Steps:**

- Connect to the machine
- Temp dir: `mktemp -d`
- Clone repo:  
  `git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo`
- Use `git log`
- Checkout previous commit:  
  `git checkout 68314e012fbaa192abfc9b78ac369c82b75fab8f`

**Password:** `4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7`

---

### Level 29 &rarr; 30

**Steps:**

- Connect to the machine
- Temp dir: `mktemp -d`
- Clone repo:  
  `git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo`
- Branch `dev`: `git branch -a`
- Checkout: `git checkout dev`
- Check README

**Password:** `qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL`

---

### Level 30 &rarr; 31

**Steps:**

- Connect to the machine
- Temp dir: `mktemp -d`
- Clone repo:  
  `git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo`
- Tag `secret`: `git tag -l`
- Read tag: `git show secret`

**Password:** `fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy`

---

### Level 31 &rarr; 32

**Steps:**

- Connect to the machine
- Temp dir: `mktemp -d`
- Clone repo:  
  `git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo`
- Update `.gitignore` (remove all contents)
- Create `key.txt` and push:
  ```bash
  echo "May I come in?" >> key.txt
  git add .
  git commit -m "May I come in?"
  git push -u origin master
  ```

**Password:** `3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K`

---

### Level 32 &rarr; 33

**Steps:**

- Connect to the machine
- All commands result in uppercase
- Enter `$0` (current shell, `sh`)
- Get shell access
- Read password: `/etc/bandit_pass/bandit33`

**Password:** `tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0`
