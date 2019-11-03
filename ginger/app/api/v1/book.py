from app.libs.redprint import Redprint


api = Redprint('book')

@api.route('', methods=['GET'])
def get_book():
    return 'i am a book'

@api.route('', methods=['POST'])
def create_book():
    return 'create book'