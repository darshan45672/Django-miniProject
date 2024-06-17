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