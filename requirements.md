# Software Requirements

### Vision

- What is the vision of this product?
  - The vision for this project is to create an e-commerce site/application that would allow users to purchase items from a variety of categories. The user would have their own profile, adding and deleting items from their cart. The user would be able to also have a search bar that would allow the user to search for their desired items from the library.
- What pain point does this project solve?
  - A convenient way for people to shop. It would allow users the ability to quickly grab any item to fulfil whatever needs they require. The user can easily grab anything they so desire using the search bar.
- Why should we care about your product?
  - Because it brings a clean UI that will keep your attention. The product would be a great way to purchase items that one needs quickly. It would also have a plethora of items from maybe even local creators, who make items and wish to sell their products on our site.

### Scope (In/Out)

- IN - What will your product do
  - Describe the individual features that your product will do.
    - Provide an online shopping experience
  - High overview of each. Only need to list 4-5
  - Example:
    - The web app will provide information to the users about various items for sale and the ability to add to cart or check out completely with the items that they choose.
    - The web app will provide search capabilities to see if the user can find what they are looking for quicker.
    - Users will be able to “Star” their favorite shops.
    - Each shop will contain reviews of the customer’s experiences
- OUT - What will your product not do.
  - These should be features that you will make very clear from the beginning that you will not do during development. These should be limited and very few. Pick your battles wisely. This should only be 1 or 2 things. Example: My website will never turn into an IOS or Android app.
    - Users will NOT be able to actually check out with any of the items on the shopping page.

#### Minimum Viable Product vs

- What will your MVP functionality be?
  - A user is able to have an account, view product inventory , search for specific product , select product to add to cart
- What are your stretch goals?
  - Some of our stretch goals could definitely be creating a user profile, a filter so that the user could find items based on price, reviews, etc, the ability to link their social media that would filter their likes and interests based on what they follow, like, etc. A user can send a message to request the admin to add a certain product

#### Stretch

- What stretch goals are you going to aim for?
  - Perhaps the filter for our page.

### Functional Requirements

List the functionality of your product. This will consist of tasks such as the following:

1. An admin can create and delete user accounts
2. A user can update their profile information
3. A user can search all of the products in the inventory
4. A user can add items to the cart
5. A user can search based on a product type

#### Data Flow

Describe the flow of data in your application. Write out what happens from the time the user begins using the app to the time the user is done with the app. Think about the “Happy Path” of the application. Describe through visuals and text what requests are made, and what data is processed, in addition to any other details about how the user moves through the site.

- The user will first enter our homepage where the user is required to login before they are able to purchase or look at anything. The user will then be able to search for their item using our search bar. Once the site has the specific item that the user wants, they can now click on the picture. After they click on the picture, the user is sent to the detailed page of that item. This page will have information about the item name, price Item Description, Product Details, User Reviews, Rating, photos. It will have the option to add it to their cart. The user can then click on the cart in the header nav bar where they can see all of the items that have been added. Here, they can see the item name, quantity, photo, and a trash icon that will allow the user to delete the item. Below in the footer, the page will have the option to empty the cart, or the ability to purchase the items. There will also be an about us page, with each group member photo, biography, and our linkedin qr code.

### Non-Functional Requirements (301 & 401 only)

Non-functional requirements are requirements that are not directly related to the functionality of the application but still important to the app.

1. Security

- The app will require authentication of users for a safer/controlled experience. The server will adhere to necessary security features including hiding sensitive information on .env and turning debugging to false. The server will be hosted on AWS, which offers relatively reliable security features. Frontend will be hosted in Vercel that also offers reliable security features

2. Usability

- The product is designed with a very user friendly and accepted approach. The user will log in, view inventory, search for a product if they wish to and add the product into the cart. The setup of the frontend is easy to understand and follow without clustering of the screen and with use of appropriate images to refer to products.
