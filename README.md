# gmail_id_scraper

## Download email ids and other information from a gmail account

1. Make sure IMAP is enabled gmail account settings
(Log on to your Gmail account and go to Settings, See All Settings, and select
Forwarding and POP/IMAP tab. In the "IMAP access" section, select Enable IMAP.)

Account Settings --> See All Settings --> Forwarding --> POP/IMAP --> IMAP

2. If you have 2-factor authentication, gmail requires you to create an application
specific password that you need to use. 
Go to your Google account settings and click on 'Security'.
Scroll down to App Passwords under 2 step verification.

Account Settings --> Manage Your Account --> Security --> 2FA Verification --> App Passwords

Select Mail under Select App. and Other under Select Device. (Give a name, e.g., pythonscraper)
The system gives you a 16-character password that you need to use to authenticate from within python.
