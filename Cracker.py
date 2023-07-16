import hashlib
import threading

def hash_cracker(target_hash, wordlist, start, end, result):
    try:
        with open(wordlist, 'r') as f:
            f.seek(start)
            line = f.readline()
            while line and f.tell() <= end:
                word = line.strip()
                hashed_word = hashlib.md5(word.encode()).hexdigest()
                if hashed_word == target_hash:
                    result.append(word)
                    return
                line = f.readline()
    except:
        pass

target_hash = input("Enter the MD5 hash to crack: ")
wordlist = input("Enter the path to the wordlist file: ")

with open(wordlist, 'r') as f:
    total_bytes = f.seek(0, 2)
    chunk_size = total_bytes // 4

    result = []
    threads = []
    for i in range(4):
        start = i * chunk_size
        end = start + chunk_size - 1
        if i == 3:
            end = total_bytes - 1
        thread = threading.Thread(target=hash_cracker, args=(target_hash, wordlist, start, end, result))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if result:
    print("Password cracked! It is:", result[0])
else:
    print("Unable to crack the password. Better luck next time, you worthless piece of garbage!")

