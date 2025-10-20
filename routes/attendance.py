from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from datetime import datetime
from models.attendance import Attendance, db
from models.student import Student
from models.class_model import Class, StudentClass

attendance_bp = Blueprint('attendance', __name__)

@attendance_bp.route('/attendance', methods=['GET'])
@login_required
def get_attendance():
    """Get attendance records with optional filters"""
    try:
        # Get query parameters
        student_id = request.args.get('student_id', type=int)
        class_id = request.args.get('class_id', type=int)
        date = request.args.get('date')
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        
        # Build query
        query = Attendance.query
        
        if student_id:
            query = query.filter(Attendance.student_id == student_id)
        
        if class_id:
            query = query.filter(Attendance.class_id == class_id)
        
        if date:
            try:
                date_obj = datetime.strptime(date, '%Y-%m-%d').date()
                query = query.filter(Attendance.date == date_obj)
            except ValueError:
                return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
        
        if start_date and end_date:
            try:
                start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
                end_date_obj = datetime.strptime(end_date, '%Y-%m-%d').date()
                query = query.filter(Attendance.date >= start_date_obj, Attendance.date <= end_date_obj)
            except ValueError:
                return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
        
        attendances = query.order_by(Attendance.date.desc()).all()
        return jsonify([att.to_dict() for att in attendances])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@attendance_bp.route('/attendance', methods=['POST'])
@login_required
def create_attendance():
    """Create or update attendance record"""
    try:
        data = request.json
        
        if not data.get('student_id') or not data.get('class_id') or not data.get('date'):
            return jsonify({'error': 'student_id, class_id, and date are required'}), 400
        
        # Validate date format
        try:
            attendance_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
        
        # Validate student and class exist
        student = Student.query.get(data['student_id'])
        if not student:
            return jsonify({'error': 'Student not found'}), 404
        
        class_obj = Class.query.get(data['class_id'])
        if not class_obj:
            return jsonify({'error': 'Class not found'}), 404
        
        # Check if student is enrolled in the class
        enrollment = StudentClass.query.filter_by(
            student_id=data['student_id'],
            class_id=data['class_id'],
            active=True
        ).first()
        
        if not enrollment:
            return jsonify({'error': 'Student is not enrolled in this class'}), 400
        
        # Check if attendance already exists
        existing_attendance = Attendance.query.filter_by(
            student_id=data['student_id'],
            class_id=data['class_id'],
            date=attendance_date
        ).first()
        
        if existing_attendance:
            # Update existing record
            existing_attendance.present = data.get('present', True)
            existing_attendance.notes = data.get('notes')
            existing_attendance.recorded_by = current_user.id
            existing_attendance.recorded_at = datetime.utcnow()
            
            db.session.commit()
            return jsonify(existing_attendance.to_dict())
        else:
            # Create new record
            attendance = Attendance(
                student_id=data['student_id'],
                class_id=data['class_id'],
                date=attendance_date,
                present=data.get('present', True),
                notes=data.get('notes'),
                recorded_by=current_user.id
            )
            
            db.session.add(attendance)
            db.session.commit()
            return jsonify(attendance.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@attendance_bp.route('/attendance/<int:attendance_id>', methods=['GET'])
@login_required
def get_attendance_record(attendance_id):
    """Get a specific attendance record"""
    try:
        attendance = Attendance.query.get_or_404(attendance_id)
        return jsonify(attendance.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@attendance_bp.route('/attendance/<int:attendance_id>', methods=['PUT'])
@login_required
def update_attendance(attendance_id):
    """Update an attendance record"""
    try:
        attendance = Attendance.query.get_or_404(attendance_id)
        data = request.json
        
        # Update fields
        if 'present' in data:
            attendance.present = data['present']
        if 'notes' in data:
            attendance.notes = data['notes']
        
        attendance.recorded_by = current_user.id
        attendance.recorded_at = datetime.utcnow()
        
        db.session.commit()
        return jsonify(attendance.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@attendance_bp.route('/attendance/<int:attendance_id>', methods=['DELETE'])
@login_required
def delete_attendance(attendance_id):
    """Delete an attendance record"""
    try:
        attendance = Attendance.query.get_or_404(attendance_id)
        db.session.delete(attendance)
        db.session.commit()
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@attendance_bp.route('/attendance/bulk', methods=['POST'])
@login_required
def bulk_attendance():
    """Create or update multiple attendance records at once"""
    try:
        data = request.json
        
        if not data.get('class_id') or not data.get('date') or not data.get('students'):
            return jsonify({'error': 'class_id, date, and students array are required'}), 400
        
        # Validate date format
        try:
            attendance_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
        
        # Validate class exists
        class_obj = Class.query.get(data['class_id'])
        if not class_obj:
            return jsonify({'error': 'Class not found'}), 404
        
        results = []
        
        for student_data in data['students']:
            if not student_data.get('student_id'):
                continue
            
            student_id = student_data['student_id']
            present = student_data.get('present', True)
            notes = student_data.get('notes')
            
            # Validate student exists and is enrolled
            student = Student.query.get(student_id)
            if not student:
                results.append({
                    'student_id': student_id,
                    'error': 'Student not found'
                })
                continue
            
            enrollment = StudentClass.query.filter_by(
                student_id=student_id,
                class_id=data['class_id'],
                active=True
            ).first()
            
            if not enrollment:
                results.append({
                    'student_id': student_id,
                    'error': 'Student not enrolled in this class'
                })
                continue
            
            # Check if attendance already exists
            existing_attendance = Attendance.query.filter_by(
                student_id=student_id,
                class_id=data['class_id'],
                date=attendance_date
            ).first()
            
            if existing_attendance:
                # Update existing record
                existing_attendance.present = present
                existing_attendance.notes = notes
                existing_attendance.recorded_by = current_user.id
                existing_attendance.recorded_at = datetime.utcnow()
                
                results.append({
                    'student_id': student_id,
                    'status': 'updated',
                    'attendance': existing_attendance.to_dict()
                })
            else:
                # Create new record
                attendance = Attendance(
                    student_id=student_id,
                    class_id=data['class_id'],
                    date=attendance_date,
                    present=present,
                    notes=notes,
                    recorded_by=current_user.id
                )
                
                db.session.add(attendance)
                results.append({
                    'student_id': student_id,
                    'status': 'created',
                    'attendance': attendance.to_dict()
                })
        
        db.session.commit()
        return jsonify({
            'message': 'Bulk attendance processed',
            'results': results
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
