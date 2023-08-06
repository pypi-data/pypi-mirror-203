# streamlit-component-dropfilltextarea

Streamlit Component DropFillTextarea allows you to drag and drop files onto a text area, making it easy to fill in large amounts of text quickly. With dropfill_textarea, users can quickly populate text areas with pre-existing text files, reducing manual input and increasing efficiency. The component also offers flexible layout options, allowing users to customize the label and text area's size, position, and other properties. Whether you're a developer or a user, dropfill_textarea is the perfect solution for simplifying your workflow.

## Installation instructions 

```sh
pip install streamlit-component-dropfilltextarea
```

## Usage instructions

```python
import streamlit as st

from st_dropfill_textarea import st_dropfill_textarea

value = st_dropfill_textarea()

st.write(value)
