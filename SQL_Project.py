

from sqlalchemy import create_engine
import pandas as pd


conn_string = 'postgresql://postgres:password@localhost/Hospital'
db = create_engine(conn_string)
conn = db.connect()


# In[52]:


df = pd.read_csv('Hospital_data.csv')
df.to_sql('patient', con = conn, if_exists = 'replace', index= False )

