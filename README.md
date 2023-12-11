# **Flying Dutchman Voyages - _"Sailing Until Doomsday!_**

## **Project Overview**

Flying Dutchman Voyages offers a one-of-a-kind experience - cruises on the fabled ghost ship, The Flying Dutchman. Customers are able to choose from a modest selection of unique rooms on board, from the opulant Captain's Quarters (of which the spectral Captain Hendrick Van der Decken no longer has any need), to 'The Brig' - lovingly named so for its location, though it is anything but a prison. They can make and manage bookings, learn a little about the vessel itself, as well as discover the spectacular events Flying Dutchman Voyages has to offer.


![Am I responsive screenshot](docs/screenshots/am-i-responsive-screenshot.png)

[**_Please follow this link to the final deployed version of this project._**](https://flying-dutchman-voyages-f488bfe43a6a.herokuapp.com/)

## **Table of Contents:**

1. [**Project Overview**](#project-overview)
1. [**Planning Stages**](#planning-stages)
    - [**Site Aims**](#site-aims)
    - [**Scope**](#scope)
    - [**User Stories**](#user-stories)
    - [**Structure**](#structure)
        - [**_ERD_**](#erd)
    - [**Client Side**](#client-side)
        - [**_Themes/Colours/Typography_**](#themes)
1. [**Technologies Used**](#technologies-used)
1. [**Agile Development**](#agile-development)
    -[**Sprints**](#sprints)
    -[**User Story Notes and Revisions**](#user-story-notes-and-revisions)
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

**Login/Registration (Must Have): Admin login**
* As a **Site Admin** I can **securely login to the admin dashboard** so that I can **view and manage booking options, manage/delete user accounts, and amend details of available bookings.**

**Login/Registration (Must Have): User registration**
* As a **Site User** I can **create an account** so that **I am able to make and manage my bookings.**

**Login/Registration (Must Have): User login**
* As a **Site User** I can **clearly see that I am logged in** so that **I know I am able to make and manage my bookings.**

**Booking (Must Have): Manage bookings (admin)**
* As a **Site Admin** I can **see bookings that have been made** so that **I can modify and delete them if necessary/contact the user with relevant information.**

**Booking (Must Have): Access booking calendar**
* As a **Site User** I can **access the booking calendar** so that **I can see the dates available to book trips.**

**Booking (Must Have): Create booking**
* As a **Site User** I can **create a booking** so that **I can secure a place on a voyage.**

**Booking (Must Have): Manage bookings (user)**
* As a **Site User** I can **manage any bookings I have made** so that **I can edit or delete them as necessary.**

**Events (Should Have): Access event information**
* As a **Site User** I can **clearly navigate to the events section** so that **I can see all upcoming events that might be of interest to me.**

**Contact (Could Have): Contact (user)**
* As a **Site User** I can **clearly access the contact form** so that **I am able to make enquiries.**

**Contact (Could Have): Contact (admin)**
* As a **Site Admin** I can **securely access messages sent through the website** so that **I can respond to user queries.**

The user stories were entered into the [GitHub Project Board linked to the Flying Dutchman Voyages repo](https://github.com/users/emmacadavra/projects/3/views/1) for me to monitor and keep track of my progress with them whilst building this project. Further notes on these can be found in the [**User Story Notes and Revisions section**](#user-story-notes-and-revisions) below.


### **Structure**


### **Client Side**


## **Technologies Used**


## **Agile Development**


### **Sprints**


### **User Story Notes and Revisions**


## **Current Features**


### **Header and Navigation


### **Home Page**


### **About Us Page**


### **Events Page**


### **Our Rooms Page**


### **Room Detail Page**


#### **Booking Success Page**


### **AllAuth Pages**


### **My Bookings Page**


#### **Amend Booking Page**


#### **Cancel Booking Page**


### **Error Pages**


## **Considerations for Future Enhancements**


### **Contact Form**


### **Additional Booking Functionality**


### **Email as Username**


## **Testing**

A separate file has been created for information about testing. Please click the following link to access it: [**TESTING.md**](TESTING.md)

## **Deployment**


## **Credits**

### **Honourable Mentions**

- [**Damon Kreft**](https://github.com/damon-kreft)

- [**Richard Wells**](https://github.com/D0nni387)

### **Code and Content References**

