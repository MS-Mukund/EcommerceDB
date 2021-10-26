Welcome to the e-commerce database BUYNOW. This database is used to store the information about the products, the customers and all the transactions.  

Some commands that you can run: 
1. Update your customer_details: first the username of the user is asked, if the username exists, then program asks  the user to input columns which need updation. Then the user is asked to input the new values for those columns in THAT order. 
- Otherwise, if the username does not exist, then the user is asked to create a new account. He then has to input every column of the user table. 

2. Inserting an new Order when placed by an User <br/>

We are adding a new tuple to the 'order' table which has all the information about the order placed. As a new order is placed this change should be reflected in Purchase Transaction table as well which is basically a relationship table. So we added the same tuple in Purchase_Transaction table as well.

4. We search a product list by its name. IF the user DOES NOT input a string that is not exactly matching, then we output (atmost 10 products), which have the closest value to the string inputted by the user. 
5. Add a category filter. Now, only products of that category which is filtered by the user will be displayed.
6. Remove a Category filter. The filters will be removed and all products are displayed.
7. List all categories. This will list all the categories in the database.
8. List all price range of products. This will list all price ranges in the database.
9. Add a price range filter. Only products which are in the product range will be displayed. 
10. Remove price range filter. Now, all price range products will be displayed. 

11. Retrieve all the orders which are yet to be delivered <br />

We retrieved all the orders which are yet to be delivered for a particular user. This can be basically done by checking the bit value of delivery status. 

12. Retrieve all the total orders for a particular user chronologically sorted <br />

We retrived all the orders that were placed in total for a particular user in the sorted order of the date at which the order was placed.

13. Exits from the program. 