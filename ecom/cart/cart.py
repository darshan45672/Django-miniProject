from store.models import Product, Profile

class Cart():
    def __init__(self, request):
        self.session = request.session

        self.request = request

        # get session key of current user
        cart = self.session.get('session_key')

        # if user is new create new key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        # making cart available in very page
        self.cart = cart
    
    def dbAdd(self, product, quantity=1):
        product_id = str(product)
        product_quantity = str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_quantity)
        self.session.modified = True

        if self.request.user.is_authenticated:
            currentUser = Profile.objects.filter(user__id=self.request.user.id)
            convertedCart = str(self.cart).replace("\'", "\"")
            currentUser.update(oldCart=str(convertedCart))
    
    def add(self, product, quantity=1):
        product_id = str(product.id)
        product_quantity = str(quantity)

        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_quantity)
        
        self.session.modified = True

        if self.request.user.is_authenticated:
            currentUser = Profile.objects.filter(user__id=self.request.user.id)
            convertedCart = str(self.cart).replace("\'", "\"")
            currentUser.update(oldCart=str(convertedCart))
    
    def __len__(self):
        return len(self.cart)
    
    def get_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return products
    
    def get_quantity(self):
        return self.cart
    
    def update(self, product, quantity):
        productId = str(product)
        productQuantity = int(quantity)

        ourCart = self.cart

        ourCart[productId] = productQuantity

        self.session.modified = True

        if self.request.user.is_authenticated:
            currentUser = Profile.objects.filter(user__id=self.request.user.id)
            convertedCart = str(self.cart).replace("\'", "\"")
            currentUser.update(oldCart=str(convertedCart))

        updated = self.cart

        return updated
    
    def delete(self, product):
        productId = str(product)    

        if productId in self.cart:
            del self.cart[productId]
            self.session.modified = True
            if self.request.user.is_authenticated:
                currentUser = Profile.objects.filter(user__id=self.request.user.id)
                convertedCart = str(self.cart).replace("\'", "\"")
                currentUser.update(oldCart=str(convertedCart))
    
    def total(self):
        total = 0

        for product in self.get_products():
            total += product.price * self.cart[str(product.id)]
        
        return total