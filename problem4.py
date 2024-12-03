def solve(N: int, H: int, D: int, S: int, P: int) -> float:
    # Time to run the distance
    time_to_run = D / S
    
    # Calculate the total damage taken while running
    damage_taken = P * time_to_run
    
    # If the damage is less than or equal to initial health, you can survive the run
    if N >= damage_taken:
        return time_to_run
    
    # If healing rate is less than or equal to storm damage rate, it's impossible to survive
    if H <= P:
        return -1
    
    # Otherwise, you need to heal
    # Calculate the time needed to heal enough to survive
    time_needed_to_heal = (damage_taken - N) / (H - P)
    
    # The total time is the time to run plus the time needed to heal
    total_time = time_to_run + time_needed_to_heal
    
    return total_time

def main():
    T = int(input())  # Number of test cases
    for _ in range(T):
        N, H, D, S, P = map(int, input().split())  # Read the input for each test case
        result = solve(N, H, D, S, P)
        if result == -1:  # If it's impossible to survive, print -1
            print("-1")
        else:
            print(f"{result:.6f}")  # Print result with 6 decimals

if __name__ == '__main__':
    main()
