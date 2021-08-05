from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from user_profile.models import UserProfile
from user_profile.serializers import UserProfileSerializer
from customer_address.models import CustomerAddress
from customer_address.serializers import CustomerAddressSerializer


class Test(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({'success': 'test Passed.'})


class AddUserAddress(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, pk):
        data = self.request.data
        contry = data['contry']
        state = data['state']
        city = data['city']
        town = data['town']
        street = data['street']
        locality = data['locality']
        society = data['society']
        flat_no = data['flat_no']
        pincode = data['pincode']
        primobileno = data['primobileno']
        secmobileno = data['secmobileno']
        try:
            customer = UserProfile.objects.get(user_id=pk)
            customeraddressserializers = UserProfileSerializer(customer)
            print(customeraddressserializers.data)
            CustomerAddress.objects.create(
                customer=customer, contry=contry, state=state, city=city, town=town, street=street, locality=locality, society=society, flat_no=flat_no,pincode=pincode,primobileno=primobileno,secmobileno=secmobileno)
            return Response({'success': customeraddressserializers.data})
        except Exception as e:
            return Response({'error': e})


class getcustomersaddress(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self,request, pk):
        try:
            customeraddress = CustomerAddress.objects.filter(customer_id=pk)
            customeraddressserializers = CustomerAddressSerializer(
                customeraddress, many=True)
            return Response({"success":customeraddressserializers.data})
        except Exception as e:
            return Response({'error': e})
