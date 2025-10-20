from flask import Blueprint, jsonify, request
from flask_login import login_required
from datetime import datetime, timedelta
from sqlalchemy import func, and_
from models.student import Student
from models.attendance import Attendance
from models.class_model import Class
from models.user import db

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/reports/frequency/<int:student_id>', methods=['GET'])
@login_required
def get_student_frequency(student_id):
    """Gera relatório de frequência individual do aluno"""
    try:
        # Parâmetros de data
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        
        # Se não especificado, usar últimos 30 dias
        if not start_date or not end_date:
            end_date = datetime.now().date()
            start_date = end_date - timedelta(days=30)
        else:
            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            except ValueError:
                return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
        
        # Buscar aluno
        student = Student.query.get_or_404(student_id)
        
        # Buscar todas as presenças do período
        attendances = Attendance.query.filter(
            and_(
                Attendance.student_id == student_id,
                Attendance.date >= start_date,
                Attendance.date <= end_date
            )
        ).all()
        
        # Calcular estatísticas
        total_classes = len(attendances)
        present_count = sum(1 for att in attendances if att.present)
        absent_count = total_classes - present_count
        frequency_rate = (present_count / total_classes * 100) if total_classes > 0 else 0
        
        # Agrupar por mês para gráfico
        monthly_data = {}
        for attendance in attendances:
            month_key = attendance.date.strftime('%Y-%m')
            if month_key not in monthly_data:
                monthly_data[month_key] = {'present': 0, 'absent': 0}
            
            if attendance.present:
                monthly_data[month_key]['present'] += 1
            else:
                monthly_data[month_key]['absent'] += 1
        
        # Converter para lista ordenada
        monthly_chart = []
        for month, data in sorted(monthly_data.items()):
            monthly_chart.append({
                'month': month,
                'present': data['present'],
                'absent': data['absent'],
                'total': data['present'] + data['absent']
            })
        
        return jsonify({
            'student': student.to_dict(),
            'period': {
                'start_date': start_date.isoformat(),
                'end_date': end_date.isoformat()
            },
            'summary': {
                'total_classes': total_classes,
                'present_count': present_count,
                'absent_count': absent_count,
                'frequency_rate': round(frequency_rate, 2)
            },
            'monthly_data': monthly_chart,
            'detailed_attendance': [att.to_dict() for att in attendances]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@reports_bp.route('/reports/general-stats', methods=['GET'])
@login_required
def get_general_stats():
    """Gera estatísticas gerais do sistema"""
    try:
        # Parâmetros de data
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        
        # Se não especificado, usar últimos 30 dias
        if not start_date or not end_date:
            end_date = datetime.now().date()
            start_date = end_date - timedelta(days=30)
        else:
            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            except ValueError:
                return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
        
        # Estatísticas básicas
        total_students = Student.query.filter_by(active=True).count()
        total_classes = Class.query.filter_by(active=True).count()
        
        # Presenças no período
        attendances_period = Attendance.query.filter(
            and_(
                Attendance.date >= start_date,
                Attendance.date <= end_date
            )
        ).all()
        
        total_attendances = len(attendances_period)
        present_count = sum(1 for att in attendances_period if att.present)
        absent_count = total_attendances - present_count
        overall_frequency = (present_count / total_attendances * 100) if total_attendances > 0 else 0
        
        # Distribuição por faixa etária
        age_distribution = {
            'children': 0,    # 0-12
            'teens': 0,       # 13-17
            'adults': 0,      # 18+
            'unknown': 0      # sem data de nascimento
        }
        
        students = Student.query.filter_by(active=True).all()
        for student in students:
            age = student.get_age()
            if age is None:
                age_distribution['unknown'] += 1
            elif age <= 12:
                age_distribution['children'] += 1
            elif age <= 17:
                age_distribution['teens'] += 1
            else:
                age_distribution['adults'] += 1
        
        # Top 5 alunos com melhor frequência
        student_frequencies = []
        for student in students:
            student_attendances = [att for att in attendances_period if att.student_id == student.id]
            if student_attendances:
                student_present = sum(1 for att in student_attendances if att.present)
                student_total = len(student_attendances)
                frequency = (student_present / student_total * 100) if student_total > 0 else 0
                student_frequencies.append({
                    'student': student.to_dict(),
                    'frequency_rate': round(frequency, 2),
                    'total_classes': student_total,
                    'present_count': student_present
                })
        
        # Ordenar por frequência e pegar top 5
        top_students = sorted(student_frequencies, key=lambda x: x['frequency_rate'], reverse=True)[:5]
        
        # Frequência por turma
        class_frequencies = []
        classes = Class.query.filter_by(active=True).all()
        for class_obj in classes:
            class_attendances = [att for att in attendances_period if att.class_id == class_obj.id]
            if class_attendances:
                class_present = sum(1 for att in class_attendances if att.present)
                class_total = len(class_attendances)
                frequency = (class_present / class_total * 100) if class_total > 0 else 0
                class_frequencies.append({
                    'class': class_obj.to_dict(),
                    'frequency_rate': round(frequency, 2),
                    'total_attendances': class_total,
                    'present_count': class_present
                })
        
        # Presenças por dia da semana
        weekday_stats = {i: {'present': 0, 'absent': 0} for i in range(7)}
        for attendance in attendances_period:
            weekday = attendance.date.weekday()
            if attendance.present:
                weekday_stats[weekday]['present'] += 1
            else:
                weekday_stats[weekday]['absent'] += 1
        
        weekday_chart = []
        weekday_names = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
        for i, name in enumerate(weekday_names):
            weekday_chart.append({
                'day': name,
                'present': weekday_stats[i]['present'],
                'absent': weekday_stats[i]['absent'],
                'total': weekday_stats[i]['present'] + weekday_stats[i]['absent']
            })
        
        return jsonify({
            'period': {
                'start_date': start_date.isoformat(),
                'end_date': end_date.isoformat()
            },
            'overview': {
                'total_students': total_students,
                'total_classes': total_classes,
                'total_attendances': total_attendances,
                'present_count': present_count,
                'absent_count': absent_count,
                'overall_frequency': round(overall_frequency, 2)
            },
            'age_distribution': age_distribution,
            'top_students': top_students,
            'class_frequencies': class_frequencies,
            'weekday_distribution': weekday_chart
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@reports_bp.route('/reports/dashboard-stats', methods=['GET'])
@login_required
def get_dashboard_stats():
    """Estatísticas rápidas para o dashboard"""
    try:
        today = datetime.now().date()
        
        # Contadores básicos
        total_students = Student.query.filter_by(active=True).count()
        total_classes = Class.query.filter_by(active=True).count()
        
        # Presenças de hoje
        today_attendances = Attendance.query.filter(
            and_(
                Attendance.date == today,
                Attendance.present == True
            )
        ).count()
        
        # Usuários ativos (logaram nos últimos 30 dias)
        from models.user import User
        thirty_days_ago = datetime.now() - timedelta(days=30)
        active_users = User.query.filter(
            and_(
                User.active == True,
                User.last_login >= thirty_days_ago
            )
        ).count()
        
        return jsonify({
            'total_students': total_students,
            'total_classes': total_classes,
            'today_attendance': today_attendances,
            'active_users': active_users
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
