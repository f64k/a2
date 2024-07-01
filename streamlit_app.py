import os, platform
import numpy as np, pandas as pd, streamlit as st
import altair as alt

st.set_page_config(page_title="Предсказания", page_icon="🦋", layout="wide", initial_sidebar_state="expanded")

st.sidebar.markdown("💎 Стартовая страница")

with st.container():
    cols1 = st.columns([3,3,3])
    dirParams = {
        "os.getcwd": os.getcwd(),
        "cpu_count": os.cpu_count(),
        #"environ": os.environ,
        #"os.listdir": os.listdir(),
        "platform": platform.platform(),
        "release": platform.release(),
        "node": platform.node(),
        "processor": platform.processor(),
        "machine": platform.machine(),
        "system": platform.system(),
        "version": platform.version(),
        "python_version": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "uname": platform.uname(),
        "libc_ver": platform.libc_ver(),
        "architecture": platform.architecture(),
    }
    cols1[0].write(dirParams)
    cols1[1].write(os.environ)
    cols1[2].write(os.listdir())

