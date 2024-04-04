import streamlit as st
import os
import cv2
import time
from image_processor.utils import draw_bounding_boxes, find_face

# Create a folder to store uploaded images
USER_DB = "pluralDB/users/"
PHOTO_DB = "pluralDB/photos/"
os.makedirs(USER_DB, exist_ok=True)
os.makedirs(PHOTO_DB, exist_ok=True)


# Add User Page
def add_user_page():
    st.title("Add User")
    name = st.text_input("Enter Name")
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if st.button("Add User"):
        if uploaded_file is not None and not os.path.exists(uploaded_file.name):
            # Save the uploaded image with the given name
            file_path = os.path.join(USER_DB, f"{name}.{str(time.time())}.jpg")
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success("User added successfully!")
        else:
            st.warning("Please upload an image.")


# Find User Page
def find_user_page():
    st.title("Find User")
    uploaded_file = st.file_uploader("Upload Photo", type=["jpg", "jpeg", "png"])

    if st.button("Find User"):
        if uploaded_file is not None:
            # Process the uploaded photo using OpenCV
            file_path = os.path.join(PHOTO_DB, f"uploaded_photo_{str(time.time())}.jpg")
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Perform OpenCV operations on the uploaded photo
            # Replace the following code with your own OpenCV logic
            img = cv2.imread(file_path)
            results = find_face(img)
            result_img = draw_bounding_boxes(results, img)
            result_img = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)
            st.image(result_img, caption="Processed Photo", use_column_width=True)

            # Display results as a table
            st.subheader("Results")
            st.write(results)
                
            
        else:
            st.warning("Please upload a photo.")


# Main App
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Add User", "Find User"))

    if page == "Add User":
        add_user_page()
    elif page == "Find User":
        find_user_page()


if __name__ == "__main__":
    main()
