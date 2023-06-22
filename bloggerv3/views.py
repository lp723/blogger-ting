from django.shortcuts import render
from google_auth_oauthlib.flow import Flow
import googleapiclient.discovery
from google.oauth2 import credentials
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse

import os

def oauth2_callback(request):
    flow = Flow.from_client_secrets_file(
        os.path.join('certs', 'client_secret_902884065417-qgsnh4ob092b5n4do6p59vbpma30fgh8.apps.googleusercontent.com.json'),  # Path to your client secrets JSON file
        scopes=['https://www.googleapis.com/auth/blogger'],
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )
    flow.fetch_token(authorization_response=request.build_absolute_uri())
    credentials = flow.credentials
    # Store the credentials in the user's session or database as needed
    # Redirect to the page to create a blog post
    return HttpResponse("OAuth2 callback successful")

def authorize(request):
    flow = Flow.from_client_secrets_file(
        os.path.join('certs', 'client_secret_902884065417-qgsnh4ob092b5n4do6p59vbpma30fgh8.apps.googleusercontent.com.json'),  # Path to your client secrets JSON file
        scopes=['https://www.googleapis.com/auth/blogger'],
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )
    authorization_url, state = flow.authorization_url()
    # Store the state in the user's session or database as needed
    return redirect(authorization_url)
    

def create_blog_post(request):
    # Retrieve the credentials from the user's session or database
    # credentials = ...
    
    # Check if credentials have expired, and refresh if needed
    if credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
        # Store the refreshed credentials if needed
    
    service = googleapiclient.discovery.build(
        'blogger', 'v3', credentials=credentials
    )
    
    # Create the blog post using the Blogger API
    blog_id = '4787800070143898927'  # Replace with your blog ID
    post_data = {
        'kind': 'blogger#post',
        'blog': {'id': blog_id},
        'title': 'My Blog Post',
        'content': '<p>This is my blog post content</p>',
        'labels': ['label1', 'label2'],
    }
    service.posts().insert(blogId=blog_id, body=post_data).execute()
    
    # Redirect to a success page or return a success message

