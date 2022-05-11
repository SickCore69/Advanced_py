"""
isPalindrome = [lambda string: str: string == string[::-1]]
    
def run(isPalindrome):
    print(f"La palabra " + isPalindrome + "es un palindromo")
"""
def isPalindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def run():
    print(isPalindrome("Anna"))
    

if __name__ == '__main__':
    run()

