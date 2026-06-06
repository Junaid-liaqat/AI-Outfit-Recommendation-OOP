

"""
AI Outfit Recommendation System (OOP Prototype)
Author: Junaid Liaqat
Degree: BS Artificial Intelligence
"""

from abc import ABC, abstractmethod

class UserProfile:
    """Manages and encapsulates user profile information."""
    def __init__(self, name: str, gender: str):
        self.__name = name        # Private attribute
        self.__gender = gender    # Private attribute
    
    # Professional Getters
    def get_name(self) -> str:
        return self.__name
        
    def get_gender(self) -> str:
        return self.__gender
    
    def display_user(self):
        print(f"\n[+] Loading profile for User: {self.__name} | Gender: {self.__gender}... 👤")


class OutfitEngine(ABC):
    """Abstract Base Class acting as a blueprint for all recommendation engines."""
    @abstractmethod
    def recommend_style(self, occasion: str):
        pass
        

class SeasonalOutfitEngine(OutfitEngine):
    """Specialized engine that handles recommendations based on seasonal constraints."""
    def __init__(self, season: str):
        self.season = season

    def recommend_style(self, occasion: str):
        current_season = self.season.lower()
        occ = occasion.lower()

        if current_season == "summer":
            if occ == "formal":
                print("-> Summer Formal: Light Linen Shirt with Khaki Chinos! ☀️👔")
            elif occ == "casual":
                print("-> Summer Casual: Breathable Cotton Tee with Shorts! 🩳")
            else:
                print("-> Style tip: Wear what makes you confident! ✨")
            
        elif current_season == "winter":
            if occ == "formal":
                print("-> Winter Formal: Woolen Blazer with Dark Trousers! 🧥")
            elif occ == "casual":
                print("-> Winter Casual: Hoodie with Denim Jacket! ❄️")
            else:
                print("-> Style tip: Wear what makes you confident! ✨")
        else:
            print("-> Alert: Season not recognized. Keeping recommendation generic.")
            print("-> Style tip: Stick to neutral colors and comfortable layers! 👕")


# ==========================================
# DYNAMIC EXECUTION (USER INTERACTION)
# ==========================================
if __name__ == "__main__":
    print("=== Welcome to the AI Outfit Recommendation Prototype ===")
    
    # Taking clean inputs
    user_name = input("Enter your name: ").strip()
    user_gender = input("Enter your gender: ").strip()
    current_season = input("Enter current season (Summer/Winter): ").strip().lower()
    user_occasion = input("Enter occasion (Formal/Casual): ").strip().lower()

    # Object Initialization
    user_profile = UserProfile(user_name, user_gender)
    ai_engine = SeasonalOutfitEngine(current_season)

    # Executing Logic
    user_profile.display_user()
    ai_engine.recommend_style(user_occasion)