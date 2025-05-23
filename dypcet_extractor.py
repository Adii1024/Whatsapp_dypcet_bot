import pandas as pd
import csv
from io import StringIO

# DYPCET College Information Extraction and CSV Generation

def create_college_info_csv():
    """Create CSV with basic college information"""
    college_info = [
        {
            'Category': 'Basic Info',
            'Field': 'College Name',
            'Value': 'D. Y. Patil College of Engineering & Technology',
            'Details': 'Kasaba Bawada, Kolhapur'
        },
        {
            'Category': 'Basic Info',
            'Field': 'Establishment Year',
            'Value': '1984',
            'Details': 'Under visionary leadership of Padmashree Dr. D. Y. Patil'
        },
        {
            'Category': 'Basic Info',
            'Field': 'Type',
            'Value': 'Autonomous Institute',
            'Details': 'Self-financing, UGC and Shivaji University conferred status in 2020'
        },
        {
            'Category': 'Basic Info',
            'Field': 'Engineering DTE Code',
            'Value': 'EN 6250',
            'Details': 'For Engineering courses'
        },
        {
            'Category': 'Basic Info',
            'Field': 'Architecture DTE Code',
            'Value': 'AR 6532',
            'Details': 'For Architecture courses'
        },
        {
            'Category': 'Accreditation',
            'Field': 'NAAC Grade',
            'Value': 'A Grade',
            'Details': 'CGPA: 3.08'
        },
        {
            'Category': 'Accreditation',
            'Field': 'NBA Accreditation',
            'Value': 'Yes',
            'Details': 'CSE, E&TC, Mechanical Engineering (2022-2025)'
        }
    ]
    
    return pd.DataFrame(college_info)

def create_courses_csv():
    """Create CSV with course information"""
    courses_data = [
        # UG Courses
        {'Level': 'UG', 'Sr_No': 1, 'Course': 'Chemical Engineering', 'Type': 'B.Tech'},
        {'Level': 'UG', 'Sr_No': 2, 'Course': 'Civil Engineering', 'Type': 'B.Tech'},
        {'Level': 'UG', 'Sr_No': 3, 'Course': 'Computer Science and Engineering', 'Type': 'B.Tech'},
        {'Level': 'UG', 'Sr_No': 4, 'Course': 'Computer Science and Engineering (AI & ML)', 'Type': 'B.Tech'},
        {'Level': 'UG', 'Sr_No': 5, 'Course': 'Computer Science and Engineering (Data Science)', 'Type': 'B.Tech'},
        {'Level': 'UG', 'Sr_No': 6, 'Course': 'Electronics and Telecommunication Engineering', 'Type': 'B.Tech'},
        {'Level': 'UG', 'Sr_No': 7, 'Course': 'Mechanical Engineering', 'Type': 'B.Tech'},
        {'Level': 'UG', 'Sr_No': 8, 'Course': 'School of Architecture', 'Type': 'B.Arch'},
        
        # PG Courses
        {'Level': 'PG', 'Sr_No': 1, 'Course': 'Computer Science and Engineering', 'Type': 'M.Tech'},
        {'Level': 'PG', 'Sr_No': 2, 'Course': 'Electronics and Telecommunication Engineering', 'Type': 'M.Tech'},
        
        # Ph.D
        {'Level': 'Ph.D', 'Sr_No': 1, 'Course': 'Computer Science and Engineering', 'Type': 'Ph.D'},
        {'Level': 'Ph.D', 'Sr_No': 2, 'Course': 'Electronics and Telecommunication Engineering', 'Type': 'Ph.D'}
    ]
    
    return pd.DataFrame(courses_data)

def create_specializations_csv():
    """Create CSV with department specializations"""
    specializations = [
        # Chemical Engineering
        {'Department': 'Chemical Engineering', 'Specialization': 'Energy Conservation and Recovery'},
        {'Department': 'Chemical Engineering', 'Specialization': 'Petrochemical Technology'},
        {'Department': 'Chemical Engineering', 'Specialization': 'Distillation Applications of MATLAB'},
        {'Department': 'Chemical Engineering', 'Specialization': 'Petroleum Refinery Engineering'},
        {'Department': 'Chemical Engineering', 'Specialization': 'Computational Techniques'},
        {'Department': 'Chemical Engineering', 'Specialization': 'Project Management and Smart Technology'},
        
        # Civil Engineering
        {'Department': 'Civil Engineering', 'Specialization': 'Transportation Engineering'},
        {'Department': 'Civil Engineering', 'Specialization': 'Remote Sensing and GIS'},
        {'Department': 'Civil Engineering', 'Specialization': 'Geotechnical Engineering'},
        {'Department': 'Civil Engineering', 'Specialization': 'Hydraulics'},
        {'Department': 'Civil Engineering', 'Specialization': 'Town and Urban Planning'},
        {'Department': 'Civil Engineering', 'Specialization': 'Structural Engineering'},
        {'Department': 'Civil Engineering', 'Specialization': 'Environmental Engineering'},
        {'Department': 'Civil Engineering', 'Specialization': 'Construction Management'},
        
        # Computer Science Engineering
        {'Department': 'Computer Science Engineering', 'Specialization': 'Software Engineering'},
        {'Department': 'Computer Science Engineering', 'Specialization': 'Artificial Intelligence'},
        {'Department': 'Computer Science Engineering', 'Specialization': 'Network Engineering'},
        {'Department': 'Computer Science Engineering', 'Specialization': 'Computer Graphics'},
        {'Department': 'Computer Science Engineering', 'Specialization': 'Data Science'},
        {'Department': 'Computer Science Engineering', 'Specialization': 'Programming Languages'},
        {'Department': 'Computer Science Engineering', 'Specialization': 'Databases'},
        
        # AI & ML
        {'Department': 'CSE (AI & ML)', 'Specialization': 'IoT'},
        {'Department': 'CSE (AI & ML)', 'Specialization': 'Healthcare Applications and Game Designing'},
        {'Department': 'CSE (AI & ML)', 'Specialization': 'Computer Vision'},
        {'Department': 'CSE (AI & ML)', 'Specialization': 'Artificial Intelligence'},
        {'Department': 'CSE (AI & ML)', 'Specialization': 'Human Computer Interface'},
        {'Department': 'CSE (AI & ML)', 'Specialization': 'Blockchain Technology'},
        
        # Data Science
        {'Department': 'CSE (Data Science)', 'Specialization': 'IoT'},
        {'Department': 'CSE (Data Science)', 'Specialization': 'Recommendation Systems'},
        {'Department': 'CSE (Data Science)', 'Specialization': 'Business Analytics'},
        {'Department': 'CSE (Data Science)', 'Specialization': 'Cyber Forensics'},
        {'Department': 'CSE (Data Science)', 'Specialization': 'Computer Vision'},
        {'Department': 'CSE (Data Science)', 'Specialization': 'E-Commerce and Marketing'},
        
        # Electronics & Telecommunication
        {'Department': 'Electronics & Telecommunication', 'Specialization': 'Embedded System'},
        {'Department': 'Electronics & Telecommunication', 'Specialization': 'Communication Systems'},
        {'Department': 'Electronics & Telecommunication', 'Specialization': 'Signal Processing'},
        {'Department': 'Electronics & Telecommunication', 'Specialization': 'VLSI & Embedded System'},
        {'Department': 'Electronics & Telecommunication', 'Specialization': 'Digital Electronics'},
        
        # Mechanical Engineering
        {'Department': 'Mechanical Engineering', 'Specialization': 'Manufacturing Processes'},
        {'Department': 'Mechanical Engineering', 'Specialization': 'Power Engineering'},
        {'Department': 'Mechanical Engineering', 'Specialization': 'Thermal Engineering'},
        {'Department': 'Mechanical Engineering', 'Specialization': 'Fluid Mechanics and Machineries'},
        {'Department': 'Mechanical Engineering', 'Specialization': 'Machine Design'},
        {'Department': 'Mechanical Engineering', 'Specialization': 'Mechatronics and Automation'},
        
        # Architecture
        {'Department': 'Architecture', 'Specialization': 'Urban Design'},
        {'Department': 'Architecture', 'Specialization': 'Green Building'},
        {'Department': 'Architecture', 'Specialization': 'Interior Design'},
        {'Department': 'Architecture', 'Specialization': 'Landscape Design'},
        {'Department': 'Architecture', 'Specialization': 'Digital Architecture'},
        {'Department': 'Architecture', 'Specialization': 'Parametric Architecture'},
        {'Department': 'Architecture', 'Specialization': 'Affordable Housing'}
    ]
    
    return pd.DataFrame(specializations)

def create_facilities_csv():
    """Create CSV with facilities information"""
    facilities = [
        {'Category': 'Infrastructure', 'Facility': 'Wi-Fi enabled campus', 'Details': 'Complete campus coverage'},
        {'Category': 'Infrastructure', 'Facility': 'Well equipped laboratories', 'Details': 'Latest technologies'},
        {'Category': 'Infrastructure', 'Facility': 'Cafeteria', 'Details': 'Student dining facility'},
        {'Category': 'Infrastructure', 'Facility': 'Gymkhana', 'Details': 'Sports and recreation'},
        {'Category': 'Infrastructure', 'Facility': 'Ladies Room', 'Details': 'Dedicated facility for female students'},
        {'Category': 'Infrastructure', 'Facility': 'Reading Hall', 'Details': 'Study facility'},
        {'Category': 'Infrastructure', 'Facility': 'Extra-curricular Activity Room', 'Details': 'For student activities'},
        {'Category': 'Infrastructure', 'Facility': 'Career Counseling Cell', 'Details': 'Career guidance services'},
        
        {'Category': 'Labs', 'Facility': '3D Printing Lab', 'Details': '11 high-end 3D printers'},
        {'Category': 'Labs', 'Facility': 'Robotics and Automation Lab', 'Details': '6-axis articulated robotic arm'},
        {'Category': 'Labs', 'Facility': 'Siemens Software Lab', 'Details': 'Hydraulic, Pneumatic, PLC and HMI Training'},
        {'Category': 'Labs', 'Facility': 'Machine Vision System', 'Details': 'AI capabilities for inspection'},
        
        {'Category': 'Transportation', 'Facility': 'Bus Facility', 'Details': 'From nearby villages'},
        {'Category': 'Scholarships', 'Facility': 'Government Scholarships', 'Details': 'All available scholarships'},
        {'Category': 'Scholarships', 'Facility': 'Merit Scholarship', 'Details': '100% fee waiver for highest merit students'}
    ]
    
    return pd.DataFrame(facilities)

def create_placement_csv():
    """Create CSV with placement information"""
    placement_data = [
        {'Metric': 'Highest Package', 'Value': '64 LPA', 'Details': 'Adobe - Miss Anamika Dakare'},
        {'Metric': 'Average Package', 'Value': '4.5 LPA', 'Details': 'Overall average'},
        {'Metric': 'Job Offers 2023-24', 'Value': '554+', 'Details': 'Still counting'},
        {'Metric': 'Campus Placement Drives', 'Value': '98', 'Details': 'Total drives conducted'},
        {'Metric': 'Students Participated', 'Value': '603', 'Details': 'In placement process'},
        {'Metric': 'Internship Students', 'Value': '249', 'Details': 'Internship by IIT Mumbai'},
        {'Metric': 'Paid Internship', 'Value': '136', 'Details': 'Students with paid internship'},
        {'Metric': 'Final Year Internship', 'Value': '149', 'Details': '6 months internship'},
        
        # Package Distribution
        {'Metric': 'Top 13 Packages', 'Value': '7-8 LPA', 'Details': 'Highest salary bracket'},
        {'Metric': 'Top 19 Packages', 'Value': '6-7 LPA', 'Details': 'Second highest bracket'},
        {'Metric': 'Top 230 Packages', 'Value': '5-4.5 LPA', 'Details': 'Mid-range packages'},
        {'Metric': 'Top 289 Packages', 'Value': '4.5-3 LPA', 'Details': 'Entry level packages'}
    ]
    
    return pd.DataFrame(placement_data)

def create_major_recruiters_csv():
    """Create CSV with major recruiters (based on visible logos/names in document)"""
    recruiters = [
        {'Company': 'Adobe', 'Package': '64 LPA', 'Selected_Students': 'Anamika Dakare'},
        {'Company': 'Technimont, Pune', 'Package': '6.5 LPA', 'Selected_Students': 'Multiple'},
        {'Company': 'Toyo Engineering', 'Package': '6 LPA', 'Selected_Students': 'Multiple'},
        {'Company': 'Control Systems', 'Package': '6 LPA', 'Selected_Students': 'Multiple'},
        {'Company': 'Technologies & Dassault Systems', 'Package': '7-8 LPA', 'Selected_Students': 'Multiple'}
    ]
    
    return pd.DataFrame(recruiters)

def create_faculty_achievements_csv():
    """Create CSV with faculty achievements"""
    achievements = [
        {'Category': 'Research', 'Metric': 'Ph.D Holders', 'Value': '62'},
        {'Category': 'Research', 'Metric': 'Ph.D Research Scholars', 'Value': '36+'},
        {'Category': 'Research', 'Metric': 'Faculty Patents', 'Value': '41'},
        {'Category': 'Research', 'Metric': 'Research Paper Publications', 'Value': '1200+'},
        {'Category': 'Funding', 'Metric': 'Project Funding', 'Value': '4 Lakh EURO'},
        {'Category': 'Training', 'Metric': 'Finishing School Training', 'Value': '320 hours'},
        {'Category': 'Training', 'Metric': 'Coding Training', 'Value': '400 hours compulsory'}
    ]
    
    return pd.DataFrame(achievements)

def create_student_achievements_csv():
    """Create CSV with student achievements"""
    achievements = [
        {'Category': 'Sports', 'Achievement': 'Gold Medal - Maharashtra State Karate Championship', 'Student': 'Miss. Siddhi Rajadhyaksh', 'Year': '2023-24'},
        {'Category': 'Sports', 'Achievement': 'Silver Medal - Asian Games Karate', 'Student': 'Miss. Siddhi Rajadhyaksh', 'Year': '2023-24'},
        {'Category': 'Sports', 'Achievement': 'Gold Medal - National Icestock Championship', 'Student': 'Mr. Saurish Salunkhe', 'Year': '2023-24'},
        {'Category': 'Sports', 'Achievement': 'First Prize - State Level Football', 'Student': 'Football Team', 'Year': '2023-24'},
        {'Category': 'Sports', 'Achievement': 'First Prize - Lead College Badminton (M)', 'Student': 'Badminton Team', 'Year': '2023-24'},
        {'Category': 'Sports', 'Achievement': 'First Prize - Lead College Basketball (W)', 'Student': 'Basketball Team', 'Year': '2023-24'},
        {'Category': 'Cultural', 'Achievement': 'Multiple Awards in Ekankika Competitions', 'Student': 'Cultural Team', 'Year': '2023-24'},
        {'Category': 'International', 'Achievement': 'Youth Exchange Program - UK', 'Student': 'Miss Vaishnavi Salokhe (NCC)', 'Year': '2023'}
    ]
    
    return pd.DataFrame(achievements)

def create_admission_requirements_csv():
    """Create CSV with admission requirements"""
    requirements = [
        {'Category': 'Eligibility', 'Requirement': 'Educational Qualification', 'Details': 'Passed 10+2 with PCM/PCB/Biotech/Technical'},
        {'Category': 'Eligibility', 'Requirement': 'Minimum Marks', 'Details': '45% aggregate (40% for reserved)'},
        {'Category': 'Eligibility', 'Requirement': 'Entrance Exam', 'Details': 'MHT-CET or JEE Main'},
        
        {'Category': 'Documents', 'Requirement': 'MHT-CET/JEE Score Card', 'Details': 'Required for all'},
        {'Category': 'Documents', 'Requirement': 'Leaving Certificate', 'Details': 'Transfer Certificate'},
        {'Category': 'Documents', 'Requirement': '10th Mark Sheet', 'Details': 'Original required'},
        {'Category': 'Documents', 'Requirement': '12th Mark Sheet', 'Details': 'Original required'},
        {'Category': 'Documents', 'Requirement': 'Domicile Certificate', 'Details': 'Age, Nationality & Domicile'},
        {'Category': 'Documents', 'Requirement': 'Caste Certificate', 'Details': 'For reserved categories'},
        {'Category': 'Documents', 'Requirement': 'Non-Creamy Layer Certificate', 'Details': 'Valid till 31st March 2025'},
        {'Category': 'Documents', 'Requirement': 'EWS Certificate', 'Details': 'For EWS category'},
        {'Category': 'Documents', 'Requirement': 'Income Certificate', 'Details': 'For TFWS - less than 8 lakhs'},
        
        {'Category': 'Reservation', 'Requirement': 'SC/ST', 'Details': 'As per Maharashtra govt norms'},
        {'Category': 'Reservation', 'Requirement': 'OBC/VJ/NT/SBC/SEBC', 'Details': 'As per Maharashtra govt norms'},
        {'Category': 'Reservation', 'Requirement': 'EWS', 'Details': 'Economically Weaker Section'},
        {'Category': 'Reservation', 'Requirement': 'Physically Handicapped', 'Details': 'Special provision'},
        {'Category': 'Reservation', 'Requirement': 'Defence Personnel Children', 'Details': 'Special category'},
        {'Category': 'Reservation', 'Requirement': 'Girls', 'Details': 'Gender-based reservation'}
    ]
    
    return pd.DataFrame(requirements)

def create_bus_routes_csv():
    """Create CSV with bus route information"""
    # Sample bus routes from the document
    bus_routes = [
        {'Route': 'Kagal', 'Departure_Time': '7:55 AM', 'Fare': '15600', 'Stops': 'Bhogavati, Kurukali, Kothali, Haldi, Kandgaon, Nandwal'},
        {'Route': 'Ashta', 'Departure_Time': '7:50 AM', 'Fare': '15400', 'Stops': 'Sangavade, Vasagade, Uchgaon, Kawala Naka'},
        {'Route': 'Sangli', 'Departure_Time': '7:35 AM', 'Fare': '19300', 'Stops': 'Direct route'},
        {'Route': 'Gargoti', 'Departure_Time': '7:35 AM', 'Fare': '19300', 'Stops': 'Madilge, Koor, Mudal, Thitta, Bidri'},
        {'Route': 'Ichalkaranji', 'Departure_Time': '7:35 AM', 'Fare': '13100', 'Stops': 'Male Fata, Chokak, Rukadi Fata, Atigre Fata'},
        {'Route': 'Islampur', 'Departure_Time': '7:30 AM', 'Fare': '24800', 'Stops': 'Watar, Kini Fata, Tandulwadi, Yeloor Fata'},
        {'Route': 'Kolhapur City', 'Departure_Time': '8:05 AM', 'Fare': '8100', 'Stops': 'Hockey Stadium, Subhash Nagar, Mauli Chowk, Rajarampuri'}
    ]
    
    return pd.DataFrame(bus_routes)

def create_rankings_csv():
    """Create CSV with college rankings"""
    rankings = [
        {'Ranking_Agency': 'Outlook India', 'Category': 'Architecture', 'Rank': '13', 'Year': '2021', 'Details': 'Top 13 Architecture Colleges in India'},
        {'Ranking_Agency': 'India Today', 'Category': 'Architecture', 'Rank': '21', 'Year': '2021', 'Details': 'Architecture department ranking'},
        {'Ranking_Agency': 'NAAC', 'Category': 'Overall', 'Grade': 'A Grade', 'CGPA': '3.08', 'Details': 'National Assessment and Accreditation Council'},
        {'Ranking_Agency': 'NBA', 'Category': 'Engineering', 'Status': 'Accredited', 'Period': '2022-2025', 'Details': 'CSE, E&TC, Mechanical Engineering'}
    ]
    
    return pd.DataFrame(rankings)

def save_all_csvs():
    """Generate and save all CSV files"""
    
    # Create all dataframes
    dataframes = {
        'college_info': create_college_info_csv(),
        'courses': create_courses_csv(),
        'specializations': create_specializations_csv(),
        'facilities': create_facilities_csv(),
        'placements': create_placement_csv(),
        'recruiters': create_major_recruiters_csv(),
        'faculty_achievements': create_faculty_achievements_csv(),
        'student_achievements': create_student_achievements_csv(),
        'admission_requirements': create_admission_requirements_csv(),
        'bus_routes': create_bus_routes_csv(),
        'rankings': create_rankings_csv()
    }
    
    # Save individual CSV files
    for name, df in dataframes.items():
        filename = f'dypcet_{name}.csv'
        df.to_csv(filename, index=False)
        print(f"Created: {filename} ({len(df)} rows)")
    
    # Create a comprehensive combined CSV
    combined_data = []
    for category, df in dataframes.items():
        for _, row in df.iterrows():
            row_dict = row.to_dict()
            row_dict['Data_Category'] = category.replace('_', ' ').title()
            combined_data.append(row_dict)
    
    # Save combined CSV
    combined_df = pd.DataFrame(combined_data)
    combined_df.to_csv('dypcet_complete_data.csv', index=False)
    print(f"Created: dypcet_complete_data.csv ({len(combined_df)} rows)")
    
    return dataframes

def display_summary():
    """Display summary of extracted information"""
    print("\n" + "="*60)
    print("DYPCET INFORMATION EXTRACTION SUMMARY")
    print("="*60)
    
    dataframes = save_all_csvs()
    
    print(f"\nTotal CSV files created: {len(dataframes) + 1}")
    print("\nData Categories Extracted:")
    for i, (name, df) in enumerate(dataframes.items(), 1):
        print(f"{i:2d}. {name.replace('_', ' ').title():<25} - {len(df):3d} records")
    
    print(f"\nKey Information Extracted:")
    print(f"• College established in 1984")
    print(f"• 8 UG programs, 2 PG programs")
    print(f"• NAAC 'A' Grade (CGPA: 3.08)")
    print(f"• 554+ job offers in 2023-24")
    print(f"• Highest package: 64 LPA (Adobe)")
    print(f"• 16000+ alumni worldwide")
    print(f"• Multiple bus routes available")
    
    print(f"\nFiles saved successfully!")
    print("="*60)

if __name__ == "__main__":
    display_summary()