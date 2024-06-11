import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load CSS from file
def load_css(file_path):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sample sales data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Sales': [2000, 3000, 2500, 4000, 3200, 3600, 3000, 3800, 4500, 4800, 5200, 6100]
}

df = pd.DataFrame(data)

# Inject CSS
load_css("design\styles.css")

# Streamlit app
st.title('Sales Dashboard')
st.write('This dashboard visualizes monthly sales data.')

# Interactive widgets
st.sidebar.header('Filter Options')
selected_month = st.sidebar.selectbox('Select a Month', df['Month'])

# Filtered data
filtered_data = df[df['Month'] == selected_month]

# Display filtered data
st.subheader('Filtered Sales Data')
st.write(filtered_data)

# Sales chart
st.subheader('Monthly Sales Chart')
fig, ax = plt.subplots()
ax.plot(df['Month'], df['Sales'], marker='o')
ax.set_xlabel('Month')
ax.set_ylabel('Sales')
ax.set_title('Monthly Sales Data')
plt.xticks(rotation=45)
st.pyplot(fig)

# Display total sales
total_sales = df['Sales'].sum()
st.subheader('Total Sales')
st.write(f'Total Sales: ${total_sales}')

# Show more details on button click
if st.button('Show Detailed Data'):
    st.subheader('Detailed Sales Data')
    st.write(df)

st.write('This dashboard provides an overview of sales data and allows you to filter by month.')
