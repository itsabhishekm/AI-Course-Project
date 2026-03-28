from problems   import START, PICKUP, DROPOFF, print_grid
from algorithms import RandomAgent, MinConflictsAgent


def run_agent(agent, start, goal, leg_name):
    """
    Runs the agent and prints the path, steps and time taken.
    """
    print(f"\n  {leg_name}: {start}  -->  {goal}")
    path, steps, time_taken, solved = agent.solve(start, goal)

    if solved:
        print("Path has been successfully found :)")
    else:
        print("Could not reach goal within step limit :(")

    print(f"  Steps taken : {steps}")
    print(f"  Time taken  : {time_taken} seconds")
    print_grid(path, pickup=PICKUP, title=leg_name)
    return path, steps, time_taken, solved


def run_full_trip(agent, agent_name):
    """
    The robot makes two trips:
    1) Start (0,0) to Pickup (3,5)
    2) Pickup (3,5) to Dropoff (7,7)
    """
    print(f"\n  Algorithm : {agent_name}")
    print(f"  Start     : {START}")
    print(f"  Pickup    : {PICKUP}")
    print(f"  Dropoff   : {DROPOFF}")

    total_steps = 0
    total_time  = 0.0
    all_solved  = True

    # Start to Pickup
    path1, steps1, time1, solved1 = run_agent(agent, START, PICKUP, "Start to Pickup")
    total_steps += steps1
    total_time  += time1
    if not solved1:
        all_solved = False

    # Pickup to Dropoff
    leg2_start = path1[-1] if path1 else PICKUP
    path2, steps2, time2, solved2 = run_agent(agent, leg2_start, DROPOFF, "Pickup to Dropoff")
    total_steps += steps2
    total_time  += time2
    if not solved2:
        all_solved = False

    print(f"\n  RESULTS — {agent_name}")
    print(f"  Total steps : {total_steps}")
    print(f"  Total time  : {round(total_time, 6)} seconds")
    print(f"  Status      : {'SUCCESS' if all_solved else 'INCOMPLETE'}\n")

    return total_steps, total_time, all_solved


def main():
    print("\n Warehouse Robot Path Planning")
    print(f"  Start   : {START}")
    print(f"  Pickup  : {PICKUP}")
    print(f"  Dropoff : {DROPOFF}")
    print("\n  Choose an algorithm:")
    print("    1 — Random Agent")
    print("    2 — Min-Conflicts Local Search")
    print("    3 — Compare both algorithms")

    choice = input("\n  Enter your choice : ").strip()

    if choice == "1":
        agent = RandomAgent(max_steps=200)
        run_full_trip(agent, "Random Agent")

    elif choice == "2":
        agent = MinConflictsAgent(max_iterations=500)
        run_full_trip(agent, "Min-Conflicts Local Search")

    elif choice == "3":
        print("\n  Running both algorithms for comparison...\n")

        results = {}

        agent = MinConflictsAgent(max_iterations=500)
        steps, t, solved = run_full_trip(agent, "Min-Conflicts Local Search")
        results["Min-Conflicts"] = (steps, t, solved)
        
        agent = RandomAgent(max_steps=200)
        steps, t, solved = run_full_trip(agent, "Random Agent")
        results["Random"] = (steps, t, solved)

        print(f"  COMPARISON TABLE")
        print(f"  {'Algorithm':<30} {'Steps':>6}  {'Time (s)':>10}  {'Solved'}")
        for name, (steps, t, solved) in results.items():
            status = "Yes" if solved else "No"
            print(f"  {name:<30} {steps:>6}  {t:>10.6f}  {status}")

    else:
        print("\n  Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
