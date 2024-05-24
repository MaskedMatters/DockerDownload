import os
from extras import *

# VARIABLE SETTING & INIT
term_size = os.get_terminal_size()

# DOWNLOAD/INSTALL STARTUP
page_1 = ["This python script makes it easier for people new to Docker, Linux, or just someone "
          "who doesn't want to deal with the install process easier! Do you want to go with the "
          "express install or custom install?", 
          
          "Express Install (Recommended)",
          
          "Custom Install"]

new_page(term_size, page_1)