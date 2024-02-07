
def caffeine():
    caffeine_mg = float(input("Enter the amount of caffeine in mg: "))
    
    half_life_hours = 6
    caffeine_after_6_hours = caffeine_mg / 2
    caffeine_after_12_hours = caffeine_after_6_hours / 2
    caffeine_after_24_hours = caffeine_after_12_hours / 2

    print(f"After 6 hours: {caffeine_after_6_hours:.2f} mg")
    print(f"After 12 hours: {caffeine_after_12_hours:.2f} mg")
    print(f"After 24 hours: {caffeine_after_24_hours:.2f} mg")
    
if __name__ == "__main__":
    caffeine()