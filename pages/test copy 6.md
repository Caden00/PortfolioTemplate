title: Final Project Report
date: 22 Jul 21
author: Caden Aragon
image:
video: 
description: This is my final project report

# 1
For this project, I designed a portfolio template website. The idea is that anyone in need of a portfolio website would be able to alter the basic template to their needs. There is also a blog functionality that allows the user to update others about their lives, projects, etc.. Currently to get this project running, the project zip would need to be downloaded from Github at [https://github.com/Caden00/PortfolioTemplate](https://github.com/Caden00/PortfolioTemplate). Then, in a terminal or command prompt, the user needs to navigate to the project directory. From here, the virtualenv will need to be activated. To activate in a unix terminal simply type `source env/bin/activate`. Windows should be the same except “source env\bin\activate. For any issues or questions, refer to [https://docs.python.org/3/tutorial/venv.html](https://docs.python.org/3/tutorial/venv.html) on more information on how to do this. Finally, the user can call “python3 app.py”, which will deploy a local flask server. You should then see in the terminal that the server is running on the local host. Now, the user can navigate to [http://localhost:5000/](http://localhost:5000/) access the site in your preferred web browser.

# 2
The components developed are the app.py which is the flask python application that is hosting the backend of the site. The front end is using the html which is held within the templates folder. Lastly, some formatting is done with css in the static folder. Upon testing, all the basic functionality for the site works. I had designed the site to work with a static blog to begin with to ensure functionality. I have had some issues with making blog posts from the site so there are those minor errors here. Upon using all pages associated with the website, I have not run into any errors.

# 3
The main modules of the project are the home, about, blog, and resume page. Each page has a somewhat unique interface. Some aspects of the page are inherited from page to page, such as the header. There is a layout file that handles this across the site. A major change to the future is adding in the user login capability to make posts to the blog from the site. This is not currently fully implemented. The module for the blog is however setup to handle this. So for the time being, adding blog posts must be done on the backend. The site does react to this dynamically. When the site recognizes this, the page will alter to handle this.

# 4
Some of the functions that are abstractions would be the Flask functions. These take the base class of some of the Flask classes and some abstractions are applied. Any of the functions within Python are going to be dynamic as the compiler does not check the data types until runtime. There could be errors if a data type is not set correctly. An extension in the future will be to the blogging functionality. I would like to be able to make more styles of cards and have more functionality on the posts. The general class of this can be reused. The overall “card” class will be inherited by the new card classes to implement the variations.

# 5
For reusability, the functions related to the blog, base template for the HTML, and page implementations. Some of the functions for the blog can be later reused to expand on this feature. The base for how a blog is created is also reused from old posts to new posts. On the HTML side, the base template is inherited by all the pages. This template brings the header and a few other components that are standard on each page. If there is a need for new pages in the future, the main class can be inherited to any new page.


