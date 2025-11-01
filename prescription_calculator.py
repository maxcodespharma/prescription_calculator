# Prescription Calculator Tool
# Portforlio Project #2
# Created October 27, 2025
# Author: Max S. 
from datetime import datetime

print("=" * 60)
print("        PRESCRIPTION CALCULATOR v1.0")
print("=" * 60)
print()
print("Calculate rx details including:")
print("  • Total quantity needed")
print("  • Rx sig (directions)")
print("  • Days supply verification")
print("  • Total cost estimation")
print()
print("Enter 'done' when finished to see summary.")
print("=" * 60)

# Store prescription in a list for summary
prescriptions = []

# Function to calculate days supply
def calculate_days_supply(total_quantity, tablets_per_day):
    """
    Calculate how many days a prescription will last
    
    Parameters:
    - total_quantity: Total number of tablets
    - tablets_per_day: Number of tablets taken per day
    
    Returns: Number of days supply
    """
    return total_quantity / tablets_per_day

# Function to calculate total quantity needed
def calculate_quantity_needed(tablets_per_dose, doses_per_day, days_supply):
    """
    Calculate total tablets needed for prescription
    
    Parameters: 
    - tablets_per_dose: Tablets taken each dose
    - doses_per_day: Number of doses per day
    - days_supply: How many days prescription should last
    
    Returns: Total tablets needed
    """
    return tablets_per_dose * doses_per_day * days_supply

# Function to generate sig (rx directions)
def generate_sig(tablets_per_dose, frequency):
    """
    Generate rx sig (directions)
    
    Parameters: 
    - tablets_per_dose: Number of tablets per dose
    - frequency: How often (e.g., "twice daily", "every 6 hours")
    
    Returns: Formatted sig string
    """
    if tablets_per_dose == 1:
        return f"Take 1 tablet {frequency}"
    else: 
        return f"Take {tablets_per_dose} tablets {frequency}"

# Function to calculate cost
def calculate_cost(quantity, cost_per_tablet):
    """
    Calculate total rx cost
    
    Parameters:
    - quantity: Total # of tablets
    - cost_per_tablet: Cost per tablet in dollars
    
    Returns: Total cost
    """
    return round(quantity * cost_per_tablet, 2)

def save_prescriptions_to_file(prescriptions, total_cost):
    """
    Save prescription summary to text file
    
    Parameters:
    - prescriptions: List of prescription dictionaries
    - total_cost: Grand total cost of all prescriptions
    """
    # Create filename with today's date
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"prescription_summary_{today}.txt"

    try:
        with open(filename, "w") as f:
            # Write header
            f.write ("=" * 60 + "\n")
            f.write("        PRESCRIPTION SUMMARY\n")
            f.write("=" * 60 + "\n")
            f.write(f"Date: {today}\n")
            f.write(f"Total Prescriptions: {len(prescriptions)}\n")
            f.write("\n")

            # Write each rx
            for i, rx in enumerate(prescriptions, 1):
                f.write(f"#{i}. {rx['drug']} {rx['strength']}\n")
                f.write(f"    Sig: {rx['sig']}\n")
                f.write(f"    Quantity: {rx['quantity']} tablets\n")
                f.write(f"    Days Supply: {rx['days_supply']} days\n")
                f.write(f"    Cost: ${rx['cost']:.2f}\n")
                f.write("\n")

            # Write total
            f.write("=" * 60 + "\n")
            f.write(f"TOTAL COST FOR ALL PRESCRIPTIONS: ${total_cost:.2f}\n")
            f.write("=" * 60 + "\n")

        return filename # Return filename so we can tell user
    
    except Exception as e:
        return None # Return none is something went wrong



# Main loop - allow multiple prescriptions
while True: 
    print("\n" + "=" * 60)
    print("        INTERACTIVE RX CALCULATOR")
    print("=" * 60)
    print()

    try:
        # Get prescription information from user
        drug_name = input("Enter drug name (or 'done' to finish): ").strip().title()

        # Check if user wants to quit
        if drug_name.lower() == 'done':
            break  # Exit loop immediately
        
        if not drug_name:
            print("❌ Error: Drug name cannot be empty")
            continue

        strength = input("Enter strength (e.g., '500mg', '10mg'): ").strip()
        tablets_per_dose = int(input("Tablets per dose: "))
        doses_per_day = int(input("Doses per day: "))
        days_supply = int(input("Days supply: "))
        cost_per_tablet = float(input("Cost per tablet ($): "))

        # Validation
        if tablets_per_dose <= 0 or doses_per_day <= 0 or days_supply <= 0:
            print("❌ Error: Values must be greater than 0")
            continue
        elif cost_per_tablet < 0:
            print("❌ Error: Cost cannot be negative")
            continue

        # Calculate everything
        total_quantity = calculate_quantity_needed(tablets_per_dose, doses_per_day, days_supply)

        # Determine frequency for sig
        if doses_per_day == 1: 
            frequency = "once daily"
        elif doses_per_day == 2:
            frequency = "twice daily"
        elif doses_per_day == 3:
            frequency = "three times daily"
        elif doses_per_day == 4:
            frequency = "four times daily"
        else: 
            frequency = f"{doses_per_day} times daily"
        
        sig = generate_sig(tablets_per_dose, frequency)
        total_cost = calculate_cost(total_quantity, cost_per_tablet)

        # Store rx data
        rx_data = {
            'drug': drug_name,
            'strength': strength,
            'sig': sig,
            'quantity': total_quantity,
            'days_supply': days_supply,
            'cost': total_cost
        }
        prescriptions.append(rx_data)

        # Display rx
        print("\n" + "=" * 60)
        print("        PRESCRIPTION DETAILS")
        print("=" * 60)
        print(f"Drug: {drug_name} {strength}")
        print(f"Sig: {sig}")
        print(f"Quantity: {total_quantity} tablets")
        print(f"Days Supply: {days_supply} days")
        print(f"Cost: ${total_cost:.2f}")
        print("=" * 60)
        print("\n✅ Prescription added!")

    except ValueError:
        print("❌ Error: Please enter valid numbers for quantity, doses, days, and cost")
        continue

# AFTER the loop ends (OUTSIDE the while loop), add the summary:
if prescriptions:
    print("\n" + "=" * 60)
    print("        PRESCRIPTION SUMMARY")
    print("=" * 60)
    print(f"\nTotal Prescriptions: {len(prescriptions)}")
    print()

    grand_total_cost = 0

    for i, rx in enumerate(prescriptions, 1):
        print(f"#{i}. {rx['drug']} {rx['strength']}")
        print(f"    Sig: {rx['sig']}")
        print(f"    Quantity: {rx['quantity']} tablets")
        print(f"    Days Supply: {rx['days_supply']} days")
        print(f"    Cost: ${rx['cost']}")
        print()
        grand_total_cost += rx['cost']
    
    print("=" * 60)
    print(f"TOTAL COST FOR ALL PRESCRIPTIONS: ${grand_total_cost:.2f}")
    print("=" * 60)
    print()
    save_choice = input("💾 Save this summary to file? (yes/no): ").lower().strip()

    if save_choice in ['yes', 'y']:
        filename = save_prescriptions_to_file(prescriptions, grand_total_cost)

        if filename:
            print(f"\n✅ Prescriptions saved to: {filename}")
            print(f"📁 File location: {filename}")
        else:
            print("\n❌ Error: Could not save file")
    
    else:
        print("\n📋 Summary not saved")
        
else: 
    print("\nNo prescriptions entered.")

print("\n✅ Calculator closed. Good work boss.")

