# utils/message_codes.py

"""
This file defines the message codes for multilanguage in the frontend
Using i18n standard, please check multilanguage folder to add or modify messages
assets/i18n/<lang>
"""

# Common Messages
OK_MSG = "OK_MSG"
CREATED_MSG = "CREATED_MSG"
NOT_FOUND_MSG = "NOT_FOUND_MSG"
CONFLICT_MSG = "CONFLICT_MSG"
UNPROCESSABLE_ENTITY_MSG = "UNPROCESSABLE_ENTITY_MSG"
INTERNAL_SERVER_ERROR_MSG = "INTERNAL_SERVER_ERROR_MSG"
SERVER_TIMEOUT_MSG = "SERVER_TIMEOUT_MSG"
NO_DATA = "NO_DATA"
ERROR_MSG = "ERROR_MSG"  # Añadir ERROR_MSG aquí
SUCCESS_MSG = "SUCCESS_MSG"  # Añadir SUCCESS_MSG aquí

INCORRECT_REQUEST_PARAM = 'INCORRECT_REQUEST_PARAM'

# Common Validations Messages
INVALID_ID = "INVALID_ID"  # Invalid Id

# Health Validations Messages
HEALTH_NOT_FOUND = "HEALTH_NOT_FOUND"  # Health not found
HEALTH_SUCCESSFULLY = "HEALTH_SUCCESSFULLY"  # Health successfully responded

# LAB Validations Messages
LAB_NOT_FOUND = "LAB_NOT_FOUND"  # LAB not found
LAB_SUCCESSFULLY_UPDATED = "LAB_SUCCESSFULLY_UPDATED"  # LAB successfully updated
LAB_SUCCESSFULLY_DELETED = "LAB_SUCCESSFULLY_DELETED"  # LAB successfully deleted
LAB_SUCCESSFULLY_CREATED = "LAB_SUCCESSFULLY_CREATED"  # LAB created successfully
LAB_ALREADY_EXIST = "LAB_ALREADY_EXIST"  # LAB already exist from database
LAB_NAME_REQUIRED = "LAB_NAME_REQUIRED"  # Requerid LAB name
LAB_NUM_REQUIRED = "LAB_NUM_REQUIRED"  # Requerid LAB Num
LAB_COMPUTERS_REQUIRED = "LAB_COMPUTERS_REQUIRED"  # Requerid Computers in Lab

# Booking validations Messages
BOOKING_SUCCESSFULLY_CREATED = "BOOKING_SUCCESSFULLY_CREATED"
BOOKING_ALREADY_EXIST = "BOOKING_ALREADY_EXIST" 
INVALID_EMAIL_DOMAIN = "INVALID_EMAIL_DOMAIN"
BOOKING_PROFESSOR_REQUIRED = "BOOKING_PROFESSOR_REQUIRED"
BOOKING_PROFESSOR_EMAIL_REQUIRED = "BOOKING_PROFESSOR_EMAIL_REQUIRED"
BOOKING_CAREER_REQUIRED = "BOOKING_CAREER_REQUIRED"
BOOKING_SUBJECT_REQUIRED = "BOOKING_SUBJECT_REQUIRED"
BOOKING_LAB_REQUIRED = "BOOKING_LAB_REQUIRED"
BOOKING_END_TIME_REQUIRED = "BOOKING_END_TIME_REQUIRED"
BOOKING_START_TIME_REQUIRED = "BOOKING_START_TIME_REQUIRED"
OK_MSG = "OK_MSG"
INVALID_DATE = "INVALID_DATE"
BOOKING_SUCCESSFULLY_RETRIEVED = "BOOKING_SUCCESSFULLY_RETRIEVED" # Booking Retrieved
BOOKINGS_RETRIEVE_ERROR = "BOOKINGS_RETRIEVE_ERROR" # Booking Retrieve Error
BOOKING_NO_MATCHING_BOOKINGS = "BOOKING_NO_MATCHING_BOOKINGS" # No matching bookings
# Professor Validations Messages
PROFESSOR_EMAIL_REQUIRED = "PROFESSOR_EMAIL_REQUIRED" # Requerid Professor Email 
PROFESSOR_NOT_FOUND = "PROFESSOR_NOT_FOUND" # Professor not found

# ISSUE Validations Messages
ISSUE_NOT_FOUND = "ISSUE_NOT_FOUND"  # ISSUE not found
ISSUE_SUCCESSFULLY_UPDATED = "ISSUE_SUCCESSFULLY_UPDATED"  # ISSUE successfully updated
ISSUE_SUCCESSFULLY_DELETED = "ISSUE_SUCCESSFULLY_DELETED"  # ISSUE successfully deleted
ISSUE_SUCCESSFULLY_CREATED = "ISSUE_SUCCESSFULLY_CREATED"  # ISSUE created successfully
ISSUE_ALREADY_EXIST= "ISSUE_ALREADY_EXIST"  # ISSUE already exist from database
ISSUE_LAB_REQUIRED= "ISSUE_LAB_REQUIRED"  # Requerid ISSUE LAB
ISSUE_DATE_ISSUE_REQUIRED = "ISSUE_DATE_ISSUE_REQUIRED"  # Requerid ISSUE DATE ISSUE
ISSUE_PERSON_REQUIRED = "ISSUE_PERSON_REQUIRED"  # Requerid Person in ISSUE
ISSUE_REQUIRED = "ISSUE_REQUIRED"  # Requerid ISSUE
ISSUE_REPORT_TO_REQUIRED = "ISSUE_REPORT_TO_REQUIRED"  # Requerid Report to in ISSUE
ISSUE_OBSERVATIONS_REQUIRED = "ISSUE_OBSERVATIONS_REQUIRED"  # Requerid OBSERVATIONS in ISSUE
ISSUE_NOTIFICATION_DATE_REQUIRED = "ISSUE_NOTIFICATION_DATE_REQUIRED"  # Requerid notification date in ISSUE
ISSUE_STATUS_REQUIRED = "ISSUE_STATUS_REQUIRED "  # Requerid status in ISSUE
ISSUE_UPDATE_REQUIRED = "ISSUE_UPDATE_REQUIRED"  # Requerid update in ISSUE
ISSUE_ID_REQUIRED = "ISSUE_ID_REQUIRED" # Requerid ID the ISSUE
ISSUE_UNAUTHORIZED_ACTION = "UNAUTHORIZED_ACTION" # UNAUTHORIZED ACTION
ISSUE_EMAIL_REQUIRED = "ISSUE_EMAIL_REQUIRED" # ISSUE_EMAIL_REQUIRED
ISUE_STATUS_PENDING = "ISUE_STATUS_PENDING" # ISUE_STATUS_PENDING
INTERNAL_ERROR = "INTERNAL_ERROR"