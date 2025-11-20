import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("BSCS Afternoon 2019-2023 Result")


# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file, skiprows=1)
  st.subheader("Dataset Preview")
  st.write(df.head())
  
  st.success("CSV loaded successfully!")
  
  # Sidebar controls

  selected_columns = df.columns[0:6]

  st.sidebar.header("Input Sliders")


  column = st.sidebar.selectbox("Select Course", df.columns[0:6])

    # Slider to filter score range
  min_score, max_score = st.sidebar.slider(
        "Select Score Range",
        0, 100, (0, 100))

  filtered = df[(df[column] >= min_score) & (df[column] <= max_score)]

  st.write(f"### Histogram for {column} (Scores between {min_score}-{max_score})")

  fig, ax = plt.subplots()
  ax.hist(filtered[column], bins=10)
  ax.set_xlabel("Scores")
  ax.set_ylabel("Number of Students")
  ax.set_title(f"Distribution of Scores for {column}")

  st.pyplot(fig)

else:

  st.info("Please upload a CSV file to begin.")




