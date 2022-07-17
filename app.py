import streamlit as st

from PIL import Image
from PIL import ImageDraw

image_path_list = ['HP0A.jpg',
 'HP1A.jpg',
 'HP2A.jpg',
 'HP3A.jpg',
 'HP4A.jpg',
 'HP5A.jpg',
 'HP6A.jpg',
 'HP7A.jpg',
 'HP8A.jpg',
 'HP9A.jpg']

# ADD DATE TO ALL 10 FILES

#can automate from datetime later
input_text = st.text_input("Text Input","17 Jul, 14:35")
checkindate = str(input_text).split(',')[0].lower().replace(' ','_')

for image_name in image_path_list:
    img = Image.open(f'original_images/{image_name}')
    I1 = ImageDraw.Draw(img)
    from PIL import ImageFont
    font = ImageFont.truetype("fonts/Manrope3 Regular 400.otf", 40)
    I1.text((310, 1840),input_text, font=font, fill =(77, 77, 77))
    img = img.save(f"populated_images/{image_name}")

# PRODUCE GIF
output_file_name = f'HP_checkedin_{checkindate}.gif'
output_path = f'gif_output/{output_file_name}'
imgs = (Image.open(f) for f in ["populated_images/" + x for x in image_path_list])
img = next(imgs)  # extract first image from iterator
img.save(fp=output_path, format='GIF', append_images=imgs,
         save_all=True, duration=1000, loop=0)

## Original image came from cv2 format, fromarray convert into PIL format
with open(output_path, "rb") as file:
    btn = st.download_button(
        label="Download image",
        data=file,
        file_name=output_file_name,
        mime="image/gif"
    )