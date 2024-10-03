import json

class Card:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __repr__(self):
        return f"Card(name='{self.name}', category='{self.category}')"

class CardCollection:
    def __init__(self):
        self.cards = []

    def load_from_json(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for item in data:
                    card = Card(item['name'], item['category'])
                    self.cards.append(card)
        except FileNotFoundError:
            print(f"Soubor {filename} nebyl nalezen.")
        except json.JSONDecodeError:
            print(f"Chyba při čtení JSON souboru {filename}.")

    def __str__(self):
        """Zobrazí všechny karty a jejich kategorie."""
        if not self.cards:
            return "Žádné karty nejsou dostupné."

        categories = {}
        for card in self.cards:
            if card.category not in categories:
                categories[card.category] = []
            categories[card.category].append(card.name)

        result = []
        for category, card_names in categories.items():
            result.append(f"Kategorie: {category}")
            for name in card_names:
                result.append(f"  - {name}")
        
        return "\n".join(result)

collection = CardCollection()
collection.load_from_json('cards.json')

print(collection)
