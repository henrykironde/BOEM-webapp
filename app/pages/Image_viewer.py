import streamlit as st
from pathlib import Path
from PIL import Image
from utils.styling import load_css
import pandas as pd

# Must be the first Streamlit command
st.set_page_config(
    page_title="Image Viewer",
    page_icon="🖼️",
    layout="wide"
)

def app():
    st.title("Model Prediction Viewer")
    
    try:
        # Get experiment data
        image_df = pd.read_csv("app/data/most_recent_all_flight_predictions.csv")
        if image_df is None:
            st.warning("No images found in experiments")
            return
            
        # Get unique species
        species_list = sorted(image_df['label'].unique())
        
        # Use standard Streamlit selector with USWDS styling
        selected_species = st.selectbox(
            "Select a species",
            options=species_list,
            index=0
        )
        
        # Filter images by selected species
        species_images = image_df[image_df['label'] == selected_species]
        
        # Create image grid
        cols = st.columns(4)
        for idx, (_, row) in enumerate(species_images.iterrows()):
            with cols[idx % 4]:
                try:
                    image = Image.open(row['image_path'])
                    st.image(image, caption=f"Experiment: {row['experiment']}")
                except Exception as e:
                    st.error(f"Error loading image: {str(e)}")
                    
    except Exception as e:
        st.error(f"Error loading experiment data: {str(e)}")
        st.info("Please ensure your Comet.ml API key and workspace are properly configured in the .env file")

if __name__ == "__main__":
    load_css()
    app()
