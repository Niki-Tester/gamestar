
## **During Development Testing**
During the development process, manual testing was carried out in the following ways:-

1. Manually tested each element responsiveness and appearance by running the application from the terminal, and opening the development browser.

1. Published the page on Heroku and shared with peers for testing and for them to provide feedback.

### **Manual Testing:**
* During testing, I used four different browsers to ensure cross-compatibility. The desktop browsers used by myself were:

  1. Chrome
  1. Firefox  
  1. Edge
  1. Safari

- Using devtools to simulate different screen sizes/devices down to 280px in width, allowed me to test responsiveness. 
- Additionally I used an iPhone 11 with Safari / Chrome browser, and Samsung Galaxy S21 with the Chrome browser, for further testing.

### **Testing User Stories from User Experience (UX) Section**

## **User Stories**:

* ### First Time Visitor Goals:
  * As a first time visitor, I want to easily understand the main purpose of the site.
   - When the user first visits the page, they are greeted with the main logo for the website, with a the tagline "Your place for video game reviews"
   - Scrolling to the bottom of the page the user will see a short "About Gamestar" proving the user with further information on what this website is about.

  * As a first time visitor, I want to be able to navigate the site to find content easily.
    - Responsive design is employed across all pages to deliver a satisfying UX on mobile, tablet, laptop and large desktop PC displays. Where the Nav elements are easily reachable regardless of screen size, with the elements collapsing into a menu for small screens

    - The navigation bar is displayed on all pages and is available regardless of the platform the user is using.

    - The user is able to click on the logo in the navigation bar at any time, this will return them back to the home screen.


  * As a first time visitor, I want to be able to create a new account.
    - Available from the navigation bar is a link to the registration page, along with other user prompts on the pages the user can view that does not require them to register or be logged in.

  * As a first time visitor, I want to be able to look through the games, and read reviews left by other users.
    - When the user selects a game from the home page, they are taken to a page displaying the game image, game name, and a brief summary of the game (if available), followed by a list of reviews that have been left by users. When a user clicks on one of the available reviews, a modal is opened displaying the full review information.

* ### Returning Visitor Goals:
  * As a returning visitor, I want to find reviews on games I haven't played yet.
    - When a user returns, they will be presented with a list of games, in the form of MaterializeCSS cards, displaying the game image, game name, and it's average rating.

    - If there are more than 24 games available, the list will be paginated, and the user is able to move between pages using the links at the bottom of the page. These links are not displayed if there are less than 25 games.

  * As a returning visitor, I want to login to my user profile.
    - When a user returns, they are able to log in by clicking the "Log In" link found in the navigation bar, or via the various user prompts through out the visible pages.

  * As a returning visitor, I want to leave reviews on games I have played.
    - When a user returns, provided they are logged in, they are presented with an "Add Review" button on the Home page.
    - If the user has not yet created a review, they are prompted to add a review within the Manage Review page.
    - If the user has previously created a review, they are also given the open to add a review using the "Add Review" button found on the Manage Review page.
    - If the user is viewing reviews for a particular game, the "Add Review" button will allow them to add a review to the currently displayed game.

  * As a returning visitor, I want to view the reviews I have created.
    - When a user returns, provided they are logged in, they are presented with a "Manage Review" link in the navigation bar, this is available site wide, and can be clicked at any time. Doing so will present the user with a page displaying all the reviews that they have created, in a style to match that of the home page.

  * As a returning visitor, I want to like reviews by other users.
    - When a user returns, they are able to view reviews left by other users. when the user chooses a review to view, the review is opened in a modal. Within the modal footer the user will see a "Like" button. When this button is clicked the users like is immediately registered and the counter is incremented by 1, this is further fed back to the user by the like icons color changing to yellow.

* ### Frequent Visitor Goals:
  * As a frequent visitor, I want to update my review to reflect my view on the game since the last time the game was updated.
    - When a frequent user returns, they are able to view their reviews on the "Manage Reviews" page. This page will display a list of reviews the user has created. When the user clicks on the "View" button a modal is opened, displaying their review. Within the modal footer, the user will see an "Edit" button giving them the option to edit their review. Clicking this button the user will be taken to the "Edit Review" page, styled to match the "Add Review" page, where all the input fields are pre-filled with their review data, allowing them to easily make changes to their review. For ease of access the user is also able to select the "Edit" button on any page that displays their review.

  * As a frequent visitor, I want to remove a review that I feel no longer applies to the game.
    - When a frequent user returns, they are able to view their reviews on the "Manage Reviews" page. This page will display a list of reviews the user has created. When the user clicks on the "View" button a modal is opened, displaying their review. Within the modal footer, the user will see a "Delete" button giving them the option to delete their review. Clicking this button the user will be prompted with a "Are You Sure" modal, providing feedback to the user that this is irreversible. For ease of access the user is also able to select the "Delete" button on any page that displays their review.

  * As a frequent visitor, I want to change my account password.
    - When a frequent user returns, they are given the option to view their user profile by clicking the "Profile" link in the navigation bar/menu. When the user clicks this link they are presented with a page displaying their username as a page heading, along with a form for the user to change their password. Once the user has completed all input fields the user will see the "Change Password" button change color, allowing them to click this button and change their password. Provided that the current password is correct, and that the new password / confirm password match, the users password will be updated, and is notified by a MaterializeCSS toast message advising the change was successful, if there was an error changing the password this will also by highlighted to the user in the form of a toast message.

  * As a frequent visitor, I want to view all reviews a particular user has created.
    - When a frequent user returns, they are able to view reviews by selecting a game from the home screen, and then clicking on a review they would like to view. While the using has the review modal open they will find the name of the user that created the review within the modal footer. When the user clicks on the users name, they are presented with a page displaying the selected users username as a page heading, along with a list of all the reviews that user has created. The user will then be able to click the "View" button on any of these reviews, to view the review in more detail.

  * As a frequent visitor, I want to remove my like from a review.
    - When a frequent user returns, they are able to view reviews left by other users. When the user chooses a review to view, the review is opened in a modal. Within the modal footer the user will see the "Like" button. When this button is clicked the users like is immediately removed and the counter is decremented by 1, this is further fed back to the user by the like icons color changing to to white.

  * As a frequent visitor, I want to delete my profile.
    - When a frequent user returns, they are given the option to view their user profile by clicking the "Profile" link in the navigation bar/menu. When the user clicks this link they are presented with a page displaying their username as a page heading, along with a section highlighted in red (to signify danger) containing a button displaying a user icon with an "X" next to it. Once the user clicks the "Delete User Profile" button, they are presented with an "Are You Sure" modal, where they are advised that "Deleting your profile will remove all user data including any reviews that you have created.", and that their username will be open to be used by another user. Finally they are warned that "This Action Is Not Reversible". The user is presented with a "Yes" / "No" button, clicking the "Yes" button immediately deletes the users profile, and any reviews they have created, the user is then returned to the "Home" page, where a MaterializeCSS toast message is displayed confirming their profile has been deleted, this destroys the users session data, and the user is logged out.

* ### Admin Goals:
  * As an Admin, I want to view a list of all registered users.
    - When the admin is logged in, they are presented with an addition button in the navigation bar/menu, labeled "Admin". Clicking this button the admin is presented with a drop down menu, containing a link to the "User Manager" page. The admin will then be presented with a list of users with each user being displayed as a separate MaterializeCSS card.

  * As an Admin, I want to view a list of all reviews created.
    - When the admin is logged in, they are presented with an addition button in the navigation bar/menu, labeled "Admin". Clicking this button the admin is presented with a drop down menu, containing a link to the "Review Manager" page. The admin will then be presented with a list of all reviews created, each with their own button allowing the admin to view the review. Upon clicking the view review button, the admin is presented with a modal, displaying the full review.

  * As an Admin, I want to remove a user.
    - When the admin is logged in, they are presented with an addition button in the navigation bar/menu, labeled "Admin". Clicking this button the admin is presented with a drop down menu, containing a link to the "User Manager" page. The admin will then be presented with a list of users, each with their own button allowing the admin to delete that user. Upon clicking the delete user button, the admin is presented with an "Are You Sure" modal, where they are advised that "Deleting this profile will remove all user data including any reviews that they have created.", and that their username will be open to be used by another user. Finally they are warned that "This Action Is Not Reversible". The admin is presented with a "Yes" / "No" button, clicking the "Yes" button immediately deletes the users profile, and any reviews they have created, and this is fed back to the admin in the form of a MaterializeCSS toast message.

  * As an Admin, I want to edit a review.
      - When the admin is logged in, they are presented with an addition button in the navigation bar/menu, labeled "Admin". Clicking this button the admin is presented with a drop down menu, containing a link to the "Review Manager" page. The admin will then be presented with a list of all reviews created, each with their own button allowing the admin to view the review. Upon clicking the view review button, the admin is presented with a modal, displaying the full review. In the footer of the review the admin will have the option to edit the review using the "Edit" button. When click this will take the admin to the "Edit Review" page, allowing them to make the required changed, and resubmit the review.

  * As an Admin, I want to remove a review.
      - When the admin is logged in, they are presented with an addition button in the navigation bar/menu, labeled "Admin". Clicking this button the admin is presented with a drop down menu, containing a link to the "Review Manager" page. The admin will then be presented with a list of all reviews created, each with their own button allowing the admin to view the review. Upon clicking the view review button, the admin is presented with a modal, displaying the full review. In the footer of the review the admin will have the option to edit the review using the "Delete" button. Upon clicking the delete review button, the admin is presented with an "Are You Sure" modal, where they are advised that "This Action Is Not Reversible". The admin is presented with a "Yes" / "No" button, clicking the "Yes" button immediately deletes the review, which is fed back to the admin in the form of a MaterializeCSS toast message.

  * As an Admin, I want to change my account password.
    - When the admin is logged in, they are given the option to view their users profile by clicking the "Profile" link in the navigation bar/menu. When the admin clicks this link they are presented with a page displaying their username (admin) as a page heading, along with a form for the admin to change their password. Once the admin has completed all input fields they will see the "Change Password" button change color, allowing them to click this button and change their password. Provided that the current password is correct, and that the new password / confirm password match, the admins password will be updated, this is notified to the admin by a MaterializeCSS toast message advising the change was successful, if there was an error changing the password this will also by highlighted to the admin in the form of a toast message.


### **Code Validation:**

The W3C Markup Validator, W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project, along with JsHint for validating all Javascript used, along with PEP8 for all Python code.

---

 [W3C Markup Validator](https://validator.w3.org/)
  - The following errors were corrected after running the validator on each page of the web app.

    - img element without alt attribute - This was corrected by adding the alt attribute to the HTML template with the attributes property updated dynamically based on the game name
      - File - manage.html
      - Route - /manage
      - Commit - [aac622687832f038e8d5602af290951719d23b79](https://github.com/Niki-Tester/gamestar/commit/aac622687832f038e8d5602af290951719d23b79)

    - div not allowed as child of ul - This was corrected by creating a second for loop for each review so that the modal is created outside of the ul element.
      - File - review_manager.html
      - Route - /review_manager
      - Commit - [4b573a66e1b27048c58dda28974279ab68121d90](https://github.com/Niki-Tester/gamestar/commit/4b573a66e1b27048c58dda28974279ab68121d90)
    
    - Elements with duplicate ids - This was corrected by removing the id attribute from the element, as the id was not being used for any styling or validation, so it was not required.
      - File - user_manager.html
      - Route - /user_manager
      - Commit - [4b573a66e1b27048c58dda28974279ab68121d90](https://github.com/Niki-Tester/gamestar/commit/4b573a66e1b27048c58dda28974279ab68121d90)

---

 [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
   The W3C CSS Validator did not show any errors after corrections were made, but did display the below warnings. But these selectors are required for changing the scroll bar styling on compatible browsers, so were left unchanged.

    -webkit-scrollbar is a vendor extended pseudo-element
    -webkit-scrollbar-thumb is a vendor extended pseudo-element
    -webkit-scrollbar-track is a vendor extended pseudo-element
    -webkit-slider-thumb is a vendor extended pseudo-element
    -moz-range-thumb is a vendor extended pseudo-element
    -ms-thumb is a vendor extended pseudo-element
  
  One error was corrected after validating my custom CSS, where the alpha value of a rgba() property was set to "5" instead of "0.5", this was also later updated to a hex value, as this did not require an alpha value to match styling.

  Commit - [53f52c9d6c2cc525e0381f4f6b3c80841bef074f](https://github.com/Niki-Tester/gamestar/commit/53f52c9d6c2cc525e0381f4f6b3c80841bef074f)

--- 

[JsHint](https://jshint.com/) - Which returned some errors for missing semicolons, these were correct and now show no errors. It is important to note that the /*jshint esversion: 6 */ flag should be used when testing via JsHint. You do this by placing this comment on line 1 of the index.js file.

File - userSearch.js | Commit - [95b2cec4f379ce7dc734f04a64ffccbf65403bac](https://github.com/Niki-Tester/gamestar/commit/95b2cec4f379ce7dc734f04a64ffccbf65403bac)

File - searchGames.js | Commit - [4b4f5e5d4da29d13da38cec74d21a66b908fc905](https://github.com/Niki-Tester/gamestar/commit/4b4f5e5d4da29d13da38cec74d21a66b908fc905)

File - passwordValidation.js | Commit - [31c00fc5c1bb1845851774ea015abcb21309650a](https://github.com/Niki-Tester/gamestar/commit/31c00fc5c1bb1845851774ea015abcb21309650a)

---

[PEP8](http://pep8online.com/) - Which returned only one error, relating to the gamestar import within \_\_init__.py file. This is required to be placed at the bottom of the file as routes requires the use of the db variable previously declared. 

To stop the linter highlighting this as a syntactical error, ```# flake8: noqa pylint: disable = wrong-import-position``` was placed as a comment above the syntax which remains in the project to advise any future developers that this is not an error.

---

[Return to README](/README.md)