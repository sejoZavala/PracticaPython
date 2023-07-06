def are_you_playing_banjo(name):
    if len(name) > 0:
        print(name.lower())
        if name.lower().startswith('r',0):
            return name + " plays banjo" 
            
    return name + " does not play banjo"

if __name__ == "__main__":
    print(are_you_playing_banjo("martin")) # "martin does not play banjo"
    print(are_you_playing_banjo("Rikke"))  # "Rikke plays banjo"
    print(are_you_playing_banjo("bravo"))  # "bravo does not play banjo"
    print(are_you_playing_banjo("rolf"))   # "rolf plays banjo"