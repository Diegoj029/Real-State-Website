# Real-State-Website
EasyBroker selection process project. Inmobiliaria de Prueba, a real estate agency wants to create a website connected to their EasyBroker account with all their published properties. The website consists of two main pages: the properties list page and the property page.

## Properties list page
The website's main page. A paginated list containing all the published properties of the company with the following requirements:
* 15 properties per page
* Only includes published properties

When click on a property, it opens the property's page

## Property page
When a user clicks on a property in the list you should take them to a page that displays all the property's detailed information. Use the properties/{property_id} endpoint.


### Contact Form
A form on the Property page that uses the contact_requests endpoint to create new leads in the agency's account. All the contact requests are linked to the property currently showing.
