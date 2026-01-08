import streamlit as st
import requests
import json

st.set_page_config(page_title="Pokemon API Demo", page_icon="⚡", layout="centered")

# Custom CSS to center content and limit width
st.markdown("""
    <style>
    .main .block-container {
        max-width: 900px;
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ Pokemon Stats Finder")


# Base URL
BASE_URL = "https://pokeapi.co/api/v2/pokemon"

# Input section
col1, col2 = st.columns([3, 1])
with col1:
    pokemon_name = st.text_input(
        "Enter Pokemon Name", 
        value="pikachu",
        placeholder="e.g., pikachu, charizard, bulbasaur",
        help="Enter the name of the Pokemon (lowercase)"
    )

with col2:
    st.write("")  # Spacing
    st.write("")  # Spacing
    fetch_button = st.button("🔍 Fetch Pokemon", type="primary", use_container_width=True)

if fetch_button and pokemon_name:
    try:
        with st.spinner(f"Loading {pokemon_name}..."):
            response = requests.get(f"{BASE_URL}/{pokemon_name.lower()}")
            response.raise_for_status()
            pokemon_data = response.json()
        
        st.success(f"✅ Successfully fetched {pokemon_data['name'].title()}!")
        
        # Main layout with image and important features
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # Display Pokemon official artwork if available, fallback to front_default
            image_url = None
            if 'sprites' in pokemon_data:
                # Try to get official artwork first
                if pokemon_data['sprites'].get('other', {}).get('official-artwork', {}).get('front_default'):
                    image_url = pokemon_data['sprites']['other']['official-artwork']['front_default']
                # Fallback to front_default
                elif pokemon_data['sprites'].get('front_default'):
                    image_url = pokemon_data['sprites']['front_default']
            
            if image_url:
                st.image(
                    image_url,
                    caption=f"{pokemon_data['name'].title()}",
                    use_container_width=True
                )
        
        with col2:
            st.subheader(f"Important Features")
            
            # Basic Info
            info_col1, info_col2 = st.columns(2)
            with info_col1:
                st.metric("ID", pokemon_data['id'])
                st.metric("Height", f"{pokemon_data['height'] / 10:.1f} m")
                st.metric("Weight", f"{pokemon_data['weight'] / 10:.1f} kg")
            
            with info_col2:
                st.metric("Base Experience", pokemon_data.get('base_experience', 'N/A'))
                st.metric("Order", pokemon_data.get('order', 'N/A'))
            
            # Types
            st.write("**Types:**")
            type_cols = st.columns(len(pokemon_data['types']))
            for idx, type_info in enumerate(pokemon_data['types']):
                type_name = type_info['type']['name'].title()
                type_cols[idx].badge(f"🔷 {type_name}")
            
            # Abilities
            st.write("**Abilities:**")
            for ability in pokemon_data['abilities']:
                ability_name = ability['ability']['name'].replace('-', ' ').title()
                hidden = " (Hidden)" if ability['is_hidden'] else ""
                st.write(f"• {ability_name}{hidden}")
            
            # Moves count
            st.write(f"**Total Moves:** {len(pokemon_data.get('moves', []))}")
        
        # Full Response in dropdown/expander section
        st.markdown("---")
        with st.expander("📋 Full API Response (JSON)", expanded=False):
            st.json(pokemon_data)
        
    except requests.exceptions.HTTPError as e:
        if hasattr(e.response, 'status_code') and e.response.status_code == 404:
            st.error(f"❌ Pokemon '{pokemon_name}' not found! Please check the spelling and try again.")
        else:
            st.error(f"❌ HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error: {e}")
elif fetch_button and not pokemon_name:
    st.warning("⚠️ Please enter a Pokemon name")

# Footer
st.markdown("---")
st.markdown("**Note:** This demo uses the [PokeAPI](https://pokeapi.co/) - a free RESTful API for Pokemon data.")
