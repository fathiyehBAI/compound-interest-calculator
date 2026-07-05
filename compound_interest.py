import matplotlib.pyplot as plt


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("❌ Please enter a number greater than 0.")
            else:
                return value
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("❌ Please enter a number greater than 0.")
            else:
                return value
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")


def calculate_yearly_balances(principal, rate, years):
    rate = rate / 100
    balance = principal
    balances = [principal]
    for year in range(1, years + 1):
        interest = balance * rate
        balance = balance + interest
        balances.append(balance)
    return balances


def simple_calculator():
    print("\n--- Simple Compound Interest Calculator ---\n")
    principal = get_positive_float("Initial investment amount ($): ")
    rate = get_positive_float("Annual interest rate (%, e.g. 20): ")
    years = get_positive_int("Number of years: ")

    balances = calculate_yearly_balances(principal, rate, years)

    print(f"\n{'Year':<10}{'Balance':<20}{'Interest Earned':<20}")
    print("-" * 50)

    for year in range(1, years + 1):
        balance = balances[year]
        interest = balance - balances[year - 1]
        print(f"{year:<10}${balance:<19,.2f}${interest:<19,.2f}")

    print("-" * 50)
    print(f"\nInitial Investment:  ${principal:,.2f}")
    print(f"Final Balance:       ${balances[-1]:,.2f}")
    print(f"Total Profit:        ${balances[-1] - principal:,.2f}")


def compare_scenarios():
    print("\n--- Scenario Comparison ---\n")
    principal = get_positive_float("Initial investment amount ($): ")
    years = get_positive_int("Number of years: ")

    results = []
    all_balances = []
    scenario_number = 1

    print("\nType 0 when you're done entering scenarios.\n")

    while True:
        print(f"Scenario {scenario_number} (or type 0 to finish):")
        rate_input = input("Annual interest rate (%, e.g. 20): ")

        if rate_input == "0":
            break

        try:
            rate = float(rate_input)
            if rate <= 0:
                print("❌ Please enter a number greater than 0.")
                continue
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
            continue

        balances = calculate_yearly_balances(principal, rate, years)
        final_balance = balances[-1]
        profit = final_balance - principal
        results.append((scenario_number, rate, final_balance, profit))
        all_balances.append((scenario_number, rate, balances))
        scenario_number += 1

    if not results:
        print("\n❌ No scenarios entered.")
        return

    print(f"\n{'Scenario':<12}{'Rate':<10}{'Final Balance':<20}{'Total Profit':<20}")
    print("-" * 60)

    for scenario, rate, balance, profit in results:
        rate_str = f"{rate:.1f}%"
        print(f"{scenario:<12}{rate_str:<10}${balance:<19,.2f}${profit:<19,.2f}")

    print("-" * 60)

    best = max(results, key=lambda x: x[2])
    print(f"\n🏆 Best scenario: Scenario {best[0]} with {best[1]}% rate")
    print(f"   Final Balance: ${best[2]:,.2f}")
    print(f"   Total Profit:  ${best[3]:,.2f}")

    show_chart = input("\nWould you like to see the chart? (yes/no): ").strip().lower()
    if show_chart == "yes":
        plot_scenarios(all_balances, years)


def plot_scenarios(all_balances, years):
    x = list(range(0, years + 1))

    plt.figure(figsize=(10, 6))

    for scenario, rate, balances in all_balances:
        plt.plot(x, balances, marker="o", label=f"Scenario {scenario} ({rate:.1f}%)")

    plt.title("Compound Interest Growth by Scenario")
    plt.xlabel("Year")
    plt.ylabel("Balance ($)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()




def show_menu():
    print("\n========================================")
    print("   💰 Compound Interest Calculator 💰   ")
    print("========================================")
    print("  1. Simple Calculation")
    print("  2. Compare Scenarios")
    print("  3. Exit")
    print("========================================")
    return input("Choose an option (1-3): ").strip()


def main():
    print("\nWelcome to the Compound Interest Calculator!")

    while True:
        choice = show_menu()

        if choice == "1":
            simple_calculator()
        elif choice == "2":
            compare_scenarios()
        elif choice == "3":
            print("\n👋 Goodbye! Happy investing!\n")
            break
        else:
            print("❌ Invalid option. Please choose 1, 2, or 3.")


main()