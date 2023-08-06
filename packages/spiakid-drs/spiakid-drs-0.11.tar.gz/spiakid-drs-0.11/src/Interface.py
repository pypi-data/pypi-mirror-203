import streamlit as st
import Functions.Modelisation as Model

#Interface Creation using streamlit librairy (to ensure a graphical interface in Docker)

st.title('SPIAKID Data Reduction System')

#Initialisation
IQ_number = 0
Meas = 0
Level = 0
Plot_List = []

#Organisation
col1, col2, col3= st.columns([1, 1, 1])

with col3:
    result_folder = st.text_input('Result folder',value="")

with col2:
    txt = st.text('')
    txt = st.text('')
    txt = st.text('')
    format = st.selectbox('Format', ['.jpg','.svg','.eps'])
with col1:
    data_location = st.text_input('Data Location',value="")
    EnergyResolution = st.checkbox('Energy Resolution')
    PulseHeight = st.checkbox('Pulse Height')
    AvgPulse = st.checkbox('Pulse Average')
    PulseIQ_avg = st.checkbox('Measurment Average')
    PulseIQ = st.checkbox('Single Pulse')
    
    #Setting level to know which class to use (level 2: Pixel, level 1: Pulse_average, level 0: Pulse_Timeline)
    if EnergyResolution:
        Plot_List.append(0)
        if Level < 2 :
            Level = 2
    if PulseHeight:
        Plot_List.append(1)
        if Level < 2 :
            Level = 2
    if AvgPulse:
        Plot_List.append(2)
        if Level < 1 :
            Level = 1
    if PulseIQ_avg:
        Plot_List.append(3)
        #Asking which pulse to plot
        # Meas = st.text_input('Measurment:',value="0 - 79")
        Meas = st.text_input('Number:',value="0 - 79")
        if Level<0:
            Level = 0
    if PulseIQ:
        Plot_List.append(4)
        #Asking which pulse to plot
        Meas = st.text_input('Measurment:',value="0 - 79")
        IQ_number = st.text_input('Pulse Number:',value="0 - 123")
        if Level<0:
            Level = 0


    #Launching the pipeline
    Launch = st.button('OK')
    if Launch:
        Model.Data_read(data_location,result_folder,format,Plot_List,Level,int(Meas),int(IQ_number))
    


