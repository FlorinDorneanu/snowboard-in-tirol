# Snowboard in Tirol Blog

Welcome to the Snowboard in Tirol Blog! This Django-based platform captures the thrill and excitement of snowboarding adventures in the breathtaking landscapes of Tirol. Users can explore captivating blog posts, leave comments, and show appreciation by liking their favorite stories.

You can view the live website [here](https://snowboard-in-tirol-1614d9ced980.herokuapp.com/).

## UX

### Project Goal

The Snowboard in Tirol Blog aims to create a platform where snowboarding enthusiasts can connect and share their experiences. Whether you're a seasoned snowboarder or someone curious about the sport, this blog provides a space to read exciting stories and engage with the community.

### User Stories

- For users:
1. As a Site User I can view a paginated list of posts so that I can easily select a post to view.
2. As a Site User I can like or unlike a post so that I can interact with the content.
3. As a Site User I can leave comments on a post so that I can be involved in the conversations.
4. As a Site User I can register an account so that I can comment and like the posts.
5. As a Site User I can click on a post so that i can read the full text.
6. As a Site User I can view a list of posts so that i can select one to read.

- For Admin:
1. As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments.
2. As a Site Admin I can create draft posts so that I can finish writing the content later.
3. As a Site Admin I can create, read, update and delete posts so that I can manage my blog content.

- For users and admin:
1. As a Site User / Admin I can view comments on an individual post so that I can read the conversation.
2. As a Site User / Admin I can view the number of likes of each post so that i can see which is the most popular.

## Design Choices

### Colors

The color palette chosen for this project harmonizes with the white background, creating a clean and inviting visual environment. The main color selections are as follows:

- **Branded Blue (#728FCE)**: This shade of blue is used for the project's brand identity, adding a sense of professionalism and reliability.

- **Mauve Board (#804b6f)**: Mauve undertones are utilized to accent certain elements, lending a touch of refinement to the overall design.

- **Subtle Gray (#6c757d)**: The subtle gray color is employed for text links and non-emphasized content, ensuring clarity and legibility.

- **Lively Red (#D22B2B)**: The lively red hue is reserved for interactive elements, such as buttons, invoking energy and encouraging user engagement.

- **Transparent Footer (#0909FF)**: A semi-transparent blue shade is chosen for the footer, allowing it to blend seamlessly with the overall design while maintaining visibility.

These color choices complement the white background, contributing to a visually appealing and user-friendly web experience.

### Typography

The typography of this project has been thoughtfully selected to create a harmonious and legible reading experience. The primary fonts used throughout the design are:

- **Montserrat**: This font family is used for headings (h1, h2, h3, h4), imparting a modern and bold aesthetic that commands attention.

- **Merriweather**: For regular paragraphs and body text, 'Merriweather' is employed to provide an elegant and classic look, enhancing readability.

These font choices work together to create a visually appealing and engaging presentation of content, contributing to the overall aesthetic of the project.

### Responsiveness

To ensure that users can access and use the app seamlessly across various devices, the project follows responsive design principles:

- **Viewport Settings**: The `<meta name="viewport">` tag is set to control the page's scaling and responsiveness, making it mobile-friendly.

- **Bootstrap Grid**: The Bootstrap grid system is utilized to create responsive layouts and adapt content to different screen sizes.

Florin Dorneanu:
	👍🏾

+43 676 4869833:
	## Features/Structure

### Navigation

The navigation system is thoughtfully designed to provide a seamless and intuitive user experience. Key features of the navigation bar include:

- **Branding**: The top-left corner prominently showcases the brand name, establishing a strong visual identity for the website.

- **Responsive Toggle**: On smaller screens, a hamburger toggle button is employed to allow users to easily expand or collapse the navigation menu, ensuring optimal usability.

- **Clear Links**: Important sections such as "Home Page," "Register," and "Login" are presented as accessible navigation links. The navigation dynamically adjusts based on user authentication, displaying appropriate options like "Logout" or "Login" and "Register."

- **Subtle Muted Text**: A subtle muted text element at the end of the navigation bar adds a touch of elegance and provides context for the website's purpose.

- **Consistency and Adaptability**: The navigation bar maintains a consistent appearance across all pages, facilitating smooth transitions between different sections. Its responsive design guarantees a seamless experience across various devices, from desktop to mobile.

- **Color Harmony**: The navigation bar seamlessly integrates with the overall color scheme, contributing to a cohesive and visually appealing design.

The navigation system serves as a user-friendly guide, enabling effortless exploration of the website's features and content. Its well-structured design ensures easy access to essential elements, enhancing the overall user experience.

### Home Page

The home page provides an inviting and dynamic environment for users, encouraging them to explore captivating blog entries. Here's an overview of the key components and features of the home page template:

- **Dynamic Content Display**: The template dynamically fetches and displays a collection of blog entries. Each entry is thoughtfully presented in a card layout, providing a structured and organized display.

- **Engaging Imagery**: The template incorporates visually engaging featured images for each blog post. These images not only enhance the aesthetic appeal but also provide a glimpse into the content of the blog.

- **Author Attribution**: Underneath each featured image, the author of the post is prominently displayed. This attribution adds a personal touch, helping users connect with the creators behind the content.

- **Clear Navigation**: Each blog entry is presented with a title and an excerpt, giving users a concise preview of the content. Clicking on a post's title or excerpt seamlessly navigates users to the full blog post, promoting deeper engagement.

- **Publication Date and Likes**: The template includes the publication date of each post, accompanied by a heart icon representing the number of likes the post has received. This interactive element allows users to gauge the popularity of the content.

- **Responsive Pagination**: For blogs with multiple entries, responsive pagination ensures a user-friendly experience. Users can easily navigate between pages to access more blog posts.

The home page template's design encourages exploration, engagement, and a seamless user journey through captivating and relevant blog content.


### Post Detail Page

The post detail page delivers an immersive experience, allowing users to delve into a specific blog post's content and interact with various elements. Here's an overview of the essential components and functionalities of the post detail template:

- **Comprehensive Content Display**: The template showcases the selected blog post's full content, ensuring readers have access to a complete and detailed narrative.

- **Engaging Masthead**: The masthead section serves as an introduction, presenting the post's title, author, and featured image. This visually appealing header offers users a glimpse into the post's essence.

- **Interactive Post Interaction**: Users have the ability to like a blog post by clicking on a heart icon, enabling them to express their appreciation for the content. The template dynamically updates the like count, giving users insight into the post's popularity.

- **Comment Interaction**: The template includes a comment section where users can read and engage with others' thoughts on the blog post. Additionally, users can "like" comments, fostering a sense of community and interactivity.

- **Comment Submission**: Authenticated users can contribute to the conversation by leaving their own comments. The template provides a user-friendly comment form, enhancing engagement and encouraging meaningful discussions.

- **Success Message**: After submitting a comment, users receive a brief success message indicating that their comment is pending approval. This responsive feedback enhances the user experience and provides clarity.

The post detail template empowers users to explore, engage, and connect with the blog post's content, contributing to an enriched and interactive reading experience.

### Sign Up

- The "Sign Up" page allows new users to create an account, granting them access to additional features such as private checklists and task management.

### Login/Logout

- The "Login" page enables registered users to log in and access their personalized packing lists.
- Users can easily log out from the navigation bar, securing their account information.

### Features for Future Development

- **Nesting Comments**: I envision a dynamic commenting system that supports nested comments, enabling users to directly respond to specific comments. This feature would encourage more in-depth discussions, facilitate meaningful conversations, and foster a stronger sense of community within the blog. By introducing a threaded structure, users can easily follow and participate in various conversations, thereby elevating the overall user experience.

The incorporation of nested comments would contribute to a more comprehensive and interactive platform, empowering users to engage with each other in a structured and engaging manner. I am excited about the prospect of exploring this feature and enhancing the blog's value for our community.

## Testing

## Validation Testing

### HTML

### HTML

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the site. It was also used to validate the CSS. As the site is created with Django and utilises Django templating language within the HTML, I have checked the HTML by inspecting the page source and then running this through the validator.

| Page                                                            | Result |
| :-------------------------------------------------------------- | :----- |
| [Home Page](documentation/w3c-validator-homepage.png)                 | Pass   |
| [Post Detail](documentation/w3c-validator-post-detail.png)   | Pass   |
| [Login](documentation/w3c-validator-login.png)                        | Pass   |
| [Logout](documentation/w3c-validator-logout.png)                      | Pass   |
| [Sign up](documentation/w3c-validator-signup.png)                     | Pass   |


### CSS

[W3C](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to validate the CSS.

| File                                                  | Result |
| :---------------------------------------------------- | :----- |
| [static/css/style.css](documentation/w3c-validator-style.css.png) | Pass   |


### Python

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python code.

| File                                                          | Result |
| :------------------------------------------------------------ | :----- |
| **Snowboard In Tirol**                                             |
| [snowboard_in_tirol/urls.py](documentation/snowboard_in_tirol-urls.png)    | Pass   |
| **Snowboard BLog**                                          |
| [snowboard_blog/views.py](documentation/snowboard_blog-views.png)   | Pass   |
| [snowboard_blog/models.py](documentation/snowboard_blog-models.png) | Pass   |
| [snowboard_blog/forms.py](documentation/snowboard_blog-forms.png)   | Pass   |
| [snowboard_blog/admin.py](documentation/snowboard_blog-admin.png)   | Pass   |
| [snowboard_blog/apps.py](documentation/snowboard_blog-apps.png)   | Pass   |
| [snowboard_blog/urls.py](documentation/snowboard_blog-urls.png)   | Pass   |


## Manual Testing

### User Stories and Test Results

| User Story                                                                                                                          | Test                                                         | Result |
| ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ------ |
| 1. As a Site User, I can view a paginated list of posts so that I can easily select a post to view.                             | Navigate to the home page and observe the paginated list of posts. | Pass   |
| 2. As a Site Admin, I can approve or disapprove comments so that I can filter out objectionable comments.                      | Post a comment as a user, then log in as an admin and approve/disapprove the comment. | Pass   |
| 3. As a Site Admin, I can create draft posts so that I can finish writing the content later.                                    | Create a new post and save it as a draft.                    | Pass   |
| 4. As a Site Admin, I can create, read, update, and delete posts so that I can manage my blog content.                         | Perform CRUD operations on a post.                           | Pass   |
| 5. As a Site User, I can like or unlike a post so that I can interact with the content.                                       | Like and unlike a post and observe the like count changes. | Pass   |
| 6. As a Site User, I can leave comments on a post so that I can be involved in the conversations.                            | Post a comment on a post and view the comment section.     | Pass   |
| 7. As a Site User, I can register an account so that I can comment and like the posts.                                       | Register a new account and log in to comment and like.      | Pass   |
| 8. As a Site User/Admin, I can view comments on an individual post so that I can read the conversation.                      | Click on a post to view the full text and its comments.    | Pass   |
| 9. As a Site User/Admin, I can view the number of likes of each post so that I can see which is the most popular.               | Observe the like count displayed next to each post.        | Pass   |
| 10. As a Site User, I can click on a post so that I can read the full text.                                                     | Click on a post and verify that it displays the full content. | Pass   |
| 11. As a Site User, I can view a list of posts so that I can select one to read.                                                | Navigate to the home page and observe the list of posts.   | Pass   |

## Deployment

Detailed below are instructions on how to clone this project repository and the steps to configure and deploy the application. Code Institute also provides a summary of similar process steps here : [CI Cheat Sheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)

1.  How to Clone the Repository
2.  Create a new PostgreSQL database instance on ElephantSQL
3.  Create Application on Heroku
4.  Configure Cloudinary to host images used by the application
5.  Connect the Heroku app to the GitHub repository
6.  Executing automated tests
7.  Final Deployment steps

### How to Clone the Repository

- Go to the [https://github.com/FlorinDorneanu/snowboard-in-tirol](https://github.com/FlorinDorneanu/snowboard-in-tirol) repository on GitHub
- Click the "Code" button to the right of the screen, click HTTPs and copy the link there
- Open a GitBash terminal and navigate to the directory where you want to locate the clone
- On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process
- To install the packages required by the application use the command : pip install -r requirements.txt
- When developing and running the application locally set DEBUG=True in the settings.py file
- Changes made to the local clone can be pushed back to the repository using the following commands :
  - git add _filenames_ (or "." to add all changed files)
  - git commit -m _"text message describing changes"_
  - git push
- N.B. Any changes pushed to the master branch will take effect on the live project once the application is re-deployed from Heroku

### Create a new PostgreSQL database instance on ElephantSQL

- Log in to [ElephantSQL.com](https://www.elephantsql.com/) to access your dashboard
- Click “Create New Instance”
- Set up your plan
- Give your plan a Name (this is commonly the name of the project)
  - Select the Tiny Turtle (Free) plan
  - You can leave the Tags field blank
- Select “Select Region”
- Select a data center near you
  - If you receive a message saying "Error: No cluster available in your-chosen-data-center yet", choose another region. Note: You're free to use any of the available free data centers, be it AWS, Azure or any of the other providers.
- Then click “Review”
- Check your details are correct and then click “Create instance”
- Return to the ElephantSQL dashboard and click on the database instance name for this project
- In the URL section, click the copy icon to copy the database URL

### Create Application on Heroku

- Log in to Heroku at [https://heroku.com](https://heroku.com/) - create an account if needed.
- From the Heroku dashboard, click the Create new app button. For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.
- On the Create New App page, enter a unique name for the application and select region. Then click Create app.
- Next, click on Settings on the Application Configuration page and click on the "Reveal Config Vars" button - add the url from ElephantSQL to DATABASE_URL
- Add a new Config Var called DISABLE_COLLECTSTATIC and assign it a value of 1.
- Add a new Config Var called SECRET_KEY and assign it a value - any random string of letters, digits and symbols.
- The settings.py file should be updated to use the DATABASE_URL and SECRET_KEY environment variable values as follows :
  - DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
  - SECRET_KEY = os.environ.get('SECRET_KEY')
- In Gitpod, in the project terminal window, to initialize the data model in the postgres database, run the command : python3 manage.py migrate
- Make sure the project requirements.txt file is up to date with all necessary supporting files by entering the command : pip3 freeze --local > requirements.txt
- Commit and push any local changes to GitHub.
- In order to be able to run the application on localhost, add SECRECT_KEY and DATABASE_URL and their values to env.py

### Configure Cloudinary to host static files used by the application

- Log in to Cloudinary - create an account if needed. To create the account provide your name, email and set up a password. For "primary interest" you can choose "Programmable Media for image and video API". Click "Create Account" and you will be sent an email to verify your account and bring you to the dashboard.
- From the dashboard, copy the "API Environment variable" value by clicking on the "Copy to clipboard" link.
- Log in to Heroku and go to the Application Configuration page for the application. Click on Settings and click on the "Reveal Config Vars" button.
- Add a new Config Var called CLOUDINARY_URL and assign it the value copied from the Cloudinary dashboard, but remove the "CLOUDINARY_URL=" at the beginning of the string.
- In order to be able to run the application on localhost, also add the CLOUDINARY_URL environment variable and value to env.py

### Connect the Heroku app to the GitHub repository

- Go to the Application Configuration page for the application on Heroku and click on the Deploy tab.
- Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter the name of the github repository and click on Connect to link up the Heroku app to the GitHub repository code.
- Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - for this project Manual Deploy was selected.
- The application can be run from the Application Configuration page by clicking on the Open App button.

### Final Deployment steps

Once code changes have been completed and tested on localhost, the application can be prepared for Heroku deployment as follows :

- Set DEBUG flag to False in settings.py
- Ensure this line exists in settings.py to make summernote work on the deployed environment (CORS security feature): X_FRAME_OPTIONS = 'SAMEORIGIN'
- Ensure requirements.txt is up to date using the command : pip3 freeze --local > requirements.txt
- Push files to GitHub
- In the Heroku Config Vars for the application delete this environment variable : DISABLE_COLLECTSTATIC
- On the Heroku dashboard go to the Deploy tab for the application and click on deploy branch

## Technologies

### Languages

- HTML, CSS, JavaScript, Python

### Database

- sqlite3, ElephantSQL

### Frameworks

- Django
- Bootstrap

### Libraries & Packages

- Font Awesome
- Django allauth
- Django Crispy Forms
- Summernote
- gunicorn
- psycopg2
- Google Fonts

### Programs

- Codeanywhere
- GitHub
- Cloudinary
- Heroku

## Credits

- The Code Institute 'I Think, Therefore I Blog' walkthrough project assisted and guided in the setup and basic structure of this project.
- Code Institute Student Template: [codeanywhere full template](https://github.com/Code-Institute-Org/ci-full-template).

## Acknowledgements

- The tutors at Code Institute, for their patience and support.
- The Code Institute Slack community, for tips and guidance.


