import json

def mobilepurchase(user_brand):
    mobile_file = open("mobileData.json")
    data_list = json.load(mobile_file)
    for i in data_list:
        if user_brand == (i["Brand"]):
            print(i)

def amountfilter(filter_price):
    filter_file = open("mobileData.json")
    amount_filter = json.load(filter_file)
    for j in amount_filter:
        if filter_price > (j["Price"]):
            print(j)

def cart():
    user_name = input("Username : ")
    cart_file = user_name+".txt"
    print("choose your favourite mobile and add to the cart")
    brand = input("Mobile phone brand : " )
    cart_data = open("mobileData.json")
    cart_data_add = json.load(cart_data)
    for k in cart_data_add:
        if brand == (k["Brand"]):
            with open(cart_file,'w') as storage:
                storage.write(json.dumps(k))


if __name__ == '__main__':
    print("1.List of mobiles","2.Filter Price of mobiles","3.add to cart")
    user_preference =  input("Enter the option : ")
    if user_preference == 1:
        Brands = ["Samsung", "Apple", "Redmi", "Oneplus", "vivo", "oppo"]
        print(Brands)
        user_brand = input("Enter the brand of mobile : ")
        mobilepurchase(user_brand)
    elif user_preference == 2:
        filter_price =int(input("Filter price of mobile : "))
        amountfilter(filter_price)
    else:
        cart()




