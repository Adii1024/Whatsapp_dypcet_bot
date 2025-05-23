from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import pandas as pd
import os
from functools import lru_cache

app = Flask(__name__)

# Cache CSV data to avoid reading files repeatedly
@lru_cache(maxsize=None)
def load_csv_data():
    """Load all CSV files into memory for faster access"""
    data = {}
    csv_files = {
        'admission_requirements': 'dypcet_admission_requirements.csv',
        'bus_routes': 'dypcet_bus_routes.csv',
        'college_info': 'dypcet_college_info.csv',
        'complete_data': 'dypcet_complete_data.csv',
        'courses': 'dypcet_courses.csv',
        'facilities': 'dypcet_facilities.csv',
        'faculty_achievements': 'dypcet_faculty_achievements.csv',
        'placements': 'dypcet_placements.csv',
        'rankings': 'dypcet_rankings.csv',
        'recruiters': 'dypcet_recruiters.csv',
        'specializations': 'dypcet_specializations.csv',
        'student_achievements': 'dypcet_student_achievements.csv'
    }
    
    for key, filename in csv_files.items():
        try:
            if os.path.exists(filename):
                df = pd.read_csv(filename)
                # Clean column names - remove extra spaces and standardize
                df.columns = df.columns.str.strip()
                data[key] = df
                print(f"✅ Loaded {filename}")
                print(f"   Columns: {list(df.columns)}")
                print(f"   Shape: {df.shape}")
                if not df.empty:
                    print(f"   Sample data: {df.iloc[0].to_dict()}")
                print()
            else:
                print(f"❌ Warning: {filename} not found")
                data[key] = pd.DataFrame()
        except Exception as e:
            print(f"❌ Error loading {filename}: {str(e)}")
            data[key] = pd.DataFrame()
    
    return data

def get_courses_info(query=""):
    """Get courses information based on query"""
    data = load_csv_data()
    courses_df = data.get('courses', pd.DataFrame())
    
    if courses_df.empty:
        return "📚 Course information is currently unavailable."
    
    response = "📚 *DYPCET Courses Available:*\n\n"
    
    # Filter based on query if provided
    if query:
        query_lower = query.lower()
        if 'ug' in query_lower or 'undergraduate' in query_lower or 'btech' in query_lower or 'bachelor' in query_lower:
            filtered_courses = courses_df[courses_df['Level'] == 'UG']
        elif 'pg' in query_lower or 'postgraduate' in query_lower or 'mtech' in query_lower or 'master' in query_lower:
            filtered_courses = courses_df[courses_df['Level'] == 'PG']
        elif 'phd' in query_lower or 'doctorate' in query_lower:
            filtered_courses = courses_df[courses_df['Level'] == 'Ph.D']
        else:
            filtered_courses = courses_df
    else:
        filtered_courses = courses_df
    
    # Group by level
    for level in ['UG', 'PG', 'Ph.D']:
        level_courses = filtered_courses[filtered_courses['Level'] == level]
        if not level_courses.empty:
            level_name = {'UG': 'Undergraduate (B.Tech/B.Arch)', 'PG': 'Postgraduate (M.Tech)', 'Ph.D': 'Doctorate (Ph.D)'}
            response += f"🎓 *{level_name[level]}:*\n"
            
            for _, course in level_courses.iterrows():
                course_name = course['Course']
                course_type = course['Type']
                response += f"   • {course_name} ({course_type})\n"
            response += "\n"
    
    return response

def get_specializations_info(query=""):
    """Get specializations information"""
    data = load_csv_data()
    spec_df = data.get('specializations', pd.DataFrame())
    
    if spec_df.empty:
        return "🔬 Specialization information is currently unavailable."
    
    response = "🔬 *DYPCET Specializations:*\n\n"
    
    # Filter by department if specified
    if query:
        query_lower = query.lower()
        dept_keywords = {
            'cse': 'Computer Science',
            'computer': 'Computer Science',
            'it': 'Information Technology',
            'mechanical': 'Mechanical',
            'civil': 'Civil',
            'electrical': 'Electrical',
            'electronics': 'Electronics',
            'chemical': 'Chemical',
            'architecture': 'Architecture'
        }
        
        filtered_spec = spec_df
        for keyword, dept in dept_keywords.items():
            if keyword in query_lower:
                filtered_spec = spec_df[spec_df['Department'].str.contains(dept, case=False, na=False)]
                break
    else:
        filtered_spec = spec_df
    
    # Group by department
    departments = filtered_spec['Department'].unique()
    for dept in sorted(departments):
        if pd.notna(dept) and str(dept).strip():
            dept_specs = filtered_spec[filtered_spec['Department'] == dept]
            response += f"🏛️ *{dept}:*\n"
            for _, spec in dept_specs.iterrows():
                spec_name = spec['Specialization']
                if pd.notna(spec_name) and str(spec_name).strip():
                    response += f"   • {spec_name}\n"
            response += "\n"
    
    return response

def get_facilities_info(query=""):
    """Get facilities information"""
    data = load_csv_data()
    facilities_df = data.get('facilities', pd.DataFrame())
    
    if facilities_df.empty:
        return "🏢 Facilities information is currently unavailable."
    
    response = "🏢 *DYPCET Facilities:*\n\n"
    
    # Filter based on query
    if query:
        query_lower = query.lower()
        if 'lab' in query_lower:
            filtered_facilities = facilities_df[facilities_df['Category'] == 'Labs']
        elif 'infrastructure' in query_lower:
            filtered_facilities = facilities_df[facilities_df['Category'] == 'Infrastructure']
        elif 'transport' in query_lower or 'bus' in query_lower:
            filtered_facilities = facilities_df[facilities_df['Category'] == 'Transportation']
        elif 'scholarship' in query_lower:
            filtered_facilities = facilities_df[facilities_df['Category'] == 'Scholarships']
        else:
            filtered_facilities = facilities_df
    else:
        filtered_facilities = facilities_df
    
    # Group by category
    categories = filtered_facilities['Category'].unique()
    for category in sorted(categories):
        if pd.notna(category) and str(category).strip():
            cat_facilities = filtered_facilities[filtered_facilities['Category'] == category]
            response += f"🔹 *{category}:*\n"
            for _, facility in cat_facilities.iterrows():
                facility_name = facility['Facility']
                details = facility['Details']
                if pd.notna(facility_name) and str(facility_name).strip():
                    response += f"   • *{facility_name}*\n"
                    if pd.notna(details) and str(details).strip():
                        response += f"     {details}\n"
            response += "\n"
    
    return response

def get_placement_info():
    """Get placement statistics"""
    data = load_csv_data()
    placements_df = data.get('placements', pd.DataFrame())
    recruiters_df = data.get('recruiters', pd.DataFrame())
    
    if placements_df.empty:
        return "💼 Placement information is currently unavailable."
    
    response = "💼 *DYPCET Placement Statistics (2023-24):*\n\n"
    
    # Key placement metrics
    key_metrics = [
        ('Highest Package', '💰'),
        ('Average Package', '📊'),
        ('Job Offers 2023-24', '🎯'),
        ('Campus Placement Drives', '🏢'),
        ('Students Participated', '👨‍🎓'),
    ]
    
    for metric, emoji in key_metrics:
        metric_data = placements_df[placements_df['Metric'] == metric]
        if not metric_data.empty:
            value = metric_data.iloc[0]['Value']
            details = metric_data.iloc[0]['Details']
            response += f"{emoji} *{metric}:* {value}\n"
            if pd.notna(details) and str(details).strip() and details != value:
                response += f"   {details}\n"
            response += "\n"
    
    # Internship information
    response += "🎓 *Internship Programs:*\n"
    internship_metrics = ['Internship Students', 'Paid Internship', 'Final Year Internship']
    for metric in internship_metrics:
        metric_data = placements_df[placements_df['Metric'] == metric]
        if not metric_data.empty:
            value = metric_data.iloc[0]['Value']
            details = metric_data.iloc[0]['Details']
            response += f"   • {details}: {value}\n"
    response += "\n"
    
    # Package distribution
    response += "💵 *Package Distribution:*\n"
    package_metrics = ['Top 13 Packages', 'Top 19 Packages', 'Top 230 Packages', 'Top 289 Packages']
    for metric in package_metrics:
        metric_data = placements_df[placements_df['Metric'] == metric]
        if not metric_data.empty:
            value = metric_data.iloc[0]['Value']
            details = metric_data.iloc[0]['Details']
            response += f"   • {details}: {value}\n"
    response += "\n"
    
    # Add recruiters if available
    if not recruiters_df.empty:
        response += "🏢 *Top Recruiters:*\n"
        for _, recruiter in recruiters_df.iterrows():
            company = recruiter['Company']
            package = recruiter['Package']
            students = recruiter['Selected_Students']
            if pd.notna(company):
                response += f"   • *{company}* - {package}"
                if pd.notna(students) and students != 'Multiple':
                    response += f" ({students})"
                response += "\n"
    
    return response

def get_college_info():
    """Get basic college information"""
    data = load_csv_data()
    college_df = data.get('college_info', pd.DataFrame())
    
    if college_df.empty:
        return "🏛️ College information is currently unavailable."
    
    response = "🏛️ *About DYPCET:*\n\n"
    
    # Group by category
    categories = college_df['Category'].unique()
    for category in categories:
        if pd.notna(category) and str(category).strip():
            cat_info = college_df[college_df['Category'] == category]
            response += f"📌 *{category}:*\n"
            for _, info in cat_info.iterrows():
                field = info['Field']
                value = info['Value']
                details = info['Details']
                if pd.notna(field) and pd.notna(value):
                    response += f"   • *{field}:* {value}\n"
                    if pd.notna(details) and str(details).strip() and details != value:
                        response += f"     {details}\n"
            response += "\n"
    
    return response

def get_rankings_info():
    """Get college rankings"""
    data = load_csv_data()
    rankings_df = data.get('rankings', pd.DataFrame())
    
    if rankings_df.empty:
        return "🏆 Rankings information is currently unavailable."
    
    response = "🏆 *DYPCET Rankings & Accreditations:*\n\n"
    
    for _, ranking in rankings_df.iterrows():
        agency = ranking['Ranking_Agency']
        category = ranking['Category']
        rank = ranking['Rank']
        year = ranking['Year']
        details = ranking['Details']
        grade = ranking['Grade']
        cgpa = ranking['CGPA']
        status = ranking['Status']
        period = ranking['Period']
        
        if pd.notna(agency):
            response += f"🎖️ *{agency}*\n"
            if pd.notna(category):
                response += f"   Category: {category}\n"
            if pd.notna(rank):
                response += f"   Rank: {rank}\n"
            if pd.notna(grade):
                response += f"   Grade: {grade}\n"
            if pd.notna(cgpa):
                response += f"   CGPA: {cgpa}\n"
            if pd.notna(status):
                response += f"   Status: {status}\n"
            if pd.notna(year):
                response += f"   Year: {year}\n"
            if pd.notna(period):
                response += f"   Period: {period}\n"
            if pd.notna(details):
                response += f"   Details: {details}\n"
            response += "\n"
    
    return response

def get_bus_routes_info(query=""):
    """Get bus routes information"""
    data = load_csv_data()
    bus_df = data.get('bus_routes', pd.DataFrame())
    
    if bus_df.empty:
        return "🚌 Bus routes information is currently unavailable."
    
    response = "🚌 *DYPCET Bus Routes:*\n\n"
    
    if query:
        # Filter by route name
        query_lower = query.lower()
        filtered_routes = bus_df[bus_df['Route'].str.contains(query_lower, case=False, na=False)]
        if filtered_routes.empty:
            filtered_routes = bus_df
    else:
        filtered_routes = bus_df
    
    for _, route in filtered_routes.iterrows():
        route_name = route['Route']
        departure_time = route['Departure_Time']
        fare = route['Fare']
        stops = route['Stops']
        
        response += f"🚍 *Route: {route_name}*\n"
        response += f"   ⏰ Departure Time: {departure_time}\n"
        response += f"   💰 Monthly Fare: ₹{fare}\n"
        if pd.notna(stops) and str(stops).strip():
            response += f"   🛑 Stops: {stops}\n"
        response += "\n"
    
    return response

def get_admission_requirements():
    """Get admission requirements"""
    data = load_csv_data()
    admission_df = data.get('admission_requirements', pd.DataFrame())
    
    if admission_df.empty:
        return "📝 Admission requirements information is currently unavailable."
    
    response = "📝 *DYPCET Admission Requirements:*\n\n"
    
    # Group by category
    categories = admission_df['Category'].unique()
    for category in categories:
        if pd.notna(category) and str(category).strip():
            cat_reqs = admission_df[admission_df['Category'] == category]
            response += f"📋 *{category}:*\n"
            for _, req in cat_reqs.iterrows():
                requirement = req['Requirement']
                details = req['Details']
                if pd.notna(requirement):
                    response += f"   • *{requirement}:* {details}\n"
            response += "\n"
    
    return response

def get_faculty_achievements():
    """Get faculty achievements"""
    data = load_csv_data()
    faculty_df = data.get('faculty_achievements', pd.DataFrame())
    
    if faculty_df.empty:
        return "👨‍🏫 Faculty achievements information is currently unavailable."
    
    response = "👨‍🏫 *DYPCET Faculty Achievements:*\n\n"
    
    # Group by category
    categories = faculty_df['Category'].unique()
    for category in categories:
        if pd.notna(category) and str(category).strip():
            cat_achievements = faculty_df[faculty_df['Category'] == category]
            response += f"🏆 *{category}:*\n"
            for _, achievement in cat_achievements.iterrows():
                metric = achievement['Metric']
                value = achievement['Value']
                if pd.notna(metric) and pd.notna(value):
                    response += f"   • {metric}: {value}\n"
            response += "\n"
    
    return response

def get_student_achievements():
    """Get student achievements"""
    data = load_csv_data()
    student_df = data.get('student_achievements', pd.DataFrame())
    
    if student_df.empty:
        return "🏅 Student achievements information is currently unavailable."
    
    response = "🏅 *DYPCET Student Achievements:*\n\n"
    
    # Group by category
    categories = student_df['Category'].unique()
    for category in categories:
        if pd.notna(category) and str(category).strip():
            cat_achievements = student_df[student_df['Category'] == category]
            response += f"🥇 *{category}:*\n"
            for _, achievement in cat_achievements.iterrows():
                achievement_name = achievement['Achievement']
                student = achievement['Student']
                year = achievement['Year']
                if pd.notna(achievement_name):
                    response += f"   • *{achievement_name}*\n"
                    response += f"     Student: {student}\n"
                    if pd.notna(year):
                        response += f"     Year: {year}\n"
            response += "\n"
    
    return response

def process_whatsapp_message(message):
    """Process incoming WhatsApp message and return appropriate response"""
    message_lower = message.lower().strip()
    
    # Course-related queries
    if any(keyword in message_lower for keyword in ['course', 'program', 'degree', 'study', 'ug', 'pg', 'undergraduate', 'postgraduate', 'btech', 'mtech']):
        return get_courses_info(message_lower)
    
    # Specialization queries
    elif any(keyword in message_lower for keyword in ['specialization', 'branch', 'department', 'cse', 'mechanical', 'civil', 'electrical', 'computer science', 'electronics']):
        return get_specializations_info(message_lower)
    
    # Facilities queries
    elif any(keyword in message_lower for keyword in ['facility', 'facilities', 'lab', 'library', 'hostel', 'infrastructure', 'campus']):
        return get_facilities_info(message_lower)
    
    # Placement queries
    elif any(keyword in message_lower for keyword in ['placement', 'job', 'recruit', 'company', 'package', 'salary', 'career']):
        return get_placement_info()
    
    # College info queries
    elif any(keyword in message_lower for keyword in ['about', 'college', 'institute', 'information', 'dypcet', 'history']):
        return get_college_info()
    
    # Rankings queries
    elif any(keyword in message_lower for keyword in ['ranking', 'rank', 'naac', 'nba', 'accreditation', 'grade']):
        return get_rankings_info()
    
    # Bus routes queries
    elif any(keyword in message_lower for keyword in ['bus', 'transport', 'route', 'travel', 'fare']):
        return get_bus_routes_info(message_lower)
    
    # Admission queries
    elif any(keyword in message_lower for keyword in ['admission', 'eligibility', 'requirement', 'document', 'apply', 'entrance']):
        return get_admission_requirements()
    
    # Faculty queries
    elif any(keyword in message_lower for keyword in ['faculty', 'teacher', 'professor', 'staff', 'research', 'phd']):
        return get_faculty_achievements()
    
    # Student achievement queries
    elif any(keyword in message_lower for keyword in ['student achievement', 'student success', 'award', 'competition', 'sports', 'cultural']):
        return get_student_achievements()
    
    # Greeting
    elif any(keyword in message_lower for keyword in ['hi', 'hello', 'hey', 'good morning', 'good afternoon', 'good evening', 'start', 'help']):
        return """👋 *Welcome to DYPCET Information Bot!*

I can help you with information about:
🎓 Courses & Programs (UG, PG, Ph.D)
🔬 Specializations by Department
🏢 Facilities & Infrastructure
💼 Placements & Career
🏛️ College Information
🏆 Rankings & Accreditations
🚌 Bus Routes & Transport
📝 Admission Requirements
👨‍🏫 Faculty Achievements
🏅 Student Achievements

Just ask me anything about DYPCET! For example:
• "Tell me about courses"
• "What are the facilities?"
• "Placement statistics"
• "Bus routes from Sangli"
• "Computer science specializations"""
    
    # Default response for unrecognized queries
    else:
        return f"""❓ I understand you're asking about: *"{message}"*

I can help you with information about:
• *Courses* - UG/PG/PhD programs
• *Specializations* - Department-wise areas
• *Facilities* - Labs, infrastructure, amenities
• *Placements* - Statistics, companies, packages
• *College Info* - About DYPCET, history
• *Rankings* - NAAC, NBA accreditations
• *Bus Routes* - Transport from various cities
• *Admissions* - Requirements, documents
• *Faculty* - Research achievements
• *Students* - Awards and achievements

Please try asking about any of these topics! 😊"""

@app.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    """Handle incoming WhatsApp messages"""
    try:
        # Debug: Print all incoming data
        print("=== INCOMING WEBHOOK DATA ===")
        print(f"Method: {request.method}")
        print(f"Headers: {dict(request.headers)}")
        print(f"Form data: {dict(request.form)}")
        print(f"Values: {dict(request.values)}")
        
        # Get the message from the request
        incoming_msg = request.values.get('Body', '').strip()
        sender = request.values.get('From', '')
        
        print(f"Incoming message: '{incoming_msg}'")
        print(f"From: {sender}")
        
        if not incoming_msg:
            print("Warning: No message body received")
            resp = MessagingResponse()
            resp.message("I didn't receive your message. Please try again.")
            return str(resp)
        
        # Process the message and get response
        response_text = process_whatsapp_message(incoming_msg)
        print(f"Response: {response_text[:100]}...")  # Print first 100 chars
        
        # Create Twilio response
        resp = MessagingResponse()
        resp.message(response_text)
        
        print("=== SENDING RESPONSE ===")
        print(str(resp))
        
        return str(resp)
    
    except Exception as e:
        # Enhanced error handling
        print(f"ERROR in whatsapp_webhook: {str(e)}")
        import traceback
        traceback.print_exc()
        
        resp = MessagingResponse()
        resp.message("Sorry, I encountered an error. Please try again later.")
        return str(resp)

@app.route('/', methods=['GET', 'POST'])
def home():
    """Home page and fallback webhook"""
    if request.method == 'POST':
        # Handle POST requests (Twilio webhook)
        return whatsapp_webhook()
    else:
        # Handle GET requests (browser access)
        return """
        <h1>DYPCET WhatsApp Bot</h1>
        <p>This bot provides information about DYPCET college through WhatsApp.</p>
        <p>Send a message to the configured WhatsApp number to interact with the bot.</p>
        <h3>Available Information:</h3>
        <ul>
            <li>Courses and Programs (UG/PG/PhD)</li>
            <li>Specializations by Department</li>
            <li>Facilities and Infrastructure</li>
            <li>Placement Statistics</li>
            <li>College Information</li>
            <li>Rankings and Accreditations</li>
            <li>Bus Routes and Transport</li>
            <li>Admission Requirements</li>
            <li>Faculty Achievements</li>
            <li>Student Achievements</li>
        </ul>
        <p><strong>Status:</strong> Webhook is ready to receive messages!</p>
        """

@app.route('/debug-csv')
def debug_csv():
    """Debug endpoint to check CSV data"""
    data = load_csv_data()
    result = "<h1>CSV Debug Information</h1>"
    
    for key, df in data.items():
        result += f"<h2>{key.upper()}</h2>"
        if df.empty:
            result += "<p>No data loaded</p>"
        else:
            result += f"<p><strong>Shape:</strong> {df.shape}</p>"
            result += f"<p><strong>Columns:</strong> {list(df.columns)}</p>"
            result += "<h3>Sample Data:</h3>"
            result += df.head(3).to_html()
        result += "<hr>"
    
    return result

@app.route('/test-whatsapp', methods=['POST'])
def test_whatsapp():
    """Test WhatsApp functionality without Twilio"""
    try:
        test_message = request.json.get('message', 'hello') if request.is_json else request.form.get('message', 'hello')
        response = process_whatsapp_message(test_message)
        return {'status': 'success', 'message': test_message, 'response': response}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}

if __name__ == '__main__':
    print("Loading CSV data...")
    load_csv_data()  # Load data on startup
    print("DYPCET WhatsApp Bot starting...")
    app.run(debug=True, host='0.0.0.0', port=5000)