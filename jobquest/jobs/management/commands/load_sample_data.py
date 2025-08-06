from django.core.management.base import BaseCommand
from django.utils import timezone
from jobs.models import Job
from datetime import timedelta
import random


class Command(BaseCommand):
    help = 'Load sample job data for testing and development'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample job data...')
        
        # Clear existing jobs first
        Job.objects.all().delete()
        
        sample_jobs = [
            {
                'title': 'Senior Frontend Developer',
                'company_name': 'TechCorp Solutions',
                'description': '''We are seeking a talented Senior Frontend Developer to join our dynamic team. 
                
You will be responsible for:
• Developing and maintaining responsive web applications using modern JavaScript frameworks
• Collaborating with UX/UI designers to implement pixel-perfect designs
• Writing clean, maintainable, and testable code
• Optimizing applications for maximum speed and scalability
• Mentoring junior developers and conducting code reviews

Requirements:
• 5+ years of experience with JavaScript, HTML5, and CSS3
• Expert knowledge of React.js and its ecosystem
• Experience with state management libraries (Redux, MobX)
• Proficiency in modern build tools and workflows
• Strong understanding of responsive design principles
• Experience with version control systems (Git)
• Excellent communication and teamwork skills

We offer competitive salary, comprehensive benefits, flexible working hours, and opportunities for professional growth.''',
                'location': 'San Francisco, CA',
                'posting_date': timezone.now() - timedelta(days=2)
            },
            {
                'title': 'Data Scientist',
                'company_name': 'Analytics Pro',
                'description': '''Join our data science team to drive insights and innovation through advanced analytics.

Key Responsibilities:
• Analyze large datasets to identify trends and patterns
• Develop machine learning models and algorithms
• Create data visualizations and reports for stakeholders
• Collaborate with cross-functional teams to solve business problems
• Present findings to technical and non-technical audiences

Requirements:
• Master's degree in Data Science, Statistics, or related field
• 3+ years of experience in data analysis and machine learning
• Proficiency in Python, R, and SQL
• Experience with machine learning libraries (scikit-learn, TensorFlow, PyTorch)
• Knowledge of data visualization tools (Tableau, Power BI, matplotlib)
• Strong statistical analysis skills
• Excellent problem-solving abilities

Benefits include health insurance, retirement plans, professional development budget, and remote work options.''',
                'location': 'New York, NY',
                'posting_date': timezone.now() - timedelta(days=5)
            },
            {
                'title': 'DevOps Engineer',
                'company_name': 'CloudTech Industries',
                'description': '''We are looking for a skilled DevOps Engineer to help streamline our development and deployment processes.

Responsibilities:
• Design and implement CI/CD pipelines
• Manage cloud infrastructure on AWS/Azure/GCP
• Automate deployment and monitoring processes
• Ensure system security and compliance
• Troubleshoot and resolve infrastructure issues
• Collaborate with development teams to optimize workflows

Requirements:
• Bachelor's degree in Computer Science or related field
• 4+ years of DevOps or system administration experience
• Expertise in containerization (Docker, Kubernetes)
• Experience with infrastructure as code (Terraform, CloudFormation)
• Proficiency in scripting languages (Bash, Python)
• Knowledge of monitoring and logging tools
• Strong understanding of networking and security principles

We offer competitive compensation, stock options, comprehensive health benefits, and a collaborative work environment.''',
                'location': 'Austin, TX',
                'posting_date': timezone.now() - timedelta(days=1)
            },
            {
                'title': 'UX/UI Designer',
                'company_name': 'Design Studio Plus',
                'description': '''Creative UX/UI Designer wanted to create exceptional user experiences for our digital products.

What you'll do:
• Conduct user research and usability testing
• Create wireframes, prototypes, and high-fidelity designs
• Design intuitive user interfaces for web and mobile applications
• Collaborate with product managers and developers
• Maintain and evolve design systems
• Present design concepts to stakeholders

Qualifications:
• 3+ years of UX/UI design experience
• Proficiency in design tools (Figma, Sketch, Adobe Creative Suite)
• Strong portfolio showcasing user-centered design process
• Understanding of front-end technologies and constraints
• Experience with design systems and accessibility standards
• Excellent communication and presentation skills
• Degree in Design, HCI, or related field preferred

Join us for exciting projects, mentorship opportunities, and a creative work environment with flexible schedules.''',
                'location': 'Seattle, WA',
                'posting_date': timezone.now() - timedelta(days=3)
            },
            {
                'title': 'Full Stack Developer',
                'company_name': 'StartupXYZ',
                'description': '''Exciting opportunity for a Full Stack Developer to join our fast-growing startup!

Your Role:
• Build and maintain web applications from concept to deployment
• Work with modern tech stack (React, Node.js, PostgreSQL)
• Participate in architectural decisions and technical planning
• Collaborate in an agile development environment
• Contribute to code reviews and team knowledge sharing
• Help scale our platform to support growing user base

We're Looking For:
• 3+ years of full stack development experience
• Strong proficiency in JavaScript/TypeScript
• Experience with React.js and Node.js
• Knowledge of database design and SQL
• Familiarity with cloud platforms and deployment
• Understanding of API design and RESTful services
• Passion for clean code and best practices

Startup perks include equity participation, flexible PTO, cutting-edge tech stack, and opportunity to make significant impact.''',
                'location': 'Remote',
                'posting_date': timezone.now() - timedelta(hours=12)
            },
            {
                'title': 'Product Manager',
                'company_name': 'InnovateCorp',
                'description': '''Lead product strategy and development as our Senior Product Manager.

Key Responsibilities:
• Define product vision and roadmap
• Conduct market research and competitive analysis
• Gather and prioritize product requirements
• Work closely with engineering and design teams
• Analyze product metrics and user feedback
• Manage product lifecycle from conception to launch

Requirements:
• 5+ years of product management experience
• Strong analytical and problem-solving skills
• Experience with agile development methodologies
• Excellent communication and leadership abilities
• Technical background preferred
• MBA or relevant degree
• Experience with product analytics tools

We offer competitive salary, performance bonuses, comprehensive benefits, and opportunities to lead innovative products.''',
                'location': 'Boston, MA',
                'posting_date': timezone.now() - timedelta(days=4)
            },
            {
                'title': 'Backend Developer',
                'company_name': 'ScaleTech Solutions',
                'description': '''Join our backend team to build robust and scalable server-side applications.

Responsibilities:
• Develop and maintain APIs and microservices
• Design efficient database schemas and queries
• Implement caching and performance optimization strategies
• Ensure code quality through testing and reviews
• Monitor and troubleshoot production systems
• Collaborate with frontend and mobile teams

Technical Requirements:
• 4+ years of backend development experience
• Proficiency in Python, Java, or Go
• Experience with relational and NoSQL databases
• Knowledge of microservices architecture
• Understanding of containerization and orchestration
• Familiarity with message queues and caching systems
• Experience with cloud platforms (AWS, GCP, Azure)

Benefits include health insurance, 401k matching, professional development budget, and flexible work arrangements.''',
                'location': 'Denver, CO',
                'posting_date': timezone.now() - timedelta(days=6)
            },
            {
                'title': 'Marketing Specialist',
                'company_name': 'GrowthHackers Inc',
                'description': '''Drive growth and engagement as our Digital Marketing Specialist.

What You'll Do:
• Develop and execute digital marketing campaigns
• Manage social media presence and content strategy
• Analyze campaign performance and optimize for ROI
• Collaborate with sales team on lead generation
• Create compelling content for various marketing channels
• Stay updated with latest marketing trends and tools

Ideal Candidate:
• 2+ years of digital marketing experience
• Proficiency in marketing tools (Google Analytics, HubSpot, etc.)
• Strong writing and communication skills
• Experience with SEO/SEM and social media advertising
• Creative mindset with analytical thinking
• Bachelor's degree in Marketing or related field
• Knowledge of graphic design tools is a plus

Join our dynamic team with opportunities for rapid growth, creative freedom, and performance-based incentives.''',
                'location': 'Miami, FL',
                'posting_date': timezone.now() - timedelta(days=7)
            },
            {
                'title': 'Cybersecurity Analyst',
                'company_name': 'SecureNet Technologies',
                'description': '''Protect our organization and clients as a Cybersecurity Analyst.

Key Duties:
• Monitor security events and incident response
• Conduct vulnerability assessments and penetration testing
• Develop and maintain security policies and procedures
• Investigate security breaches and implement countermeasures
• Collaborate with IT teams on security implementations
• Provide security training and awareness programs

Requirements:
• Bachelor's degree in Cybersecurity or related field
• 3+ years of information security experience
• Knowledge of security frameworks (NIST, ISO 27001)
• Experience with security tools (SIEM, IDS/IPS, firewalls)
• Understanding of network protocols and architectures
• Professional certifications (CISSP, CEH, CompTIA) preferred
• Strong attention to detail and problem-solving skills

We offer excellent benefits, ongoing training, certification support, and opportunity to work with cutting-edge security technologies.''',
                'location': 'Washington, DC',
                'posting_date': timezone.now() - timedelta(days=8)
            },
            {
                'title': 'Mobile App Developer',
                'company_name': 'MobileFirst Studios',
                'description': '''Create amazing mobile experiences as our iOS/Android Developer.

Your Mission:
• Develop native and cross-platform mobile applications
• Collaborate with designers to implement intuitive UIs
• Integrate with APIs and backend services
• Optimize app performance and user experience
• Publish apps to App Store and Google Play
• Stay current with mobile development trends

Skills We Need:
• 3+ years of mobile development experience
• Proficiency in Swift/Objective-C or Kotlin/Java
• Experience with React Native or Flutter is a plus
• Understanding of mobile UI/UX best practices
• Knowledge of app store submission processes
• Familiarity with mobile testing frameworks
• Experience with version control and CI/CD

Join our innovative team with competitive salary, flexible schedule, latest devices and tools, and opportunity to work on award-winning apps.''',
                'location': 'Los Angeles, CA',
                'posting_date': timezone.now() - timedelta(days=9)
            }
        ]
        
        created_jobs = []
        for job_data in sample_jobs:
            job = Job.objects.create(**job_data)
            created_jobs.append(job)
            
        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {len(created_jobs)} sample jobs')
        )
        
        # Display summary
        self.stdout.write('\nJobs created:')
        for job in created_jobs:
            self.stdout.write(f'- {job.title} at {job.company_name} ({job.location})')