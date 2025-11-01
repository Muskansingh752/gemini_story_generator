import streamlit as st
from story_generator import generate_story_from_image,narrate_story
from PIL import Image
st.title("IMAGE TO STORY ")
st.markdown("uplode 1 to 10 images, choose a style and let AI write and narrate a story for you. ")


with st.sidebar:
    st.header("controls")


    uploded_files = st.file_uploader(
        "uplode  your images...",
        type=["png","jpg","jpeg"],
        accept_multiple_files=True
    )


    story_style= st.selectbox(
        "choose a story style",
        ("comedy","fairy tale","sci-fi","Adventure")
    )

    generate_button= st.button("generate your uniqe story and narration",type ="primary")



if generate_button:
    if not uploded_files:
        st.write("please uplode at-least 1 image...")
    elif len(uploded_files)>10:
        st.write("uploded images limet is 10")
    else:
        with st.spinner("your story is generating pleas wait.. this may take few min."):
            try:
                pil_images =[Image.open(uploaded_file)for uploaded_file in uploded_files]
                st.subheader('your visual inspiration:')
                image_colums = st.columns(len(pil_images))

                for i, image in enumerate(pil_images):
                    with image_colums[i]:
                        st.image(image,use_column_width=True)

                
                generate_story= generate_story_from_image(pil_images,story_style)
                if "error" in generate_story or "failed" in generate_story or "API key" in generate_story:
                    st.error(generate_story)
                else:
                    st.subheader(f"your {story_style} story :")
                    st.success(generate_story)
                st.subheader("Listen your story :🎶")
                audio_file =narrate_story(generate_story)
                if audio_file:
                    st.audio(audio_file,format="audio/mp3")

            except Exception as e:
                st.error(f"An application error occorred {e}")






