from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        # get session key of current user
        cart = self.session.get('session_key')

        # if user is new create new key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        # making cart available in very page
        self.cart = cart
    
    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
        
        self.session.modified = True
    
    def __len__(self):
        return len(self.cart)
    
    def get_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return products