import psycopg2
from psycopg2 import sql
from faker import Faker
import random
from datetime import datetime, timedelta

# Faker kütüphanesini başlat
fake = Faker()

# Veritabanı bağlantı parametreleri
DB_NAME = "db2"        
DB_USER = "postgres"   
DB_PASSWORD = "arda"   
DB_HOST = "localhost"
DB_PORT = "5432"

#==========================================================================================================
#   Events tablosunun Description (Açıklama) alanı için içerik oluşturma bileşenleri:
#==========================================================================================================

# Açılış cümleleri
description_openings = [
    'Join us for', 'Dont miss', 'Be part of', 'Experience', 'Attend',
    'We invite you to', 'Get ready for', 'Mark your calendars for',
    'Prepare for', 'Come and enjoy', 'Discover', 'Participate in',
    'Explore', 'Celebrate', 'Immerse yourself in', 'Engage with',
    'Step into', 'Save the date for', 'Be inspired by', 'Dive into',
    'Get involved in', 'Celebrate with us at', 'Start your journey with',
    'Take part in', 'Enjoy', 'Uncover the opportunities at', 'Learn from',
    'Shape the future with', 'Embrace', 'Find yourself at'
]

# Etkinlik özellikleri veya vurguları
description_features = [
    'a day filled with insightful sessions', 'networking opportunities with industry leaders',
    'hands-on workshops led by experts', 'inspiring keynote speeches',
    'interactive panel discussions', 'the latest trends in the industry',
    'innovative solutions and ideas', 'cutting-edge technology demonstrations',
    'collaborative learning experiences', 'a showcase of emerging talent',
    'engaging activities and entertainment', 'exclusive access to new products',
    'practical strategies for success', 'a platform to share your ideas',
    'opportunities to expand your network', 'a celebration of creativity and innovation',
    'an environment that fosters growth', 'valuable insights from seasoned professionals',
    'a unique blend of education and entertainment', 'breakthrough ideas and strategies',
    'state-of-the-art exhibits and demos', 'meaningful connections with peers',
    'the future of innovation and creativity', 'a wide range of engaging discussions',
    'hands-on learning opportunities', 'a celebration of groundbreaking achievements',
    'a forum for collaborative problem-solving', 'personalized mentorship sessions',
    'a first look at cutting-edge products', 'thought-provoking ideas and insights',
    'entertainment that will leave you inspired', 'a truly transformative experience',
    'an opportunity to shape your career', 'new tools and techniques for success',
    'a gathering of forward-thinking minds', 'in-depth discussions with thought leaders'
]

# Kapanış cümleleri
description_closings = [
    'Register now to secure your spot!', 'We look forward to seeing you there.',
    'Dont miss this exciting opportunity.', 'Join us and be inspired.',
    'Spaces are limited—sign up today!', 'Prepare to be amazed.',
    'This is an event you wont want to miss.', 'Come and be part of something special.',
    'Take the next step in your professional journey.', 'Elevate your skills and knowledge.',
    'Engage with like-minded individuals.', 'Unlock new possibilities.',
    'We cant wait to welcome you.', 'Experience the future of {topic}.',
    'Lets shape the future together.', 'Seize this chance to innovate and grow.',
    'Your journey starts here—dont miss it.', 'Secure your place today.',
    'Explore endless opportunities with us.', 'Let us inspire you.',
    'Learn, grow, and connect—register now!', 'Discover whats possible at {event}.',
    'Make this a defining moment in your journey.', 'Join us to create lasting memories.'
]

# Açıklama şablonları
description_templates = [
    "{opening} the {adjective} {event} on {topic}. {feature}. {closing}",
    "{opening} {event}: {feature}. {closing}",
    "{opening} our {adjective} {event} focused on {topic}. {feature}. {closing}",
    "{opening} {event} {additional}, where {feature}. {closing}",
    "{opening} the {event} and {feature}. {closing}",
    "{opening} {feature} at the {adjective} {event}. {closing}",
    "{opening} {event} {year}, {feature}. {closing}",
    "{opening} {event}—a {adjective} experience in {topic}. {feature}. {closing}",
    "{opening} the {adjective} {event} {year}. {feature}. {closing}",
    "{opening} {event} {year}, {feature} and more. {closing}",
    "{opening} {feature} at this {adjective} {event} focused on {topic}. {closing}",
    "{opening} the {event}—a unique chance to explore {topic}. {feature}. {closing}",
    "{opening} {event} {additional}. {feature}. {closing}",
    "{opening} the {adjective} {event} in {topic}. {feature}. {closing}",
    "{opening} {feature}, exclusively at the {event}. {closing}",
    "{opening} {event} on {topic}, featuring {feature}. {closing}",
    "{opening} {event} {additional} with {feature}. {closing}",
    "{opening} an {adjective} {event} that brings {feature} to the forefront. {closing}",
    "{opening} {feature} as part of this {adjective} {event}. {closing}",
    "{opening} {event}—{feature}. Dont miss this {adjective} opportunity. {closing}"
]

def generate_event_description():
    # Rastgele bir şablon seç
    template = random.choice(description_templates)
    
    # Yer tutucular için rastgele elemanlar seç
    opening = random.choice(description_openings)
    adjective = random.choice(title_adjectives)
    event = random.choice(title_events)
    topic = random.choice(title_topics)
    feature = random.choice(description_features)
    closing = random.choice(description_closings)
    additional = random.choice(title_additionals)
    year = str(random.choice([datetime.now().year, datetime.now().year + 1]))
    
    # Şablonu doldur
    description = template.format(
        opening=opening,
        adjective=adjective,
        event=event,
        topic=topic,
        feature=feature,
        closing=closing,
        additional=additional,
        year=year
    )
    
    return description

#==========================================================================================================
#   Events tablosunun Title (Başlık) alanı için içerik oluşturma bileşenleri:
#==========================================================================================================

# Sıfatlar/Tanımlayıcılar
title_adjectives = [
    'International', 'Annual', 'Exciting', 'Innovative', 'Interactive', 'Virtual',
    'Intensive', 'Hands-on', 'Advanced', 'Beginner', 'Expert', 'Professional',
    'Comprehensive', 'Exclusive', 'Cutting-edge', 'Global', 'Regional', 'National',
    'Local', 'Live', 'Mega', 'Dynamic', 'Ultimate', 'Premier', 'Elite', 'Insightful',
    'Inspiring', 'Creative', 'Collaborative', 'Engaging', 'Informative', 'Thought-provoking',
    'Revolutionary', 'Groundbreaking', 'Influential', 'Transformative', 'Empowering',
    'Visionary', 'Educational', 'Motivational', 'Strategic', 'Impactful', 'Forward-Thinking',
    'Diverse', 'Immersive', 'Futuristic', 'Breakthrough', 'Trailblazing', 'Pioneering',
    'High-Tech', 'Next-Gen', 'Multi-disciplinary', 'Award-Winning', 'Hybrid', 
    'Sustainable', 'Cultural', 'Experiential', 'Game-changing', 'Insight-driven', 
    'Bespoke', 'Customized', 'High-Energy', 'Trendsetting', 'Resilient', 'Agile',
    'Performance-focused', 'Visionary', 'Proven', 'Success-Oriented', 'Future-Ready'
]

# Etkinlik türleri
title_events = [
    'Conference', 'Workshop', 'Seminar', 'Meetup', 'Festival', 'Concert',
    'Symposium', 'Summit', 'Expo', 'Webinar', 'Forum', 'Gala', 'Hackathon',
    'Retreat', 'Bootcamp', 'Lecture Series', 'Panel Discussion', 'Networking Event',
    'Trade Show', 'Showcase', 'Roundtable', 'Competition', 'Tournament', 'Gathering',
    'Convention', 'Fair', 'Celebration', 'Open House', 'Show', 'Experience',
    'Colloquium', 'Camp', 'Carnival', 'Debate', 'Exhibition', 'Festival',
    'Career Fair', 'Design Sprint', 'Hackathon Weekend', 'Award Ceremony',
    'Mentorship Program', 'Interactive Session', 'Masterclass', 'Ideation Camp',
    'Knowledge Exchange', 'Case Study Workshop', 'Think Tank', 'Challenge',
    'Leadership Forum', 'Innovation Summit', 'Pitch Night', 'Skill-Building Session',
    'Thought Leaders Panel', 'Tech Jam', 'Demo Day', 'Product Showcase'
]

# Konular/Temalar
title_topics = [
    'Technology', 'Music', 'Business', 'Art', 'Health', 'Gaming', 'Food', 'Travel',
    'Science', 'Literature', 'Film', 'Photography', 'Dance', 'Comedy', 'Education',
    'Sports', 'Environment', 'Finance', 'Startups', 'Politics', 'History', 'Space',
    'Culture', 'Meditation', 'Fitness', 'AI and Robotics', 'Blockchain', 'Marketing',
    'Sales', 'Productivity', 'Self-Development', 'Public Speaking', 'Writing',
    'Architecture', 'Adventure', 'Social Impact', 'Spirituality', 'Mindfulness',
    'Cybersecurity', 'E-Sports', 'Culinary Arts', 'Wine Tasting', 'Lifestyle',
    'Wellness', 'Innovation', 'Design', 'Entrepreneurship', 'Leadership', 'Sustainability',
    'Renewable Energy', 'Data Science', 'Machine Learning', 'Augmented Reality',
    'Virtual Reality', 'Networking', 'Cloud Computing', 'Human Resources', 'Psychology',
    'Project Management', 'Customer Experience', 'Digital Transformation', 'Big Data',
    'Social Media', 'UX/UI Design', 'Climate Change', 'Creative Writing', 'Mental Health',
    'Clean Energy', 'Supply Chain', 'Circular Economy', 'Web Development', 'Mobile Applications',
    'Quantum Computing', 'Genomics', 'Bioinformatics', 'Health Tech', 'Civic Engagement',
    'Policy Advocacy', 'Personal Branding', 'Investment Strategies'
]

# Ek detaylar
title_additionals = [
    '2023', '2024', 'for Startups', 'Summit', 'Expo', 'Bootcamp', 'Masterclass',
    'Series', 'Festival', 'Week', 'Day', 'Night', 'Showcase', 'Challenge',
    'Marathon', 'Carnival', 'Extravaganza', 'Live', 'Online', 'Fair', 'Forum',
    'Edition', 'Symposium', 'Experience', 'Conference', 'Gala', 'Annual Meeting',
    'Celebration', 'Gathering', 'Retreat', 'Camp', 'Open House', 'Tour', 'Awards',
    'Think Tank', 'Keynote Series', 'Interactive Program', 'Learning Pathway',
    'Innovation Awards', 'Leadership Series', 'Virtual Experience', 'Hackathon Series',
    'Tech Show', 'Interactive Forum', 'Hands-on Session', 'Networking Gala', 
    'Design Competition', 'Incubator Event', 'Knowledge Fair', 'Discovery Series'
]

# Başlık şablonları
title_templates = [
    "{adjective} {topic} {event}",
    "{topic} {event} {additional}",
    "{adjective} {event} on {topic}",
    "{topic} {adjective} {event}",
    "{adjective} {topic} {event} {additional}",
    "{event} on {topic}",
    "{event}: {adjective} {topic}",
    "{adjective} {event}: {topic}",
    "{event} {additional}: {topic}",
    "{topic} {event} {additional}",
    "{adjective} {event} {additional}",
    "{topic} {adjective} {event} {additional}",
    "{event}: {topic} {additional}",
    "{adjective} {topic} {event} {year}",
    "{event} {year}: {adjective} {topic}",
    "{adjective} {event} {topic} {additional}",
    "{event} {topic}: {adjective} {additional}",
    "{event} on {adjective} {topic}",
    "{adjective} {event}: Exploring {topic}",
    "{event} {year} - {adjective} {topic}"
]

def generate_event_title():
    # Rastgele bir şablon seç
    template = random.choice(title_templates)
    
    # Yer tutucular için rastgele elemanlar seç
    adjective = random.choice(title_adjectives)
    event = random.choice(title_events)
    topic = random.choice(title_topics)
    additional = random.choice(title_additionals)
    year = str(random.choice([datetime.now().year, datetime.now().year + 1]))
    
    # Şablonu doldur
    title = template.format(
        adjective=adjective,
        event=event,
        topic=topic,
        additional=additional,
        year=year
    )
    
    return title

#==========================================================================================================
#   Announcements tablosunun Content alanı için içerik oluşturma bileşenleri:
#==========================================================================================================

# Etkinlik türleri
event_types2 = [
    'Hackathon', 'Concert', 'Sports', 'Conference', 'Theatre',
    'Workshop', 'Festival', 'Webinar', 'Exhibition', 'Meetup',
    'Networking', 'Seminar', 'Tournament', 'Charity', 'Comedy',
    'Dance', 'Other'
]

# Duyuru türleri
announcement_types2 = [
    'We are excited to announce', 'Please be informed', 'Attention all attendees',
    'Important update regarding', 'Introducing', 'Join us for', 'Dont miss',
    'We regret to inform you', 'Mark your calendars for', 'Announcing',
    'We are pleased to share', 'Heads up about', 'Reminder about', 'Update on',
    'Welcome to', 'Special announcement for', 'Exclusive invitation to',
    'Last chance to register for', 'New addition to', 'Changes to',
    'Breaking news regarding', 'A special offer for', 'Exciting news about',
    'Urgent announcement for', 'A sneak peek at', 'Dont forget about',
    'A friendly reminder about', 'We are thrilled to unveil', 'Be part of',
    'Make sure to join', 'Save the date for', 'A fresh update on',
    'Newsflash about', 'An insider update about', 'Highlights for',
    'Celebrate with us at', 'A major development regarding'
]

# Sıfatlar/Tanımlayıcılar
adjectives2 = [
    'an exciting', 'a significant', 'a crucial', 'a fantastic', 'an important',
    'a thrilling', 'a noteworthy', 'a major', 'a delightful', 'a surprising',
    'a valuable', 'a beneficial', 'a wonderful', 'a necessary', 'a timely',
    'a special', 'a remarkable', 'a unique', 'a comprehensive', 'an informative',
    'a dynamic', 'a vibrant', 'a memorable', 'a challenging', 'a rewarding',
    'a seamless', 'an innovative', 'a creative', 'a well-organized', 'a successful',
    'an inspiring', 'a transformative', 'a captivating', 'a strategic', 'a professional',
    'an engaging', 'a collaborative', 'a supportive', 'a flexible', 'an exclusive',
    'a groundbreaking', 'an empowering', 'a motivational', 'a once-in-a-lifetime',
    'a cutting-edge', 'a forward-thinking', 'a community-driven', 'a trendsetting',
    'an action-packed', 'a highly-anticipated', 'a prestigious'
]

# Eylemler/Aksiyonlar
actions2 = [
    'event', 'workshop', 'conference', 'seminar', 'webinar', 'meeting',
    'session', 'presentation', 'panel discussion', 'networking opportunity',
    'training', 'lecture', 'summit', 'forum', 'expo', 'hackathon',
    'retreat', 'roundtable', 'symposium', 'lecture series', 'bootcamp',
    'talk', 'demonstration', 'award ceremony', 'product launch',
    'strategy meeting', 'charity drive', 'fundraising event', 'launch party',
    'innovation summit', 'industry meetup', 'career fair', 'team-building event',
    'interactive panel', 'community gathering', 'cultural festival',
    'seasonal celebration', 'technical demo', 'masterclass', 'startup showcase',
    'open house', 'design sprint', 'job fair', 'knowledge-sharing session',
    'collaborative brainstorming', 'leadership forum', 'hackathon weekend',
    'creative workshop', 'executive briefing', 'mentorship session'
]

# Detaylar
details2 = [
    'new venue at the downtown convention center', 'additional sessions on AI and Robotics',
    'keynote speaker Dr. Jane Smith', 'extended hours to accommodate more attendees',
    'interactive workshops on digital marketing', 'exclusive networking opportunities with industry leaders',
    'free registration for early birds', 'a new track on sustainable technologies',
    'enhanced virtual participation features', 'special discounts for group registrations',
    'a guest appearance by renowned artist John Doe', 'updated agenda with more diverse topics',
    'comprehensive materials provided in advance', 'improved attendee experience with better facilities',
    'a partnership with local businesses to support the event', 'advanced technical support for seamless sessions',
    'interactive Q&A sessions after each presentation', 'hands-on demonstrations with the latest technology',
    'a relaxed dress code to encourage comfort', 'a complimentary meal for all participants',
    'access to exclusive online resources post-event', 'extended networking breaks for meaningful connections',
    'live streaming available for remote attendees', 'an on-site help desk for all your needs',
    'informative panels with experts in the field', 'a vibrant exhibition area showcasing new products',
    'certificates of participation for all attendees', 'a feedback survey to improve future events',
    'key industry leaders sharing insights', 'exciting giveaways for attendees',
    'cutting-edge tools on display', 'a range of interactive activities',
    'a focus on practical skills', 'an engaging lineup of speakers',
    'early access to new products', 'dedicated networking lounges'
]

# Kapanış ifadeleri
closing_remarks2 = [
    'Register now to secure your spot.', 'Dont miss out on this opportunity.',
    'We look forward to your participation.', 'Mark your calendars and join us.',
    'Early registration is recommended.', 'Seats are limited, so act fast.',
    'Visit our website for more details.', 'Stay tuned for more updates.',
    'We cant wait to see you there.', 'Contact us for any inquiries.',
    'Prepare to be inspired and informed.', 'Take advantage of this unique opportunity.',
    'Join a community of like-minded professionals.', 'Enhance your skills and knowledge.',
    'Be part of something special.', 'Experience the best in the industry.',
    'Connect with leaders and innovators.', 'Expand your professional network.',
    'Gain valuable insights and expertise.', 'Participate in dynamic discussions.',
    'Enjoy a day of learning and networking.', 'Seize the chance to grow and excel.',
    'Be among the first to experience this.', 'Take the first step toward innovation.',
    'Dont wait—join us now!'
]

# Duyuru şablonları
announcement_templates2 = [
    "{announcement_type} {adjective} {action}, {details}. {closing_remark}",
    "{announcement_type} {adjective} {action} {details}. {closing_remark}",
    "{announcement_type} {adjective} {action}, featuring {details}. {closing_remark}",
    "{announcement_type} {adjective} {action} with {details}. {closing_remark}",
    "{announcement_type} {adjective} {action}, including {details}. {closing_remark}",
    "{announcement_type} {adjective} {action}. {closing_remark} More details can be found on our website.",
    "{announcement_type} {adjective} {action}, {details}. {closing_remark} Be sure to reserve your spot today.",
    "{announcement_type} {adjective} {action} at the {details}. {closing_remark}",
    "{announcement_type} {adjective} {action} that includes {details}. {closing_remark}",
    "{announcement_type} {adjective} {action}. {details}. {closing_remark}",
    "{announcement_type} {adjective} {action}. {closing_remark}",
    "{announcement_type} {adjective} {action}, {details}. {closing_remark}",
    "{announcement_type} {adjective} {action}. {closing_remark} Spaces are filling fast!",
    "{announcement_type} {adjective} {action}, enhanced by {details}. {closing_remark}",
    "{announcement_type} {adjective} {action}. Join us for {details}. {closing_remark}"
]

def generate_announcement_content():
    # Rastgele bir şablon seç
    template = random.choice(announcement_templates2)
    
    # Yer tutucular için rastgele elemanlar seç
    announcement_type = random.choice(announcement_types2)
    adjective = random.choice(adjectives2)
    # Hata düzeltildi: action yanlış listelerden seçiliyordu
    action = random.choice(actions2 + event_types2)  # Eylemin bağlama uygun olduğundan emin ol
    detail = random.choice(details2)
    closing_remark = random.choice(closing_remarks2)
    
    # Şablonu doldur
    announcement = template.format(
        announcement_type=announcement_type,
        adjective=adjective,
        action=action,
        details=detail,
        closing_remark=closing_remark
    )
    
    return announcement

#==========================================================================================================
#   Reviews tablosunun Comment alanı için içerik oluşturma bileşenleri:
#==========================================================================================================

# Konular
subjects1 = [
    'The event', 'The performer', 'The venue', 'The organization', 'The speakers',
    'The workshops', 'The registration process', 'The catering', 'The schedule',
    'The networking opportunities', 'The decorations', 'The lighting', 'The sound system',
    'The security', 'The accessibility', 'The parking facilities', 'The merchandise',
    'The live streaming', 'The marketing', 'The customer service', 'The panel discussions',
    'The breakout sessions', 'The keynote speaker', 'The stage design', 'The entertainment lineup',
    'The event staff', 'The social media coverage', 'The WiFi availability',
    'The digital materials', 'The technical setup', 'The seating arrangement',
    'The ticketing process', 'The mobile app', 'The event promotion',
    'The photo booth', 'The audience participation', 'The special effects',
    'The event coordination', 'The VIP area', 'The event theme', 'The giveaways',
    'The souvenir shop', 'The accessibility features', 'The family-friendly activities',
    'The outdoor setup', 'The safety protocols', 'The volunteer team',
    'The on-site assistance', 'The event duration', 'The breakout sessions',
    'The transportation options', 'The charging stations', 'The interactive activities'
]

# Sıfatlar
adjectives1 = [
    'amazing', 'disappointing', 'enjoyable', 'boring', 'incredible', 'mediocre',
    'fantastic', 'poor', 'exceptional', 'lackluster', 'thrilling', 'underwhelming',
    'spectacular', 'subpar', 'engaging', 'unimpressive', 'remarkable', 'forgettable',
    'superb', 'deficient', 'well-executed', 'chaotic', 'smooth', 'challenging',
    'memorable', 'forgettable', 'uninspired', 'refreshing', 'modern', 'classic',
    'innovative', 'predictable', 'creative', 'outdated', 'heartwarming', 'awkward',
    'dynamic', 'motivational', 'monotonous', 'uplifting', 'disorganized', 'polished',
    'exciting', 'tedious', 'intriguing', 'overwhelming', 'calm', 'chaotic', 'rewarding'
]

# Fiiller/Eylemler
verbs1 = [
    'exceeded expectations', 'fell short', 'provided', 'offered', 'delivered',
    'failed to deliver', 'impressed', 'disappointed', 'engaged the audience',
    'struggled to keep attention', 'set a high standard', 'did not meet standards',
    'was well-organized', 'was poorly organized', 'captivated the audience',
    'left much to be desired', 'enhanced the experience', 'hindered the experience',
    'boosted the overall atmosphere', 'detracted from the overall atmosphere',
    'surpassed expectations', 'was underwhelming', 'enriched the event',
    'simplified the process', 'stood out', 'failed to engage', 'energized the attendees',
    'created excitement', 'delivered a lasting impression', 'missed the mark',
    'supported the overall goals', 'did not resonate with attendees', 'sparked interest',
    'inspired attendees', 'fell flat', 'kept attendees engaged', 'left a positive impression',
    'was seamless', 'was inconsistent', 'provided ample value', 'lacked value'
]

# Detaylar
details1 = [
    'excellent sound quality', 'poor seating arrangements', 'a wide variety of topics',
    'limited interactive sessions', 'friendly staff', 'unhelpful staff', 
    'state-of-the-art equipment', 'outdated equipment', 'ample networking opportunities',
    'scarce networking opportunities', 'delicious food options', 'limited food options',
    'well-paced schedule', 'overly packed schedule', 'beautiful decorations',
    'lackluster decorations', 'effective security measures', 'inadequate security measures',
    'comfortable seating', 'uncomfortable seating', 'seamless registration process',
    'complicated registration process', 'innovative workshop formats',
    'traditional workshop formats', 'engaging speakers', 'monotonous speakers',
    'flexible event timings', 'rigid event timings', 'comprehensive materials provided',
    'insufficient materials provided', 'impressive technical setup', 'inefficient WiFi',
    'creative stage design', 'unimpressive giveaways', 'limited parking',
    'accessible facilities', 'fast response from staff', 'slow response from staff',
    'high-quality merchandise', 'mediocre food selection', 'personalized interactions',
    'generalized experiences', 'interactive activities', 'boring activities',
    'great lighting effects', 'distracting sound system', 'seamless live streaming',
    'frequent technical glitches', 'diverse event lineup', 'repetitive content'
]

# Sonuçlar
conclusions1 = [
    'highly recommend to others.', 'would attend again without hesitation.',
    'would not recommend to others.', 'suggest improvements in future events.',
    'left a lasting positive impression.', 'left me wanting more.',
    'was a valuable experience.', 'was not worth the time.',
    'look forward to the next event.', 'do not plan to attend future events.',
    'provided great learning opportunities.', 'lacked sufficient engagement.',
    'offered exceptional value.', 'did not offer much value.',
    'was well worth the investment.', 'was a waste of resources.',
    'set a new standard for events.', 'needs significant improvements.',
    'exceeded expectations in every way.', 'fell short of expectations.'
]

# Cümle şablonları
sentence_templates = [
    "{subject} {adjective} and {verb}, {details}. Overall, it {conclusion}",
    "{subject} was {adjective}. It {verb}, particularly {details}. I {conclusion}",
    "I found {subject} to be {adjective}. They {verb} with {details}. {conclusion}",
    "{subject} {verb} because of {details}. It was {adjective}. {conclusion}",
    "The {subject} {adjective}, {details}. {conclusion}",
    "Overall, {subject} was {adjective}. It {verb} and had {details}. {conclusion}",
    "{subject} was {adjective}. {details} made it {conclusion}",
    "The experience with {subject} was {adjective}. It {verb}, especially {details}. {conclusion}",
    "Regarding {subject}, it was {adjective} due to {details}. {conclusion}",
    "I {conclusion} because {subject} was {adjective} and {verb} with {details}.",
    "From my perspective, {subject} was {adjective}. It {verb} and included {details}. {conclusion}",
    "Many attendees agreed that {subject} was {adjective} due to {details}. {conclusion}",
    "{subject} {verb}, thanks to {details}, making it {adjective}. {conclusion}",
    "I felt that {subject} {verb}, especially with {details}. It was {adjective}. {conclusion}",
    "The event's focus on {subject} was {adjective}. It {verb} and had {details}. {conclusion}",
    "Without a doubt, {subject} {verb}. {details} made it {adjective}. {conclusion}"
]

def generate_review():
    # Rastgele bir şablon seç
    template = random.choice(sentence_templates)
    
    # Yer tutucular için rastgele elemanlar seç
    subject = random.choice(subjects1)
    adjective = random.choice(adjectives1)
    verb = random.choice(verbs1)
    detail = random.choice(details1)
    conclusion = random.choice(conclusions1)
    
    # Şablonu doldur
    review = template.format(
        subject=subject,
        adjective=adjective,
        verb=verb,
        details=detail,
        conclusion=conclusion
    )
    
    return review

#==========================================================================================================

# Veritabanı bağlantısını kur
try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    conn.autocommit = False  # İşlemleri etkinleştir
    cursor = conn.cursor()
    print("Database connection established.")
except Exception as e:
    print("Error connecting to the database:", e)
    exit(1)

def insert_addresses(n):
    # Adresleri ekleme fonksiyonu
    addresses = []
    for _ in range(n):
        zip_code = fake.postcode()
        city = fake.city()
        country = fake.country()
        # Rastgele enlem ve boylam üret
        latitude = float(fake.latitude())
        longitude = float(fake.longitude())
        addresses.append((zip_code, city, country, longitude, latitude))
    
    insert_query = """
        INSERT INTO Address (ZipCode, City, Country, Location)
        VALUES (%s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326))
        RETURNING AddressID;
    """
    
    address_ids = []
    try:
        for address in addresses:
            cursor.execute(insert_query, address)
            address_id = cursor.fetchone()[0]
            address_ids.append(address_id)
        conn.commit()
        print(f"Inserted {n} addresses.")
    except Exception as e:
        conn.rollback()
        print("Error inserting addresses:", e)
    return address_ids

def insert_users(n, address_ids):
    # Kullanıcıları ekleme fonksiyonu
    users = []
    for _ in range(n):
        first = fake.first_name()
        last = fake.last_name()
        try:
            email = fake.unique.email()
        except Exception as e:
            fake.unique.clear()
            email = fake.unique.email()
        phone = fake.phone_number()
        address_id = random.choice(address_ids)
        users.append((first, last, email, phone, address_id))
    
    insert_query = """
        INSERT INTO Users (First, Last, Email, Phone, AddressID)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING UserID;
    """
    
    user_ids = []
    try:
        for user in users:
            cursor.execute(insert_query, user)
            user_id = cursor.fetchone()[0]
            user_ids.append(user_id)
        conn.commit()
        print(f"Inserted {n} users.")
    except Exception as e:
        conn.rollback()
        print("Error inserting users:", e)
    return user_ids

def insert_organizers(n):
    # Organizatörleri ekleme fonksiyonu
    organizers = []
    for _ in range(n):
        name = fake.company()
        contact = fake.email()
        rating = random.randint(0, 10)
        organizers.append((name, contact, rating))
    
    insert_query = """
        INSERT INTO Organizers (Name, Contact, Rating)
        VALUES (%s, %s, %s)
        RETURNING OrganizerID;
    """
    
    organizer_ids = []
    try:
        for organizer in organizers:
            cursor.execute(insert_query, organizer)
            organizer_id = cursor.fetchone()[0]
            organizer_ids.append(organizer_id)
        conn.commit()
        print(f"Inserted {n} organizers.")
    except Exception as e:
        conn.rollback()
        print("Error inserting organizers:", e)
    return organizer_ids

def insert_categories():
    # Kategorileri ekleme fonksiyonu
    # Önceden tanımlanmış kategori isimleri
    category_names = [
        'Technology', 'Music', 'Sports', 'Business', 'Art', 'Education',
        'Health', 'Gaming', 'Food', 'Travel', 'Networking', 'Science',
        'Literature', 'Film', 'Photography', 'Dance', 'Comedy', 'Charity',
        'Workshop', 'Conference', 'Fashion', 'Environment', 'Finance',
        'Startups', 'Politics', 'History', 'Space', 'Astrology', 'Cultural',
        'Meditation', 'Fitness', 'Theatre', 'Parenting', 'Women Empowerment',
        'Youth', 'Leadership', 'Real Estate', 'AI and Robotics', 'Blockchain',
        'Marketing', 'Sales', 'Customer Experience', 'Productivity',
        'Self-Development', 'Public Speaking', 'Writing', 'Architecture',
        'Interior Design', 'Adventure', 'Extreme Sports', 'Social Impact',
        'Spirituality', 'Mindfulness', 'Hiking', 'Wildlife', 'Marine Life',
        'DIY', 'Coding', 'Hackathons', 'Career Development', 'Agriculture',
        'Culinary Arts', 'Wine Tasting', 'Event Management', 'Personal Finance',
        'E-Sports', 'Cosplay', 'Magic Shows', 'Automotive', 'Antiques',
        'Pets', 'Human Rights', 'Disabilities Awareness', 'Virtual Reality',
        'Augmented Reality', 'Cybersecurity', 'Gaming Tournaments', 
        'Food Festivals', 'Startup Pitches', 'Music Festivals',
        'Street Performances', 'Cultural Exhibitions', 'Spoken Word', 
        'Poetry Slams', 'Carnivals', 'Seasonal Celebrations', 'Trade Shows',
        'Book Launches', 'Product Launches', 'Science Fairs', 'Hackathons',
        'Photography Walks', 'Wellness Retreats', 'Lifestyle'
    ]

    categories = [(name,) for name in category_names]
    
    insert_query = """
        INSERT INTO Categories (Name)
        VALUES (%s)
        ON CONFLICT (Name) DO NOTHING
        RETURNING CategoryID;
    """
    
    category_ids = []
    try:
        for category in categories:
            cursor.execute(insert_query, category)
            result = cursor.fetchone()
            if result:
                category_id = result[0]
                category_ids.append(category_id)
        conn.commit()
        print(f"Inserted {len(category_ids)} categories.")
    except Exception as e:
        conn.rollback()
        print("Error inserting categories:", e)
    return category_ids

def insert_services():
    # Servisleri ekleme fonksiyonu
    # Önceden tanımlanmış servis türleri
    service_types = [
        'Catering', 'Audio/Visual', 'Security', 'Transportation', 'Photography',
        'Lighting', 'Decorations', 'Marketing', 'Registration', 'Ticketing',
        'Cleaning', 'Entertainment', 'IT Support', 'Logistics', 'First Aid',
        'Live Streaming', 'Video Editing', 'Virtual Event Setup', 'Stage Design',
        'Event Planning', 'Venue Booking', 'Host/MC Services', 'Sound Systems',
        'WiFi Setup', 'Crowd Management', 'Fire Safety', 'Interpretation Services',
        'VIP Services', 'Mobile App Development', 'Drone Photography', 
        'Event Promotion', 'Backup Power Supply', 'Legal Consulting', 
        'Waste Management', 'Table & Chair Rentals', 'Food Trucks', 
        'Bartending Services', 'Valet Parking', 'Gift Bag Preparation', 
        'Eco-Friendly Solutions', 'Insurance Services', 'Accessibility Services',
        'Kids Entertainment', 'Emergency Response', 'Floristry', 
        'Green Room Setup', 'Personalized Invitations', 'Printing Services',
        'Exhibit Design', 'Coat Check', 'Stage Rigging', 'Pyrotechnics',
        'Custom Merchandise', 'Seating Arrangement', 'Shuttle Services',
        'Badge Printing', 'Health and Safety Compliance', 'Facilitation',
        'Audience Engagement Tools', 'Digital Signage', 'Interactive Kiosks',
        'Event Analytics', 'Social Media Coverage', 'Backdrop Setup',
        'Floor Management', 'Sponsor Liaison', 'Photo Booths', 
        'Virtual Reality Experiences', 'Augmented Reality Features'
    ]

    services = [(service,) for service in service_types]
    
    insert_query = """
        INSERT INTO Services (ServiceType)
        VALUES (%s)
        ON CONFLICT (ServiceType) DO NOTHING
        RETURNING ServiceID;
    """
    
    service_ids = []
    try:
        for service in services:
            cursor.execute(insert_query, service)
            result = cursor.fetchone()
            if result:
                service_id = result[0]
                service_ids.append(service_id)
        conn.commit()
        print(f"Inserted {len(service_ids)} services.")
    except Exception as e:
        conn.rollback()
        print("Error inserting services:", e)
    return service_ids

def insert_events(n, address_ids, organizer_ids):
    # Etkinlikleri ekleme fonksiyonu
    event_types = [
        'Hackathon', 'Concert', 'Sports', 'Conference', 'Theatre',
        'Workshop', 'Festival', 'Webinar', 'Exhibition', 'Meetup',
        'Networking', 'Seminar', 'Tournament', 'Charity', 'Comedy',
        'Dance', 'Other'
    ]
    
    events = []
    past_event_ids = []
    future_event_ids = []
    
    for i in range(n):
        title = generate_event_title()
        description = generate_event_description()
        event_type = random.choice(event_types)
        capacity = random.randint(50, 1000)
        
        # Etkinliğin geçmişte mi gelecekte mi olduğuna karar ver
        if random.choice([True, False]):
            # Geçmiş etkinlik: son bir yıl içinde
            date = fake.date_between(start_date='-1y', end_date='today')
        else:
            # Gelecek etkinlik: önümüzdeki bir yıl içinde
            date = fake.date_between(start_date='today', end_date='+1y')
        
        start_time = fake.time()
        
        # end_time'in start_time'dan sonra olduğundan emin ol
        try:
            start_dt = datetime.strptime(start_time, "%H:%M:%S")
            end_dt = start_dt + timedelta(hours=random.randint(1, 5))
            end_time = end_dt.time().strftime("%H:%M:%S")
        except ValueError:
            # start_time saniyeleri içermiyorsa
            end_time = None
        
        address_id = random.choice(address_ids)
        organized_by = random.choice(organizer_ids)
        price = round(random.uniform(10.0, 500.0), 2)
        events.append((title, description, event_type, capacity, date, start_time, end_time, address_id, organized_by, price))
    
    insert_query = """
        INSERT INTO Events (Title, Description, EventType, Capacity, Date, StartTime, EndTime, AddressID, OrganizedBy, Price)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING EventID, Date;
    """
    
    event_ids = []
    past_event_ids = []
    future_event_ids = []
    
    try:
        for event in events:
            cursor.execute(insert_query, event)
            result = cursor.fetchone()
            event_id = result[0]
            event_date = result[1]
            event_ids.append(event_id)
            if event_date < datetime.today().date():
                past_event_ids.append(event_id)
            else:
                future_event_ids.append(event_id)
        conn.commit()
        print(f"Inserted {n} events.")
        return event_ids, past_event_ids, future_event_ids
    except Exception as e:
        conn.rollback()
        print("Error inserting events:", e)
        return [], [], []

def insert_event_categories(event_ids, category_ids, max_categories_per_event=3):
    # Etkinlik kategorilerini ekleme fonksiyonu
    event_categories = []
    for event_id in event_ids:
        num_categories = random.randint(1, max_categories_per_event)
        if len(category_ids) < num_categories:
            selected_categories = category_ids  # Yeterli kategori yoksa tümünü seç
        else:
            selected_categories = random.sample(category_ids, num_categories)
        for category_id in selected_categories:
            event_categories.append((event_id, category_id))
    
    insert_query = """
        INSERT INTO EventCategories (EventID, CategoryID)
        VALUES (%s, %s)
        ON CONFLICT (EventID, CategoryID) DO NOTHING;
    """
    
    try:
        for ec in event_categories:
            cursor.execute(insert_query, ec)
        conn.commit()
        print(f"Inserted {len(event_categories)} event-category relationships.")
    except Exception as e:
        conn.rollback()
        print("Error inserting event categories:", e)

def insert_event_services(event_ids, service_ids, max_services_per_event=5):
    # Etkinlik servislerini ekleme fonksiyonu
    event_services = []
    for event_id in event_ids:
        num_services = random.randint(1, max_services_per_event)
        if len(service_ids) < num_services:
            selected_services = service_ids  # Yeterli servis yoksa tümünü seç
        else:
            selected_services = random.sample(service_ids, num_services)
        for service_id in selected_services:
            event_services.append((event_id, service_id))
    
    insert_query = """
        INSERT INTO EventServices (EventID, ServiceID)
        VALUES (%s, %s)
        ON CONFLICT (EventID, ServiceID) DO NOTHING;
    """
    
    try:
        for es in event_services:
            cursor.execute(insert_query, es)
        conn.commit()
        print(f"Inserted {len(event_services)} event-service relationships.")
    except Exception as e:
        conn.rollback()
        print("Error inserting event services:", e)

def insert_announcements(n, event_ids):
    # Duyuruları ekleme fonksiyonu
    announcements = []
    for _ in range(n):
        content = generate_announcement_content()  # Gelişmiş duyuru içerik oluşturucu kullanılıyor
        # Rastgele bir etkinlik seç
        event_id = random.choice(event_ids)
        # Etkinlik tarihini al
        cursor.execute("SELECT Date FROM Events WHERE EventID = %s;", (event_id,))
        result = cursor.fetchone()
        if result:
            event_date = result[0]
            # Duyuru tarihi, etkinlikten 30 gün öncesi ile etkinlik tarihi arasında
            announcement_date = fake.date_between(start_date=event_date - timedelta(days=30), end_date=event_date)
            announcements.append((content, announcement_date, event_id))
        else:
            # Etkinlik bulunamazsa, devam et
            continue
    
    insert_query = """
        INSERT INTO Announcements (Content, Date, EventID)
        VALUES (%s, %s, %s)
        RETURNING AnnouncementID;
    """
    
    try:
        for announcement in announcements:
            cursor.execute(insert_query, announcement)
        conn.commit()
        print(f"Inserted {n} announcements.")
    except Exception as e:
        conn.rollback()
        print("Error inserting announcements:", e)

def insert_reviews(n, user_ids, past_event_ids):
    # Yorumları ekleme fonksiyonu
    if not past_event_ids:
        print("No past events available for reviews. Skipping reviews insertion.")
        return
    
    reviews = []
    for _ in range(n):
        user_id = random.choice(user_ids)
        event_id = random.choice(past_event_ids)
        rating = random.randint(0, 10)
        comment = generate_review()  # Gelişmiş yorum oluşturucu kullanılıyor
        # Etkinlik tarihini al
        cursor.execute("SELECT Date FROM Events WHERE EventID = %s;", (event_id,))
        result = cursor.fetchone()
        if result:
            event_date = result[0]
            review_date = fake.date_between(start_date=event_date, end_date='today')
            reviews.append((user_id, event_id, rating, comment, review_date))
        else:
            # Etkinlik bulunamazsa, devam et
            continue
    
    insert_query = """
        INSERT INTO Reviews (UserID, EventID, Rating, Comment, Date)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (UserID, EventID) DO NOTHING;
    """
    
    try:
        for review in reviews:
            cursor.execute(insert_query, review)
        conn.commit()
        print(f"Inserted {len(reviews)} reviews.")
    except Exception as e:
        conn.rollback()
        print("Error inserting reviews:", e)

def insert_registrations(n, user_ids, event_ids):
    # Kayıtları ekleme fonksiyonu
    registration_statuses = [
        'Confirmed', 'Pending', 'Cancelled', 'Waitlisted',
        'CheckedIn', 'NoShow', 'Declined', 'Refunded', 'Transferred'
    ]
    
    registrations = []
    for _ in range(n):
        user_id = random.choice(user_ids)
        event_id = random.choice(event_ids)
        status = random.choice(registration_statuses)
        ticket = fake.uuid4()
        # Etkinlik tarihini al
        cursor.execute("SELECT Date FROM Events WHERE EventID = %s;", (event_id,))
        result = cursor.fetchone()
        if result:
            event_date = result[0]
            registration_date = fake.date_between(start_date='-1y', end_date=event_date)
            registrations.append((user_id, event_id, status, ticket, registration_date))
        else:
            # Etkinlik bulunamazsa, devam et
            continue
    
    insert_query = """
        INSERT INTO Registrations (UserID, EventID, Status, Ticket, Date)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (UserID, EventID) DO NOTHING;
    """
    
    try:
        for registration in registrations:
            cursor.execute(insert_query, registration)
        conn.commit()
        print(f"Inserted {len(registrations)} registrations.")
    except Exception as e:
        conn.rollback()
        print("Error inserting registrations:", e)

if __name__ == "__main__":
    try:
        
        num_addresses_value = 1000
        num_users_value = 5000
        num_organizers_value = 500 
        num_events_value = 2000
        num_announcements_value = 3000
        num_reviews_value = 10000
        num_registrations_value = 20000
        
        # Adım 1: Adresleri ekle
        num_addresses = num_addresses_value  # İhtiyaca göre ayarlayın
        address_ids = insert_addresses(num_addresses)
        
        if not address_ids:
            raise Exception("No addresses were inserted. Aborting population script.")
        
        # Adım 2: Kullanıcıları ekle
        num_users = num_users_value  # İhtiyaca göre ayarlayın
        user_ids = insert_users(num_users, address_ids)
        
        if not user_ids:
            raise Exception("No users were inserted. Aborting population script.")
        
        # Adım 3: Organizatörleri ekle
        num_organizers = num_organizers_value  # İhtiyaca göre ayarlayın
        organizer_ids = insert_organizers(num_organizers)
        
        if not organizer_ids:
            raise Exception("No organizers were inserted. Aborting population script.")
        
        # Adım 4: Kategorileri ekle
        category_ids = insert_categories()
        
        if not category_ids:
            raise Exception("No categories were inserted. Aborting population script.")
        
        # Adım 5: Servisleri ekle
        service_ids = insert_services()
        
        if not service_ids:
            raise Exception("No services were inserted. Aborting population script.")
        
        # Adım 6: Etkinlikleri ekle
        num_events = num_events_value  # İhtiyaca göre ayarlayın
        event_ids, past_event_ids, future_event_ids = insert_events(num_events, address_ids, organizer_ids)
        
        if not event_ids:
            raise Exception("No events were inserted. Aborting population script.")
        
        # Adım 7: Etkinlik Kategorilerini ekle
        insert_event_categories(event_ids, category_ids)
        
        # Adım 8: Etkinlik Servislerini ekle
        insert_event_services(event_ids, service_ids)
        
        # Adım 9: Duyuruları ekle
        num_announcements = num_announcements_value  # İhtiyaca göre ayarlayın
        insert_announcements(num_announcements, event_ids)
        
        # Adım 10: Yorumları ekle (sadece geçmiş etkinlikler için)
        num_reviews = num_reviews_value  # İhtiyaca göre ayarlayın
        if past_event_ids:
            insert_reviews(num_reviews, user_ids, past_event_ids)
        else:
            print("No past events available for reviews. Skipping reviews insertion.")
        
        # Adım 11: Kayıtları ekle
        num_registrations = num_registrations_value  # İhtiyaca göre ayarlayın
        insert_registrations(num_registrations, user_ids, event_ids)
        
        print("Database population completed successfully.")
    except Exception as e:
        print("An error occurred during database population:", e)
    finally:
        cursor.close()
        conn.close()
        print("Database connection closed.")
