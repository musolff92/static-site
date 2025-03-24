from textnode import TextNode

def main():
    new = TextNode("This is some anchor text", 
                   "link", "https://www.boot.dev/")
    print(new)

main()