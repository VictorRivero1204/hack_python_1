"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    mapa_palabra = {
        "f": "F",
        "o": "0",
        "z": "Z",
        "i": "1",
        "m": "M",
        "a": "@",
        "n": "N",
    }
    result = [mapa_palabra[char] for char in result]
    return result  

output = fn_hack_10()
print(output)