#Create a variable named grocery_list. 
#It should be a list,
#and the elements in the list should be a least 3 things that you need to buy from the grocery store.
grocery_list = ["fuse", "tape", "screw_driver"]

#Create a function named make_grocery_list. 
#When run, this function should write the contents of the grocery_list variable to a file named my_grocery_list.txt.
def make_grocery_list(grocery_list):
    with open('my_grocery_list.txt', 'w') as f:
        for item in grocery_list:
            f.write(item + "\n")
        
#Create a function named show_grocery_list. 
#When run, it should read the items from the text file and show each item on the grocery list.
def show_grocery_list():
    with open("my_grocery_list.txt") as f:
        items = f.read()
    return items
print(show_grocery_list()) 

#Create a function named buy_item. 
#It should accept the name of an item on the grocery list, and remove that item from the list.
def buy_item(item):
    grocery_list.remove(item)
    return grocery_list
buy_item("tape")