from app import app
@app.route('/admin/dashboard')
def admin_dashboard():
    return 'This is our admin dashboard'

@app.route('/admin/profile')
def admin_profile():
    return "<h1 style='Color:#ed872d'>Admin profile</h1>"