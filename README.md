# Vovs Store

### This is an E-commerce Website designed to help small businesses/ commercial store owners sell marchandise online. The Pandameic changed the way people shop with more people bying and selling online and with this in mind, my idea is to design an open source website that business owners can use by accessing the site source code with a key that allows them customise the site and database to suite the business needs.

 The website has 10 pages that have been developed:
 ### index page
The index page contains a hero corousel that can be used to display hot items as well as a diplay for featured products. This page can also be accessed when the store logo is clicked.
### Shop page
This page features the products sold by the store. When a customer clicks on one of the items on the page, they will be  directed to the product page. The customer however will not have access to the add to cart button in the product page unless they are logged in.
### Register page
A customer will have acess to register for and gain access to buy after they have filled in the necessary information. The page takes username, password, confirm password, email and Telephone as input. Each of the input fileds are verified and passwords are hashed before added to the database.
After Registering the custmer will be directed to the login page.
### Login page

login takes username and password as input fields. The database is checked for the username and if the user ecsists then a session is created for the user.
### Product page
A user/customer with an active session will have access or that has been logged in, will have acess to the product page and the add to cart button. The product page features a detailed discription of the item, the price, name, photo of the time and an input field where the quantity of the item to buy can be adjusted up or down by the user.
When a user adds to cart a success message is displayed at the top of the page.
The success banner where the sucess message is displayed will have a link to view cart.
### cart page
Once the cart icon is clicked, the user will have access to the list of purchased products in the cart to the right as well as the invoice to the right.
The list of cart products feature the the photo of the item, the name of the item and the price.
The invoice receipt will have the subtotal, shipping fee, handling fee if any, hst, the business owner can add any additional charges if required, and lastly the estimated total. Once proceed to checkout button is clicked,
The user will be directed to the billing address form where they can fill in or verify the billing address information as well as insert the credit card information. 
All these fileds are verified and stored in a database. Credit card information is also verified.

## Proceed to checkout button
This button is loacted under the billing adress and credit card information form. Once clicked the order will be placed and and the list of previous and current orders will be displayed in a collapsible accordian where when the view link is clicked, the list of items purcahed in that order is displayed.

## Reoder Page
The logged in user will have access to this page. It lists all the previous ordered items the gives the user the advantage of reodering without searching for the product. 
## Search button
This button helps the user find the product by name or category.

## Drop down list
This drop down list is located on the left side of the navigation bar next to the cart.Once the user has logged in, their username will be the name of the drop down menue. The drop down menue will containg the following features: 

- Change Password
- change Address 
- Cancel my Oder
- Logout

Once previous password and address have been verified new input will be address to the database. 
When an order is cancelled, the cart is cleared and the refund process is initiated.

Once the user logs out the session is cleared. Should the user logg out with an active cart, the cart will be saved and the user can pick up from where they left off in the previous session or they can clear cart and restart.















