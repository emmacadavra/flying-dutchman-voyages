# **Flying Dutchman Voyages - _"Sailing Until Doomsday!_**

## **Project Overview**

Flying Dutchman Voyages offers a one-of-a-kind experience - cruises on the fabled ghost ship, The Flying Dutchman. Customers are able to choose from a modest selection of unique rooms on board, from the opulant Captain's Quarters (of which the spectral Captain Hendrick Van der Decken no longer has any need), to 'The Brig' - lovingly named so for its location, though it is anything but a prison. They can make and manage bookings, learn a little about the vessel itself, as well as discover the spectacular events Flying Dutchman Voyages has to offer.


![Am I responsive screenshot](docs/images/am-i-responsive.png)

[**_Please follow this link to the final deployed version of this project._**](https://flying-dutchman-voyages-f488bfe43a6a.herokuapp.com/)

## **Table of Contents:**

1. [**Project Overview**](#project-overview)
1. [**Planning Stages**](#planning-stages)
    - [**Site Aims**](#site-aims)
    - [**Scope**](#scope)
    - [**User Stories**](#user-stories)
    - [**Server Side**](#server-side)
        - [**_Data Models_**](#data-models)
        - [**_Entity Relationship Diagram_**](#entity-relationship-diagram)
    - [**Client Side**](#client-side)
        - [**_Colour Scheme_**](#colour-scheme)
        - [**_Typography_**](#typography)
1. [**Technologies Used**](#technologies-used)
1. [**Agile Development**](#agile-development)
1. [**Current Features**](#current-features)
    - [**Header and Navigation**](#header-and-navigation)
    - [**Home Page**](#home-page)
    - [**About Us Page**](#about-us-page)
    - [**Events Page**](#events-page)
    - [**Our Rooms Page**](#our-rooms-page)
    - [**Room Detail Page**](#room-detail-page)
        - [**_Booking Success Page_**](#booking-success-page)
    - [**AllAuth Pages**](#allauth-pages)
    - [**My Bookings Page**](#my-bookings-page)
        - [**_Amend Booking Page_**](#amend-booking-page)
        - [**_Cancel Booking Page_**](#cancel-booking-page)
    - [**Error Pages**](#error-pages)
1. [**Considerations for Future Enhancements**](#considerations-for-future-enhancements)
    - [**Contact Form**](#contact-form)
    - [**Additional Booking Functionality**](#additional-booking-functionality)
    - [**Email as Username**](#email-as-username)
    - [**Slugs**](#slugs)
1. [**Testing**](#testing)
1. [**Deployment**](#deployment)
    - [**Cloning/Forking**](#cloningforking)
    - [**Setting Up the Database**](#setting-up-the-database)
    - [**Environment Variables and Settings**](#environment-variables-and-settings)
    - [**Cloudinary**](#cloudinary)
    - [**Deployment to Heroku**](#deployment-to-heroku)
1. [**Credits**](#credits)
    - [**Honourable Mentions**](#honourable-mentions)
    - [**Code and Content References**](#code-and-content-references)

## **Planning Stages**

### **Site Aims**

The primary aim for the Flying Dutchman Voyages project is to provide a seamless, user-friendly link between the services offered by Flying Dutchman Voyages, and potential customers looking to make a booking for a voyage. This link crucially includes information about The Flying Dutchman, and provides site users with a clear view of the rooms available to them. It provides the means to make a booking, amend existing bookings, and cancel bookings with ease - remaining clear and consistent for a smooth user experience.

Additionally, from the perspective of site admins, it provides a user-friendly way to manage site content by adding, removing and updating rooms, as well as the ability to view, update and cancel all bookings made by users through the site - all from one convenient admin page.

### **Scope**

When planning the project, I initially made a mind map using [**_Excalidraw_**](https://excalidraw.com/) of what I felt the project should contain - although crude, it helped me begin formulating what I thought the models should look like and I was able to build from there.

![Original project mind map](docs/images/mindmap.png)

From here, I expanded on this basic mind map and put some consideration into other features I'd like the project to have, such a contact form, and also put more thought into what each room (or, room category at the time) would look like. I was then able to filter these requirements into three categories: 'must have', 'should have', and 'could have'. By doing this, I was able to determine the MVP, as well as consider the agile epics that could be broken down into user stories.

### **User Stories**

The four agile epics that were determined by the scope mindmap are as follows:

1. **Login/Registration (Must Have):**
    * User - the ability for new users to create an account, and returning users to log in to access content only available for authorised users.
    * Admin - the ability for administrators to securely log in to access the site and admin dashboard.

1. **Bookings (Must Have):**
    * User - the ability to access booking functionality on the website, create bookings that are saved into a database, and amend/cancel those bookings from a convenient and secure view.
    * Admin - the ability to access booking data that has been made by all users on the website, and view/amend/cancel those individual bookings when needed from the secure admin dashboard.

1. **Events (Should Have):**
    * User - the ability to access information about the various events held by Flying Dutchman Voyages.

1. **Contact (Could Have):**
    * User - the ability to securely send enquiries through a contact form on the website.
    * Admin - the ability to securely access enquiries sent by users, and respond to them.

From these four epics, the following user stories were created:

**Login/Registration (Must Have):**
* **Admin login:** As a _Site Admin_ I can securely login to the admin dashboard so that I can view and manage booking options, manage/delete user accounts, and amend details of available bookings.
* **User registration:** As a _Site User_ I can create an account so that I am able to make and manage my bookings.
* **User login:** As a _Site User_ I can clearly see that I am logged in so that I know I am able to make and manage my bookings.

**Booking (Must Have):**
* **Manage bookings (admin):** As a _Site Admin_ I can see bookings that have been made so that I can modify and delete them if necessary/contact the user with relevant information.
* **Access booking calendar:** As a _Site User_ I can access the booking calendar so that I can see the dates available to book trips.
* **Create booking:** As a _Site User_ I can create a booking so that I can secure a place on a voyage.
* **Manage bookings (user):** As a _Site User_ I can manage any bookings I have made so that I can edit or delete them as necessary.

**Events (Should Have):**
* **Access event information:** As a _Site User_ I can clearly navigate to the events section so that I can see all events that might be of interest to me.

**Contact (Could Have):**
* **Contact (user):** As a _Site User_ I can clearly access the contact form so that I am able to make enquiries.
* **Contact (admin):** As a _Site Admin_ I can securely access messages sent through the website so that I can respond to user queries.

The user stories were entered into the [**_GitHub Project Board linked to the Flying Dutchman Voyages repo_**](https://github.com/users/emmacadavra/projects/3/views/1) for me to monitor and keep track of my progress with them whilst building this project. Further notes on these can be found in the **User Story Notes and Revisions section** of my separate [**_AGILE.md_**](AGILE.md) document.


### **Server Side**

#### **Data Models**

When planning for the project, these were the considerations I made for the models:

1. **User Model:**
* The User model will be imported from Django AllAuth, which will have a one-to-many relationship with the Room and Booking models - one User can have multiple Bookings across multiple Rooms, but every booking is unique to one User and will never be available to other Users.

1. **Room Model:**
* The Room model will allow for admins to create, edit and delete rooms from the database, but will not be editable by Users. Each room in the Room model has a one-to-many relationship with both the User and Booking models - every room can have multiple bookings associated with it for multiple Users, but again every booking is unique to only one User and one Room.

1. **Booking Model:**
* The Booking model allows for Users to create, amend and delete bookings made through the booking form for a specific room. Every booking is unique to the User and room, and ensures that no bookings can be made for rooms that have already been booked on certain dates. It stores the data on the database and fetches data using the unique booking ID if the User is authenticated, so that the User is able to manage the booking.

#### **Entity Relationship Diagram**

Below is an updated version of my initial ERD to include the current model fields (the Room model only includes image & alt text fields once for the sake of space), made using [**_Excalidraw_**](https://excalidraw.com/):

![ERD made on Excalidraw](docs/images/erd.png)

The User interacts with the booking process initially by being introduced to the different rooms available. When the user clicks to view a specific room, they are then able to make a booking for that room. Their request is validated by the booking form, linked to the Booking model and returned to the User if invalid with information about why it was invalid. If valid, their booking is successfully created, and the User can then access that booking information to cancel it if they want to, or amend it (in which case a similar process will begin again where validation checks are performed to make sure the User is able to make those changes).

### **Client Side**

#### **Colour Scheme**

Before I started working on the styling of the website, I was fortunate enough to come across this beautiful painting titled 'The Flying Dutchman', by Charles Temple Dix. I had already decided that I wanted a somewhat light and airy theme for the website and this provided me not only with the perfect background images for the site, but also a great place to start in terms of colour scheme.

!['The Flying Dutchman' by Charles Temple Dix](docs/images/the-flying-dutchman-charles-temple-dix.jpg)

I also found I like the info button colour styling that was provided by Bootstrap4, so I started off very simple with this colour palette from [**_mycolor.space_**](https://mycolor.space/):

![Original colour palette from mycolor.space](docs/images/initial-colour-palette.png)

I also used [**_mycolor.space/gradient3_**](https://mycolor.space/gradient3) for the gradients seen in the header and footer.

To expand on the palette and rework it closer to the colours seen in Charles Temple Dix's painting, I uploaded the image to [**_colormind.io_**](http://colormind.io/) to generate additional colours to use on the website. Below is a colour grid created by [**_contrast-grid.eightshapes.com_**](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%2353adbb%2C%0D%0A%233d5246%2C%0D%0A%23303030%2C%0D%0A%23080808%2C%0D%0A%23212529%2C%0D%0A%23f3ead7%2C%0D%0A%23f2efe080%2C%0D%0A%23f2efe0cc%2C%0D%0A%23f4f2e3%2C%0D%0A&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp) that includes the final colours used across the website:

![Colour contrast grid](docs/images/colour-contrast-grid.png)

#### **Typography**

For the main titles and some occasional features on the site, I decided to use the font 'Charm', found on Google Fonts. I felt this font was a perfect balance between extravagent and scriptive, whilst remaining clear and readable. I feel it accurately carries the theme of the website without being too overpowering.

For the main body of the website I considered using a different font to Bootstrap4's native font stack, however I found that I quite liked the contrast between it and 'Charm', as they seem to compliment one another in an unexpected and simple way.

## **Technologies Used**

* Python
* Django
* Heroku
* ElephantSQL
* HTML5
* CSS3
* Bootstrap4
* Javascript (through Bootstrap4)
* FontAwesome
* Cloudinary

## **Agile Development**

Throughout this project, I adopted an agile approach, which I have detailed and reflected on in my separate [**_AGILE.md_**](AGILE.md) document.

## **Current Features**

### **Header and Navigation

![Navbar full](docs/images/navbar-full.png)

![Navbar collapsed](docs/images/navbar-collapsed.png)

![Navbar expanded](docs/images/navbar-expanded.png)

### **Home Page**

![Homepage on desktop](docs/images/homepage.png)

![Homepage mobile 320x480px](docs/images/homepage-mobile-320x480px.png)

![Homepage iPhone 12 Pro](docs/images/homepage-iphone12pro.png) 

### **About Us Page**

![About Us page landing view desktop](docs/images/about-page-landing-desktop.png)

![About Us page landing view iPhone 12 Pro](docs/images/about-page-landing-iphone12pro.png)

![About Us main section 1 desktop](docs/images/about-page-section-1.png)

![About Us main section 2 desktop](docs/images/about-page-section-2.png)

![About Us sections on tablet video](link)

### **Events Page**

![Events page landing view desktop](docs/images/events-landing-desktop.png)

![Events page landing view iPhone 12 Pro](docs/images/events-landing-iphone12pro.png)

![Holiday Events section desktop](docs/images/holiday-events-desktop.png)

![Easter Sunday Event section 1 desktop](docs/images/easter-event-desktop-1.png)

![Easter Sunday Event section 2 desktop](docs/images/easter-event-desktop-2.png)

### **Our Rooms Page**

![Our Rooms page landing view desktop](docs/images/our-rooms-landing-desktop.png)

![Our Rooms page landing iPhone 12 Pro](docs/images/our-rooms-landing-iphone12pro.png)


### **Room Detail Page**

![Room Detail page landing desktop](docs/images/room-detail-landing-desktop.png)

![Room Detail page landing iPhone 12 Pro](docs/images/room-detail-landing-iphone12pro.png)


#### **Booking Success Page**

![Booking Success page desktop](docs/images/booking-success-desktop.png)

![Booking Success page iPhone 12 Pro](docs/images/booking-success-iphone12pro.png)

### **My Bookings Page**

![My Bookings page landing desktop](docs/images/my-bookings-landing-desktop.png)

![My Bookings page landing iPhone 12 Pro](docs/images/my-bookings-landing-iphone12pro.png)


#### **Amend Booking Page**

![Amend Booking page landing desktop](docs/images/amend-booking-desktop.png)

![Amend Booking page landing iPhone 12 Pro](docs/images/amend-booking-landing-iphone12pro.png)


#### **Cancel Booking Page**

![Cancel Booking page landing iPhone 12 Pro](docs/images/cancel-booking-desktop.png)

![Cancel Booking confirmation message desktop](docs/images/cancel-booking-confirmation-message-desktop.png)

![Cancel Booking page landing iPhone 12 Pro](docs/images/cancel-booking-landing-iphone12pro.png)

![Cancel Booking confirmation message iPhone 12 Pro](docs/images/cancel-booking-confirmation-message-iphone12pro.png)

### **AllAuth Pages**

#### **Register Page**

![Register page desktop](docs/images/register-desktop.png)

![Register page iPhone 12 Pro](docs/images/register-landing-iphone12pro.png)

#### **Login Page**

![Login page desktop](docs/images/login-desktop.png)

![Login confirmation message desktop](docs/images/login-confirmation-message-desktop.png)

![Login page iPhone 12 Pro](docs/images/login-landing-iphone12pro.png)

![Login confirmation message iPhone 12 Pro](docs/images/login-confirmation-message-iphone12pro.png)

#### **Logout Page**

![Logout page desktop](docs/images/logout-desktop.png)

![Logout confirmation message desktop](docs/images/logout-confirmation-message-desktop.png)

![Logout page iPhone 12 Pro](docs/images/logout-iphone12pro.png)

![Logout confirmation message iPhone 12 Pro](docs/images/logout-confirmation-message-iphone12pro.png)

### **Error Pages**

![404 error page desktop](docs/images/custom-404-page.png)

![500 error page desktop](docs/images/custom-500-page.png)

## **Considerations for Future Enhancements**

### **Contact Form**

One of the things I would most like to implement to this project in future is a contact form, which I ended up not including in the initial development of this project. More information about this can be found in the **User Story Notes** section of my separate [**_AGILE.md_**](AGILE.md) document.

### **Additional Account & Booking Information**

Currently, when users sign up for the website to make a booking, they only need to enter a username and password. For the scope of this project, that is fine - however in the future I would like to look into implementing a more robust account creation process that means users must enter in details such as their full name, age, address, etc. This would mean that the booking information stored on the database would be more useful to the site owners and be more realistic for a booking website.

Additionally, I would like to add a feature to the booking process that asks for the names of additional passengers.

### **Email as Username & Email Confirmation**

Following on from the above, current users need only register with a username and password, which would be fine if this were a blog or Reddit-style website, but for a booking website I feel that using an email address for a username (and removing the 'username' part entirely so it's only the email address) would be more appropriate. It would also mean that users can receive email confirmations for their bookings, and it would be easier for site admins to manage bookings made on the site.

When starting this project, I implemented the basic Django AllAuth account creation, but didn't consider until later the impact that favouring usernames over email addresses would have on future enhancements. I plan to look into this with the hopes of implementing a reformed account creation system in future.

### **Slugs**

When I first created this project, my Room model contained a dictionary called "ROOM_CATEGORIES" that included a room category string (ie. "CAPQ") and then a name string (ie. "Captain's Quarters"). This was because I had originally intended on having more than one of a certain room category available. Each room category's URL would be generated from the category string, and the page would be populated with the name string. Because I worked like this for a while before refactoring my code, when it came to refactoring I focused instead on having one of each room, and using the room's primary key as it's ID which is fed to the URL. Unfortunately it occurred to me a little too late that it might be better to add a slug field into the Room model - by which point so much of my code had been written around URLs being generated by room IDs that it became unfeasible to refactor it again to accommodate slugs instead. However, I think the site would benefit from this addition and I intend to implement it in future. 

## **Testing**

A separate file has been created for information about testing. Please click the following link to access it: [**_TESTING.md_**](TESTING.md)

## **Deployment**

In this section I explain the steps I took in order to deploy this project.

### **Cloning/Forking**

If you wish to create a clone of this project to use on your local machine or virtual IDE environment such as Gitpod, first navigate to [this project's GitHub Repository](https://github.com/emmacadavra/flying-dutchman-voyages), and follow [GitHub's instructions on how to clone a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository). If you are using a local environment, you can enter the following command in the terminal:
```pip install -r requirements.txt```
This will install all the required libraries and packages in one go, meaning you will not have to follow the set-up steps below.

As I developed this project locally, I had to create a virtual environment using the command ```python -m venv .venv``` - if you clone this project to use locally, you must do the same. Ensure that the virtual environment is not tracked by version control by adding it to the .gitignore file.

Below is a list of the steps and terminal commands I used to install the necessary libraries and packages for this project following the creation of the GitHub repository:

1. Create a virtual environment (as mentioned above):
    * ```python -m venv .venv```
    * Add the .venv file to .gitignore
1. Open the virtual environment and install Django with Gunicorn:
    * ```pip3 install 'django<4' gunicorn```
1. Install the supporting database libraries:
    * ```pip3 install dj_database_url==0.5.0 psycopg2```
1. Install Cloudinary libraries:
    * ```pip3 install dj3-cloudinary-storage```
    * ```pip3 install urllib3==1.26.15```
1. Create a 'requirements.txt' file:
    * ```pip3 freeze --local > requirements.txt```
1. Create the Django project:
    ```django-admin startproject project_name .``` (note: 'project_name' in this case is 'flying_dutchman' - do not forget the '.' after the project name)
1. Create a Django app:
    * ```python3 manage.py startapp app_name``` (note: 'app_name' in this case is 'fd_bookings'. A separate app should be created for each major aspect of the project - for example I plan to create a contact form in future which will require its own app as it is separate from the booking fucntions)
1. In 'settings.py', which is created in the main project directory, add the following apps to the 'INSTALLED_APPS' section:
    * ![INSTALLED_APPS additions](docs/images/installed-apps.png)
1. Run the following command to make migrations:
    * ```python3 manage.py makemigrations```
1. Run the following command to migrate changes:
    * ```python3 manage.py migrate```
1. Run the following command to run the server and test whether the project is working locally:
    * ```python3 manage.py runserver```
1. The Django success page should now show, but if not, the 'ALLOWED_HOSTS' section of 'settings.py' needs updating to include the URL given by Django if an error is displayed.

### **Setting Up the Database**

This project uses [**_ElephantSQL_**](https://www.elephantsql.com/) to host its database. Below are the steps I took following account creation:
1. Click on 'Create New Instance'
1. Provide a project name and select the 'Tiny Turtle (Free)' plan
1. Click 'Select Region' and choose a nearby data centre
1. Review the details of the project before returning to the dashboard
1. Copy the ElephantSQL URL, which starts with 'postgres://', in order to link it to the Django project (detailed further below)

### **Environment Variables and Settings**

1. Create a file in the main project directory called 'env.py', and add it to the .gitignore file - this files stores private environment variables and must be kept hidden
1. Add the key 'DATABASE_URL' to env.py and assign it the ElephantSQL URL as a value:
    * ```os.environ["DATABASE_URL"] = "postgres://ElephantSQL Database URL"```
1. Add the key 'SECRET_KEY' to env.py and assign it something secret (and more secure than "SecretKey123"!) as a value:
    * ```os.environ["SECRET_KEY"] = "SecretKey123"```
1. Navigate to the 'settings.py' file and make sure the following code is added to the top of the file:
    * ![Settings.py imports](docs/images/settings-imports.png)
1. Replace Django's default 'DATABASES' in the with the following code:
    * ![Updated DATABASES code](docs/images/databases-updated-code.png)
1. Replace Django's default 'SECRET_KEY' with the following code:
    * ![Updated SECRET_KEY code](docs/images/secret-key-code.png)
1. Add the following code to 'settings.py' to correctly link up project templates:
    * ```BASE_DIR = Path(__file__).resolve().parent.parent```
    * ```TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')```
    * ![Templates code in settings.py](docs/images/templates-settings.png)

### **Cloudinary**

[**_Cloudinary_**](https://cloudinary.com/) is installed as part of this project in order to host media and static files. Below are the steps I took following account creation and installing Cloudinary through Django:
1. Navigate to the Cloudinary Dashboard
1. Copy the code from the 'API Environment variable', section of the Dashboard:
    * ![Cloudinary API Environment variable](docs/images/cloudinary-api.png)
1. Add the key 'CLOUDINARY_URL' to 'env.py' and assign it the Cloudinary API URL as a value:
    * ```os.environ["CLOUDINARY_URL"] = "cloudinary://Cloudinary API URL"```
1. Add the following code to 'settings.py' to tell Django to use Cloudinary to store and manage media and static files:
    *![Cloudinary code for settings.py](docs/images/cloudinary-settings.png)


### **Deployment to Heroku**

This project is hosted on [**_Heroku_**](https://www.heroku.com/). Below are the steps I took to deploy my project following account creation, project setup and database setup with [**_ElephantSQL_**](https://www.elephantsql.com/):

1. On the Heroku Dashboard, create a new app. The app name must be unique and should be related to the Django project name
1. Set your location as appropriate

1. Open the 'Settings' tab and navigate to 'Config Vars' - Click 'Reveal Config Vars'
1. Add the following config vars:
    * ```PORT = 8000```
    * ```DATABASE_URL = postgres://ElephantSQL Database URL``` (note that this must be the unique ElephantSQL URL from the created database)
    * ```SECRET KEY = SecretKey123``` (note that this must be the unique secret key made previously for this project)
    * ```CLOUDINARY_URL = cloudinary://Cloudinary API URL``` (note that this must be the unique Cloudinary API URL obtained previously)
1. Add the following temporary config var (to be removed before final deployment):
    * ```DISABLE_COLLECT_STATIC = 1```
1. Obtain the project URL from Heroku, and add it to the 'ALLOWED_HOSTS' section of 'settings.py'
1. Create a Procfile in the root project directory and add the following code:
    * ```web: gunicorn project_name.wsgi``` (note that 'project_name' must be the same as your Django project)
1. Save all project files, and use the following commands to add, commit and push the changes to the GitHub repository:
    * ```git add .```
    * ```git commit -m "Initial commit"```
    * ```git push```
1. Navigate to the 'Deploy' tab in the Heroku dashboard and link the GitHub repository to the project.
1. Manually deploy from the main GitHub repository branch.

## **Credits**

### **Honourable Mentions**

- [**_Damon Kreft_**](https://github.com/damon-kreft)

- [**_Richard Wells_**](https://github.com/D0nni387)

### **Code and Content References**

