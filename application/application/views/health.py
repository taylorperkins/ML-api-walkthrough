from flask_api import status

from application import api


@api.route('/health')
def health():
    return {'message': 'Success!', 'status_code': 200}, status.HTTP_200_OK
