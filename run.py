from app import app, api
from app.resources.index import Index
from app.resources.users import UserRegistration, \
    UserLogin, UserLogoutAccess, UserLogoutRefresh, \
    TokenRefresh, GetUsers, GetUser, SecretResource

api.add_resource(Index, "/", "/index")
api.add_resource(UserRegistration, "/users/registration")
api.add_resource(UserLogin, "/users/login")
api.add_resource(UserLogoutAccess, "/logout/access")
api.add_resource(UserLogoutRefresh, "/logout/refresh")
api.add_resource(TokenRefresh, "/token/refresh")
api.add_resource(GetUsers, "/users")
api.add_resource(GetUser, "/users/<int:id>")
api.add_resource(SecretResource, "/secret")

if __name__ == '__main__':
    app.run(debug = True)
