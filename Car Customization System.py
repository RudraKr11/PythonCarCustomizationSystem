class Car:
    def __init__(self, base_price):
        self.base_price = base_price
        self.total_price = base_price

    def add_option(self, option_price):
        self.total_price += option_price

class Tire:
    def __init__(self, tire_type):
        self.tire_type = tire_type
        self.price = self.get_tire_price()

    def get_tire_price(self):
        if self.tire_type == "regular":
            return 200
        elif self.tire_type == "performance":
            return 400
        elif self.tire_type == "off-road":
            return 600
        else:
            return 0

class Window:
    def __init__(self, window_type):
        self.window_type = window_type
        self.price = self.get_window_price()

    def get_window_price(self):
        if self.window_type == "manual":
            return 300
        elif self.window_type == "automatic":
            return 500
        else:
            return 0

class Paint:
    def __init__(self, color):
        self.color = color
        self.price = self.get_paint_price()

    def get_paint_price(self):
        if self.color == "red":
            return 1000
        elif self.color == "blue":
            return 800
        elif self.color == "black":
            return 1200
        else:
            return 0

class Interior:
    def __init__(self, material):
        self.material = material
        self.price = self.get_interior_price()

    def get_interior_price(self):
        if self.material == "leather":
            return 1500
        elif self.material == "fabric":
            return 1000
        elif self.material == "suede":
            return 2000
        else:
            return 0

class AudioSystem:
    def __init__(self, system_type):
        self.system_type = system_type
        self.price = self.get_audio_price()

    def get_audio_price(self):
        if self.system_type == "basic":
            return 500
        elif self.system_type == "premium":
            return 1000
        elif self.system_type == "luxury":
            return 2000
        else:
            return 0

class Sunroof:
    def __init__(self, has_sunroof):
        self.has_sunroof = has_sunroof
        self.price = self.get_sunroof_price()

    def get_sunroof_price(self):
        if self.has_sunroof:
            return 1000
        else:
            return 0

class NavigationSystem:
    def __init__(self, has_navigation):
        self.has_navigation = has_navigation
        self.price = self.get_navigation_price()

    def get_navigation_price(self):
        if self.has_navigation:
            return 800
        else:
            return 0

class SafetyFeatures:
    def __init__(self, has_safety_features):
        self.has_safety_features = has_safety_features
        self.price = self.get_safety_features_price()

    def get_safety_features_price(self):
        if self.has_safety_features:
            return 1500
        else:
            return 0

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
        self.price = self.get_engine_price()

    def get_engine_price(self):
        if self.engine_type == "standard":
            return 1000
        elif self.engine_type == "turbo":
            return 2000
        elif self.engine_type == "electric":
            return 3000
        else:
            return 0

class BodyKit:
    def __init__(self, model):
        self.model = model
        self.price = self.get_price()

    def get_price(self):
        if self.model == "sport":
            return 1500
        elif self.model == "racing":
            return 2000
        elif self.model == "luxury":
            return 2500
        else:
            return 0

class Spoiler:
    def __init__(self, style):
        self.style = style
        self.price = self.get_price()

    def get_price(self):
        if self.style == "low-profile":
            return 800
        elif self.style == "wing":
            return 1000
        elif self.style == "lip":
            return 600
        else:
            return 0

class AmbientLighting:
    def __init__(self, color):
        self.color = color
        self.price = self.get_price()

    def get_price(self):
        if self.color == "blue":
            return 500
        elif self.color == "red":
            return 600
        elif self.color == "green":
            return 550
        else:
            return 0

class SeatCover:
    def __init__(self, material):
        self.material = material
        self.price = self.get_price()

    def get_price(self):
        if self.material == "leather":
            return 800
        elif self.material == "neoprene":
            return 600
        elif self.material == "cloth":
            return 400
        else:
            return 0

print("Welcome to Car Customization!")

base_price = float(input("Enter the base price of the car: "))

car = Car(base_price)

tire_type = input("Choose tire type (regular, performance, off-road): ")
tire = Tire(tire_type)
car.add_option(tire.price)

window_type = input("Choose window type (manual, automatic): ")
window = Window(window_type)
car.add_option(window.price)

paint_color = input("Choose paint color (red, blue, black): ")
paint = Paint(paint_color)
car.add_option(paint.price)

interior_material = input("Choose interior material (leather, fabric, suede): ")
interior = Interior(interior_material)
car.add_option(interior.price)

audio_system_type = input("Choose audio system type (basic, premium, luxury): ")
audio_system = AudioSystem(audio_system_type)
car.add_option(audio_system.price)

has_sunroof = input("Does it have a sunroof? (yes/no): ").lower() == "yes"
sunroof = Sunroof(has_sunroof)
car.add_option(sunroof.price)

has_navigation = input("Does it have a navigation system? (yes/no): ").lower() == "yes"
navigation_system = NavigationSystem(has_navigation)
car.add_option(navigation_system.price)

has_safety_features = input("Does it have additional safety features? (yes/no): ").lower() == "yes"
safety_features = SafetyFeatures(has_safety_features)
car.add_option(safety_features.price)

engine_type = input("Choose engine type (standard, turbo, electric): ")
engine = Engine(engine_type)
car.add_option(engine.price)

body_kit_model = input("Choose body kit model (sport, racing, luxury): ")
body_kit = BodyKit(body_kit_model)
car.add_option(body_kit.price)

spoiler_style = input("Choose spoiler style (low-profile, wing, lip): ")
spoiler = Spoiler(spoiler_style)
car.add_option(spoiler.price)

ambient_lighting_color = input("Choose ambient lighting color (blue, red, green): ")
ambient_lighting = AmbientLighting(ambient_lighting_color)
car.add_option(ambient_lighting.price)

seat_cover_material = input("Choose seat cover material (leather, neoprene, cloth): ")
seat_cover = SeatCover(seat_cover_material)
car.add_option(seat_cover.price)

print("\nCustomized Car Details:")
print("Base Price: $", base_price)
print("Tire Type: ", tire.tire_type, " - Price: $", tire.price)
print("Window Type: ", window.window_type, " - Price: $", window.price)
print("Paint Color: ", paint.color, " - Price: $", paint.price)
print("Interior Material: ", interior.material, " - Price: $", interior.price)
print("Audio System Type: ", audio_system.system_type, " - Price: $", audio_system.price)
print("Sunroof: ", "Yes" if sunroof.has_sunroof else "No", " - Price: $", sunroof.price)
print("Navigation System: ", "Yes" if navigation_system.has_navigation else "No", " - Price: $", navigation_system.price)
print("Additional Safety Features: ", "Yes" if safety_features.has_safety_features else "No", " - Price: $", safety_features.price)
print("Engine Type: ", engine.engine_type, " - Price: $", engine.price)
print("Body Kit Model: ", body_kit.model, " - Price: $", body_kit.price)
print("Spoiler Style: ", spoiler.style, " - Price: $", spoiler.price)
print("Ambient Lighting Color: ", ambient_lighting.color, " - Price: $", ambient_lighting.price)
print("Seat Cover Material: ", seat_cover.material, " - Price: $", seat_cover.price)
print("Total Price: $", car.total_price)