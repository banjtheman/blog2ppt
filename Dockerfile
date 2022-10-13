FROM python:3.9

WORKDIR /home

# Add files
ADD requirements.txt /home/
ADD blog2ppt_st.py /home/
ADD html_scrape_play.py /home/
ADD utils.py /home/

# Install deps
RUN apt-get update && apt-get install chromium -y
RUN pip install -r requirements.txt

# Install carbon
RUN git clone https://github.com/StarkBotsIndustries/Carbon.git
RUN cd Carbon/ && python setup.py install && cd ..

# Make dirs
RUN mkdir -p /home/ppts/
RUN mkdir -p /home/downloaded_images/

# Expose port
EXPOSE 8501

# Start App
CMD [ "streamlit", "run" ,"blog2ppt_st.py" ]