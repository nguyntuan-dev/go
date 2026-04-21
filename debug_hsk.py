import json
import urllib.request

HSK_DATA_URL = "https://raw.githubusercontent.com/drkameleon/complete-hsk-vocabulary/master/complete.json"

def debug_parse():
    print("Downloading...")
    response = urllib.request.urlopen(HSK_DATA_URL)
    data = json.loads(response.read().decode("utf-8"))
    
    new_hsk = {i: [] for i in range(1, 10)}
    counts_newest = {i: 0 for i in range(1, 10)}
    counts_any = {i: 0 for i in range(1, 10)}
    
    for item in data:
        word = item.get("simplified")
        levels = item.get("level", [])
        
        found_newest = False
        for lvl_str in levels:
            if "newest-" in lvl_str:
                l = int(lvl_str.split("-")[1])
                if word not in new_hsk[l]:
                    new_hsk[l].append(word)
                counts_newest[l] += 1
                found_newest = True
            
            # Count any level match
            try:
                l_any = int(lvl_str.split("-")[1])
                counts_any[l_any] += 1
            except: pass
            
    print("\nResults for 'newest-X' logic:")
    for i in range(1, 10):
        print(f"Level {i}: {len(new_hsk[i])} words (raw count: {counts_newest[i]})")

    print("\nResults for ANY tag logic (newest, new, old):")
    for i in range(1, 10):
        print(f"Level {i}: {counts_any[i]} words")

if __name__ == "__main__":
    debug_parse()
