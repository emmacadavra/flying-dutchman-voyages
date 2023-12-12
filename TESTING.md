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
        - [**_Lighthouse Scores and PageSpeed Insights_**](#lighthouse-scores-and-pagespeed-insights)
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

#### **Lighthouse Scores and PageSpeed Insights**


### **Unresolved Bugs**

* our rooms - safari (screenshot)

