from flask import Response


class ApiResponse(Response):
    default_mimetype = 'application/json'
