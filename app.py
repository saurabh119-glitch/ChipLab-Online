import streamlit as st
import pandas as pd
import time

# Page Config
st.set_page_config(page_title="ChipLab Online", layout="wide")

st.title("🔬 ChipLab Online: Digital Logic Simulator")
st.markdown("Design, Simulate, and Visualize Digital Circuits in your Browser.")

# Sidebar: Input Code
st.sidebar.header("✍️ Write Your Logic")
code_input = st.sidebar.text_area("Verilog-like Logic", 
                                  value="output = A AND B", 
                                  height=100)

# Main Area: Circuit Builder
col1, col2 = st.columns(2)

with col1:
    st.subheader("⚙️ Inputs")
    input_a = st.checkbox("Input A", value=False)
    input_b = st.checkbox("Input B", value=False)
    
    # Simple Logic Parser (Demo Purpose)
    if "AND" in code_input.upper():
        result = input_a and input_b
        gate_type = "AND Gate"
    elif "OR" in code_input.upper():
        result = input_a or input_b
        gate_type = "OR Gate"
    elif "XOR" in code_input.upper():
        result = input_a ^ input_b
        gate_type = "XOR Gate"
    else:
        result = False
        gate_type = "Unknown"

with col2:
    st.subheader("📊 Output & Visualization")
    
    # Display Result
    status_color = "green" if result else "red"
    st.markdown(f"""
    <div style='padding: 20px; border-radius: 10px; background-color: {status_color}; color: white; text-align: center;'>
        <h2>OUTPUT: {int(result)}</h2>
        <p>Gate: {gate_type}</p>
    </div>
    """, unsafe_allow_html=True)

    # Truth Table Generator
    st.write("Truth Table:")
    data = {
        'A': [0, 0, 1, 1],
        'B': [0, 1, 0, 1],
        'Result': [0, 0, 0, 1] if "AND" in code_input.upper() else 
                  [0, 1, 1, 1] if "OR" in code_input.upper() else
                  [0, 1, 1, 0]
    }
    df = pd.DataFrame(data)
    st.table(df)

# Footer
st.markdown("---")
st.caption("Built with Streamlit | Inspired by Open Source Silicon")


import plotly.graph_objects as go

# ... inside col2 ...

# Fake Waveform Visualization
fig = go.Figure()
fig.add_trace(go.Scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 0, 1, 0], mode='lines', name='Clock'))
fig.add_trace(go.Scatter(x=[0, 1, 2, 3, 4], y=[int(input_a)]*5, mode='lines', name='Input A'))
fig.add_trace(go.Scatter(x=[0, 1, 2, 3, 4], y=[int(result)]*5, mode='lines', name='Output'))

fig.update_layout(title="Signal Waveform", height=300)
st.plotly_chart(fig)
