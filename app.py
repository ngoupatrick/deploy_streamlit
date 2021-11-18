import streamlit as st
import numpy as np
import pandas as pd

if __name__ == "__main__":
	st.write("This streamlit app is deploy with nginx!!")
	st.markdown(">Here we are going to see some basic of **streamlit code**")
	_code = '''#How to import streamlit \nimport streamlit as st'''
	st.code(body=_code, language='python')
	st.markdown(">Here we are going to plot lines using streamlit")
	chart_data = pd.DataFrame(np.random.randn(20,2), columns=['a','b'])
	st.line_chart(chart_data)
	_code = '''
chart_data = pd.DataFrame(np.random.randn(20,2), columns=['a','b'])
st.line_chart(chart_data)	
'''
	st.code(body=_code, language='python')

