import os
import pandas as pd
import gradio as gr
from groq import Groq
from datasets import load_dataset

ds = load_dataset("sowmya14/agriculture_QA")

# Initialize Groq API
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Use environment variable for security
client = Groq(api_key="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")

# Global variable for dataset
df = None

def load_data(file):
    """Load CSV file and display first few rows."""
    global df
    df = pd.read_csv(file.name)
    
    if "ID" not in df.columns:
        return "Error: 'ID' column missing. Ensure your dataset has an 'ID' column."
    
    return f"Dataset loaded successfully! {len(df)} records found."

def get_available_ids():
    """Return list of available IDs for dropdown selection."""
    if df is None:
        return []
    return df["ID"].astype(str).tolist()

def get_land_data(land_id):
    """Fetch land details based on ID."""
    if df is None:
        return "Please upload a dataset first."
    
    land_data = df[df["ID"] == int(land_id)]
    if land_data.empty:
        return "ID not found. Please enter a valid land ID."
    
    return land_data.to_dict(orient="records")[0]

def generate_insights(land_id):
    """Generate AI insights for a given land ID using Groq API."""
    land_info = get_land_data(land_id)
    
    if isinstance(land_info, str):  # If error message
        return land_info

    # Format prompt for Groq API
    prompt = f"""
    Given the following agricultural data, provide insights on soil quality, crop health, 
    and estimated yield for the land:
    - Soil Quality: {land_info['Soil_Quality']}
    - Seed Variety: {land_info['Seed_Variety']}
    - Fertilizer Amount: {land_info['Fertilizer_Amount_kg_per_hectare']} kg/ha
    - Sunny Days: {land_info['Sunny_Days']} days
    - Rainfall: {land_info['Rainfall_mm']} mm
    - Irrigation Schedule: {land_info['Irrigation_Schedule']}
    Provide an estimated yield and recommendations for better crop health.
    """

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )

    return response.choices[0].message.content

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 🌾 AI-Powered Crop Yield Prediction 🚜")
    gr.Markdown("Upload your agricultural dataset, select an ID, and get AI-driven insights!")

    # Upload CSV
    file_upload = gr.File(label="Upload your CSV file", file_types=[".csv"])
    file_status = gr.Textbox(label="File Status", interactive=False)

    # Dropdown for ID Selection
    with gr.Row():
        id_dropdown = gr.Dropdown(label="Select Land ID", choices=[], interactive=True)
        refresh_button = gr.Button("Refresh IDs")

    # Predict Button
    predict_button = gr.Button("Get Insights")
    output_box = gr.Textbox(label="AI Insights & Yield Prediction", interactive=False)

    # Functions to update UI
    file_upload.change(load_data, inputs=[file_upload], outputs=[file_status])
    refresh_button.click(lambda: get_available_ids(), outputs=[id_dropdown])
    predict_button.click(generate_insights, inputs=[id_dropdown], outputs=[output_box])

# Launch App
if __name__ == "__main__":
    demo.launch()