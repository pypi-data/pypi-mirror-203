# fastapi_framework
A mvc framework used FastApi
Simple and elegant use of FastApi in MVC mode

## usage:
install:
```bash
pip install fastapi-mvc-framework
```

controller:
```python
from fastapi_mvc_framework import api_router,api,Request,Response,BaseController,application,WebSocket,WebSocketDisconnect
from typing import Dict 
from app.services import UserService

application._public_auth_url = '/user/login'
application._user_auth_url = '/user/login'

@api_router(auth='public')
class TestController(BaseController): 
    @api.get("/user/login")
    def login(self):
        """:title Login"""  
        redirect = self.params['redirect'] if 'redirect' in self.params else '/' 
        return self.view() 
    
    @api.get("/user/logout")
    def logout(self):
        return self._user_logout()
    
    @api.post("/test/verity_user")
    async def verity_user(self): 
        form = self.params
        username = form['username']
        password = form['password']
        redirect = form['redirect']
        if username and password:
            #do veritied
            if username in ['bruce','alice'] and password:
                return self._verity_successed(username,redirect)
            else:
                return self._verity_error() 
        return self._verity_error()
    
    @api.get("/" )
    def home(self,request:Request): 
        '''
        :title Home
        '''
        c = self.session.get('home',1)
        c = c+1  
        self.cookies["a"] = c
        if c>10:
            del self.cookies["a"]
            c = 0
        self.session['home'] = c
        text = "Hello World! I'm in FastapiMvcFramework"
        routers_map = application.routers_map
        routers = application.routes 
        return self.view()
    
    @api.get("/xml",auth='user')
    def get_legacy_data(self):
        """:title XML(Protected)"""

        data = """<?xml version="1.0"?>
        <shampoo>
        <Header>
            Apply shampoo here.
        </Header>
        <Body>
            You'll have to use soap here.
        </Body>
        </shampoo>
        """
        return self.view(content=data,media_type="application/xml")
          
    @api.get("/chatgpt")
    def chatgpt(self):
        """
        :title Chat
        """
        return self.view()


```

home.html:

```html
<body>
    <header>
        <h1>My Website</h1>
    </header>
    <nav>
        {% for item in routers_map %} {% if 'GET' in routers_map[item]['methods'] %}
        <a href="{{routers_map[item]['path']}}">{{routers_map[item]['doc'] and routers_map[item]['doc']['title'] or item}}</a> {% endif %} {% endfor %}

        <a href="#">About</a>
        <a href="#">Contact</a> {% if request.session['user'] %}
        <a href="/user/logout"><b>{{request.session['user']['username']}}</b> Logout</a> {% endif %}
    </nav>
    <section>
        <h2>Welcome to my website</h2>
        <p>This is an example of a responsive design that works well on both desktop and mobile devices.</p>
        <p>here is the `text` variable in class method:{{text}}</p>
        <p style="color:red"><b>{{flash}}</b></p>
    </section>
    <footer>
        <p>&copy; 2023 My Website</p>
    </footer>
</body>
```

your project directory structrue like this:
```
+---app
|   |   __init__.py
|   |
|   +---controllers
|   |   |   test_controller.py
|   |   |   __init__.py
|   |   |
|   +---models
|   |   |   user_model.py
|   |   |   __init__.py
|   |   |
|   +---services
|   |   |   user_service.py
|   |   |   __init__.py
|   |   |
|   +---views
|   |   +---abc
|   |   |   \---2.0
|   |   |           css.css
|   |   |           home.html
|   |   |
|   |   +---test
|   |   |       chatgpt.css
|   |   |       chatgpt.html
|   |   |       chatgpt.js
|   |   |       home.html
|   |   |       home.js
|   |   |       login.html
|   |   |
|   |   \---ws
|   |           ws_home.html
|   |
+---app1
|   |   __init__.py
|   |
|   +---controllers
|   |   |   test1_controller.py
|   |   |   __init__.py
|   |   |
|   +---views
|   |   +---test1
|   |   |   \---v1.0
|   |   |           home.css
|   |   |           home.html
|   |   |           home1.css
|   |   |
|   |   \---test2
|
+---configs
|       alembic.ini
|       cache.yaml
|       casbin-adapter.csv
|       casbin-model.conf
|       database.yaml
|       general.yaml
|       session.yaml
|
+---data
|   +---alembic
|   |   |   env.py
|   |   |   README
|   |   |   script.py.mako
|   |   |
|   |   +---versions
|   |   |   |   0d0205db5b39_create_tables.py
|   |   |   |   0e4e15e67367_autogenerate.py
|   |   |   |   108dad121227__new_upgrade_operations_detected__add_.py
|   |   |   |   ac7ce07126b3_autogenerate.py
|   |   |   |   e51711eb3d84_autogenerate.py
|   |   |   |
|   \---db
|           test.db

```