import streamlit as st  # Import Streamlit as 'st'

# Set the title of the app
st.title('Streamlit Dashboard')

# Display some content
st.write("Hello, this is a sample Streamlit app embedded in Thymeleaf!")
st.write("You can display charts, graphs, and other interactive elements here.")

# Display a simple chart
import numpy as np
import pandas as pd
import altair as alt

# Generate some sample data
df = pd.DataFrame({
    'x': np.arange(0, 10, 1),
    'y': np.random.random(10)
})

# Create a simple line chart using Altair
chart = alt.Chart(df).mark_line().encode(
    x='x',
    y='y'
)

st.altair_chart(chart, use_container_width=True)
