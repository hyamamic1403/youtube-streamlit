import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('progress bar')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'Done!!'




st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b', 'c']
)
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

df2 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df2)

st.write('Display Image')

option = st.selectbox(
    'teach me your favorite number',
    list(range(1,11))
)

st.write('interactive widgets')

left_column, right_column = st.beta_columns(2)
button = left_column.button('migi column ni moji wo hyouji')
if button:
    right_column.write('this is right column')

expander = st.beta_expander('query')
expander.write('write expander')

text = st.text_input('teach me your hobby.')
'your hobby is ', text, '.'


'your favorite number is ', option, '.'


condition = st.slider('your condition?', 0, 100, 50)
'your condition:', condition

# if st.checkbox('Show image'):
#     img = Image.open('51DPwXSMx-L.jpg')
#     st.image(img, caption='picture', use_column_width=True)
# st.write(df)

# st.dataframe(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0))

"""
# sho
## setsu
### kou

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""