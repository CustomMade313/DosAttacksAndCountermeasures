#Extra modules needed for this to run: panadas, numpy and sklearn
#code based on: https://github.com/mudgalabhay/intrusion-detection-system
import time
import os
import pandas as pd
import numpy as nm 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
import pickle

#Step 0: setting up the prerequisite for the dataset processing

cols ="""duration,
protocol_type,
service,
flag,
src_bytes,
dst_bytes,
land,
wrong_fragment,
urgent,
hot,
num_failed_logins,
logged_in,
num_compromised,
root_shell,
su_attempted,
num_root,
num_file_creations,
num_shells,
num_access_files,
num_outbound_cmds,
is_host_login,
is_guest_login,
count,
srv_count,
serror_rate,
srv_serror_rate,
rerror_rate,
srv_rerror_rate,
same_srv_rate,
diff_srv_rate,
srv_diff_host_rate,
dst_host_count,
dst_host_srv_count,
dst_host_same_srv_rate,
dst_host_diff_srv_rate,
dst_host_same_src_port_rate,
dst_host_srv_diff_host_rate,
dst_host_serror_rate,
dst_host_srv_serror_rate,
dst_host_rerror_rate,
dst_host_srv_rerror_rate"""
  
columns =[]
for c in cols.split(',\n'):
    if(c.strip()):
        columns.append(c.strip())
  
columns.append('target')

attacks_types = {
    'normal': 'normal',
'back': 'dos',
'buffer_overflow': 'u2r',
'ftp_write': 'r2l',
'guess_passwd': 'r2l',
'imap': 'r2l',
'ipsweep': 'probe',
'land': 'dos',
'loadmodule': 'u2r',
'multihop': 'r2l',
'neptune': 'dos',
'nmap': 'probe',
'perl': 'u2r',
'phf': 'r2l',
'pod': 'dos',
'portsweep': 'probe',
'rootkit': 'u2r',
'satan': 'probe',
'smurf': 'dos',
'spy': 'r2l',
'teardrop': 'dos',
'warezclient': 'r2l',
'warezmaster': 'r2l',
}

#Step 1: Loading the dataset and processing it 



path_to_data10 = "C:\\Users\\Taxia\\Desktop\\Git\\DosAttacksAndCountermeasures\\dos_src\\datasets\\kddcup.data_10_percent.gz"
df = pd.read_csv(path_to_data10, names = columns)

# Adding Attack Type column
df['Attack Type'] = df.target.apply(lambda r:attacks_types[r[:-1]])



df = df.dropna('columns')# drop columns with NaN

df = df[[col for col in df if df[col].nunique() > 1]]# keep columns where there are more than 1 unique values


#drop variables with high corellation 
df.drop('num_root', axis = 1, inplace = True)
 
df.drop('srv_serror_rate', axis = 1, inplace = True)
  
df.drop('srv_rerror_rate', axis = 1, inplace = True)
  
df.drop('dst_host_srv_serror_rate', axis = 1, inplace = True)
  
df.drop('dst_host_serror_rate', axis = 1, inplace = True)
  
df.drop('dst_host_rerror_rate', axis = 1, inplace = True)
  
df.drop('dst_host_srv_rerror_rate', axis = 1, inplace = True)
  
df.drop('dst_host_same_srv_rate', axis = 1, inplace = True)


pmap = {'icmp':0, 'tcp':1, 'udp':2}
df['protocol_type'] = df['protocol_type'].map(pmap)
 
fmap = {'SF':0, 'S0':1, 'REJ':2, 'RSTR':3, 'RSTO':4, 'SH':5, 'S1':6, 'S2':7, 'RSTOS0':8, 'S3':9, 'OTH':10}
df['flag'] = df['flag'].map(fmap)

# remove irellevant features 
df.drop('service', axis = 1, inplace = True) 

df = df.drop(['target', ], axis = 1)

y = df[['Attack Type']]
X = df.drop(['Attack Type', ], axis = 1)

sc = MinMaxScaler()
print(X)
X = sc.fit_transform(X)
  
# Split test and train data 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)
print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)

clfr = RandomForestClassifier(n_estimators = 30)
clfr.fit(X_train, y_train.values.ravel())


#tart_time = time.time()
#y_test_pred = clfr.predict(X_train)
#end_time = time.time()
#print("Testing time: ", end_time-start_time)

#print("Train score is:", clfr.score(X_train, y_train))
#print("Test score is:", clfr.score(X_test, y_test))

filename = "TrainnedModel.sav"
pickle.dump(clfr, open(filename, 'wb'))
 

"""
# loading the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)
"""