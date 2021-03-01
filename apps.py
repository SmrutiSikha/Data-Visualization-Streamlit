import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use('TkAgg')

st.title('Data Visualizations')
st.markdown('Smruti Sikha Panigrahi')

@st.cache(allow_output_mutation=True)
def load_data(file_path):
    df1 = pd.read_csv(file_path)
    return df1

file_path = 'response.csv'

df = load_data(file_path)

if st.checkbox('view raw data'):
    DF = load_data(file_path)
    n_rows = st.slider('rows',5,len(DF),10)
    st.subheader('raw data')
    st.write(DF.iloc[0:n_rows,:])
    st.subheader('data description')
    st.write(DF.describe())

df.rename(columns = {'Name':'name', 'Email':'email','Year Of Study':'year','Current Job title or future Job goal title':'currentjob','Which programming language you mostly use in your work ? *':'lang','Your College Name ?':'college'},inplace=True)

def identify_job_type(job):
    if 'software' in job.lower() or job.lower()=='SDE':
        return 'software developer'
    elif 'ML' in job.lower() or 'data' in job.lower():
        return 'data analyst'
    elif job.lower()=='core job' or 'engineer' in job.lower() or job.lower()=='embedded designer':
        return 'core job'
    elif 'web' in job.lower() or 'stack' in job.lower() or 'web' in job.lower():
        return 'web developer'
    elif 'developer' in job.lower():
        return 'product developer'
    elif 'student' in job.lower():
        return 'student'
    else:
        return 'others'

job_final = [identify_job_type(x) for x in df['currentjob']]
df['job_final'] = job_final

def initialize_college(c):
    if 'rourkela' in c.lower() or c == 'NITRKL' or c == 'NITR' or c == 'NIT,Roukela':
        return 'nitrkl'
    elif c =='College of Engineering and Technology, Bhubaneswar' or 'cet' in c.lower():
        return 'cet'
    elif c == 'IIT Bhubaneswar' or c =='IIT, Bhubaneswar':
        return 'IIT  BBSR'
    elif c == 'IIT BHU' or c =='IIT,BHU':
        return 'IIT  BHU'
    else:
        return c
colleges = [initialize_college(x) for x in df['college']]
df['colleges_final'] = colleges
df['lang'].replace('python','Python',inplace=True)
df['lang'].replace('matlab','Matlab',inplace=True)
df['lang'].replace('PHP, Javascript','Javascript',inplace=True)
df.drop( df[ df['lang'] == 'Hxsxa' ].index , inplace=True)
isStudent = []
for j in df['job_final']:
    if j == 'student':
        isStudent.append('student')
    else:
        isStudent.append('working professionals')
df['isStudent'] = isStudent
if st.checkbox('view processed data'):
    np_rows = st.slider('row',5,len(df),10)
    st.subheader('processed data')
    st.write(df.iloc[0:np_rows,:])
    st.subheader('data description')
    st.write(df.describe())

questions = st.selectbox("select the Visualization",['select an option','language VS career path','college VS career path','language VS working professionals/students'])

if questions=='language VS career path':
    df.groupby(['lang', 'job_final']).size().unstack().plot(kind='bar', stacked=True, figsize=(15, 5)).figure
    jobs = questions = st.selectbox("select a job",['select an option','software','web','data','core','student','product','others'])
    if jobs == 'web':
        fig,ax = plt.subplots()
        language_web = {'Python':0, 'Java':0, 'C++':0, 'Julia':0, 'Matlab':0, 'C':0, 'R':0, 'Javascript':0}
        for idx in df.index:
            if df['job_final'][idx] == 'web developer':
                language_web[df['lang'][idx]] +=1
        ax = plt.bar(*zip(*language_web.items()))
        # plt.show()
        st.pyplot(fig)
    elif jobs == 'software':
        fig,ax = plt.subplots()
        language_software = {'Python':0, 'Java':0, 'C++':0, 'Julia':0, 'Matlab':0, 'C':0, 'R':0, 'Javascript':0}
        for idx in df.index:
            if df['job_final'][idx] == 'software developer':
                language_software[df['lang'][idx]] +=1
        ax = plt.bar(*zip(*language_software.items()))
        # plt.show()
        st.pyplot(fig)
    elif jobs == 'data':
        fig,ax = plt.subplots()
        language_data = {'Python':0, 'Java':0, 'C++':0, 'Julia':0, 'Matlab':0, 'C':0, 'R':0, 'Javascript':0}
        for idx in df.index:
            if df['job_final'][idx] == 'data analyst':
                language_data[df['lang'][idx]] +=1
        ax = plt.bar(*zip(*language_data.items()))
        # plt.show()
        st.pyplot(fig)
    elif jobs == 'student':
        fig,ax = plt.subplots()
        language_student = {'Python':0, 'Java':0, 'C++':0, 'Julia':0, 'Matlab':0, 'C':0, 'R':0, 'Javascript':0}
        for idx in df.index:
            if df['job_final'][idx] == 'student':
                language_student[df['lang'][idx]] +=1
        ax = plt.bar(*zip(*language_student.items()))
        # plt.show()
        st.pyplot()
    elif jobs == 'product':
        fig,ax = plt.subplots()
        language_product = {'Python':0, 'Java':0, 'C++':0, 'Julia':0, 'Matlab':0, 'C':0, 'R':0, 'Javascript':0}
        for idx in df.index:
            if df['job_final'][idx] == 'product developer':
                language_product[df['lang'][idx]] +=1
        ax = plt.bar(*zip(*language_product.items()))
        # plt.show()
        st.pyplot(fig)
    elif jobs=='core':
        fig,ax = plt.subplots()
        language_core = {'Python':0, 'Java':0, 'C++':0, 'Julia':0, 'Matlab':0, 'C':0, 'R':0, 'Javascript':0}
        for idx in df.index:
            if df['job_final'][idx] == 'core job':
                language_core[df['lang'][idx]] +=1
        ax = plt.bar(*zip(*language_core.items()))
        # plt.show()
        st.pyplot(fig)
    elif jobs == 'others':
        fig,ax = plt.subplots()
        language_others = {'Python':0, 'Java':0, 'C++':0, 'Julia':0, 'Matlab':0, 'C':0, 'R':0, 'Javascript':0}
        for idx in df.index:
            if df['job_final'][idx] == 'others':
                language_others[df['lang'][idx]] +=1
        ax = plt.bar(*zip(*language_others.items()))
        # plt.show()
        st.pyplot(fig)
if questions=='college VS career path':
    df.groupby(['colleges_final', 'job_final']).size().unstack().plot(kind='bar', stacked=True, figsize=(15, 5)).figure

if questions=='language VS working professionals/students':
    df.groupby(['lang','isStudent']).size().unstack().plot(kind='bar', stacked=True, figsize=(15, 5)).figure
