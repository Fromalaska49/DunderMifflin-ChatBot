from ChatBot.views.misc.Constants import *

UNKNOWN_REQUEST = 'I do not understand your question. Please reword and try again.'

UPDATE_DIRECTORY = {KEYWORDS: ['update', 'utsa', 'directory', 'personal', 'information'],
                    RESPONSE: 'You can change your personal information in the UTSA directory at http://www.utsa.edu/directory/help'}

REQUEST_ACCESS = {KEYWORDS: ['request', 'access'],
                  RESPONSE: 'You can submit an access request form at http://aam.utsa.edu'}

UPLOAD_GRADES = {KEYWORDS: ['upload', 'grades'],
                 RESPONSE: 'Information about uploading gades can be found at https://utsacloudpublic.com/Pages/OnlineLearning/FacultyAndStaff/GradeTransfer.aspx'}

intents = [UPDATE_DIRECTORY, REQUEST_ACCESS, UPLOAD_GRADES]

