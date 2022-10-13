import streamlit as st
import html_scrape_play as blog2text_funcs
import asyncio

###
# Streamlit Main Functionality
###


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


async def app() -> None:
    # Spin up the sidebar
    sidebar()

    st.header("Convert dev.to blog posts to PowerPoints")
    # st.snow()

    dev_to_article = st.text_input("Enter dev.to article link")
    if st.button("Convert Blog Post"):

        if dev_to_article:
            try:
                with st.spinner("Converting..."):
                    print("Getting sections")
                    blog_sections, num_sections = blog2text_funcs.get_html_sections(
                        dev_to_article
                    )
                    print("Sections Converted")

                    prog_bar = st.progress(0.0)

                    ppt = await blog2text_funcs.convert_sections_to_ppt(
                        blog_sections, num_sections, prog_bar
                    )
                    # TODO will need to make unquie name
                    # Could just use uuids i guess?
                    # too dangerous to let people enter name
                    ppt.save("ppts/end_to_end_st.pptx")

                    st.success("Created power point!!!")

                    with open("ppts/end_to_end_st.pptx", "rb") as file:
                        btn = st.download_button(
                            label="Download PowerPoint",
                            data=file,
                            file_name="end_to_end_st.pptx",
                        )

            except Exception as error:
                st.error(error)
                st.error("Conversion failed")
        else:
            st.error("Enter valid url")


async def main() -> None:
    # Start the streamlit app
    await app()


if __name__ == "__main__":
    asyncio.run(main())
