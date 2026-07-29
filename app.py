import streamlit as st
import pandas as pd
import plotly.graph_objects as go

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
    
    # Simple Logic Parser
    if "AND" in code_input.upper():
        result = input_a and input_b
        gate_type = "AND Gate"
        truth_results = [0, 0, 0, 1]
    elif "OR" in code_input.upper():
        result = input_a or input_b
        gate_type = "OR Gate"
        truth_results = [0, 1, 1, 1]
    elif "XOR" in code_input.upper():
        result = input_a ^ input_b
        gate_type = "XOR Gate"
        truth_results = [0, 1, 1, 0]
    else:
        result = False
        gate_type = "Unknown Gate"
        truth_results = [0, 0, 0, 0]

with col2:
    st.subheader("📊 Output & Visualization")
    
    # Display Result Box
    status_color = "#28a745" if result else "#dc3545"
    st.markdown(f"""
    <div style='padding: 20px; border-radius: 10px; background-color: {status_color}; color: white; text-align: center;'>
        <h2>OUTPUT: {int(result)}</h2>
        <p>Gate Detected: {gate_type}</p>
    </div>
    """, unsafe_allow_html=True)

    # Truth Table
    st.write("**Truth Table:**")
    data = {
        'A': [0, 0, 1, 1],
        'B': [0, 1, 0, 1],
        'Result': truth_results
    }
    df = pd.DataFrame(data)
    st.table(df)

    # Waveform Chart
    st.write("**Signal Waveform:**")
    
    # Create Plotly Figure
    fig = go.Figure()
    
    # Add Clock Trace
    fig.add_trace(go.Scatter(
        x=[0, 1, 2, 3, 4, 5], 
        y=[0, 1, 0, 1, 0, 1], 
        mode='lines+markers', 
        name='Clock'
    ))
    
    # Add Input A Trace
    fig.add_trace(go.Scatter(
        x=[0, 1, 2, 3, 4, 5], 
        y=[int(input_a)] * 6, 
        mode='lines+markers', 
        name='Input A'
    ))
    
    # Add Output Trace
    fig.add_trace(go.Scatter(
        x=[0, 1, 2, 3, 4, 5], 
        y=[int(result)] * 6, 
        mode='lines+markers', 
        name='Output'
    ))

    fig.update_layout(
        title="Logic Signals", 
        height=300, 
        xaxis_title="Time Steps", 
        yaxis_title="State (0/1)"
    )
    
    st.plotly_chart(fig)

# Footer
st.markdown("---")
st.caption("Built with Streamlit | Inspired by Open Source Silicon")
