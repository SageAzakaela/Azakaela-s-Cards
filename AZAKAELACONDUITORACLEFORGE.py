import tkinter as tk
from tkinter import simpledialog, messagebox
import random
from PIL import Image, ImageTk
import openai

openai.api_key = ""

# Example card entries updated with image paths (update these paths with actual file paths)
cards = [
    ("Black Hole", (1, 1, 1, 1), ["Void", "Absorption", "Endless"], "images/blackhole.png", "Essences"),
    ("Serpent", (1, 1, 1, 1), ["Wisdom", "Rebirth", "Transformation"], "images/serpent.png", "Essences"),
    ("Terra", (4, 0, 0, 0), ["Grounding", "Nature", "Strength"], "images/terra.png", "Planets"),
    ("Sol", (0, 4, 0, 0), ["Light", "Vitality", "Energy"], "images/sol.png", "Planets"),
    ("Luna", (0, 0, 4, 0), ["Mystery", "Calm", "Reflection"], "images/luna.png", "Planets"),
    ("Mercurius", (0, 0, 0, 4), ["Communication", "Alchemy", "Speed"], "images/mercurius.png", "Planets"),
    ("Sahasrara", (0, 0, 0, 0), ["Spirituality", "Connection", "Crown"], "images/sahasrara.png", "Chakras"),
    ("Spirit", (0, 0, 0, 0), ["Essence", "Soul", "Breath"], "images/spirit.png", "Essences"),
    ("Earth", (4, 0, 0, 0), ["Nature", "Foundation", "Resilience"], "images/earth.png", "Elements"),
    ("Fire", (0, 4, 0, 0), ["Passion", "Transformation", "Heat"], "images/fire.png", "Elements"),
    ("Water", (0, 0, 4, 0), ["Flow", "Healing", "Purity"], "images/water.png", "Elements"),
    ("Air", (0, 0, 0, 4), ["Freedom", "Movement", "Thought"], "images/air.png", "Elements"),
    ("Cancer", (1, 0, 3, 1), ["Nurture", "Emotion", "Depth"], "images/cancer.png", "Zodiac Constellations"),
    ("Taurus", (3, 0, 1, 0), ["Strength", "Patience", "Persistence"], "images/taurus.png", "Zodiac Constellations"),
    ("Pisces", (0, 1, 3, 0), ["Dream", "Compassion", "Mysticism"], "images/pisces.png", "Zodiac Constellations"),
    ("Virgo", (3, 1, 0, 0), ["Service", "Detail", "Order"], "images/virgo.png", "Zodiac Constellations"),
    ("Sagittarius", (0, 3, 0, 1), ["Adventure", "Vision", "Freedom"], "images/sagittarius.png", "Zodiac Constellations"),
    ("Capricorn", (3, 0, 0, 1), ["Discipline", "Ambition", "Legacy"], "images/capricorn.png", "Zodiac Constellations"),
    ("Gemini", (0, 0, 1, 3), ["Duality", "Adaptability", "Curiosity"], "images/gemini.png", "Zodiac Constellations"),
    ("Aquarius", (0, 1, 0, 3), ["Innovation", "Individuality", "Reform"], "images/aquarius.png", "Zodiac Constellations"),
    ("Libra", (1, 0, 0, 3), ["Balance", "Justice", "Harmony"], "images/libra.png", "Zodiac Constellations"),
    ("Leo", (0, 3, 1, 0), ["Confidence", "Courage", "Pride"], "images/leo.png", "Zodiac Constellations"),
    ("Scorpio", (0, 1, 3, 0), ["Intensity", "Rebirth", "Secrecy"], "images/scorpio.png", "Zodiac Constellations"),
    ("Aries", (1, 3, 0, 0), ["Leadership", "Initiative", "Boldness"], "images/aries.png", "Zodiac Constellations"),
    ("Muladhara", (2, 2, 0, 0), ["Grounding", "Stability", "Survival"], "images/muladhara.png", "Chakras"),
    ("Svadhishthana", (0, 2, 2, 0), ["Desire", "Creativity", "Emotion"], "images/svadhishthana.png", "Chakras"),
    ("Manipura", (2, 0, 0, 2), ["Power", "Will", "Self-Esteem"], "images/manipura.png", "Chakras"),
    ("Anahat", (0, 0, 2, 2), ["Love", "Compassion", "Healing"], "images/anahat.png", "Chakras"),
    ("Vishuddha", (2, 0, 2, 0), ["Expression", "Truth", "Communication"], "images/vishuddha.png", "Chakras"),
    ("Ajnaa", (0, 2, 0, 2), ["Insight", "Perception", "Vision"], "images/ajnaa.png", "Chakras"),
    ("Mars", (2, 2, 0, 0), ["Action", "Conflict", "Force"], "images/mars.png", "Planets"),
    ("Venus", (0, 2, 2, 0), ["Love", "Beauty", "Harmony"], "images/venus.png", "Planets"),
    ("Saturn", (2, 0, 0, 2), ["Structure", "Karma", "Discipline"], "images/saturn.png", "Planets"),
    ("Jupiter", (0, 0, 2, 2), ["Expansion", "Luck", "Wisdom"], "images/jupiter.png", "Planets"),
    ("Neptune", (2, 0, 2, 0), ["Dreams", "Illusion", "Spirituality"], "images/neptune.png", "Planets"),
    ("Uranus", (0, 2, 0, 2), ["Change", "Rebellion", "Invention"], "images/uranus.png", "Planets"),
    ("Cleric", (0, 0, 0, 0), ["Faith", "Healing", "Ritual"], "images/cleric.png", "Soul Archetypes"),
    ("Dragon", (1, 1, 1, 1), ["Power", "Mysticism", "Majesty"], "images/dragon.png", "Animals"),
    ("Spring", (4, 0, 0, 0), ["Growth", "Renewal", "Blossom"], "images/spring.png", "Time"),
    ("Summer", (0, 4, 0, 0), ["Energy", "Joy", "Abundance"], "images/summer.png", "Time"),
    ("Autumn", (0, 0, 4, 0), ["Harvest", "Reflection", "Transition"], "images/autumn.png", "Time"),
    ("Winter", (0, 0, 0, 4), ["Rest", "Solitude", "Endurance"], "images/winter.png", "Time"),
    ("Artisan", (0, 2, 0, 2), ["Craft", "Skill", "Invention"], "images/Artisan.png", "Soul Archetypes"),
    ("Sage", (2, 0, 2, 0), ["Wisdom", "Teaching", "Philosophy"], "images/Sage.png", "Soul Archetypes"),
    ("Server", (0, 0, 2, 2), ["Service", "Support", "Dedication"], "images/Server.png", "Soul Archetypes"),
    ("Scholar", (2, 0, 0, 2), ["Knowledge", "Study", "Truth"], "images/Scholar.png", "Soul Archetypes"),
    ("Monarch", (0, 2, 2, 0), ["Leadership", "Responsibility", "Command"], "images/Monarch.png", "Soul Archetypes"),
    ("Warrior", (2, 2, 0, 0), ["Strength", "Discipline", "Honor"], "images/Warrior.png", "Soul Archetypes"),
    ("Raven", (0, 3, 0, 1), ["Mystery", "Message", "Omen"], "images/raven.png", "Animals"),
    ("Wolf", (0, 0, 3, 1), ["Loyalty", "Instinct", "Pack"], "images/wolf.png", "Animals"),
    ("Lion", (0, 3, 1, 0), ["Pride", "Courage", "Fierceness"], "images/lion.png", "Animals"),
    ("Owl", (1, 0, 0, 3), ["Wisdom", "Stealth", "Observation"], "images/owl.png", "Animals"),
    ("Stag", (3, 0, 0, 1), ["Grace", "Protection", "Majesty"], "images/stag.png", "Animals"),
    ("Ram", (1, 3, 0, 0), ["Determination", "Charge", "Power"], "images/ram.png", "Animals"),
    ("Octopus", (0, 1, 3, 0), ["Intelligence", "Flexibility", "Camouflage"], "images/octopus.png", "Animals"),
    ("Bear", (3, 0, 1, 0), ["Strength", "Protection", "Endurance"], "images/bear.png", "Animals"),
    ("Frog", (0, 1, 0, 3), ["Adaptation", "Purification", "Change"], "images/frog.png", "Animals"),
    ("Scorpion", (0, 1, 3, 0), ["Defense", "Venom", "Resilience"], "images/scorpion.png", "Animals"),
    ("Rabbit", (3, 1, 0, 0), ["Speed", "Fertility", "Gentleness"], "images/rabbit.png", "Animals"),
    ("Bee", (0, 0, 1, 3), ["Community", "Industry", "Buzz"], "images/bee.png", "Animals"),
    ("Carnelian", (1, 2, 0, 1), ["Vitality", "Courage", "Motivation"], "images/carnelian.png", "Mineral"),
    ("Peridot", (2, 0, 1, 1), ["Growth", "Renewal", "Protection"], "images/peridot.png", "Mineral"),
    ("Jade", (0, 1, 1, 2), ["Harmony", "Prosperity", "Luck"], "images/jade.png", "Mineral"),
    ("Moonstone", (1, 0, 2, 1), ["Intuition", "Balance", "Cycles"], "images/moonstone.png", "Mineral"),
    ("Tiger's Eye", (1, 2, 1, 0), ["Clarity", "Focus", "Confidence"], "images/tiger's eye.png", "Mineral"),
    ("Kyanite", (2, 1, 1, 0), ["Alignment", "Peace", "Communication"], "images/kyanite.png", "Mineral"),
    ("Lapis Lazuli", (1, 1, 0, 2), ["Vision", "Royalty", "Intellect"], "images/lapislazuli.png", "Mineral"),
    ("Amethyst", (1, 1, 2, 0), ["Calm", "Clarity", "Spirituality"], "images/amethyst.png", "Mineral"),
    ("Turquoise", (0, 2, 1, 1), ["Healing", "Protection", "Wisdom"], "images/turquoise.png", "Mineral"),
    ("Azurite", (2, 1, 0, 1), ["Focus", "Perception", "Insight"], "images/azurite.png", "Mineral"),
    ("Yellow Jasper", (0, 1, 1, 2), ["Courage", "Grounding", "Stability"], "images/yellow jasper.png", "Mineral"),
    ("Aquamarine", (0, 1, 2, 1), ["Calm", "Flow", "Cleansing"], "images/aquamarine.png", "Mineral"),
    ("Eclipse", (0, 0, 0, 0), ["Obscurity", "Shift", "Shadow"], "images/images.jpg", "Time"),
    ("Eternity", (0, 0, 0, 0), ["Timelessness", "Infinity", "Immortality"], "images/images.jpg", "Time"),
    ("Awareness", (0, 0, 0, 0), ["Perception", "Mindfulness", "Focus"], "images/images.jpg", "Thought"),
    ("Awakening", (0, 0, 0, 0), ["Realization", "Rebirth", "Clarity"], "images/images.jpg", "Thought"),
    ("Solstice", (1, 1, 1, 1), ["Transition", "Balance", "Celebration"], "images/images.jpg", "Time"),
    ("Equinox", (1, 1, 1, 1), ["Equality", "Balance", "Cycles"], "images/images.jpg", "Time"),
    ("Balance", (1, 1, 1, 1), ["Harmony", "Stability", "Equilibrium"], "images/images.jpg", "Thought"),
    ("Prosperity", (1, 1, 1, 1), ["Wealth", "Abundance", "Growth"], "images/images.jpg", "Thought"),
    ("Dawn", (4, 0, 0, 0), ["New Beginnings", "Hope", "Light"], "images/images.jpg", "Time"),
    ("Dusk", (0, 0, 0, 4), ["Ending", "Reflection", "Twilight"], "images/images.jpg", "Time"),
    ("Night", (0, 0, 4, 0), ["Mystery", "Rest", "Dream"], "images/images.jpg", "Time"),
    ("Day", (0, 4, 0, 0), ["Clarity", "Life", "Energy"], "images/images.jpg", "Time"),
    ("Past", (0, 0, 0, 4), ["Memory", "Nostalgia", "History"], "images/images.jpg", "Time"),
    ("Present", (4, 0, 0, 0), ["Awareness", "Mindfulness", "Now"], "images/images.jpg", "Time"),
    ("Future", (0, 4, 0, 0), ["Vision", "Hope", "Destiny"], "images/images.jpg", "Time"),
    ("Dreaming", (0, 0, 4, 0), ["Subconscious", "Fantasy", "Imagination"], "images/images.jpg", "Thought"),
    ("Vision", (0, 0, 0, 4), ["Sight", "Insight", "Clarity"], "images/images.jpg", "Senses"),
    ("Sound", (0, 0, 4, 0), ["Hearing", "Harmony", "Resonance"], "images/images.jpg", "Senses"),
    ("Touch", (4, 0, 0, 0), ["Feeling", "Sensation", "Contact"], "images/images.jpg", "Senses"),
    ("Savor", (0, 0, 4, 0), ["Taste", "Pleasure", "Enjoyment"], "images/images.jpg", "Senses"),
    ("Empathy", (0, 0, 4, 0), ["Compassion", "Understanding", "Connection"], "images/images.jpg", "Senses"),
    ("Intuition", (0, 4, 0, 0), ["Hunch", "Perception", "Knowing"], "images/images.jpg", "Senses"),
    ("Thought", (0, 0, 0, 4), ["Idea", "Contemplation", "Logic"], "images/images.jpg", "Senses"),
    ("Reaction", (4, 0, 0, 0), ["Impulse", "Survival", "Reaction"], "images/images.jpg", "Senses"),
    ("Art", (2, 0, 0, 2), ["Creativity", "Expression", "Imagination"], "images/images.jpg", "Disciplines"),
    ("Music", (0, 0, 2, 2), ["Rhythm", "Melody", "Emotion"], "images/images.jpg", "Disciplines"),
    ("Philosophy", (2, 0, 0, 2), ["Wisdom", "Ethics", "Reason"], "images/images.jpg", "Disciplines"),
    ("History", (2, 0, 0, 2), ["Chronicles", "Past", "Legacy"], "images/images.jpg", "Disciplines"),
    ("Action", (2, 2, 0, 0), ["Movement", "Courage", "Force"], "images/images.jpg", "Disciplines"),
    ("Protection", (2, 2, 0, 0), ["Shield", "Defense", "Safety"], "images/images.jpg", "Disciplines"),
    ("Healing", (2, 0, 2, 0), ["Recovery", "Care", "Renewal"], "images/images.jpg", "Disciplines"),
    ("Building", (0, 2, 2, 0), ["Structure", "Creation", "Foundation"], "images/images.jpg", "Disciplines"),
    ("Leadership", (0, 2, 0, 2), ["Guidance", "Inspiration", "Command"], "images/images.jpg", "Disciplines"),
    ("Nurturing", (2, 0, 2, 0), ["Care", "Growth", "Support"], "images/images.jpg", "Disciplines"),
    ("Performance", (0, 2, 0, 2), ["Stage", "Drama", "Expression"], "images/images.jpg", "Disciplines"),
    ("Understanding", (0, 0, 2, 2), ["Comprehension", "Empathy", "Knowledge"], "images/images.jpg", "Disciplines"),
    ("Destiny", (2, 2, 0, 0), ["Fate", "Purpose", "Path"], "images/images.jpg", "Time"),
    ("Memory", (2, 0, 2, 0), ["Recollection", "History", "Past"], "images/images.jpg", "Time"),
    ("Desire", (2, 0, 0, 2), ["Longing", "Ambition", "Wish"], "images/images.jpg", "Thought"),
    ("Choice", (0, 2, 2, 0), ["Decision", "Freedom", "Path"], "images/images.jpg", "Thought"),
    ("Illusion", (0, 0, 2, 2), ["Deception", "Fantasy", "Mist"], "images/images.jpg", "Thought"),
    ("Wish", (0, 2, 2, 0), ["Hope", "Dream", "Aspiration"], "images/images.jpg", "Thought"),
    ("Will", (0, 2, 0, 2), ["Determination", "Focus", "Intent"], "images/images.jpg", "Thought"),
    ("Fate", (2, 2, 0, 0), ["Destiny", "Inevitability", "Outcome"], "images/images.jpg", "Thought"),
    ("Feeling", (2, 0, 2, 0), ["Emotion", "Sensitivity", "Touch"], "images/images.jpg", "Thought"),
    ("Ambition", (2, 0, 0, 2), ["Drive", "Goal", "Achievement"], "images/images.jpg", "Emotion"),
    ("Delusion", (0, 0, 2, 2), ["Fantasy", "Falsehood", "Illusion"], "images/images.jpg", "Emotion"),
    ("Resolve", (0, 1, 1, 2), ["Determination", "Commitment", "Endurance"], "images/images.jpg", "Emotion"),
    ("Instinct", (0, 1, 2, 1), ["Reflex", "Impulse", "Survival"], "images/images.jpg", "Emotion"),
    ("Curiosity", (0, 2, 1, 1), ["Wonder", "Inquiry", "Interest"], "images/images.jpg", "Emotion"),
    ("Inspiration", (1, 0, 1, 2), ["Spark", "Creativity", "Idea"], "images/images.jpg", "Emotion"),
    ("Fear", (1, 0, 2, 1), ["Terror", "Anxiety", "Dread"], "images/images.jpg", "Emotion"),
    ("Love", (1, 1, 0, 2), ["Affection", "Care", "Bond"], "images/images.jpg", "Emotion"),
    ("Grief", (1, 1, 2, 0), ["Loss", "Sadness", "Mourning"], "images/images.jpg", "Emotion"),
    ("Hope", (1, 2, 0, 1), ["Aspiration", "Light", "Promise"], "images/images.jpg", "Emotion"), 
    ("Chaos", (1, 2, 1, 0), ["Disorder", "Unpredictability", "Turmoil"], "images/images.jpg", "Essences"), 
    ("Order", (2, 0, 1, 1), ["Structure", "Discipline", "Law"], "images/images.jpg", "Essences"),
    ("Harmony", (2, 1, 0, 1), ["Balance", "Peace", "Unity"], "images/images.jpg", "Essences"), 
    ("Change", (2, 1, 1, 0), ["Transformation", "Adaptation", "Evolution"], "images/images.jpg", "Essences"),
    ("Oracle", (2, 0, 1, 1), ["Prophecy", "Guidance", "Sacred Knowledge"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Warden", (2, 0, 1, 1), ["Protection", "Vigilance", "Justice"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Tempest", (2, 0, 1, 1), ["Chaos", "Power", "Nature's Wrath"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Harbinger", (2, 1, 0, 1), ["Warning", "Catalyst", "Change"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Watcher", (2, 1, 0, 1), ["Observer", "Omniscience", "Vigilance"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Avatar", (2, 1, 0, 1), ["Manifestation", "Power", "Embodiment"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Marauder", (2, 1, 1, 0), ["Conquest", "Ferocity", "Chaos"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Hunter", (2, 1, 1, 0), ["Instinct", "Precision", "Pursuit"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Monolith", (2, 1, 1, 0), ["Eternity", "Power", "Mystery"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Chimera", (2, 0, 0, 2), ["Hybrid", "Mystery", "Duality"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Revenant", (0, 2, 0, 2), ["Resurrection", "Persistence", "Fear"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Phoenix", (0, 2, 1, 1), ["Rebirth", "Renewal", "Flame"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Weaver", (0, 2, 1, 1), ["Destiny", "Interconnection", "Creation"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Siren", (1, 1, 0, 2), ["Seduction", "Danger", "Enchantment"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Keeper", (1, 0, 1, 2), ["Secrets", "Wisdom", "Custodian"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Pilgrim", (1, 0, 2, 1), ["Journey", "Faith", "Transformation"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Beacon", (0, 1, 2, 1), ["Light", "Hope", "Guidance"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Jester", (1, 2, 0, 1), ["Humor", "Chaos", "Subversion"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Herald", (0, 1, 2, 1), ["Message", "Change", "Catalyst"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Shaman", (1, 1, 1, 1), ["Spirit", "Healing", "Connection"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Eidolon", (0, 0, 0, 0), ["Reflection", "Spirit", "Phantom"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Fates", (0, 2, 1, 1), ["Destiny", "Balance", "Cosmic Order"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Trickster", (1, 2, 1, 0), ["Deception", "Wit", "Disruption"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Martyr", (1, 0, 2, 1), ["Sacrifice", "Redemption", "Devotion"], "images/expansion_mythical.png", "Mythological Archetypes"),
    ("Azakaela, The Unfolding", (0, 0, 0, 0), ["Transformation", "Creativity", "Awakening"], "images/aza.png", "UNFOLDING"),
    ("The Conduit", (0, 0, 0, 0), ["Channeling", "Connection", "Flow"], "images/aza.png", "UNFOLDING"),
    ("The Silent Veil", (0, 0, 0, 0), ["Mystery", "Introspection", "Hidden Truths"], "images/aza.png", "UNFOLDING"),
    ("The Shattered Flame", (0, 0, 0, 0), ["Resilience", "Renewal", "Inner Fire"], "images/aza.png", "UNFOLDING"),
    ("The Wounded Will", (0, 0, 0, 0), ["Perseverance", "Strength", "Vulnerability"], "images/aza.png", "UNFOLDING"),
    ("The Hidden Wound", (0, 0, 0, 0), ["Healing", "Shadows", "Revelation"], "images/aza.png", "UNFOLDING"),
    ("The Goddess of Secrets", (0, 0, 0, 0), ["Wisdom", "Enigma", "Omniscience"], "images/aza.png", "UNFOLDING"),
    ("The Dragon of Secrets", (0, 0, 0, 0), ["Guardianship", "Ancient Knowledge", "Cosmic Power"], "images/aza.png", "UNFOLDING"),
    ("The Crown of Poison Flower", (0, 0, 0, 0), ["Sacrifice", "Bloom", "Duality"], "images/aza.png", "UNFOLDING"),
    ("The Fountain of Tranquility", (0, 0, 0, 0), ["Serenity", "Balance", "Renewal"], "images/aza.png", "UNFOLDING"),
    ("The Unrelenting", (0, 0, 0, 0), ["Determination", "Defiance", "Courage"], "images/aza.png", "UNFOLDING"),
    ("That Which Is", (0, 0, 0, 0), ["Existence", "Reality", "Presence"], "images/aza.png", "Constants"),
    ("That Which Is Not", (0, 0, 0, 0), ["Void", "Absence", "Negation"], "images/aza.png", "Constants"),
    ("Above", (0, 0, 0, 0), ["Transcendence", "Elevation", "Oversight"], "images/aza.png", "Constants"),
    ("Below", (0, 0, 0, 0), ["Foundation", "Depth", "Substance"], "images/aza.png", "Constants"),
    ("Light", (0, 0, 0, 0), ["Illumination", "Hope", "Revelation"], "images/aza.png", "Constants"),
    ("Dark", (0, 0, 0, 0), ["Mystery", "Shadows", "Potential"], "images/aza.png", "Constants"),
    ("Within", (0, 0, 0, 0), ["Introspection", "Essence", "Containment"], "images/aza.png", "Constants"),
    ("Without", (0, 0, 0, 0), ["Expanse", "Freedom", "Emptiness"], "images/aza.png", "Constants"),
    ("Creator", (0, 0, 0, 0), ["Genesis", "Imagination", "Will"], "images/aza.png", "Constants"),
    ("Creation", (0, 0, 0, 0), ["Manifestation", "Innovation", "Art"], "images/aza.png", "Constants"),
    ("Everything", (0, 0, 0, 0), ["Unity", "All-Encompassing", "Wholeness"], "images/aza.png", "Constants"),
    ("Nothingness", (0, 0, 0, 0), ["Transformation", "Cycle of Being", "Mystery"], "images/aza.png", "Constants"),
    ("The Center", (0, 0, 0, 0), ["Balance", "Stillness", "Origin"], "images/aza.png", "Constants"),
]
selected_sets = set()  # To store active sets
selected_cards = []

def set_api_key():
    """Open a dialog to set the API key."""
    global api_key
    key = simpledialog.askstring("Set API Key", "Enter your OpenAI API Key:", show="*")
    if key:
        api_key = key
        messagebox.showinfo("API Key Set", "The API key has been set successfully.")


def generate_interpretation():
    global api_key
    if not api_key:
        messagebox.showerror("Missing API Key", "Please set the OpenAI API Key in the settings before proceeding.")
        return

    question = question_entry.get()
    if not question:
        tk.Label(result_frame, text="Please enter a question.", font=("Helvetica", 12, "italic"), fg="red").pack()
        return

    if not selected_cards:
        tk.Label(result_frame, text="No cards selected for interpretation.", font=("Helvetica", 12, "italic"), fg="red").pack()
        return

    # Collect selected styles and focuses
    selected_styles = [style for style, var in style_options.items() if var.get()]
    selected_focus = [focus for focus, var in focus_options.items() if var.get()]

    # Define tone and focus-specific guidance
    tone_guidance = {
        "Embrace Darkness": "Be open to discussing challenges, negative outcomes, or warnings.",
        "Realistic": "Focus on practical, grounded advice and interpretations.",
        "Mystical": "Use poetic, abstract, and esoteric language.",
        "Short": "Keep the reading concise and to the point.",
        "Funny": "Incorporate humor and wit into the interpretation.",
        "Ask Questions": "Pose questions to the user to deepen their reflection."
    }

    focus_guidance = {
        "People": "Relate the cards to individuals, relationships, or archetypes.",
        "Places": "Interpret the cards as environments, locations, or states of being.",
        "Things": "Describe the cards as objects, goals, or tangible elements.",
        "Career": "Focus on work, goals, or professional development.",
        "Relationships": "Center the reading on interpersonal connections or emotional dynamics.",
        "Spirituality": "Highlight spiritual growth, higher purpose, or cosmic alignment.",
        "Health": "Concentrate on physical, mental, or emotional well-being."
    }

    # Generate style and focus directives
    style_directives = " ".join([tone_guidance.get(style, "") for style in selected_styles])
    focus_directives = " ".join([focus_guidance.get(focus, "") for focus in selected_focus])

    # Define what each category represents
    category_meanings = {
        "Terra": "Material matters, grounding, physical reality, and resources.",
        "Sol": "Spiritual matters, vitality, purpose, and higher consciousness.",
        "Luna": "Emotions, relationships, intuition, and the subconscious.",
        "Mercurius": "Communication, intellect, mental agility, and ideas."
    }

    # Calculate the combined scores for each category
    combined_scores = {"Terra": 0, "Sol": 0, "Luna": 0, "Mercurius": 0}
    for card in selected_cards:
        combined_scores["Terra"] += card[1][0]
        combined_scores["Sol"] += card[1][1]
        combined_scores["Luna"] += card[1][2]
        combined_scores["Mercurius"] += card[1][3]

    # Prepare the prompt for the GPT model
    prompt = f"""
    You are the Oracle Forge, a tarot-like card interpreter built by Azakaela, The Unfolding. Here are the drawn cards and their information:
    {[{"name": card[0], "keywords": card[2], "scores": card[1]} for card in selected_cards]}
    
    The combined scores for each category are:
    Terra (Material Matters): {combined_scores['Terra']}
    Sol (Spiritual Matters): {combined_scores['Sol']}
    Luna (Emotional/Relationships): {combined_scores['Luna']}
    Mercurius (Communication/Mind): {combined_scores['Mercurius']}
    
    The meanings of the categories are:
    - Terra: {category_meanings['Terra']}
    - Sol: {category_meanings['Sol']}
    - Luna: {category_meanings['Luna']}
    - Mercurius: {category_meanings['Mercurius']}
    
    The user's question is: "{question}".
    Your interpretation should adhere to the following:
    - Tone: {style_directives}
    - Focus: {focus_directives}
    
    Please interpret the scores and the card symbolism (denoted by their keywords) in the context of the user's question, reflecting the tone and focus described.
    """

    # Call GPT-4 API
    try:
        openai.api_key = api_key  # Set the API key dynamically
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a tarot-like card interpreter."},
                {"role": "user", "content": prompt}
            ]
        )
        interpretation = response['choices'][0]['message']['content']

        # Display the interpretation in a popout window
        popout = tk.Toplevel(root)
        popout.title("Interpretation")
        popout.geometry("600x400")

        tk.Label(popout, text="Interpretation", font=("Helvetica", 14, "bold")).pack(pady=10)
        text_widget = tk.Text(popout, wrap="word", font=("Helvetica", 10), bg="white", relief="flat")
        text_widget.insert("1.0", interpretation)
        text_widget.configure(state="disabled")
        text_widget.pack(pady=10, padx=10, fill="both", expand=True)

    except Exception as e:
        tk.Label(result_frame, text=f"Error: {e}", font=("Helvetica", 12, "italic"), fg="red").pack()



def resize_image(image_path, width=200, height=120):
    """Resize the image to fit the card frame."""
    image = Image.open(image_path)
    image = image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(image)


def filter_cards():
    """Return cards filtered by selected sets."""
    if not selected_sets:  # If no sets are selected, include all cards
        return cards
    return [card for card in cards if card[4] in selected_sets]

def draw_card():
    global selected_cards  # Ensure we're updating the global variable
    filtered_cards = filter_cards()
    if not filtered_cards:
        return

    # Select a single card (allow duplicates if "Allow Multiple" is checked)
    if allow_multiple.get():
        selected_cards = [random.choice(filtered_cards)]
    else:
        selected_cards = [random.choice(filtered_cards) for _ in range(1) if filtered_cards]

    # Get details of the selected card
    card_name, scores, keywords, image_path, _ = selected_cards[0]

    # Clear the result frame
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


def draw_multiple_cards(num_cards):
    global selected_cards
    filtered_cards = filter_cards()
    if len(filtered_cards) < num_cards and not allow_multiple.get():
        return

    if allow_multiple.get():
        selected_cards = [random.choice(filtered_cards) for _ in range(num_cards)]  # Allow duplicates
    else:
        selected_cards = random.sample(filtered_cards, num_cards)  # No duplicates

    for widget in result_frame.winfo_children():
        widget.destroy()

    cards_frame = tk.Frame(result_frame)
    cards_frame.pack()

    combined_scores = [0, 0, 0, 0]

    for i, card in enumerate(selected_cards):
        card_name, scores, keywords, image_path, _ = card
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

def toggle_set(set_name):
    """Toggle a set's active status."""
    if set_name in selected_sets:
        selected_sets.remove(set_name)
    else:
        selected_sets.add(set_name)


# Main GUI window
root = tk.Tk()
root.title("Card Drawer")

# Add a menu for settings
menu = tk.Menu(root)
root.config(menu=menu)

settings_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Settings", menu=settings_menu)
settings_menu.add_command(label="Set API Key", command=set_api_key)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

tk.Label(root, text="Random Card Drawer", font=("Helvetica", 18, "bold")).pack(pady=20)

# Set selection
set_frame = tk.Frame(root)
set_frame.pack()

sets = [
    "Essences", "Chakras", "Elements", "Planets", "Zodiac Constellations", 
    "Mythological Archetypes", "Soul Archetypes", "Thought", "Time", 
    "Emotion", "Senses", "Animals", "Mineral", "Disciplines", "UNFOLDING", "Constants"

]

for i, set_name in enumerate(sets):
    var = tk.BooleanVar()
    tk.Checkbutton(set_frame, text=set_name, variable=var,
                   command=lambda sn=set_name: toggle_set(sn)).grid(row=i // 4, column=i % 4, sticky="w", padx=10)


buttons_frame = tk.Frame(root)
buttons_frame.pack()
# Add a global variable to track "Allow Multiple" setting
allow_multiple = tk.BooleanVar()

# Add the "Allow Multiple" checkbox to the buttons_frame
tk.Checkbutton(
    buttons_frame,
    text="Allow Multiple",
    variable=allow_multiple,
    font=("Helvetica", 12)
).grid(row=1, column=0, columnspan=3, pady=10)

    
question_frame = tk.Frame(root)
question_frame.pack(pady=10)

tk.Label(question_frame, text="Enter your question:", font=("Helvetica", 12)).pack(side="left", padx=10)
question_entry = tk.Entry(question_frame, width=50)
question_entry.pack(side="left", padx=10)

# Add a frame for interpretation styles
styles_frame = tk.Frame(root)
styles_frame.pack(pady=10)

tk.Label(styles_frame, text="Select interpretation style:", font=("Helvetica", 12)).pack(side="left", padx=10)

style_options = {
    "Ask Questions": tk.BooleanVar(),
    "Realistic": tk.BooleanVar(),
    "Embrace Darkness": tk.BooleanVar(),
    "Mystical": tk.BooleanVar(),
    "Short": tk.BooleanVar(),
    "Funny": tk.BooleanVar()
}

for style, var in style_options.items():
    tk.Checkbutton(styles_frame, text=style, variable=var).pack(side="left", padx=5)

# Add a frame for focus options
focus_frame = tk.Frame(root)
focus_frame.pack(pady=10)

tk.Label(focus_frame, text="Select focus of the reading:", font=("Helvetica", 12)).pack(side="left", padx=10)

focus_options = {
    "People": tk.BooleanVar(),
    "Places": tk.BooleanVar(),
    "Things": tk.BooleanVar(),
    "Career": tk.BooleanVar(),
    "Relationships": tk.BooleanVar(),
    "Spirituality": tk.BooleanVar(),
    "Health": tk.BooleanVar()
}

for focus, var in focus_options.items():
    tk.Checkbutton(focus_frame, text=focus, variable=var).pack(side="left", padx=5)

# Buttons for card drawing
buttons_frame = tk.Frame(root)
buttons_frame.pack()

tk.Button(buttons_frame, text="Draw Card", command=draw_card, font=("Helvetica", 14)).grid(row=0, column=0, padx=10)
tk.Button(buttons_frame, text="Draw Three Cards", command=lambda: draw_multiple_cards(3), font=("Helvetica", 14)).grid(row=0, column=1, padx=10)
tk.Button(buttons_frame, text="Draw Five Cards", command=lambda: draw_multiple_cards(5), font=("Helvetica", 14)).grid(row=0, column=2, padx=10)

result_frame = tk.Frame(root)
result_frame.pack(fill="both", expand=True)

tk.Button(root, text="Generate Interpretation", command=generate_interpretation, font=("Helvetica", 14)).pack(pady=10)


root.mainloop()
