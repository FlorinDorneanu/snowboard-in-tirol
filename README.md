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

