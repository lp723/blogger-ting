from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.sessions.backends.db import SessionStore
from django.core import serializers
import googleapiclient.discovery
from google_auth_oauthlib.flow import Flow
from google.oauth2 import credentials
from pprint import pprint
import os
#from django.core.cache import cache

from .serializers import GoogleCredentialsSerializer

def oauth2_callback(request):
    flow = Flow.from_client_secrets_file(
        os.path.join('certs', 'client_secret_902884065417-qgsnh4ob092b5n4do6p59vbpma30fgh8.apps.googleusercontent.com.json'),  # Path to your client secrets JSON file
        scopes=['https://www.googleapis.com/auth/blogger'],
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )
    flow.fetch_token(authorization_response=request.build_absolute_uri())
    credentials = flow.credentials

    serializer = GoogleCredentialsSerializer(credentials.__dict__)
    request.session['credentials'] = serializer.data
    return redirect('create_blog_post')

def authorize(request):
    flow = Flow.from_client_secrets_file(
        os.path.join('certs', 'client_secret_902884065417-qgsnh4ob092b5n4do6p59vbpma30fgh8.apps.googleusercontent.com.json'),  # Path to your client secrets JSON file
        scopes=['https://www.googleapis.com/auth/blogger'],
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )
    authorization_url, state = flow.authorization_url()
    # Store the state in the user's session or database as needed
    return redirect(authorization_url)
    

def create_blog_post(request, ):

    credentials = request.session['credentials']
    print(credentials)
    credentials['expiry']

    return HttpResponse('babba booey')
    #if credentials.expired:
    #    credentials.refresh(Request())
    #     Store the refreshed credentials if needed
    
    #service = googleapiclient.discovery.build(
    #    'blogger', 'v3', credentials=CREDENTIALS
    #)
    
    # Create the blog post using the Blogger API
    #blog_id = '4787800070143898927'  # Replace with your blog ID
    #post_data = {
    #    'kind': 'blogger#post',
    #    'blog': {'id': blog_id},
    #    'title': 'My Blog Post',
    #    'content': '<p>This is my blog post content</p>',
    #    'labels': ['label1', 'label2'],
    #}
    #service.posts().insert(blogId=blog_id, body=post_data).execute()
    
    # Redirect to a success page or return a success message

