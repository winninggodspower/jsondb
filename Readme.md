# Hello 🙋‍♀️👋. welcome To Jsondb Docuentation

## what is jsondb 🤷‍♂️🤷‍♀️ ?
 jsondb is a python library that allows you to create a database with a json file. 

 it gives you a very easy way to interact with your json file without going through the stress of writting the whole code yourself.  

 it comes with awesome _methods_ that resembles those of a real database modules and __more__.

## importance of using jsondb
* it is free from ___sql injection___
* enables you to encrypt you data after any operation preventing you whole data from being seen in cased of   
<br>
<br>

## Guide
1.  __To create your data base you first need to instatian the ```json_database``` class__

    ``` python
    db = jsondatabase(["username", "password"], "user.json", id = True)
    ```

* The ```json_database``` class takes in 2 __compulsory parameters__
    * list of column in your database __eg. (["username","password"])__
    * the path to the file to store your json __eg. "user.json"__

* It also takes in an optional __id__ paremter, which when set to _True_ tells the program to keep track of id which will be unique.

    >__Note:__ We suggest that you set the __id__ to __True__ to have a unique property that you can query with

<br>

2.  __Add a row to the database__  
After instantiating the class user the ```.add_row()``` method.

    ``` python
    db.add_row(["Daniel","Daniel234"])
    ```

    this method takes in just a parameter which is a list of informations to be passed to the columns specified while innitialising the class

    In this examples we are passing 
    * __Daniel__ as the __usernane__ field and;

    * __Daniel123__ as the __password__ field. 

    it will be formated in the json file as
    ``` python
    {
        "id" : 1
        "username" : "Daniel",
        "password" : "Daniel234"
    }
    ```

<br>

3. __Get row from database__
* use the ```.get_row``` method to get a single row the database

    _get row takes in 2 parameters_:  
    a __column__ and the __value__  
    it returns the first row it could find that fits the condition 

    ### Eg:
    ``` python
        db.get_row("username","Daniel")
    ```

    ### output
    ``` python
    {
     "id" : 1
     "username" : "Daniel",
     "password" : "Daniel234"
    }
    ```
    > ___Note:___ you should get row by the __id__ in cases where there is a probability that other columns might have same value



* use the ```.filter_row``` method to filter out a list of rows with specified properties.  
It takes as many arguments that you'll like to filter by.
    ### Eg.
    ``` python
    db.filter_row(username = "daniel", password = "Daniel234")
    ```

    This method will return a list of __all row__ whose 
    * __username__ is __daniel__ and;
    * __password__ is __Daniel234__  


    >  more arguments can be passed depending on the number of rows present.

<br>

4. __Delete row__  
You use the ```.delter_row``` method to delete the row.  
It works just as the ```.get_row``` method does. but instead of returning the row it deletes it.
   
    ``` python
        db.delete_row("username","Daniel")
    ``` 
     the example deletes the first row whose _username_ is _Daniel_.

4. __view data__  
The ```.view_data``` method return a list of all the row in the database.

    * the ```.view_data``` and ```.view_data_class``` methods are similar.
    while view_data returns a list of all the rows
    view_data_class retuns a dictionary with data attribute set to a list of data.  

    <br>

5. __encrypting your data__  
    > encryption is a risky thing with jsondb, because leaving your data encrypted on termination of the program losses the special key produced on innitialization of the class.

    it there are two method available
    * ```.encrypt_data``` which encrypts your data
    * ```.decrypt data``` decrypts your data

    > for any operaation to be performed with the jsondb the data needs to be __decrypted__.

    the encryption also comes with a context '````.SecureData ````' manager that prevent your data from being decrypted in the middle of the program.  

    ``` python

        db.encrypt_data() # to encrypt  your data

        # the SecureData context manager allows you to operate on your database without encryption
        with SecureData():
            # All your operations goes here
            db.filter_row(username = "Daniel")

        #Dont forget to decrypt the file before termination
        db.dectypt() #to dectypt the data
    ```

    ___

    ## Authors contact
    ### phone 📞: [+2348123902721](tel:+234812392721)  
    ### email 📨: [winninggodspower@gmail.com](mailto:winninggodspower@gmail.com)
    ### website 🌐: [winningtech.tk](winningtech.tk)










