from rest_framework import serializers


class UserSubscribedPointsInputSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()


class UserSubscribedPointsOutputSerializer(serializers.Serializer):
    checkpoint__location_name = serializers.CharField()
    status = serializers.SerializerMethodField()

    def get_status(self, claim):
        number_of_open = claim.get("status_summation")
        if number_of_open >= claim.get("checkpoint__min_number"):
            return "Open"
        else:
            return "Close"