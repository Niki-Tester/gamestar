# **GAME REVIEW**

![Readme Landing Image](doc/images/amiresponsive.webp)

# **Project Overview**

The aim behind this project is to demonstrate my skills in the following areas:

* **Data handling**: Build a Relational Database backed Flask project for a web application that allows users to store and manipulate data records about a particular domain.

* **Database structure**: Design a database structure well-suited for my domain. Using relationships between records of different entities.

* **User functionality**: Create functionality for users to create, locate, display, edit and delete records (CRUD functionality).

* **Use of technologies**: Use HTML and custom CSS for the website's front-end, and Python for the back-end.

* **Structure**: Incorporate a main navigation menu and structured layout using Materialize.

* **Documentation**: Write a README.md file for your project that explains what the project does and the value that it provides to its users.

* **Version control**: Use Git & GitHub for version control.

* **Deployment**: Deploy the final version of your code to a hosting platform such as Heroku.

* **Testing**: Test and deploy frontend web application to a cloud platform, using Test Driven Development.

---

# **User Experience (UX)** 

## **User Stories**:

* ### First Time Visitor Goals:
  * As a first time visitor, I want to easily understand the main purpose of the site.

  * As a first time visitor, I want to be able to navigate the site to find content easily.

  * As a first time visitor, I want to be able to create a new account.

  * As a first time visitor, I want to be able to search for a game, and read reviews left by other users.

* ### Returning Visitor Goals:
  * As a returning visitor, I want to find reviews on games I haven't played yet.

  * As a returning visitor, I want to leave reviews on games I have played.

  * As a returning visitor, I want to login to my user profile.

* ### Frequent Visitor Goals:
  * As a frequent visitor, I want to update my review to reflect my view on the game since the last time the game was updated.

  * As a frequent visitor, I want to remove a review that I feel no longer applies to the game.

  * As a frequent visitor, I want to change my account password.

---

# **Frontend Design**

## **Colours**:

These are the main colours used throughout the project:

  * ![#212121](https://via.placeholder.com/15/212121/000000?text=+) `#212121`
  * ![#999](https://via.placeholder.com/15/999/000000?text=+) `#999`
  * ![#FFF](https://via.placeholder.com/15/FFF/000000?text=+) `#FFF`
  * ![#64B5F6](https://via.placeholder.com/15/64B5F6/000000?text=+) `#64B5F6`
  * ![#03A9F4](https://via.placeholder.com/15/03A9F4/000000?text=+) `#03A9F4`
  * ![#F8CE0B](https://via.placeholder.com/15/F8CE0B/000000?text=+) `#F8CE0B`

  A contrast grid was used to ensure that the contrast between background and forground elements are compliant with WCAG 2.0 minimum contrast [Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23212121%0D%0A%23999%0D%0A%23FFF%0D%0A%2364B5F6%0D%0A%2303A9F4%0D%0A%23F8CE0B%0D%0A&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp).

  ![Contrast Grid Image](doc/images/contrast_grid.png)

## **Typography**:
  * Two fonts are used throughout the project, Roboto is used for all main text. With Saira Stencil One being used for headings. Sans Serif as the fallback font in case for any reason the font is not being imported into the site correctly.

## **Imagery**:
  * Imagery is especially important in this project, the background image is used throughout the website, with the execption where a game review is being displayed, and a game image is available.

## **Features**

### **Home Page**:

  This is the page that the user will be greeted with upon arriving at the site. This page will consist of a navigation bar along the top, containint the website name, as well as links to other pages within the web app.

### **Register Page**:

  This page will be available by clicking the register link in the naviagion bar/menu. A user will be able to create a profile by choosing a username, and setting a password. 

  If a user chooses a username that already exists, or the passwords do not match, they will be presented the relevant flash message.

### **Log In Page**:

  This page will be available by clicking the login link in the naviagion bar/menu. A user will be able to log in to a previously created user profile.

  If a user enteres a username that does not exist, or the if password is incorrect, they will be presented with the flash message "Username/Password combination not recognised".

### **User Profile Page**:

  This page will be available by clicking the profile link in the naviagion bar/menu, allowing a user to change their password by first confiriming their current password, followed by entering their new password and matching confirm password.

### **Manage Reviews Page**:

  This page will be available by clicking the manage reviews link in the naviagion bar/menu.

  On this page a user with be greeted by one of two outcomes.

  1. If a user has not submitted any reviews, the page will display "You have not added any reviews yet". Followed by a prompt to add a review.

  2. If a user has submitted a review, this page will display a list of the reviews they have created, each with a link to the review, along with the option to delete or edit their review.

### **Add Game Page**:

  This page will be available by clicking the add review link/button found on the home page if the user is logged in, or via the Manage Reviews page.

  Once loaded the user will be greeted with a search bar, allowing the user to enter the name of a game they wish to leave a review for.

  This will make a request to the IGDB api, returning a list of games matching the users search criteria.

  Each game returned from the api will generate a collapsable list containing the game cover art, game name and a summary of the game.

  The user will also find a button prompting them to add the game.

### **Add Review Page**:

  This page will be available by clicking the add game button found in the collapsible list of the relevant game from the Add Game Page.

  Once loaded the user will be greeted with a form asking them to give their review a heading, what they liked about the game, what they disliked about the game and how many hours they played the game.

  The user will then be asked "How do you rate" the game, and will be presented with a range slider that has a range between 0-5. When the user activates the slider, they will all so that the "rating stars" will update dynamically with the value of the range slider.

  The user will then need to click the submit button in order for their review to be saved. This will submit their review and return them to the home screen, displaying a flash message if the review has/not been successfully created.

### **Game Review Page**:

  This page will be visible after a user selects to view reviews on a particular game, displayed on the home page.

  At the top of the page there will be an image depicting the game cover art, with a heading displaying the name of the game along side the image and below the heading will be the official summary of the game.

  Under the heading described above, will be each review a user has created.

  Within the review a user will find the username of the user that left the review along with a time stamp, under which will be the rating and review text left by that user.

  At the very bottom of each review, will be a like and dislkie button and counter.

## **Wireframes**
  To organize and streamline the development process, I created wireframes for this project, to help me during the development process and to prevent scope creep.

  Below are links to each wireframe page of the project, created to cover both Mobile and Desktop versions.

### **Mobile Wireframes**:

  **Home Page**:

  ![Homepage](/doc/Wireframes/Mobile/Home.png)

  **User Registration**:

  ![Register](/doc/Wireframes/Mobile/Register.png)

  **User Login**:

  ![Login](/doc/Wireframes/Mobile/Login.png)
  
  **User Profile**:

  ![User_Profile](/doc/Wireframes/Mobile/User_Profile.png)

  **Manage Reviews (No Reviews)**:

  ![Game_Review_No_Reviews](/doc/Wireframes/Mobile/Manage_Reviews_No_Reviews_Found.png)

  **Manage Reviews**:

  ![Manage_Reviews](/doc/Wireframes/Mobile/Manage_Reviews.png)

  **Add Game**:

  ![Add_Game](/doc/Wireframes/Mobile/Add_Game.png)
  
  **Add Review**:

  ![Add_Review](/doc/Wireframes/Mobile/Add_Review.png)
  
  **Game Review**:

  ![Game_Review](/doc/Wireframes/Mobile/Game_Review.png)


### **Desktop Wireframes**:

  **Home Page**:

  ![Homepage](/doc/Wireframes/Desktop/Home.png)

  **User Registration**:

  ![Register](/doc/Wireframes/Desktop/Register.png)

  **User Login**:

  ![Login](/doc/Wireframes/Desktop/Login.png)
  
  **User Profile**:

  ![User_Profile](/doc/Wireframes/Desktop/User_Profile.png)

  **Manage Reviews (No Reviews)**:

  ![Manage_Reviews_No_Reviews](/doc/Wireframes/Desktop/Manage_Reviews_No_Reviews_Found.png)

  **Manage Reviews**:

  ![Manage_Reviews](/doc/Wireframes/Desktop/Manage_Reviews.png)

  **Add Game**:

  ![Add_Game](/doc/Wireframes/Desktop/Add_Game.png)
  
  **Add Review**:

  ![Add_Review](/doc/Wireframes/Desktop/Add_Review.png)
    
  **Game Review**:

  ![Game_Review](/doc/Wireframes/Desktop/Game_Review.png)

---

# **Database Schema**
  
  Using drawSQL i created custom models, which I predicted would be required when building the website. 

  In order for users to create reviews custom user, game and review models are required, the user id will be used as a foreign key in the review model, along with the game id being used as a foreign key also in the review model.

  ![Database_Schema](/doc/images/drawSQL-export.png)

---

## **Technologies Used**:
  * [HTML5](https://en.wikipedia.org/wiki/HTML5)
  * [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
  * [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  * [MongoDB](https://en.wikipedia.org/wiki/MongoDB)

## **Frameworks, Libraries and Programs Used**:

  1. [Google Fonts](https://fonts.google.com/):
    Google fonts was used to import the 'Roboto' & Saira Stencil One fonts into the style.css file which is used on all pages throughout the project.

  1. [Font Awesome](https://fontawesome.com/):
    Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.

  1. [Git](https://git-scm.com/):
    Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

  1. [GitHub](https://github.com/):
    GitHub is used to store the projects code after being pushed from Git.

  1. [Balsamiq](https://balsamiq.com/):
    Balsamiq was used to create the wireframes during the design process.

  1. [GitPod](https://gitpod.io/):
    Open-source developer platform used for development.

## **Deployment**

  ### **Heroku**
  Before you can deploy your app to Heroku, initialize a local Git repository and commit your application code to it.

  #### **Create a Heroku Remote**
  Git remotes are versions of your repository that live on other servers. You deploy your app by pushing its code to a special Heroku-hosted remote that’s associated with your app.

  #### **For a New App**:

  The heroku create CLI command creates a new empty application on Heroku, along with an associated empty Git repository. If you run this command from your app’s root directory, the empty Heroku Git repository is automatically set as a remote for your local repository.

      heroku create -a gamestar-app

  You can use the "git remote -v" command to confirm that a remote named heroku has been set for your app.

  #### **For an Existing App**:

  Add a remote to your local repository with the heroku git:remote command. All you need is your Heroku app’s name:

      heroku git:remote -a gamestar-app

  #### **Deploy Your Code**:
  To deploy your app to Heroku, use the "git push" command to push the code from your local repository’s main branch to your heroku remote. For example:

      git push heroku main

  Use this same command whenever you want to deploy the latest committed version of your code to Heroku.

  Heroku only deploys code that you push to the master or main branches of the remote. Pushing code to another branch of the heroku remote has no effect.

  ---

  ### **Forking the GitHub Repository**
  By forking the GitHub Repository you make a copy of the original repository on your GitHub account to view and/or make changes without affecting the original repository.

  You can do this by completing the following steps:

  1. Log in to GitHub and locate the GitHub Repository
  1. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
  1. You should now have a copy of the original repository in your GitHub account.

  ---

  ### **Making a Local Clone**:
  1. Log in to GitHub and locate the GitHub Repository
  1. Under the repository name, click "Clone or download".
  1. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
  1. Open Git Bash
  1. Change the current working directory to the location where you want the cloned directory to be made.
  1. Type git clone, and then paste the URL you copied in Step 3.

  
    $ git clone https://github.com/Niki-Tester/gamestar.git
  

### **Link to deployed website**:
[Heroku - GameStar](https://gamestar-app.herokuapp.com/)