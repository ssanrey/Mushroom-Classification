import streamlit as st
import joblib
import pandas as pd
import os

# Load the saved model
model_path = os.path.join(os.path.dirname(__file__), "mushroom_model.pkl")
model = joblib.load(model_path)

st.title("🍄 Mushroom Edibility Predictor")
st.write("Select the physical characteristics of your mushroom to find out if it's safe to eat.")

# --- Feature options (from UCI dataset) ---
cap_shape = st.selectbox("Cap Shape", ["bell (b)", "conical (c)", "convex (x)", "flat (f)", "knobbed (k)", "sunken (s)"])
cap_surface = st.selectbox("Cap Surface", ["fibrous (f)", "grooves (g)", "scaly (y)", "smooth (s)"])
cap_color = st.selectbox("Cap Color", ["brown (n)", "buff (b)", "cinnamon (c)", "gray (g)", "green (r)", "pink (p)", "purple (u)", "red (e)", "white (w)", "yellow (y)"])
bruises = st.selectbox("Bruises", ["yes (t)", "no (f)"])
odor = st.selectbox("Odor", ["almond (a)", "anise (l)", "creosote (c)", "fishy (y)", "foul (f)", "musty (m)", "none (n)", "pungent (p)", "spicy (s)"])
gill_attachment = st.selectbox("Gill Attachment", ["attached (a)", "descending (d)", "free (f)", "notched (n)"])
gill_spacing = st.selectbox("Gill Spacing", ["close (c)", "crowded (w)", "distant (d)"])
gill_size = st.selectbox("Gill Size", ["broad (b)", "narrow (n)"])
gill_color = st.selectbox("Gill Color", ["black (k)", "brown (n)", "buff (b)", "chocolate (h)", "gray (g)", "green (r)", "orange (o)", "pink (p)", "purple (u)", "red (e)", "white (w)", "yellow (y)"])
stalk_shape = st.selectbox("Stalk Shape", ["enlarging (e)", "tapering (t)"])
stalk_root = st.selectbox("Stalk Root", ["bulbous (b)", "club (c)", "cup (u)", "equal (e)", "rhizomorphs (z)", "rooted (r)", "unknown"])
stalk_surface_above_ring = st.selectbox("Stalk Surface Above Ring", ["fibrous (f)", "scaly (y)", "silky (k)", "smooth (s)"])
stalk_surface_below_ring = st.selectbox("Stalk Surface Below Ring", ["fibrous (f)", "scaly (y)", "silky (k)", "smooth (s)"])
stalk_color_above_ring = st.selectbox("Stalk Color Above Ring", ["brown (n)", "buff (b)", "cinnamon (c)", "gray (g)", "orange (o)", "pink (p)", "red (e)", "white (w)", "yellow (y)"])
stalk_color_below_ring = st.selectbox("Stalk Color Below Ring", ["brown (n)", "buff (b)", "cinnamon (c)", "gray (g)", "orange (o)", "pink (p)", "red (e)", "white (w)", "yellow (y)"])
veil_color = st.selectbox("Veil Color", ["brown (n)", "orange (o)", "white (w)", "yellow (y)"])
ring_number = st.selectbox("Ring Number", ["none (n)", "one (o)", "two (t)"])
ring_type = st.selectbox("Ring Type", ["cobwebby (c)", "evanescent (e)", "flaring (f)", "large (l)", "none (n)", "pendant (p)", "sheathing (s)", "zone (z)"])
spore_print_color = st.selectbox("Spore Print Color", ["black (k)", "brown (n)", "buff (b)", "chocolate (h)", "green (r)", "orange (o)", "purple (u)", "white (w)", "yellow (y)"])
population = st.selectbox("Population", ["abundant (a)", "clustered (c)", "numerous (n)", "scattered (s)", "several (v)", "solitary (y)"])
habitat = st.selectbox("Habitat", ["grasses (g)", "leaves (l)", "meadows (m)", "paths (p)", "urban (u)", "waste (w)", "woods (d)"])

# --- Extract just the letter code from each selection ---
def extract_code(selection):
    return selection.split("(")[-1].replace(")", "").strip()

input_data = pd.DataFrame([{
    "cap-shape": extract_code(cap_shape),
    "cap-surface": extract_code(cap_surface),
    "cap-color": extract_code(cap_color),
    "bruises": extract_code(bruises),
    "odor": extract_code(odor),
    "gill-attachment": extract_code(gill_attachment),
    "gill-spacing": extract_code(gill_spacing),
    "gill-size": extract_code(gill_size),
    "gill-color": extract_code(gill_color),
    "stalk-shape": extract_code(stalk_shape),
    "stalk-root": extract_code(stalk_root),
    "stalk-surface-above-ring": extract_code(stalk_surface_above_ring),
    "stalk-surface-below-ring": extract_code(stalk_surface_below_ring),
    "stalk-color-above-ring": extract_code(stalk_color_above_ring),
    "stalk-color-below-ring": extract_code(stalk_color_below_ring),
    "veil-color": extract_code(veil_color),
    "ring-number": extract_code(ring_number),
    "ring-type": extract_code(ring_type),
    "spore-print-color": extract_code(spore_print_color),
    "population": extract_code(population),
    "habitat": extract_code(habitat),
}])

# --- Predict ---
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == "p":
        st.error("⚠️ This mushroom is likely POISONOUS. Do not eat it.")
    else:
        st.success("✅ This mushroom is likely EDIBLE.")
    st.warning("Disclaimer: This tool is for educational purposes only. Never eat a wild mushroom based solely on this prediction.")
