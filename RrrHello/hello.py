from flask.ext.restful import fields, Resource, marshal


class HelloAPI(Resource):
    """ Returns the inputted name in JSON  """
    def __init__(self):
        self.hello_fields = {'name': fields.String}
        super(HelloAPI, self).__init__()

    def get(self, name='World'):
        response = {'name': name}
        return marshal(response, self.hello_fields), 200

    def options(self):
        response = \
        {
            "GET": {
                "description": "Display name in JSON",
                "examples": [
                        "\/hello",
                        "\/hello\/:name"
                ],
                "properties": {
                    "name": {
                        "description": "Name to return",
                        "type": "string",
                        "required": False,
                        "default": "World"
                    }
                }
            }
        }
        return (response, 200)

