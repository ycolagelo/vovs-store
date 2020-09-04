# Vov's Store

This is an e-commerce web application designed to help small businesses and commercial store owners sell merchandise online. The pandemic changed the way people shop with more people buying and selling online. With this in mind, my idea is to design an open source website that business owners can use by accessing the site source code along with a tool that allows them customize the site and database to suite the business needs.

## The website has 10 pages that have been developed:

### Home page

The home page contains a hero carousel that can be used to display hot items as well as a display for featured products. This page can also be accessed when the store logo is clicked.

### Shop page

This page features the products sold by the store. When a customer clicks on one of the items on the page, they will be directed to the product page. The customer however will not have access to the add to cart button in the product page unless they are logged in.

### Register page

A customer can register to gain access to purchase after they have filled in the necessary information. The page takes username, password, confirm password, email and telephone as input. Each of the input fields are verified and passwords are hashed before added to the database.
After Registering the customer will be directed to the login page.

### Login page

Login takes username and password as input fields. The database is checked for the username and password and if the user exists then a session is created for the user.

### Product page

The product page features a detailed description of the item, the price, name, one or more photos of the item and an input field where the quantity of the item to buy can be adjusted up or down by the user.

Logged in users will have access to the add to cart button. The add to cart button will otherwise be disabled.
When a user adds to cart a success message is displayed at the top of the page.
The success banner also has a link to view the cart.

### Cart page

When the cart icon link is clicked, the user will have access to the list of products in the cart as well as a price summary to show the breakdown of the costs.
The list of cart products feature a photo of the item, the name of the item and the price.
The price summary will have the subtotal, shipping fee, handling fee (if any), tax and total. The business owner can add any additional charges if required. 

Once the proceed to checkout button is clicked, the user will be redirected to the checkout page.


### Checkout page

In the checkout page the user can fill in or verify the billing address information as well as input the credit card information. All these fields are validated.

When the checkout button is clicked, the order will be placed and and the list of previous and current orders will be displayed in a collapsible accordion format. When an order is expanded in the accordion, the list of items purchased in that order is displayed.

### Reorder Page

The logged in users will have access to this page. It lists all the previously ordered items by the user. This gives the user the advantage of being able to easily reorder without searching for the product.

### Search button

This button helps the user find the product by name or category. The results are displayed in the shop page.

### Drop down link list

This drop down list is located on the right side of the navigation bar next to the cart. Once the user has logged in, their username will be the name of the drop down menu. The drop down menu contains the following features:

- Order History
- Change Password
- Change Address
- Cancel my Oder
- Logout

Once previous password and address have been verified new input will be address to the database.

Once the user logs out the session is cleared. Should the user log out with an active cart, the cart is saved and the user can pick up from where they left off in the previous session or they can clear the cart and restart.
