import streamlit as st

# Page configs
# st.set_page_config(page_title="BMI Calculator")
# st.set_page_config(page_bg_color="#0E1117")

def calculate_bmi(weight, height):
  return weight / (height ** 2)

st.title("BMI Calculator")

weight = st.number_input("Enter weight (kg)")

height_input = st.number_input("Enter height (feet.inches)")

if st.button("Calculate BMI"):

  if not height_input:
    st.error("Please enter height")

  else:
    # Split height input 
    height_data = str(height_input).split(".")  

    if len(height_data) != 2:
      st.error("Invalid height format")

    else:
      feet = int(height_data[0])
      inches = float(height_data[1])

      if feet < 0 or inches < 0 or inches > 11.99:
        st.error("Invalid height")

      else:
        # Convert to meters 
        height_in_meters = feet * 0.3048 + inches * 0.0254

        bmi = calculate_bmi(weight, height_in_meters)

        # Display BMI
        st.write("Your BMI is: ", bmi)
        st.progress(bmi/50)

        if bmi < 18.5:
          st.info("Underweight")
        elif bmi >= 18.5 and bmi < 25:  
          st.success("Healthy")
        elif bmi >= 25 and bmi < 30:
          st.warning("Overweight")
        else:  
          st.error("Obese")