# **Flying Dutchman Voyages - Testing**

## **Table of Contents (Testing):**

1. [**Testing Throughout Development**](#testing-throughout-development)
    - [**Manual Testing Methods**](#manual-testing-methods)
    - [**Logic Validation**](#logic-validation)
1. [**Noteable Bugs During Development**](#noteable-bugs-during-development)
1. [**Post Development Testing**](#post-development-testing)
    - [**Responsive Design and Functionality**](#responsive-design-and-functionality)
        - [**_Post Development Bugs_**](#post-development-bugs)
    - [**Site Validation**](#site-validation)
        - [**_Accessibility_**](#accessibility)
        - [**_Lighthouse Scores and Cloudinary_**](#lighthouse-scores-and-cloudinary)
        - [**_PageSpeed Insights_**](#pagespeed-insights)
    - [**Unresolved Bugs**](#unresolved-bugs)
    - [**Testing Final Deployed Site**](#testing-final-deployed-site)


## **Testing Throughout Development**

### **Manual Testing Methods**


### **Logic Validation**


## **Noteable Bugs During Development**

* Using & installing python & django on ubuntu - my_venv

* Linking templates

* "valid_form()"

* success_url & reverse/reverse_lazy (now removed from code)

* unable to make booking after removing room category name from template (+ screenshot)

* database

* changing from room categories to room names had a bigger knock-on effect than anticipated

* trying to use Bootstrap grid and flex in the same page = break

* trying to input form manually meant that no validation errors could be generated

* sweetify/sweet alert 2 css overriding bootstrap css (now removed)

* images not shrinking responsively when everything else was

* confusion between room.[data] and booking.room.[data]


## **Post Development Testing**

### **Responsive Design and Functionality**

Tested and confirmed working on all browsers except for one page when using safari (see unresolved bugs)

#### **Post Development Bugs**

* static files (Debug = False)

* issue with check_availability

### **Site Validation**

HTML - link to Accessibility below

#### **Accessibility**

HTML validation made me realise that Cloudinary alt text wasn't pulling through, leading to amending the Room model to include it

#### **Lighthouse Scores and Cloudinary**

On desktop, my average Lighthouse validation scores for peformance were between 95 and 100. The accessibility score drops from 100 to 94-95 on some pages, and upon investigation I found it was due to Bootstrap's info button styling.

Unfortunately, on mobile I only saw one page get into the green for performance, which was the Our Rooms page, however most of the pages are above 84 with the exception of the About Us page.

Initially, I was getting much lower scores across the board - in the 60s & 70s for mobile, and in the 80s for desktop. Looking into why this was, I found that part of the reason was Bootstrap, which cannot be helped, but I also realised that I had not taken into consideration the size of the image files that were being served by Cloudinary - the browser was trying to render them at full size and quality, even on smaller screens. To remedy this, I looked into how I could adjust the images based on where they were being served on the website, and found that (quite annoyingly) Cloudinary includes its responsive image options in the middle of the URLs, rather than at the end. This meant that I was unable to add the additional rules to any images that were being inserted into templates by Django, so I read through the relevant parts of Cloudinary's documentation to find a workaround. In the end I was able to massively improve overall scores by including Cloudinary-specific data strings in my templates, rather than putting the URL inside image tags. I also decided to add specific quality rules into the background images used in my CSS, which helped improve the scores.

Despite this, there are still some performance issues with a couple of pages - mostly the About Us page on mobile due to the need for the images to remain high enough quality when at full height on desktop and tablet.

All Lighthouse tests were performed using the published Heroku link, and done in an Incognito window.

**Homepage:**

![Homepage Lighthouse score - desktop](docs/testing/lighthouse-desktop-homepage.png)

![Homepage Lighthouse score - mobile](docs/testing/lighthouse-mobile-homepage.png)

**About Us:**

![About page Lighthouse score - desktop](docs/testing/lighthouse-desktop-about.png)

![About page Lighthouse score - mobile](docs/testing/lighthouse-mobile-about.png)

**Events:**

![Events page Lighthouse score - desktop](docs/testing/lighthouse-desktop-events.png)

![Events page Lighthouse score - mobile](docs/testing/lighthouse-mobile-events.png)

**Our Rooms:**

![Our Rooms page Lighthouse score - desktop](docs/testing/lighthouse-desktop-our-rooms.png)

![Our Rooms page Lighthouse score - mobile](docs/testing/lighthouse-mobile-our-rooms.png)

**Room Details:**

![Room Details page Lighthouse score - desktop](docs/testing/lighthouse-desktop-room-detail.png)

![Room Details page Lighthouse score - mobile](docs/testing/lighthouse-mobile-room-detail.png)

**My Bookings:**

![My Bookings page Lighthouse score - desktop](docs/testing/lighthouse-desktop-manage-bookings.png)

![My Bookings page Lighthouse score - mobile](docs/testing/lighthouse-mobile-manage-bookings.png)

**Booking Success:**

![Booking Success page Lighthouse score - desktop](docs/testing/lighthouse-desktop-booking-success.png)

![Booking Success page Lighthouse score - mobile](docs/testing/lighthouse-mobile-booking-success.png)

**Amend Booking:**

![Amend Booking page Lighthouse score - desktop](docs/testing/lighthouse-desktop-amend-booking.png)

![Amend Booking page Lighthouse score - mobile](docs/testing/lighthouse-mobile-amend-booking.png)

**Cancel Booking:**

![Cancel Booking page Lighthouse score - desktop](docs/testing/lighthouse-desktop-cancel-booking.png)

![Cancel Booking page Lighthouse score - mobile](docs/testing/lighthouse-mobile-cancel-booking.png)

**Login:**

![Login page Lighthouse score - desktop](docs/testing/lighthouse-desktop-login.png)

![Login page Lighthouse score - mobile](docs/testing/lighthouse-mobile-login.png)

**Logout:**

![Logout page Lighthouse score - desktop](docs/testing/lighthouse-desktop-logout.png)

![Logout page Lighthouse score - mobile](docs/testing/lighthouse-mobile-logout.png)

**Register:**

![Sign Up page Lighthouse score - desktop](docs/testing/lighthouse-desktop-register.png)

![Sign Up page Lighthouse score - mobile](docs/testing/lighthouse-mobile-register.png)

**Login Error:**

![Login Error page Lighthouse score - desktop](docs/testing/lighthouse-desktop-login-error.png)

![Login Error page Lighthouse score - mobile](docs/testing/lighthouse-mobile-login-error.png)

#### **PageSpeed Insights

Across the board, my PageSpeed Insights were lower than the Lighthouse scores - averaging at around 95 on Desktop and 70-80 on mobile, averaging at around 78. The insights provided were largely the same as the ones given by Lighthouse, and mostly had to do with using external stylesheets, and the Cloudinary image sizes.

![Homepage PageSpeed Insights score - desktop](docs/testing/pagespeed-desktop-homepage.png)

![Homepage PageSpeed Insights score - mobile](docs/testing/pagespeed-mobile-homepage.png)

### **Unresolved Bugs**

* our rooms - safari (screenshot)

