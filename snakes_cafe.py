Menu = ["Wings",'Cookies',"Spring Rolls","Salmon","Steak","Meat Tornado","A Literal Garden","Ice Cream","Cake","Pie","Coffee","Tea","Unicorn Tears"]
 
currentOrder = dict()

def intro():
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

''')
    print('''
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
    ''')

def user_insertion():
    user_input=input(">")  
    return user_input        

def main():
    user_input = user_insertion()
    while(user_input.lower() != "quit"): 
            if user_input in Menu:
                add_item_to_order(user_input)
                print("** " + str(currentOrder[user_input]) + " orders of " + user_input + " have been added to your meal **")
            else:
                print(user_input + " does not exist in the menu but was added as customized item in order")
                add_item_to_order(user_input)

                
            user_input = user_insertion()  
      
    print_summary()
    end_application()

def add_item_to_order(item):
    if item in currentOrder:
        currentOrder[item] = currentOrder[item]+1
    else:
        currentOrder[item] =1

def end_application():
    print("thanks for using snakes cafe application !")  

def print_summary():
    totalItems = 0

    print('') 
    print('*********** Order Summary ************') 

    for item in currentOrder:
        totalItems += currentOrder[item]
        print(item + ":" + str(currentOrder[item]))

    print('') 
    print("total items:" + str(totalItems))
    print('**************************************') 



if __name__=="__main__": 
    intro()  
    main()
