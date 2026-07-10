
def main():
    text = input("")
    print(convert(text))

def convert(str):
    str=str.replace(":1st_place_medal:","🥇")
    str=str.replace(":money_bag:","💰")
    str=str.replace(":smile_cat:","😸")
    str=str.replace(":candy:","🍬")
    str=str.replace(":ice_cream:","🍨")
    str=str.replace(":thumbsup:","👍")
    str=str.replace(":earth_asia:","hello, 🌏")
    return str

main()
