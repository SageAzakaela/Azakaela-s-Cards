import tkinter as tk
import random

# Sub Syllables
sub_syllables = [
    ("Jak", "Red"), ("Jai", "Orange"), ("Jin", "Yellow"), ("Niin", "Green"),
    ("Osoy", "Blue"), ("Noso", "Violet"), ("Oson", "Magenta"), ("Danath", "Black"),
    ("Nataha", "White"), ("Dantho", "Grey"), ("Imven", "Unseeable"), ("Venai", "Known to All"),
    ("Zul", "None"), ("Ahnd", "One"), ("Daga", "Two"), ("Traga", "Three"),
    ("Veerk", "Four"), ("Vai", "Five"), ("Ess", "Six"), ("Essen", "Seven"),
    ("Oszo", "Eight"), ("Okzo", "Nine"), ("Zulok", "Infinity"), ("Hai", "Close"),
    ("Quax", "Far"), ("Hena", "Here"), ("Drona", "There"), ("Ayix", "Of Sight"),
    ("Erix", "Of Hearing"), ("Orix", "Of Smell"), ("Nakix", "Of Touch"),
    ("Verso", "Young"), ("Krixanth", "Old"), ("Yanid", "Up"), ("Dani", "Down"),
    ("Ixmin", "Center")
]

# Main Syllables
main_syllables = [
    ("Aash", "That which is"), ("Aaz", "That which is not"), ("Iihn", "Self"), ("Ohn", "Other"),
    ("Oos", "Past"), ("Ey", "Present"), ("Ai", "Future"), ("Ker", "Thought"),
    ("Thra", "Action"), ("Vah", "To Witness"), ("Gri", "Form"), ("Dra", "Of Fire"),
    ("Thix", "Of Wind"), ("Naad", "Of Water"), ("Mun", "Of Earth"), ("Iz", "Energy"),
    ("Zol", "Contentment"), ("Yid", "Discontentment"), ("Sver", "Honor"), ("Biz", "Movement"),
    ("Groz", "Directional Forward"), ("Vroz", "Directional Behind"), ("Zran", "Directional Left"),
    ("Dirn", "Directional Right"), ("Vex", "Opposition"), ("Sos", "Alignment"),
    ("Gith", "Small"), ("Vaath", "Large"), ("Jaan", "Ownership"), ("Gix", "Acknowledgment"),
    ("Zor", "Shifting"), ("Roz", "Balanced"), ("Krith", "Many"), ("Vizi", "Few"),
    ("Xo", "Desire"), ("Xa", "Fear")
]

# Emphasis Syllables
emphasis_syllables = [
    ("-Jor", "Augments"), ("-Vez", "Empowers"), ("-Lyn", "Enlightens"),
    ("-Thrum", "Resonates"), ("-Ebon", "Darkens"), ("-Zyr", "Uplifts"),
    ("-Seren", "Calms"), ("-Izer", "Ignites"), ("-Aegis", "Protects"),
    ("-Ker", "Entrances"), ("-Elys", "Transcends"), ("-Daan", "Corrupts")
]

def generate_dragon_sentence(include_sub=True, include_emphasis=True, unions=2):
    sub = random.choice(sub_syllables) if include_sub else None
    mains = random.sample(main_syllables, unions)
    emphasis = random.choice(emphasis_syllables) if include_emphasis else None

    # Form unions with explicit pairing and handle odd syllables
    unions_combined = []
    translations_combined = []

    for i in range(0, len(mains) - 1, 2):  # Step by 2 to group syllables into pairs
        if i + 1 < len(mains):  # Ensure there is a second syllable to pair
            union = mains[i][0] + mains[i + 1][0].lower()
            translation = f"{mains[i][1]} {mains[i + 1][1]}"
        else:
            union = mains[i][0]  # Handle the leftover syllable
            translation = mains[i][1]
        unions_combined.append(union)
        translations_combined.append(translation)

    # Add the final standalone syllable if it's an odd number
    if len(mains) % 2 != 0:
        unions_combined.append(mains[-1][0])
        translations_combined.append(mains[-1][1])

    # Add sub and emphasis syllables
    sentence_parts = []
    if sub:
        sentence_parts.append(f"{sub[0]}-")
    sentence_parts.extend(unions_combined)
    if emphasis:
        sentence_parts.append(emphasis[0])

    dragon_sentence = "".join(sentence_parts)

    # Create translation
    translation_parts = []
    if sub:
        translation_parts.append(sub[1])
    translation_parts.extend(translations_combined)
    if emphasis:
        translation_parts.append(emphasis[1])

    translation = " -> ".join(translation_parts)

    return dragon_sentence, translation


def display_sentence():
    include_sub = sub_var.get()
    include_emphasis = emphasis_var.get()
    unions = union_var.get()

    dragon_sentence, translation = generate_dragon_sentence(
        include_sub=include_sub, include_emphasis=include_emphasis, unions=unions
    )

    for widget in result_frame.winfo_children():
        widget.destroy()

    tk.Label(result_frame, text="Dragon Sentence:", font=("Helvetica", 16, "bold")).pack(pady=10)
    tk.Label(result_frame, text=dragon_sentence, font=("Helvetica", 14)).pack(pady=10)

    tk.Label(result_frame, text="Translation:", font=("Helvetica", 16, "bold")).pack(pady=10)
    tk.Label(result_frame, text=translation, font=("Helvetica", 14)).pack(pady=10)

# Main GUI window
root = tk.Tk()
root.title("Dragon Language Sentence Generator")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

tk.Label(root, text="Dragon Language Generator", font=("Helvetica", 18, "bold")).pack(pady=20)

# Options frame
options_frame = tk.Frame(root)
options_frame.pack(pady=10)

sub_var = tk.BooleanVar(value=True)
tk.Checkbutton(options_frame, text="Include Sub Syllable", variable=sub_var, font=("Helvetica", 12)).grid(row=0, column=0, padx=10)

emphasis_var = tk.BooleanVar(value=True)
tk.Checkbutton(options_frame, text="Include Emphasis Syllable", variable=emphasis_var, font=("Helvetica", 12)).grid(row=0, column=1, padx=10)

union_var = tk.IntVar(value=2)
tk.Label(options_frame, text="Number of Unions:", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5)
union_slider = tk.Scale(options_frame, from_=2, to=4, orient="horizontal", variable=union_var)
union_slider.grid(row=1, column=1, padx=10, pady=5)

# Generate button
tk.Button(root, text="Generate Dragon Sentence", command=display_sentence, font=("Helvetica", 14)).pack(pady=10)

# Result frame
result_frame = tk.Frame(root)
result_frame.pack(fill="both", expand=True)

root.mainloop()
