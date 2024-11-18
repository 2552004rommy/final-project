import streamlit as st
from PIL import Image
import streamlit as st




st.title("Sales Insights")

image = Image.open(r"E:\depi\1667099680241.png")
st.image(image)

# Page title

# Insights Section
with st.container():
    st.markdown("## Insights")

    # Recommendations for the Owner
    with st.expander("Recommendations for the Owner"):
        st.markdown("1. **Focus on the best-selling sub-category**: The data suggests that tables and chairs are the best-selling sub-category. Consider increasing production and marketing efforts for this category to maximize sales.")
        st.markdown("2. **Target customers who purchased in the best year**: The data shows that 2015 was the best year for sales. Consider targeting customers who purchased in 2017 with personalized marketing campaigns to increase repeat business.")
        st.markdown("3. **Expand product offerings in the best-selling sub-category**: Consider expanding product offerings in the tables and chairs sub-category to attract more customers and increase sales.")
        st.markdown("4. **Promote the best-selling product**: The data suggests that the best-selling product is a desk chair. Consider promoting this product to attract more customers and increase sales.")
        st.markdown("5. **Day 16 is the best day**: The data suggests that day 16 is the best day for sales. Consider increasing production and marketing efforts for this day to maximize sales.")
        st.markdown("6. **Journey month is the best month**: The data suggests that journey month is the best month for sales. Consider increasing production and marketing efforts for this month to maximize sales.")
        st.markdown("7. **Ship mode is the best ship mode**: The data suggests that ship mode is the best ship mode. Consider increasing production and marketing efforts for this ship mode to maximize sales.")

    # Recommendations for the Manager
    with st.expander("Recommendations for the Manager"):
        st.markdown("1. **Focus on the best-selling sub-category**: Concentrate on tables and chairs to drive sales.")
        st.markdown("2. **Target customers who purchased in the best year**: Utilize data from 2017 to inform marketing strategies.")
        st.markdown("3. **Employee Engagement**: Ensure that your employees are motivated and engaged, as they play a crucial role in the success of your strategies keep him 17 on month .")

# Thank You message
st.markdown("### Thank you all for your attention!")
