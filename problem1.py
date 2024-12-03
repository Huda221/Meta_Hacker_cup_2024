def solve(S: str):
    # """
    # Print one line for each token in S to draw the cookie.

    # S: cookie name
    
    # """
    tokens = []
    i = 0
    while i < len(S):
        if S[i:i+2] == "RE":
            tokens.append("RE")
            i += 2
        elif S[i] == "O":
            tokens.append("O")
            i += 1
        elif S[i] == "&":
            tokens.append("&")
            i += 1
    for token in tokens:
        if token == "O":
            print("[###OREO###]")
        elif token == "RE":
            print("[--------]")
        elif token == "&":
            print("")


def main():
    T = int(input())
    for _ in range(T):
        S = input()
        solve(S)

if __name__ == '__main__':
    main()
