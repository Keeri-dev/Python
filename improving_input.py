#while True:
    #n = int(input("What's n? "))
    #if n < 0:
        #continue
    #else:
        #break

# Turns out the continue keyword is redundant in this case

# Can improve code as follows
#while True:
    #n = int(input("What's n? "))
    #if n > 0:
        #break

#for _ in range(n):
    #print("meow")

# We can use functions to further improve our code
def main():
    meow(get_number())

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow():
    for _ in range(n):
        print("meow")

main()
