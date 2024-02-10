import streamlit as st
import pandas as pd
import os

def load_table(table_path):
    """
    Function to load a table from a given path
    """
    table_data = pd.read_csv(table_path)
    return table_data

def main():
    st.title('Image and Table Display')

    # Define the directory path where the image and table are stored
    directory_path = "./"

    # List all files in the directory
    files = os.listdir(directory_path)

    # Filter out image and table files
    image_files = [file for file in files if file.endswith(('.jpg', '.jpeg', '.png'))]
    table_files = [file for file in files if file.endswith('.csv')]

    # print("image_files,table_files",image_files,table_files)
        
    # Select an image and table file
    selected_image = st.selectbox("Select Image", image_files)
    selected_table = st.selectbox("Select Table", table_files)

    # print(selected_image,selected_table)
    
    # Display the selected image
    image_path = os.path.join(directory_path, selected_image)
    st.image(image_path)

    # Display the selected table
    table_path = os.path.join(directory_path, selected_table)
    table_data = load_table(table_path)
    st.write("Table Data:")
    st.write(table_data)
    
    link_text = "Click here for more information"
    link_url = "https://example.com/more_info"
    st.markdown(f'<a href="{link_url}" target="_blank">{link_text}</a>', unsafe_allow_html=True)
    

if __name__ == '__main__':
    main()

# import streamlit as st
# import pandas as pd
# import os
# import requests

# def load_image(image_path):
#     """
#     Function to load an image from a given path
#     """
#     with open(image_path, "rb") as f:
#         image = f.read()
#     return image

# def load_table(table_path):
#     """
#     Function to load a table from a given path
#     """
#     table_data = pd.read_csv(table_path)
#     return table_data

# def main():
#     st.title('Image and Table Display')

#     # Define the directory path where the image and table are stored
#     directory_path = "./"

#     # List all files in the directory
#     files = os.listdir(directory_path)
#     print(files)
#     # Filter out image and table files
#     image_files = [file for file in files if file.endswith(('.jpg', '.jpeg', '.png'))]
#     table_files = [file for file in files if file.endswith('.csv')]

#     # Select an image and table file
#     selected_image = st.selectbox("Select Image", image_files)
#     selected_table = st.selectbox("Select Table", table_files)

#     # Display the selected image
#     image_path = os.path.join(directory_path, selected_image)
#     st.image(load_image(image_path))

#     # Display the selected table
#     table_path = os.path.join(directory_path, selected_table)
#     table_data = load_table(table_path)
#     st.write("Table Data:")
#     st.write(table_data)

# if __name__ == '__main__':
#     main()
