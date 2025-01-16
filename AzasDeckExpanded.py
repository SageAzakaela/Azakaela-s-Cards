import tkinter as tk
import random
from PIL import Image, ImageTk

# Example card entries updated with image paths (update these paths with actual file paths)
cards = [
    ("Black Hole", (1, 1, 1, 1), ["Void", "Absorption", "Endless"], "images/blackhole.png"),
    ("Serpent", (1, 1, 1, 1), ["Wisdom", "Rebirth", "Transformation"], "images/serpent.png"),
    ("Terra", (4, 0, 0, 0), ["Grounding", "Nature", "Strength"], "images/terra.png"),
    ("Sol", (0, 4, 0, 0), ["Light", "Vitality", "Energy"], "images/sol.png"),
    ("Luna", (0, 0, 4, 0), ["Mystery", "Calm", "Reflection"], "images/luna.png"),
    ("Mercurius", (0, 0, 0, 4), ["Communication", "Alchemy", "Speed"], "images/mercurius.png"),
    ("Sahasrara", (0, 0, 0, 0), ["Spirituality", "Connection", "Crown"], "images/sahasrara.png"),
    ("Spirit", (0, 0, 0, 0), ["Essence", "Soul", "Breath"], "images/spirit.png"),
    ("Earth", (4, 0, 0, 0), ["Nature", "Foundation", "Resilience"], "images/earth.png"),
    ("Fire", (0, 4, 0, 0), ["Passion", "Transformation", "Heat"], "images/fire.png"),
    ("Water", (0, 0, 4, 0), ["Flow", "Healing", "Purity"], "images/water.png"),
    ("Air", (0, 0, 0, 4), ["Freedom", "Movement", "Thought"], "images/air.png"),
    ("Cancer", (1, 0, 3, 1), ["Nurture", "Emotion", "Depth"], "images/cancer.png"),
    ("Taurus", (3, 0, 1, 0), ["Strength", "Patience", "Persistence"], "images/taurus.png"),
    ("Pisces", (0, 1, 3, 0), ["Dream", "Compassion", "Mysticism"], "images/pisces.png"),
    ("Virgo", (3, 1, 0, 0), ["Service", "Detail", "Order"], "images/virgo.png"),
    ("Sagittarius", (0, 3, 0, 1), ["Adventure", "Vision", "Freedom"], "images/sagittarius.png"),
    ("Capricorn", (3, 0, 0, 1), ["Discipline", "Ambition", "Legacy"], "images/capricorn.png"),
    ("Gemini", (0, 0, 1, 3), ["Duality", "Adaptability", "Curiosity"], "images/gemini.png"),
    ("Aquarius", (0, 1, 0, 3), ["Innovation", "Individuality", "Reform"], "images/aquarius.png"),
    ("Libra", (1, 0, 0, 3), ["Balance", "Justice", "Harmony"], "images/libra.png"),
    ("Leo", (0, 3, 1, 0), ["Confidence", "Courage", "Pride"], "images/leo.png"),
    ("Scorpio", (0, 1, 3, 0), ["Intensity", "Rebirth", "Secrecy"], "images/scorpio.png"),
    ("Aries", (1, 3, 0, 0), ["Leadership", "Initiative", "Boldness"], "images/aries.png"),
    ("Muladhara", (2, 2, 0, 0), ["Grounding", "Stability", "Survival"], "images/muladhara.png"),
    ("Svadhishthana", (0, 2, 2, 0), ["Desire", "Creativity", "Emotion"], "images/svadhishthana.png"),
    ("Manipura", (2, 0, 0, 2), ["Power", "Will", "Self-Esteem"], "images/manipura.png"),
    ("Anahat", (0, 0, 2, 2), ["Love", "Compassion", "Healing"], "images/anahat.png"),
    ("Vishuddha", (2, 0, 2, 0), ["Expression", "Truth", "Communication"], "images/vishuddha.png"),
    ("Ajnaa", (0, 2, 0, 2), ["Insight", "Perception", "Vision"], "images/ajnaa.png"),
    ("Mars", (2, 2, 0, 0), ["Action", "Conflict", "Force"], "images/mars.png"),
    ("Venus", (0, 2, 2, 0), ["Love", "Beauty", "Harmony"], "images/venus.png"),
    ("Saturn", (2, 0, 0, 2), ["Structure", "Karma", "Discipline"], "images/saturn.png"),
    ("Jupiter", (0, 0, 2, 2), ["Expansion", "Luck", "Wisdom"], "images/jupiter.png"),
    ("Neptune", (2, 0, 2, 0), ["Dreams", "Illusion", "Spirituality"], "images/neptune.png"),
    ("Uranus", (0, 2, 0, 2), ["Change", "Rebellion", "Invention"], "images/uranus.png"),
    ("Cleric", (0, 0, 0, 0), ["Faith", "Healing", "Ritual"], "images/cleric.png"),
    ("Dragon", (1, 1, 1, 1), ["Power", "Mysticism", "Majesty"], "images/dragon.png"),
    ("Spring", (4, 0, 0, 0), ["Growth", "Renewal", "Blossom"], "images/spring.png"),
    ("Summer", (0, 4, 0, 0), ["Energy", "Joy", "Abundance"], "images/summer.png"),
    ("Autumn", (0, 0, 4, 0), ["Harvest", "Reflection", "Transition"], "images/autumn.png"),
    ("Winter", (0, 0, 0, 4), ["Rest", "Solitude", "Endurance"], "images/winter.png"),
    ("Artisan", (0, 2, 0, 2), ["Craft", "Skill", "Invention"], "images/Artisan.png"),
    ("Sage", (2, 0, 2, 0), ["Wisdom", "Teaching", "Philosophy"], "images/Sage.png"),
    ("Server", (0, 0, 2, 2), ["Service", "Support", "Dedication"], "images/Server.png"),
    ("Scholar", (2, 0, 0, 2), ["Knowledge", "Study", "Truth"], "images/Scholar.png"),
    ("Monarch", (0, 2, 2, 0), ["Leadership", "Responsibility", "Command"], "images/Monarch.png"),
    ("Warrior", (2, 2, 0, 0), ["Strength", "Discipline", "Honor"], "images/Warrior.png"),
    ("Raven", (0, 3, 0, 1), ["Mystery", "Message", "Omen"], "images/raven.png"),
    ("Wolf", (0, 0, 3, 1), ["Loyalty", "Instinct", "Pack"], "images/wolf.png"),
    ("Lion", (0, 3, 1, 0), ["Pride", "Courage", "Fierceness"], "images/lion.png"),
    ("Owl", (1, 0, 0, 3), ["Wisdom", "Stealth", "Observation"], "images/owl.png"),
    ("Stag", (3, 0, 0, 1), ["Grace", "Protection", "Majesty"], "images/stag.png"),
    ("Ram", (1, 3, 0, 0), ["Determination", "Charge", "Power"], "images/ram.png"),
    ("Octopus", (0, 1, 3, 0), ["Intelligence", "Flexibility", "Camouflage"], "images/octopus.png"),
    ("Bear", (3, 0, 1, 0), ["Strength", "Protection", "Endurance"], "images/bear.png"),
    ("Frog", (0, 1, 0, 3), ["Adaptation", "Purification", "Change"], "images/frog.png"),
    ("Scorpion", (0, 1, 3, 0), ["Defense", "Venom", "Resilience"], "images/scorpion.png"),
    ("Rabbit", (3, 1, 0, 0), ["Speed", "Fertility", "Gentleness"], "images/rabbit.png"),
    ("Bee", (0, 0, 1, 3), ["Community", "Industry", "Buzz"], "images/bee.png"),
    ("Carnelian", (1, 2, 0, 1), ["Vitality", "Courage", "Motivation"], "images/carnelian.png"),
    ("Peridot", (2, 0, 1, 1), ["Growth", "Renewal", "Protection"], "images/peridot.png"),
    ("Jade", (0, 1, 1, 2), ["Harmony", "Prosperity", "Luck"], "images/jade.png"),
    ("Moonstone", (1, 0, 2, 1), ["Intuition", "Balance", "Cycles"], "images/moonstone.png"),
    ("Tiger's Eye", (1, 2, 1, 0), ["Clarity", "Focus", "Confidence"], "images/tiger's eye.png"),
    ("Kyanite", (2, 1, 1, 0), ["Alignment", "Peace", "Communication"], "images/kyanite.png"),
    ("Lapis Lazuli", (1, 1, 0, 2), ["Vision", "Royalty", "Intellect"], "images/lapislazuli.png"),
    ("Amethyst", (1, 1, 2, 0), ["Calm", "Clarity", "Spirituality"], "images/amethyst.png"),
    ("Turquoise", (0, 2, 1, 1), ["Healing", "Protection", "Wisdom"], "images/turquoise.png"),
    ("Azurite", (2, 1, 0, 1), ["Focus", "Perception", "Insight"], "images/azurite.png"),
    ("Yellow Jasper", (0, 1, 1, 2), ["Courage", "Grounding", "Stability"], "images/yellow jasper.png"),
    ("Aquamarine", (0, 1, 2, 1), ["Calm", "Flow", "Cleansing"], "images/aquamarine.png"),
#     ("Eclipse", (0, 0, 0, 0), ["Obscurity", "Shift", "Shadow"], "images/images.jpg"),
#     ("Eternity", (0, 0, 0, 0), ["Timelessness", "Infinity", "Immortality"], "images/images.jpg"),
#     ("Awareness", (0, 0, 0, 0), ["Perception", "Mindfulness", "Focus"], "images/images.jpg"),
#     ("Awakening", (0, 0, 0, 0), ["Realization", "Rebirth", "Clarity"], "images/images.jpg"),
#     ("Solstice", (1, 1, 1, 1), ["Transition", "Balance", "Celebration"], "images/images.jpg"),
#     ("Equinox", (1, 1, 1, 1), ["Equality", "Balance", "Cycles"], "images/images.jpg"),
#     ("Balance", (1, 1, 1, 1), ["Harmony", "Stability", "Equilibrium"], "images/images.jpg"),
#     ("Prosperity", (1, 1, 1, 1), ["Wealth", "Abundance", "Growth"], "images/images.jpg"),
#     ("Dawn", (4, 0, 0, 0), ["New Beginnings", "Hope", "Light"], "images/images.jpg"),
#     ("Dusk", (0, 0, 0, 4), ["Ending", "Reflection", "Twilight"], "images/images.jpg"),
#     ("Night", (0, 0, 4, 0), ["Mystery", "Rest", "Dream"], "images/images.jpg"),
#     ("Day", (0, 4, 0, 0), ["Clarity", "Life", "Energy"], "images/images.jpg"),
#     ("Past", (0, 0, 0, 4), ["Memory", "Nostalgia", "History"], "images/images.jpg"),
#     ("Present", (4, 0, 0, 0), ["Awareness", "Mindfulness", "Now"], "images/images.jpg"),
#     ("Future", (0, 4, 0, 0), ["Vision", "Hope", "Destiny"], "images/images.jpg"),
#     ("Dreaming", (0, 0, 4, 0), ["Subconscious", "Fantasy", "Imagination"], "images/images.jpg"),
#     ("Vision", (0, 0, 0, 4), ["Sight", "Insight", "Clarity"], "images/images.jpg"),
#     ("Sound", (0, 0, 4, 0), ["Hearing", "Harmony", "Resonance"], "images/images.jpg"),
#     ("Touch", (4, 0, 0, 0), ["Feeling", "Sensation", "Contact"], "images/images.jpg"),
#     ("Savor", (0, 0, 4, 0), ["Taste", "Pleasure", "Enjoyment"], "images/images.jpg"),
#     ("Empathy", (0, 0, 4, 0), ["Compassion", "Understanding", "Connection"], "images/images.jpg"),
#     ("Intuition", (0, 4, 0, 0), ["Hunch", "Perception", "Knowing"], "images/images.jpg"),
#     ("Thought", (0, 0, 0, 4), ["Idea", "Contemplation", "Logic"], "images/images.jpg"),
#     ("Instinct", (4, 0, 0, 0), ["Impulse", "Survival", "Reaction"], "images/images.jpg"),
#     ("Art", (2, 0, 0, 2), ["Creativity", "Expression", "Imagination"], "images/images.jpg"),
#     ("Music", (0, 0, 2, 2), ["Rhythm", "Melody", "Emotion"], "images/images.jpg"),
#     ("Philosophy", (2, 0, 0, 2), ["Wisdom", "Ethics", "Reason"], "images/images.jpg"),
#     ("History", (2, 0, 0, 2), ["Chronicles", "Past", "Legacy"], "images/images.jpg"),
#     ("Action", (2, 2, 0, 0), ["Movement", "Courage", "Force"], "images/images.jpg"),
#     ("Protection", (2, 2, 0, 0), ["Shield", "Defense", "Safety"], "images/images.jpg"),
#     ("Healing", (2, 0, 2, 0), ["Recovery", "Care", "Renewal"], "images/images.jpg"),
#     ("Building", (0, 2, 2, 0), ["Structure", "Creation", "Foundation"], "images/images.jpg"),
#     ("Leadership", (0, 2, 0, 2), ["Guidance", "Inspiration", "Command"], "images/images.jpg"),
#     ("Nurturing", (2, 0, 2, 0), ["Care", "Growth", "Support"], "images/images.jpg"),
#     ("Performance", (0, 2, 0, 2), ["Stage", "Drama", "Expression"], "images/images.jpg"),
#     ("Understanding", (0, 0, 2, 2), ["Comprehension", "Empathy", "Knowledge"], "images/images.jpg"),
#     ("Destiny", (2, 2, 0, 0), ["Fate", "Purpose", "Path"], "images/images.jpg"),
#     ("Memory", (2, 0, 2, 0), ["Recollection", "History", "Past"], "images/images.jpg"),
#     ("Desire", (2, 0, 0, 2), ["Longing", "Ambition", "Wish"], "images/images.jpg"),
#     ("Choice", (0, 2, 2, 0), ["Decision", "Freedom", "Path"], "images/images.jpg"),
#     ("Illusion", (0, 0, 2, 2), ["Deception", "Fantasy", "Mist"], "images/images.jpg"),
#     ("Wish", (0, 2, 2, 0), ["Hope", "Dream", "Aspiration"], "images/images.jpg"),
#     ("Will", (0, 2, 0, 2), ["Determination", "Focus", "Intent"], "images/images.jpg"),
#     ("Fate", (2, 2, 0, 0), ["Destiny", "Inevitability", "Outcome"], "images/images.jpg"),
#     ("Feeling", (2, 0, 2, 0), ["Emotion", "Sensitivity", "Touch"], "images/images.jpg"),
#     ("Ambition", (2, 0, 0, 2), ["Drive", "Goal", "Achievement"], "images/images.jpg"),
#     ("Delusion", (0, 0, 2, 2), ["Fantasy", "Falsehood", "Illusion"], "images/images.jpg"),
#     ("Resolve", (0, 1, 1, 2), ["Determination", "Commitment", "Endurance"], "images/images.jpg"),
#     ("Instinct", (0, 1, 2, 1), ["Reflex", "Impulse", "Survival"], "images/images.jpg"),
#     ("Curiosity", (0, 2, 1, 1), ["Wonder", "Inquiry", "Interest"], "images/images.jpg"),
#     ("Inspiration", (1, 0, 1, 2), ["Spark", "Creativity", "Idea"], "images/images.jpg"),
#     ("Fear", (1, 0, 2, 1), ["Terror", "Anxiety", "Dread"], "images/images.jpg"),
#     ("Love", (1, 1, 0, 2), ["Affection", "Care", "Bond"], "images/images.jpg"),
#     ("Grief", (1, 1, 2, 0), ["Loss", "Sadness", "Mourning"], "images/images.jpg"),
#     ("Hope", (1, 2, 0, 1), ["Aspiration", "Light", "Promise"], "images/images.jpg"), 
#     ("Chaos", (1, 2, 1, 0), ["Disorder", "Unpredictability", "Turmoil"], "images/images.jpg"), 
#     ("Order", (2, 0, 1, 1), ["Structure", "Discipline", "Law"], "images/images.jpg"),
#     ("Harmony", (2, 1, 0, 1), ["Balance", "Peace", "Unity"], "images/images.jpg"), 
#     ("Change", (2, 1, 1, 0), ["Transformation", "Adaptation", "Evolution"], "images/images.jpg")
]

def resize_image(image_path, width=200, height=120):
    """Resize the image to fit the card frame."""
    image = Image.open(image_path)
    image = image.resize((width, height), Image.LANCZOS)  # Use LANCZOS for high-quality downscaling
    return ImageTk.PhotoImage(image)

def draw_card():
    card = random.choice(cards)
    card_name, scores, keywords, image_path = card

    for widget in result_frame.winfo_children():
        widget.destroy()

    # Display card name
    tk.Label(result_frame, text=f"Card: {card_name}", font=("Helvetica", 16, "bold")).pack(pady=10)

    # Display image (if it exists)
    if image_path:
        img = resize_image(image_path)
        img_label = tk.Label(result_frame, image=img)
        img_label.image = img  # Keep a reference to avoid garbage collection
        img_label.pack(pady=10)

    # Display keywords
    tk.Label(result_frame, text="Keywords: " + ", ".join(keywords), font=("Helvetica", 12)).pack()

    # Display scores
    symbols = ["Terra", "Sol", "Luna", "Mercurius"]
    scores_text = "".join([f"{symbols[i]}: {scores[i]}  " for i in range(4)])
    tk.Label(result_frame, text=f"Scores: {scores_text}", font=("Helvetica", 12)).pack()

def draw_three_cards():
    selected_cards = random.sample(cards, 3)

    for widget in result_frame.winfo_children():
        widget.destroy()

    cards_frame = tk.Frame(result_frame)
    cards_frame.pack()

    combined_scores = [0, 0, 0, 0]

    for i, card in enumerate(selected_cards):
        card_name, scores, keywords, image_path = card
        combined_scores = [combined_scores[j] + scores[j] for j in range(4)]

        card_frame = tk.Frame(cards_frame, borderwidth=2, relief="ridge")
        card_frame.grid(row=0, column=i, padx=10)

        tk.Label(card_frame, text=f"Card: {card_name}", font=("Helvetica", 14, "bold")).pack(pady=5)

        if image_path:
            img = resize_image(image_path)
            img_label = tk.Label(card_frame, image=img)
            img_label.image = img
            img_label.pack(pady=5)

        tk.Label(card_frame, text="Keywords: " + ", ".join(keywords), font=("Helvetica", 12)).pack()

        symbols = ["Terra", "Sol", "Luna", "Mercurius"]
        scores_text = "".join([f"{symbols[j]}: {scores[j]}  " for j in range(4)])
        tk.Label(card_frame, text=f"Scores: {scores_text}", font=("Helvetica", 12)).pack(pady=5)

    combined_scores_text = "".join([f"{symbols[j]}: {combined_scores[j]}  " for j in range(4)])
    tk.Label(result_frame, text=f"Combined Scores: {combined_scores_text}", font=("Helvetica", 14, "italic")).pack(pady=10)

# Main GUI window
root = tk.Tk()
root.title("Card Drawer")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

tk.Label(root, text="Random Card Drawer", font=("Helvetica", 18, "bold")).pack(pady=20)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

tk.Button(buttons_frame, text="Draw Card", command=draw_card, font=("Helvetica", 14)).grid(row=0, column=0, padx=10)
tk.Button(buttons_frame, text="Draw Three Cards", command=draw_three_cards, font=("Helvetica", 14)).grid(row=0, column=1, padx=10)

result_frame = tk.Frame(root)
result_frame.pack(fill="both", expand=True)

root.mainloop()
