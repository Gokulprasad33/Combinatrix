import requests

# Finding all combinations
def combinatrix():
    # Getting input
    frag_size=int(input("Enter number of fragments:"))
    input_set=set()
    fragments_to_join=int(input("Enter number of fragements to be joined"))

    for x in range(frag_size):
        fragment=input("Enter Fragment:").strip()
        input_set.add(fragment)
    # input_set = {"ti", "red", "res", "ed", "an", "le", "ca", "bo", "to", "man", "hu", "cao"}
    print("---------------------------")
    combinations = set()
    
    for x in input_set:
        for y in input_set:
            if x != y:
                combinations.add(x + y)
    if fragments_to_join>1:
        for x in range(fragments_to_join-1):
            for i in input_set:
                for j in combinations:
                    if i not in j:
                        input_set.add(i+j)

    return combinations if combinations else -1

# Word or not
def get_definition(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    response = requests.get(f'{url}{word}')
    return response.status_code == 200

# Filter valid words
def result():
    combi = combinatrix()
    comb_res = set()
    if combi != -1:
        for c in combi:
            if get_definition(c):
                print(f"Valid word found: {c}")
                comb_res.add(c)
    print("---------------------------")
    
    return comb_res

# Main entry point
if __name__ == "__main__":
    valid_words = result()
    print("\nAll valid combinations found:")
    print(valid_words)
