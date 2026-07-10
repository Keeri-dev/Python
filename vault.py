###### Operator Overloading ######

##### Some operators such as + and - can be "overloaded" such that they can have more abilities beyond arithmetic.
#### In your terminal window, type code vault.py.

### Then, code as follows:

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)

#### Notice how the __str__ method returns a formatted string.
### Further, notice how the __add__ method allows for the addtion of the values of two vaults.
## self is what is on the left of the + operator.
# other is what is right of the +/

