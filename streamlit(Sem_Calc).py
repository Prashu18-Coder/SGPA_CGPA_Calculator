import streamlit as st
import time as t

st.set_page_config(page_title="Semester Calculator",page_icon="📅",layout="centered",initial_sidebar_state="expanded")

st.markdown("<h2 style ='color:rgb(96,184,168);'><i><b>SGPA And CGPA CALCULATOR</b></i></h2>",unsafe_allow_html=True)

if "final" not in st.session_state:
   st.session_state.final= False
   
if not st.session_state.final:
      if "submitted" not in st.session_state:
         st.session_state.submitted = False
      if not st.session_state.submitted:     
         name   = st.text_input("Enter Your Name:")
         reg_no = st.text_input("Enter Your Register Number:")
         branch = st.selectbox("Select Your Branch:",['CSE/CSD/CSM/CSO/IT','ECE','EEE','MECH','CIV','CHE'],index=None,placeholder="--Select Branch--")
         if st.button("Next"):
            with st.spinner("Loading..."):
                  t.sleep(2)
            if not name:
                  st.error("⚠️ Please enter your name.")
            else:
                  if len(reg_no)!=8:
                     st.error("⚠️ Enter Valid Register Number")
                  elif not reg_no:
                     st.error("⚠️ Please enter your register number.")
                  elif not branch:
                     st.error("⚠️ Please select your branch.")
                  else:
                     st.success("✅ All fields are filled! Proceeding with SGPA calculation...")
                     st.session_state.submitted = True
                     st.rerun()
      else: 
            with st.sidebar:
                  with st.expander("3rd Semester Subjects"):
                     st.write("CO211-Maths(3 Credits)")
                     st.write("CO212-Universal Human Values(2 Credits)")
                     st.write("CO213-Discrete Maths(3 Credits)")
                     st.write("CO214-Computer Organization(3 Credits)")
                     st.write("CO215-Design and Analysis of Algorithms(3 Credits)")
                     st.write("CO216-Object Oriented Programming(3 Credits)")
                     st.write("CO252-Design and Analysis of Algorithms Lab(1 Credits)")
                     st.write("CO253-Object Oriented Programming Lab(1 Credits)")
            if "submit" not in st.session_state:
               st.session_state.submit = False
            if not st.session_state.submit:
                  sum,credits= 0.0,19
                  a = st.selectbox("**CO211-Maths(3 Credits)**",['A+','A','B','C','D','E','F'],index=None,placeholder="--Select Grade--")
                  if   a=='A+':
                     sum += 3*(10.0)
                  elif a=='A':
                     sum += 3*(9.0)
                  elif a=='B':
                     sum += 3*(8.0)
                  elif a=='C':
                     sum += 3*(7.0)
                  elif a=='D':
                     sum += 3*(6.0)
                  elif a=='E':
                     sum += 3*(5.0)
                  else:
                     sum += 0.0
               


                  b = st.selectbox("**CO212-Universal Human Values(2 Credits)**",['A+','A','B','C','D','E','F'],index=None,placeholder="--Select Grade--")

                  if   b=='A+':
                     sum += 2*(10.0)
                  elif b=='A':
                     sum += 2*(9.0)
                  elif b=='B':
                     sum += 2*(8.0)
                  elif b=='C':
                     sum += 2*(7.0)
                  elif b=='D':
                     sum += 2*(6.0)
                  elif b=='E':
                     sum += 2*(5.0)
                  else:
                     sum += 0.0


                  c = st.selectbox("**CO213-Discrete Maths(3 Credits)**",['A+','A','B','C','D','E','F'],index=None,placeholder="--Select Grade--")

                  if   c=='A+':
                     sum += 3*(10.0)
                  elif c=='A':
                     sum += 3*(9.0)
                  elif c=='B':
                     sum += 3*(8.0)
                  elif c=='C':
                     sum += 3*(7.0)
                  elif c=='D':
                     sum += 3*(6.0)
                  elif c=='E':
                     sum += 3*(5.0)
                  else:
                     sum += 0.0


                  d = st.selectbox("**CO214-Computer Organization(3 Credits)**",['A+','A','B','C','D','E','F'],index=None,placeholder="--Select Grade--")

                  if   d=='A+':
                     sum += 3*(10.0)
                  elif d=='A':
                     sum += 3*(9.0)
                  elif d=='B':
                     sum += 3*(8.0)
                  elif d=='C':
                     sum += 3*(7.0)
                  elif d=='D':
                     sum += 3*(6.0)
                  elif d=='E':
                     sum += 3*(5.0)
                  else:
                     sum += 0.0


                  e = st.selectbox("**CO215-Design and Analysis of Algorithms(3 Credits)**",['A+','A','B','C','D','E','F'],index=None,placeholder="--Select Grade--")

                  if   e=='A+':
                     sum += 3*(10.0)
                  elif e=='A':
                     sum += 3*(9.0)
                  elif e=='B':
                     sum += 3*(8.0)
                  elif e=='C':
                     sum += 3*(7.0)
                  elif e=='D':
                     sum += 3*(6.0)
                  elif e=='E':
                     sum += 3*(5.0)
                  else:
                     sum += 0.0


                  f = st.selectbox("**CO216-Object Oriented Programming(3 Credits)**",['A+','A','B','C','D','E','F'],index=None,placeholder="--Select Grade--")

                  if   f=='A+':
                     sum += 3*(10.0)
                  elif f=='A':
                     sum += 3*(9.0)
                  elif f=='B':
                     sum += 3*(8.0)
                  elif f=='C':
                     sum += 3*(7.0)
                  elif f=='D':
                     sum += 3*(6.0)
                  elif f=='E':
                     sum += 3*(5.0)
                  else:
                     sum += 0.0

                  g = st.selectbox("**CO251-Skill Enhancement Course-1(2 Credits)**",['A+','A','B','C','D','E','F'],index=None,placeholder="--Select Grade--")

                  if   g=='A+':
                     sum += 2*(10.0)
                  elif g=='A':
                     sum += 2*(9.0)
                  elif g=='B':
                     sum += 2*(8.0)
                  elif g=='C':
                     sum += 2*(7.0)
                  elif g=='D':
                     sum += 2*(6.0)
                  elif g=='E':
                     sum += 2*(5.0)
                  else:
                     sum += 0.0

                  h = st.selectbox("**CO252-Design and Analysis of Algorithms Lab(1 Credits)**",['A+','A','B','C','D','E','F'],index=None,placeholder="--Select Grade--")

                  if   h=='A+':
                     sum += 10.0
                  elif h=='A':
                     sum += 9.0
                  elif h=='B':
                     sum += 8.0
                  elif h=='C':
                     sum += 7.0
                  elif h=='D':
                     sum += 6.0
                  elif h=='E':
                     sum += 5.0
                  else:
                     sum += 0.0

                  i = st.selectbox("**CO253-Object Oriented Programming Lab(1 Credits)**",['A+','A','B','C','D','E','F'],index=None,placeholder="--Select Grade--")

                  if   i=='A+':
                     sum += 10.0
                  elif i=='A':
                     sum += 9.0
                  elif i=='B':
                     sum += 8.0
                  elif i=='C':
                     sum += 7.0
                  elif i=='D':
                     sum += 6.0
                  elif i=='E':
                     sum += 5.0
                  else:
                     sum += 0.0

                  sgp = sum/credits

                  if st.button("Calculate SGPA"):
                     with st.spinner("Calculating...."):
                              t.sleep(2)
                     st.success(f"Your SGPA is {sgp}")
            
                  if st.button("Calculate CGPA"):
                     with st.spinner("Please Wait...."):
                           t.sleep(2)
                     st.session_state.submit = True
                     st.rerun()
            else:
                  x   = st.number_input("1st Semester GPA:",min_value=0.0,max_value=10.0,step=0.05)
                  y   = st.number_input("2nd Semester GPA:",min_value=0.0,max_value=10.0,step=0.05)
                  c1  = st.selectbox("Credits for 1st Sem:",[18,19,20,21],index=None,placeholder="--Credits--")
                  c2  = st.selectbox("Credits for 2nd Sem:",[18,19,20,21],index=None,placeholder="--Credits--")
                  
                  if c1 is not None and c2 is not None:
                     cgp = (x*c1 + y*c2)/(c1+c2)
           
                  if st.button("Calculate CGPA"):
                     with st.spinner("Please Wait...."):
                        t.sleep(2)
                     st.success(f"Your CGPA is {cgp}")
               
if st.button("Calculate again"):
      with st.spinner("Please Wait...."):
         t.sleep(2)
      st.session_state.final = False
      st.session_state.submitted = False
      st.session_state.submit = False
      st.rerun()   
                           
      
      

         

