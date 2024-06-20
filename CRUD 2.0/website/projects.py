from flask import Blueprint, flash, render_template, request, redirect
from .model import Project, Member
from . import db

projects = Blueprint('projects', __name__)

@projects.route('/projects', methods=['GET', 'POST'])
def project():
    project=Project.query.all()
    return render_template("projects.html", project=project)

@projects.route('/projects/create' , methods = ['POST','GET'])
def create():
    if request.method == 'GET':
        return render_template('create_project.html')
    
    if request.method == 'POST':
        projectid = request.form.get('project_id')
        projectname = request.form.get('projectname')
        manager = request.form.get('manager')
        startdate = request.form.get('startdate')
        enddate = request.form.get('enddate')#gets input
    new_project = Project (project_id=projectid,
                           projectname=projectname, 
                           manager=manager,
                           startdate = startdate,
                           enddate = enddate)
    db.session.add(new_project)
    db.session.commit()
    
    return redirect('/projects')
    
@projects.route('/projects/delete/<int:project_id>', methods=['POST'])
def delete_row(project_id):

    row_to_delete = Project.query.get_or_404(project_id)     
    db.session.delete(row_to_delete)
    db.session.commit()
    return redirect('/projects')



@projects.route('/projects/update/<int:project_id>', methods=['GET','POST'])
def update(project_id):
    project_to_update = Project.query.get_or_404(project_id)
    
    if request.method == 'GET':
        return render_template('projectupdate.html', project=project_to_update)

    if request.method == 'POST':
        if project_to_update:
            db.session.delete(project_to_update)
            db.session.commit()
            projectid = request.form.get('project_id')
            projectname = request.form.get('projectname')
            manager = request.form.get('manager')
            startdate = request.form.get('startdate')
            enddate = request.form.get('enddate')

            update_project = Project (project_id=projectid,
                           projectname=projectname, 
                           manager=manager,
                           startdate = startdate,
                           enddate = enddate)
        
            db.session.add(update_project)
            db.session.commit()
            return redirect('/projects')
        
    else:
        return render_template("projectupdate.html", project_to_update=project_to_update)
 


@projects.route('/members', methods=['GET', 'POST'])
def members():
    return render_template("members.html", member=Member.query.all())


@projects.route('/members/create' , methods = ['GET','POST'])
def createmember():
    projectname = None
    member = None
    role = None
    startdate2 = None
    enddate2 = None

    if request.method == 'GET':
        return render_template("create_member.html")

    if request.method == 'POST':
        projectname = request.form.get('projectname')
        member = request.form.get('member')
        role = request.form.get('role')
        startdate2 = request.form.get('startdate')
        enddate2 = request.form.get('enddate')#gets input

    new_member = Member (  projectname = projectname, 
                           membername = member,
                           role = role,
                           startdate = startdate2,
                           enddate = enddate2)
    
    db.session.add(new_member)
    db.session.commit()
    flash('Member added!', category='success')
    return redirect('/members')

@projects.route('/members/update/<int:member_id>', methods=['GET','POST'])
def updatemember(member_id):
    member_to_update = Member.query.get_or_404(member_id)
    
    if request.method == 'GET':
        return render_template('memberupdate.html', member=member_to_update)

    if request.method == 'POST':
        if member_to_update:
            db.session.delete(member_to_update)
            db.session.commit()
            projectname = request.form.get('projectname')
            member = request.form.get('member')
            role = request.form.get('role')
            startdate2 = request.form.get('startdate')
            enddate2 = request.form.get('enddate')#gets input

            update_member = Member (  projectname = projectname, 
                           membername = member,
                           role = role,
                           startdate = startdate2,
                           enddate = enddate2)
        
            db.session.add(update_member)
            db.session.commit()
            return redirect('/members')
        
    else:
        return render_template("memberupdate.html", member_to_update=member_to_update)


@projects.route('/members/delete/<int:member_id>', methods=['POST'])
def delete_member(member_id):
    row_to_delete = Member.query.get_or_404(member_id)     
    db.session.delete(row_to_delete)
    db.session.commit()
    return redirect('/members')