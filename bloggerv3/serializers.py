from rest_framework import serializers

class GoogleCredentialsSerializer(serializers.Serializer):
    _client_id = serializers.CharField()
    _client_secret = serializers.CharField()
    _default_scopes = serializers.CharField(allow_null=True)
    _enable_reauth_refresh = serializers.BooleanField()
    _granted_scopes = serializers.ListField(child=serializers.CharField())
    _id_token = serializers.CharField(allow_null=True)
    _quota_project_id = serializers.CharField(allow_null=True)
    _rapt_token = serializers.CharField(allow_null=True)
    _refresh_handler = serializers.CharField(allow_null=True)
    _refresh_token = serializers.CharField()
    _scopes = serializers.ListField(child=serializers.CharField())
    _token_uri = serializers.CharField()
    expiry = serializers.DateTimeField()
    token = serializers.CharField()

    #def to_representation(self, instance):
    #    #data = super().to_representation(instance)
    #    data['expiry'] = instance.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    #    return data