# **Flying Dutchman Voyages - Agile Development**

## **Agile Overview**

For this project, I adopted an agile approach in order to better organise the workload, and prioritise work to be completed in increments. To do this, I looked at my User Stories and divided them up into 3 sprints, which were approximately 10-14 days each.

## **Table of Contents (Agile Development):**

1. [**Agile Overview**](#agile-overview)
1. [**Sprints**](#sprints)
    - [**First Sprint**](#site-validation)
    - [**Second Sprint**](#site-validation)
    - [**Third Sprint**](#site-validation)
1. [**User Story Notes**](#user-story-notes-and-revisions)
    - [**Reflections**](#reflections)
    - [**Revisions**](#revisions)
    - [**User Stories Still To Do**](#user-stories-still-in-process)

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

Despite the fact that, by the end of the first sprint, I had imlemented the functionality for administrators and users to _cancel_ bookings, I had not included the functionality to _amend_ bookings. It was at this point that I realised I had put together a lot of code that had become quite messy, to the point that I felt I didn't fully understand a lot of it. This was largely due to adding/removing small amounts of code as I went, without considering the larger picture of what that code was doing/how it was interacting with the rest of the code. It created a 'tangled web' of sorts that was overly complicated and difficult to keep track of.

It was because of this that I dedicated this sprint first of all to refactoring much of my code, as well as reviewing the complexity of what I was trying to achieve in some cases. I realised I had allowed some scope creep by being too ambitious with how I wanted the project to work, and worked to bring it back in line with something that was more realistic and less complicated. During this process I struggled with the relationship between the booking form and code I'd written for the views, but the process of refactoring eased this struggle and allowed me to successfully implement the ability for users to amend their bookings.

By the end of this sprint, there was still absolutely zero styling on the client side, as my focus remained entirely on making sure that the MVP was met, and that the functionality of the website was solid as a top priority. However, I had started collating potential images and information to use on the website

### **Third Sprint**

Technically, the third sprint only had one User Story attached to it, which was:

* **Access event information:** As a _Site User_ I can clearly navigate to the events section so that I can see all events that might be of interest to me.

However, this is misleading as it was really only a very small part of the work undertaken throughout this sprint - which was working on the entirity of the website's content and styling! This User Story started out much bigger in my mind at the beginning of the project, but ended up being dialled back enormously due to other things taking priority (I reflect on this in more detail in the [**_User Story Notes and Revisions_**](#user-story-notes-and-revisions) section below).

I had started collating images and content ahead of this sprint, and thankfully had already come across the beautiful painting 'The Flying Dutchman' by Charles Temple Dix which I knew I wanted to use as my main homepage background. Although it is one of the simplest pages, I spent time making sure I was happy with homepage before moving on to the Room Detail page and other pages that interact with the models database. The events page was actually one of the last pages I focused on, as it is one of the pages that does not interact with Django beyond standard template rendering functionality.

Throughout the styling process, I found many opportunities to improve on my Room model, which improved the site overall. I added a short room summary, longer summary description, additional images so that I could implement a carousel effect, and alt text for those images (detailed in the **Accessibility** section of my separate [TESTING.md](TESTING.md) document). These changes meant that the website was much less bare in some places and overall made the website feel more refined.

At the end of this sprint, I had a complete project that I was able to review and perform post-development tests on, in order to make any final tweaks before completion. More about this can be found in the **Post Development Testing** section of my separate [TESTING.md](TESTING.md) document.

## **User Story Notes**

### **Reflections**

Upon reflection, I feel that I might have benefited from breaking down my User Stories into smaller, more specific ones. While I started out with my main epics and broke them down a little, I do think they were too broad in some areas, and didn't cover many aspects of the development process at all. Looking in particular at my third sprint, at no point did I create User Stories specifically pertaining to the styling of the website, nor, in my first sprint, did I include ones that covered the basic project set-up, and so on. In future, I plan to make sure I pay attention to this as I have found that when the User Stories are too broad, it is easier to get 'lost' as to where you are in the overall development process.

### **Revisions**

As briefly mentioned above in the **Third Sprint** section, the User Story for accessing events information had to undergo a necessary revision during development. Originally, the User Story read "As a _Site User_ I can clearly navigate to the events section so that I can see all **upcoming** events that might be of interest to me." This is because I had originally hoped to explore a number of different options that I had vastly oversimplified in my mind when planning the project. These were things like, having a calendar that would automatically inform a user of the event taking place if they picked a date of an event, by changing the page template to thematically match the event with additional images, flavour text, etc.

It didn't take long for me to realise the sheer complexity of what I was envisioning, and how unfeasible it was considering both time contraints and the current limitations of my knowledge. Therefore, I made the decision to strip this particular User Story down to its simplest form, which is the form currently present on the website. However, I did decide to keep this feature of the website as a "Should Have", rather than move it down to a "Could Have", due to how integral the concept of the Easter Sunday event was to my vision for the project.

### **User Stories Still To Do**

Currently, there are two User Stories on my [**_GitHub Project Board_**](https://github.com/users/emmacadavra/projects/3/views/1) that are still in the 'To Do' column. These are both User Stories relating to having a page on the website that serves as a Contact form. I marked both of these as a "Could Have", as they were not integral to the overall project but would be nice to have if there was time. Unfortunately, as I mentioned above, time constraints along with the current scope of my knowledge led me to decide that completing these User Stories would not be possible, so I opted instead to feature an email address on the 'About Us' and 'Events' pages.

The reason I've decided to keep these User Stories on the project board is that, in future, I would like to implement this feature to the project in my own time, as I plan to continue building on this project going forward.
