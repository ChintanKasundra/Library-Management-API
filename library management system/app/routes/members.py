from flask import Blueprint, request, jsonify
from app.utils.auth import token_required
from app.utils.helpers import paginate

members_bp = Blueprint('members', __name__)

# In-memory data storage
members = []

@members_bp.route('/', methods=['GET', 'POST'])
@token_required
def manage_members():
    if request.method == 'POST':
        member = request.json
        member['id'] = len(members) + 1
        members.append(member)
        return jsonify({'message': 'Member added successfully', 'member': member}), 201

    elif request.method == 'GET':
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 5))
        paginated_members = paginate(members, page, per_page)
        return jsonify({
            'members': paginated_members,
            'total_members': len(members),
            'current_page': page,
            'per_page': per_page
        }), 200

@members_bp.route('/<int:member_id>', methods=['GET', 'PUT', 'DELETE'])
@token_required
def manage_member(member_id):
    for member in members:
        if member['id'] == member_id:
            if request.method == 'GET':
                return jsonify(member), 200

            elif request.method == 'PUT':
                member.update(request.json)
                return jsonify({'message': 'Member updated successfully', 'member': member}), 200

            elif request.method == 'DELETE':
                members.remove(member)
                return jsonify({'message': 'Member deleted successfully'}), 200

    return jsonify({'message': 'Member not found'}), 404
