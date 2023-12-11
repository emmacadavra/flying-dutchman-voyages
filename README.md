# **Flying Dutchman Voyages - _"Sailing Until Doomsday!_**

## **Project Overview**

Flying Dutchman Voyages offers a one-of-a-kind experience - cruises on the fabled ghost ship, The Flying Dutchman. Customers are able to choose from a modest selection of unique rooms on board, from the opulant Captain's Quarters (of which the spectral Captain Hendrick Van der Decken no longer has any need), to 'The Brig' - lovingly named so for its location, though it is anything but a prison. They can make and manage bookings, learn a little about the vessel itself, as well as discover the spectacular events Flying Dutchman Voyages has to offer.


![Am I responsive screenshot](docs/images/am-i-responsive-screenshot.png)

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
        - [**_Themes/Colours/Typography_**](#themes)
1. [**Technologies Used**](#technologies-used)
1. [**Agile Development**](#agile-development)
1. [**Current Features**](#current-features)
    - [**Header and Navigation**](#header-and-navigation)
    - [**Home Page**](#home-page)
    - [**About Us Page**](#about-us-page)
    - [**Events Page**](#events-page)
    - [**Our Rooms Page**](#our-rooms-page)
    - [**Room Detail Page**](#room-detail-page)
        - [**_Booking Success Page**](#booking-success-page)
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
1. [**Credits**](#credits)
    - [**Honourable Mentions**](#honourable-mentions)
    - [**Code and Content References**](#code-and-content-references)

## **Planning Stages**

### **Site Aims**

The primary aim for the Flying Dutchman Voyages project is to provide a seamless, user-friendly link between the services offered by Flying Dutchman Voyages, and potential customers looking to make a booking for a voyage. This link crucially includes information about The Flying Dutchman, and provides site users with a clear view of the rooms available to them. It provides the means to make a booking, amend existing bookings, and cancel bookings with ease - remaining clear and consistent for a smooth user experience.

Additionally, from the perspective of site admins, it provides a user-friendly way to manage site content by adding, removing and updating rooms, as well as the ability to view, update and cancel all bookings made by users through the site - all from one convenient admin page.

### **Scope**

When planning the project, I initially made a mind map of what I felt the project should contain - both from the user perspective and the admin perspective.

![Original project mind map](link)

From here, I was able to break down these requirements into three categories: 'must have', 'should have', and 'could have'. By doing this, I was able to determine the MVP, as well as consider the agile epics that could be broken down into user stories.

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
* **Access event information:** As a _Site User_ I can clearly navigate to the events section so that I can see all upcoming events that might be of interest to me.

**Contact (Could Have):**
* **Contact (user):** As a _Site User_ I can clearly access the contact form so that I am able to make enquiries.
* **Contact (admin):** As a _Site Admin_ I can securely access messages sent through the website so that I can respond to user queries.

The user stories were entered into the [**_GitHub Project Board linked to the Flying Dutchman Voyages repo_**](https://github.com/users/emmacadavra/projects/3/views/1) for me to monitor and keep track of my progress with them whilst building this project. Further notes on these can be found in the **User Story Notes and Revisions section** of my separate [**_AGILE.md_**](AGILE.md) document.


### **Server Side**

#### **Data Models**

Data models

#### **Entity Relationship Diagram**

ERD

### **Client Side**

#### **Colour Scheme**

!['The Flying Dutchman' by Charles Temple Dix](docs/images/the-flying-dutchman-charles-temple-dix.jpg)

![Original colour palette from mycolor.space](docs/images/initial-colour-palette.png)

contrast-grid.eightshapes.com

#### **Typography**

Charm by Google Fonts

## **Technologies Used**

* Python
* Django
* HTML5
* CSS3
* Bootstrap4
* Javascript (indirectly)

## **Agile Development**

Throughout this project, I adopted an agile approach, which I have detailed and reflected on in my separate [**_AGILE.md_**](AGILE.md) document.

### **User Story Notes and Revisions**


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

[link to User Stories Still In Process section of AGILE.md]

### **Additional Booking Functionality**


### **Email as Username**


### **Slugs**


## **Testing**

A separate file has been created for information about testing. Please click the following link to access it: [**_TESTING.md_**](TESTING.md)

## **Deployment**


## **Credits**

### **Honourable Mentions**

- [**_Damon Kreft_**](https://github.com/damon-kreft)

- [**_Richard Wells_**](https://github.com/D0nni387)

### **Code and Content References**

