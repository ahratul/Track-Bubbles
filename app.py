# Import libraries
from __future__ import division, unicode_literals, print_function  # for compatibility with Python 2 and 3
import streamlit as st
import matplotlib as mpl
import matplotlib.pyplot as plt
import pims
import trackpy as tp

st.set_option('deprecation.showPyplotGlobalUse', False)

st.subheader('Repository Link')
Repository_Link = {
    "GitHub": "https://github.com/ahratul/Track-Bubbles",
}

st.write('\n')
cols = st.columns(len(Repository_Link))
for index, (platform, link) in enumerate(Repository_Link.items()):
    cols[index].write(f"[{platform}]({link})")

st.write("---")

mpl.rc('figure', figsize=(10, 5))
mpl.rc('image', cmap='gray')

st.sidebar.markdown('<p class="font">Bubble</p>', unsafe_allow_html=True)
with st.sidebar.expander("About the App"):
    st.write("""
        Bubble Tracking
     """)

st.title('Air Bubble Detect')
st.write("---")


@pims.pipeline
def gray(image):
    return image[:, :, 1]

image=st.selectbox("Image", city)
frames = gray(pims.open("Original.png"))
st.subheader('Original Image')
st.write(frames[0])
st.write("---")

st.subheader('Detected Bubbles From Image')
f = tp.locate(frames[0], 11, invert=True)
h = tp.annotate(f, frames[0])

st.pyplot(h.figure.show())

st.write("---")

st.subheader('Counted Bubbles from Image')
fig, ax = plt.subplots()
ax.hist(f['mass'], bins=20)

# Optionally, label the axes.
ax.set(xlabel='mass', ylabel='count')
st.pyplot(fig.show())
