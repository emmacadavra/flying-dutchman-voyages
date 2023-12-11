# **Flying Dutchman Voyages - Agile Development**

## **Agile Overview**

For this project, I adopted an agile approach in order to better organise the workload, and prioritise work to be completed in increments. To do this, I looked at my User Stories and divided them up into 3 sprints, which were approximately 10-14 days each.

## **Table of Contents (Agile Development):**

1. [**Agile Overview**](#agile-overview)
1. [**Sprints**](#sprints)
    - [**First Sprint**](#site-validation)
    - [**Second Sprint**](#site-validation)
    - [**Third Sprint**](#site-validation)
1. [**User Story Notes and Revisions**](#user-story-notes-and-revisions)

## **Sprints**

### **First Sprint**

The first sprint focussed on the following User Stories:

* **Admin login:** As a _Site Admin_ I can securely login to the admin dashboard so that I can view and manage booking options, manage/delete user accounts, and amend details of available bookings.
* **User registration:** As a _Site User_ I can create an account so that I am able to make and manage my bookings.
* **User login:** As a _Site User_ I can clearly see that I am logged in so that I know I am able to make and manage my bookings.
* **Access booking calendar:** As a _Site User_ I can access the booking calendar so that I can see the dates available to book trips.
* **Create booking:** As a _Site User_ I can create a booking so that I can secure a place on a voyage.

I was able to achieve these by focussing solely at first on the overall skeleton of the project in Django. My initial models were created, with basic views and templates set up - no CSS or styling, just the bare HTML necessary for me to check my site was functioning.

I created an admin superuser, and familiarised myself with the Django admin dashboard, confirming along the way that my views were connecting my models and templates successfully. Then, I inserted the Django form into my HTML template, and tested to ensure that data being sent through it was being stored successfully on the database.

After this, I created a separate, non-admin account on the website to test the register and login functionality, and made bookings to check later on the admin dashboard with the admin superuser account.

### **Second Sprint**

My second sprint focused almost entirely on the following two User Stories:

* **Manage bookings (admin):** As a _Site Admin_ I can see bookings that have been made so that I can modify and delete them if necessary/contact the user with relevant information.
* **Manage bookings (user):** As a _Site User_ I can manage any bookings I have made so that I can edit or delete them as necessary.

Although by the end of the first sprint I had imlemented the ability for administrators and users to _cancel_ their bookings, I had not done anything to include functionality to _amend_ bookings. It was at this point that I realised I had put together a lot of code that I didn't fully understand, or that was poorly written/overly verbose.

It was because of this that I dedicated this sprint first of all to refactoring much of my code, as well as reviewing the complexity of what I was trying to achieve in some cases. I realised I had allowed some scope creep by being too ambitious with how I wanted the project to work, and worked to bring it back in line with something that guaranteed the MVP was delivered first and foremost.

By the end of this sprint, there was still 0 styling at all on the client side, 