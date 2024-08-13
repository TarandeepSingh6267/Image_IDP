# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
import pandas as pd

# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")
st.write(
    """Pick a sweatsuit color or style:
    """
)
