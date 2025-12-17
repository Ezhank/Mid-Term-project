import json
import random
import os

CAR_DATA_FILE = 'cars.json'
TARGET_COUNT = 100

MAKES_MODELS = {
    "Toyota": ["Corolla", "Camry", "RAV4", "Highlander", "Prius", "Yaris", "Land Cruiser"],
    "Honda": ["Civic", "Accord", "CR-V", "Pilot", "Fit", "HR-V"],
    "Ford": ["F-150", "Mustang", "Explorer", "Escape", "Focus", "Ranger"],
    "Chevrolet": ["Silverado", "Equinox", "Malibu", "Tahoe", "Bolt EV", "Camaro"],
    "Nissan": ["Altima", "Sentra", "Rogue", "Pathfinder", "Leaf"],
    "BMW": ["3 Series", "5 Series", "X3", "X5", "M3"],
    "Mercedes-Benz": ["C-Class", "E-Class", "GLC", "GLE", "S-Class"],
    "Audi": ["A4", "A6", "Q5", "Q7", "e-tron"],
    "Hyundai": ["Elantra", "Sonata", "Tucson", "Santa Fe", "Ioniq 5"],
    "Kia": ["Forte", "K5", "Sportage", "Sorento", "Telluride"],
    "Tesla": ["Model 3", "Model Y", "Model S", "Model X"],
    "Volkswagen": ["Jetta", "Passat", "Tiguan", "Atlas", "Golf"],
    "Subaru": ["Impreza", "Legacy", "Forester", "Outback", "Crosstrek"],
    "Mazda": ["Mazda3", "Mazda6", "CX-5", "CX-9", "MX-5 Miata"],
    "Lexus": ["IS", "ES", "RX", "NX", "GX"]
}

TYPES = ["Sedan", "SUV", "Truck", "Hatchback", "Coupe", "Convertible", "Minivan"]
FUELS = ["Petrol", "Diesel", "Hybrid", "Electric"]
CONDITIONS = ["New", "Used"]

def load_base_data():
    if os.path.exists(CAR_DATA_FILE):
        with open(CAR_DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def generate_car(id_counter):
    make = random.choice(list(MAKES_MODELS.keys()))
    model = random.choice(MAKES_MODELS[make])
    
    # Heuristic for type based on model name keywords
    car_type = random.choice(TYPES)
    if "Truck" in model or "150" in model or "Silverado" in model: car_type = "Truck"
    elif "SUV" in model or "RAV4" in model or "CR-V" in model or "X5" in model: car_type = "SUV"
    elif "Miata" in model or "Mustang" in model or "Camaro" in model: car_type = "Coupe"

    base_price = 20000
    if make in ["BMW", "Mercedes-Benz", "Audi", "Lexus", "Tesla", "Porsche"]:
        base_price = 45000
    
    price = base_price + random.randint(-5000, 30000)
    if car_type == "SUV": price += 5000
    if car_type == "Truck": price += 10000
    
    fuel = random.choice(FUELS)
    if make == "Tesla" or "Bolt" in model or "Leaf" in model or "e-tron" in model:
        fuel = "Electric"
    
    usage_scores = {
        "City": random.randint(4, 10),
        "Family": random.randint(3, 10),
        "Performance": random.randint(3, 10)
    }
    
    # Adjust scores based on type
    if car_type == "Sedan" or car_type == "Hatchback": usage_scores["City"] = min(10, usage_scores["City"] + 2)
    if car_type == "SUV" or car_type == "Minivan": usage_scores["Family"] = min(10, usage_scores["Family"] + 2)
    if "GT" in model or "Mustang" in model or "Camaro" in model or make in ["Porsche", "BMW", "Tesla"]:
        usage_scores["Performance"] = min(10, usage_scores["Performance"] + 3)

    return {
        "id": id_counter,
        "make": make,
        "model": model,
        "price": price,
        "condition": random.choice(CONDITIONS),
        "fuel": fuel,
        "type": car_type,
        "image": "", # Placeholder will be used by app
        "usage_scores": usage_scores
    }

def main():
    current_data = load_base_data()
    print(f"Current count: {len(current_data)}")
    
    if len(current_data) >= TARGET_COUNT:
        print("Target count already reached.")
        return

    needed = TARGET_COUNT - len(current_data)
    next_id = max([c.get("id", 0) for c in current_data], default=0) + 1
    
    new_cars = []
    for _ in range(needed):
        new_cars.append(generate_car(next_id))
        next_id += 1
        
    final_data = current_data + new_cars
    
    with open(CAR_DATA_FILE, 'w') as f:
        json.dump(final_data, f, indent=4)
        
    print(f"Added {len(new_cars)} new cars. Total count: {len(final_data)}")

if __name__ == "__main__":
    main()
