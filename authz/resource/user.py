from flask_restful import Resource


class UserResource(Resource):

    def get(self):
        return {"Hello": "World!"}
