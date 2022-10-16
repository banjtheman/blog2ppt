import streamlit as st
import requests
###
# Streamlit Main Functionality
###

BLOG2PPT_API = "https://ixdgqj6lrhyzndf3cu2ase6pfy0adgxb.lambda-url.us-east-1.on.aws/"


def sidebar() -> None:
    """
    Purpose:
        Shows the side bar
    Args:
        N/A
    Returns:
        N/A
    """

    st.sidebar.header(f"Dev.to blog2ppt")
    st.sidebar.image("https://d2fltix0v2e0sb.cloudfront.net/dev-black.png")


def app() -> None:
    # Spin up the sidebar
    sidebar()

    st.header("Convert dev.to blog posts to PowerPoints")
    # st.snow()

    dev_to_article = st.text_input("Enter dev.to article link")

    if st.button("Convert Blog Post"):

        if dev_to_article:

            if not dev_to_article.startswith("https://dev.to/"):
                st.error("Not a dev.to link")
                return

            try:
                with st.spinner("Converting..."):
                
                    data = {"blog_url":dev_to_article}
                    rep = requests.post(BLOG2PPT_API,json=data)
                    rep_json = rep.json()


                    if "powerpoint_url" in rep_json:
                        powerpoint_url = rep_json["powerpoint_url"]
                        st.success("PowerPoint created")
                        st.markdown(f'<a href={powerpoint_url}>{powerpoint_url}</a>',unsafe_allow_html=True)
                        
                    else:
                        st.error(f"Error with url {dev_to_article}")



            except Exception as error:
                st.error(error)
                st.error("Conversion failed")
        else:
            st.error("Enter valid url")


def main() -> None:
    # Start the streamlit app
    app()


if __name__ == "__main__":
    main()
