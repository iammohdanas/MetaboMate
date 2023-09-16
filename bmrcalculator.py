import pyttsx3
import streamlit as st

def Speak(Text):
    engine = pyttsx3.init('sapi5')   #sapi5 helps google ko bulwane me
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty("rate", 170)
    print("")
    st.subheader(f"You : {Text}.")
    engine.say(Text)
    engine.runAndWait()
weight = st.number_input('Enter the weight:', 1,200)
height = st.number_input('Enter the height:', 1,250)
age = st.number_input('Enter the age:', 1,120)
# isMale = st.number_input('Enter the Gender\n(For female Enter 0 and for male Enter 1):', 0,1)
isMale=st.text_input('Enter the Gender (m/f):')
weightmanage= st.text_input("Do you want to gain weight or lose weight?  Enter in (gain/loss) : ")

def bmrCalculate():
    # weight = int(input("Enter your weight in KG: \n"))
    # height = int(input("Enter your height in cm: \n"))
    # age = int(input("Enter your age in years: \n"))
    # isMale = str(input("Are you male? (y/n)"))

    
    # if isMale == "y":
    #     isMale = True
    # elif isMale == "n":
    #     isMale = False
    # else:
    #     st.subheader("Error")
    #     quit()

        

    # Mifflin St. Jeor Equation for males
    if isMale=="m":
        bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
    else:
        bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

    bmr = round(bmr)
    # print(bmr)
    Speak("Your bmr is :")
    Speak(bmr)
    # Speak("Now answer some of the questions so that i can tell you the amount of macro nutrients ")
    
    calmanage = 200
    st.write("\nokay sir, i have provided you the maintenance calories below :\n")
    if weightmanage == "gain":
        st.write("You need to add ",calmanage,"daily to your diet plan and consume ",bmr+calmanage," calories\n")
    elif weightmanage == "loss":
        st.write("You need to add ",calmanage,"daily to your diet plan and consume ",bmr+calmanage," calories\n")
    else:
        st.write("Error")
        quit()

    calforweightloss = bmr - calmanage
    protein_for_loss = (calforweightloss/100)*35
    protein_for_loss_gm = ((calforweightloss/100)*35)/4
    carbs_for_loss = (calforweightloss/100)*50
    carbs_for_loss_gm = ((calforweightloss/100)*50)/4
    fat_need_for_loss = (calforweightloss/100)*15
    fat_need_for_loss_gm = ((calforweightloss/100)*15)/9

    calforweightgain = bmr + calmanage
    protein_for_gain = (calforweightgain/100)*35
    protein_for_gain_gm = ((calforweightgain/100)*35)/4
    carbs_for_gain = (calforweightgain/100)*50
    carbs_for_gain_gm = ((calforweightgain/100)*50)/4
    fatneed_for_gain = (calforweightgain/100)*15
    fatneed_for_gain_gm = ((calforweightgain/100)*15)/9


    if weightmanage == "gain":
        st.write("Calories from protein : ",protein_for_gain, " / ",protein_for_gain_gm,"gm")
        st.write("Calories from carbohyderates : ",carbs_for_gain, " / ",carbs_for_gain_gm,"gm")
        st.write("Calories from Fat : ",fatneed_for_gain, " / ",fatneed_for_gain_gm,"gm")

    elif weightmanage == "loss":
        st.write("Calories from protein : ",protein_for_loss, " / ",protein_for_loss_gm,"gm")
        st.write("Calories from carbohyderates : ",carbs_for_loss, " / ",carbs_for_loss_gm,"gm")
        st.write("Calories from Fat : ",fat_need_for_loss, " / ",fat_need_for_loss_gm,"gm")
    else:
        st.write("Error")
        quit()


if st.button("Calculate"):
    response = bmrCalculate()
    st.write(f"**Assistant:** {response}")


st.markdown("---")

footer_content = """
<footer style="text-align: center; margin-top: 20px;">
    <p>Made by - Mohd Anas Ansari</p>
</footer>
"""

# Render the footer using markdown
st.markdown(footer_content, unsafe_allow_html=True)